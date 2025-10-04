"""
Nearby Search Module for Google Places API

This module contains the Nearby Search functionality for Google Places API (New).
It implements the searchNearby endpoint for finding places within a specific radius.

This module is completely independent and can be used standalone.
"""

from typing import Dict, List, Optional
from .shared_utils import APIRequestHandler, FieldMaskHelper


class NearbySearch:
    """
    Nearby Search functionality for Google Places API (New)
    
    This class provides location-based search capabilities for finding places
    within a specific radius of given coordinates.
    """
    
    def __init__(self, api_key: str = None):
        """
        Initialize the Nearby Search client
        
        Args:
            api_key: Google Places API key (optional, uses global config if not provided)
        """
        self.api_handler = APIRequestHandler(api_key)
        self.field_helper = FieldMaskHelper()
        self.search_url = f"{self.api_handler.base_url}/places:searchNearby"
    
    def search(
        self,
        location: Dict,
        field_mask: Optional[str] = None,
        included_types: Optional[List[str]] = None,
        include_pure_service_area_businesses: Optional[bool] = None,
        language_code: Optional[str] = None,
        max_result_count: Optional[int] = None,
        min_rating: Optional[float] = None,
        open_now: Optional[bool] = None,
        price_levels: Optional[List[str]] = None,
        rank_preference: Optional[str] = None,
        region_code: Optional[str] = None,
        strict_type_filtering: Optional[bool] = None,
        radius: float = 5000
    ) -> Optional[Dict]:
        """
        Search places using nearby search
        
        Args:
            location: Dictionary with 'latitude' and 'longitude' keys (required)
            field_mask: Fields to return (optional, uses default if None)
            included_types: List of place types to include (optional)
            include_pure_service_area_businesses: Include service area businesses (optional)
            language_code: Language for results (optional)
            max_result_count: Maximum number of results (optional, max 20)
            min_rating: Minimum rating filter (optional)
            open_now: Filter for places currently open (optional)
            price_levels: Price level filters (optional)
            rank_preference: How to rank results (optional)
            region_code: Region code for results (optional)
            strict_type_filtering: Strict type filtering (optional)
            radius: Search radius in meters (optional, default 5000)
            
        Returns:
            Dictionary containing search results or None if failed
            
        Example:
            # Basic nearby search
            nearby_search = NearbySearch("your_api_key")
            results = nearby_search.search(
                location={"latitude": 37.7749, "longitude": -122.4194},
                radius=1000
            )
            
            # Advanced nearby search with filters
            results = nearby_search.search(
                location={"latitude": 37.7749, "longitude": -122.4194},
                field_mask=nearby_search.get_restaurant_field_mask(),
                included_types=["restaurant"],
                min_rating=4.0,
                radius=500
            )
        """
        # Set default field mask if not provided
        if field_mask is None:
            field_mask = "places.attributions,places.id,places.displayName"
        
        # Build request body with required parameters
        request_body = {
            "locationRestriction": {
                "circle": {
                    "center": {
                        "latitude": location["latitude"],
                        "longitude": location["longitude"]
                    },
                    "radius": radius
                }
            }
        }
        
        # Add optional parameters if provided
        if included_types:
            request_body["includedTypes"] = included_types
        if include_pure_service_area_businesses is not None:
            request_body["includePureServiceAreaBusinesses"] = include_pure_service_area_businesses
        if language_code:
            request_body["languageCode"] = language_code
        if max_result_count is not None:
            request_body["maxResultCount"] = min(max_result_count, 20)  # API limit
        if min_rating is not None:
            request_body["minRating"] = min_rating
        if open_now is not None:
            request_body["openNow"] = open_now
        if price_levels:
            request_body["priceLevels"] = price_levels
        if rank_preference:
            request_body["rankPreference"] = rank_preference
        if region_code:
            request_body["regionCode"] = region_code
        if strict_type_filtering is not None:
            request_body["strictTypeFiltering"] = strict_type_filtering
        
        # Build headers with field mask
        headers = self.api_handler.build_headers_with_field_mask(
            field_mask=field_mask,
            language_code=language_code,
            region_code=region_code
        )
        
        # Make the request
        return self.api_handler.make_request(
            url=self.search_url,
            method="POST",
            data=request_body,
            headers=headers
        )
    
    def search_restaurants(self, location: Dict, radius: float = 1000,
                          min_rating: float = 4.0, **kwargs) -> Optional[Dict]:
        """
        Convenience method for searching nearby restaurants
        
        Args:
            location: Dictionary with 'latitude' and 'longitude' keys
            radius: Search radius in meters
            min_rating: Minimum rating filter
            **kwargs: Additional parameters for search
            
        Returns:
            Dictionary containing restaurant search results
        """
        # Use restaurant field mask
        field_mask = kwargs.pop('field_mask', self.field_helper.get_restaurant_field_mask())
        
        # Add restaurant-specific parameters
        search_params = {
            'location': location,
            'field_mask': field_mask,
            'included_types': ['restaurant'],
            'min_rating': min_rating,
            'radius': radius,
            **kwargs
        }
        
        return self.search(**search_params)
    
    def search_hotels(self, location: Dict, radius: float = 2000,
                     min_rating: float = 4.0, **kwargs) -> Optional[Dict]:
        """
        Convenience method for searching nearby hotels
        
        Args:
            location: Dictionary with 'latitude' and 'longitude' keys
            radius: Search radius in meters
            min_rating: Minimum rating filter
            **kwargs: Additional parameters for search
            
        Returns:
            Dictionary containing hotel search results
        """
        # Use hotel field mask
        field_mask = kwargs.pop('field_mask', self.field_helper.get_hotel_field_mask())
        
        # Add hotel-specific parameters
        search_params = {
            'location': location,
            'field_mask': field_mask,
            'included_types': ['lodging'],
            'min_rating': min_rating,
            'radius': radius,
            **kwargs
        }
        
        return self.search(**search_params)
    
    def search_attractions(self, location: Dict, radius: float = 2000,
                          min_rating: float = 4.0, **kwargs) -> Optional[Dict]:
        """
        Convenience method for searching nearby tourist attractions
        
        Args:
            location: Dictionary with 'latitude' and 'longitude' keys
            radius: Search radius in meters
            min_rating: Minimum rating filter
            **kwargs: Additional parameters for search
            
        Returns:
            Dictionary containing attraction search results
        """
        # Use attraction field mask
        field_mask = kwargs.pop('field_mask', self.field_helper.get_attraction_field_mask())
        
        # Add attraction-specific parameters
        search_params = {
            'location': location,
            'field_mask': field_mask,
            'min_rating': min_rating,
            'radius': radius,
            **kwargs
        }
        
        return self.search(**search_params)
    
    def search_gas_stations(self, location: Dict, radius: float = 5000,
                           **kwargs) -> Optional[Dict]:
        """
        Convenience method for searching nearby gas stations
        
        Args:
            location: Dictionary with 'latitude' and 'longitude' keys
            radius: Search radius in meters
            **kwargs: Additional parameters for search
            
        Returns:
            Dictionary containing gas station search results
        """
        # Use basic field mask for gas stations
        field_mask = kwargs.pop('field_mask', self.field_helper.get_basic_field_mask())
        
        # Add gas station-specific parameters
        search_params = {
            'location': location,
            'field_mask': field_mask,
            'included_types': ['gas_station'],
            'radius': radius,
            **kwargs
        }
        
        return self.search(**search_params)
    
    def search_atms(self, location: Dict, radius: float = 2000, **kwargs) -> Optional[Dict]:
        """
        Convenience method for searching nearby ATMs
        
        Args:
            location: Dictionary with 'latitude' and 'longitude' keys
            radius: Search radius in meters
            **kwargs: Additional parameters for search
            
        Returns:
            Dictionary containing ATM search results
        """
        # Use basic field mask for ATMs
        field_mask = kwargs.pop('field_mask', self.field_helper.get_basic_field_mask())
        
        # Add ATM-specific parameters
        search_params = {
            'location': location,
            'field_mask': field_mask,
            'included_types': ['atm'],
            'radius': radius,
            **kwargs
        }
        
        return self.search(**search_params)
