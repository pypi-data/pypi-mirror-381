"""
Parameter Builders for Google Places API

This module contains utility classes for building location bias, location restriction,
and other parameter objects for the core Google Places API methods.
"""

import requests
from typing import Dict, Optional, List, Union


class LocationBuilder:
    """Builder for location-related parameters"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.geocoding_base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    def geocode_place(self, place_name: str) -> Optional[Dict]:
        """
        Geocode a place name to get latitude and longitude coordinates
        
        Args:
            place_name: Name of the place to geocode
            
        Returns:
            Dictionary with latitude, longitude, and formatted_address, or None if failed
        """
        try:
            params = {
                'address': place_name,
                'key': self.api_key
            }
            
            response = requests.get(self.geocoding_base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            if data['status'] == 'OK' and data['results']:
                location = data['results'][0]['geometry']['location']
                return {
                    'latitude': location['lat'],
                    'longitude': location['lng'],
                    'formatted_address': data['results'][0]['formatted_address']
                }
            else:
                print(f"Geocoding failed for '{place_name}': {data.get('status', 'Unknown error')}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Error geocoding '{place_name}': {e}")
            return None
    
    def create_location_bias(self, place_name: str, radius_meters: Optional[int] = None, 
                           use_rectangle: bool = False) -> Optional[Dict]:
        """
        Create a location bias for search queries.
        This INFLUENCES RANKING but does not exclude results outside the area.
        
        Args:
            place_name: Name of the place to create bias around
            radius_meters: Optional radius in meters
            use_rectangle: If True, use rectangle format; if False, use circle format
            
        Returns:
            Location bias object or None if geocoding fails
        """
        coords = self.geocode_place(place_name)
        if coords is None:
            return None
        
        latitude = coords['latitude']
        longitude = coords['longitude']
        
        if radius_meters and use_rectangle:
            # For rectangular bias with radius
            lat_delta = radius_meters / 111000.0
            lng_delta = radius_meters / (111000.0 * abs(latitude) * 0.017453292519943295)
            
            return {
                "rectangle": {
                    "low": {
                        "latitude": latitude - lat_delta,
                        "longitude": longitude - lng_delta
                    },
                    "high": {
                        "latitude": latitude + lat_delta,
                        "longitude": longitude + lng_delta
                    }
                }
            }
        elif radius_meters:
            # For circular bias with radius
            return {
                "circle": {
                    "center": {
                        "latitude": latitude,
                        "longitude": longitude
                    },
                    "radius": radius_meters
                }
            }
        else:
            # For point bias without radius
            return {
                "point": {
                    "latitude": latitude,
                    "longitude": longitude
                }
            }
    
    def create_location_restriction(self, place_name: str, radius_meters: int) -> Optional[Dict]:
        """
        Create a location restriction for search queries using rectangle.
        This STRICTLY RESTRICTS results to only within the specified area.
        
        Args:
            place_name: Name of the place to create restriction around
            radius_meters: Search radius in meters
            
        Returns:
            Location restriction object (rectangle format) or None if geocoding fails
        """
        coords = self.geocode_place(place_name)
        if coords is None:
            return None
        
        latitude = coords['latitude']
        longitude = coords['longitude']
        
        # Convert radius to approximate lat/lng degrees
        lat_delta = radius_meters / 111000.0
        lng_delta = radius_meters / (111000.0 * abs(latitude) * 0.017453292519943295)
        
        return {
            "rectangle": {
                "low": {
                    "latitude": latitude - lat_delta,
                    "longitude": longitude - lng_delta
                },
                "high": {
                    "latitude": latitude + lat_delta,
                    "longitude": longitude + lng_delta
                }
            }
        }
    
    def create_location_coordinates(self, place_name: str) -> Optional[Dict]:
        """
        Create location coordinates for nearby search
        
        Args:
            place_name: Name of the place to get coordinates for
            
        Returns:
            Dictionary with latitude and longitude, or None if geocoding fails
        """
        coords = self.geocode_place(place_name)
        if coords is None:
            return None
        
        return {
            "latitude": coords['latitude'],
            "longitude": coords['longitude']
        }


class TextSearchBuilder:
    """Builder for text search parameters with location utilities"""
    
    def __init__(self, location_builder: LocationBuilder):
        self.location_builder = location_builder
    
    def build_params(self, text_query: str, field_mask: Optional[str] = None, **kwargs) -> Dict:
        """
        Build text search parameters with optional location parameters
        
        Args:
            text_query: The text query to search for
            field_mask: Field mask for the response
            **kwargs: Additional parameters including:
                - location_bias_place: Place name for location bias
                - location_bias_radius: Radius for location bias
                - location_restriction_place: Place name for location restriction
                - location_restriction_radius: Radius for location restriction
                - All other text search parameters
        
        Returns:
            Dictionary of parameters ready for text_search method
        """
        # Extract location-related parameters
        location_bias = None
        location_restriction = None
        
        if 'location_bias_place' in kwargs:
            radius = kwargs.pop('location_bias_radius', None)
            use_rectangle = kwargs.pop('location_bias_rectangle', False)
            location_bias = self.location_builder.create_location_bias(
                kwargs.pop('location_bias_place'), radius, use_rectangle
            )
        
        if 'location_restriction_place' in kwargs:
            radius = kwargs.pop('location_restriction_radius', 5000)
            location_restriction = self.location_builder.create_location_restriction(
                kwargs.pop('location_restriction_place'), radius
            )
        
        # Add location parameters to kwargs
        if location_bias:
            kwargs['location_bias'] = location_bias
        if location_restriction:
            kwargs['location_restriction'] = location_restriction
        
        # Return parameters dictionary
        params = {'text_query': text_query}
        if field_mask:
            params['field_mask'] = field_mask
        params.update(kwargs)
        return params


class NearbySearchBuilder:
    """Builder for nearby search parameters with location utilities"""
    
    def __init__(self, location_builder: LocationBuilder):
        self.location_builder = location_builder
    
    def build_params(self, location: Union[str, Dict], field_mask: Optional[str] = None, **kwargs) -> Dict:
        """
        Build nearby search parameters with location handling
        
        Args:
            location: Either a place name (string) or coordinates dict
            field_mask: Field mask for the response
            **kwargs: Additional parameters for nearby search
        
        Returns:
            Dictionary of parameters ready for nearby_search method
        """
        # Handle location parameter
        if isinstance(location, str):
            # Geocode the place name
            coords = self.location_builder.create_location_coordinates(location)
            if coords is None:
                raise ValueError(f"Could not geocode location: {location}")
            location = coords
        
        # Return parameters dictionary
        params = {'location': location}
        if field_mask:
            params['field_mask'] = field_mask
        params.update(kwargs)
        return params
