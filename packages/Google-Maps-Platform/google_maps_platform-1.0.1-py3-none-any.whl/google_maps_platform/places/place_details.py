"""
Place Details Module for Google Places API

This module contains the Place Details functionality for Google Places API (New).
It implements the places/{place_id} endpoint for getting detailed information about specific places.

This module is completely independent and can be used standalone.
"""

from typing import Dict, Optional
from .shared_utils import APIRequestHandler, FieldMaskHelper


class PlaceDetails:
    """
    Place Details functionality for Google Places API (New)
    
    This class provides detailed information retrieval capabilities for specific places
    using their Google Places ID.
    """
    
    def __init__(self, api_key: str = None):
        """
        Initialize the Place Details client
        
        Args:
            api_key: Google Places API key (optional, uses global config if not provided)
        """
        self.api_handler = APIRequestHandler(api_key)
        self.field_helper = FieldMaskHelper()
        self.details_base_url = f"{self.api_handler.base_url}/places/"
    
    def get_details(
        self, 
        place_id: str, 
        field_mask: Optional[str] = None,
        language_code: Optional[str] = None,
        region_code: Optional[str] = None
    ) -> Optional[Dict]:
        """
        Get detailed information about a specific place
        
        Args:
            place_id: Google Places ID of the place (required)
            field_mask: Fields to return (optional, uses default if None)
            language_code: Language for results (optional, e.g., "en", "es")
            region_code: Region code for results (optional, e.g., "US", "GB")
            
        Returns:
            Dictionary containing place details or None if failed
            
        Example:
            # Basic place details
            place_details = PlaceDetails("your_api_key")
            result = place_details.get_details("ChIJk35bizx-j4AREil6UPp7Jn4")
            
            # With custom field mask
            result = place_details.get_details(
                "ChIJk35bizx-j4AREil6UPp7Jn4",
                field_mask="id,displayName,formattedAddress,rating,priceLevel"
            )
            
            # With language and region
            result = place_details.get_details(
                "ChIJk35bizx-j4AREil6UPp7Jn4",
                language_code="es",
                region_code="ES"
            )
        """
        # Set default field mask if not provided
        if field_mask is None:
            field_mask = "id,displayName,formattedAddress,location,rating,userRatingCount,priceLevel,types,websiteUri,internationalPhoneNumber,editorialSummary,photos,reviews"
        
        # Build headers with field mask
        headers = self.api_handler.build_headers_with_field_mask(
            field_mask=field_mask,
            language_code=language_code,
            region_code=region_code
        )
        
        # Make the request
        url = f"{self.details_base_url}{place_id}"
        return self.api_handler.make_request(url=url, headers=headers)
    
    def get_restaurant_details(self, place_id: str, **kwargs) -> Optional[Dict]:
        """
        Get detailed information about a restaurant
        
        Args:
            place_id: Google Places ID of the restaurant
            **kwargs: Additional parameters (language_code, region_code)
            
        Returns:
            Dictionary containing restaurant details
        """
        # Use restaurant field mask
        field_mask = kwargs.pop('field_mask', self.field_helper.get_restaurant_field_mask())
        
        return self.get_details(
            place_id=place_id,
            field_mask=field_mask,
            **kwargs
        )
    
    def get_hotel_details(self, place_id: str, **kwargs) -> Optional[Dict]:
        """
        Get detailed information about a hotel
        
        Args:
            place_id: Google Places ID of the hotel
            **kwargs: Additional parameters (language_code, region_code)
            
        Returns:
            Dictionary containing hotel details
        """
        # Use hotel field mask
        field_mask = kwargs.pop('field_mask', self.field_helper.get_hotel_field_mask())
        
        return self.get_details(
            place_id=place_id,
            field_mask=field_mask,
            **kwargs
        )
    
    def get_attraction_details(self, place_id: str, **kwargs) -> Optional[Dict]:
        """
        Get detailed information about a tourist attraction
        
        Args:
            place_id: Google Places ID of the attraction
            **kwargs: Additional parameters (language_code, region_code)
            
        Returns:
            Dictionary containing attraction details
        """
        # Use attraction field mask
        field_mask = kwargs.pop('field_mask', self.field_helper.get_attraction_field_mask())
        
        return self.get_details(
            place_id=place_id,
            field_mask=field_mask,
            **kwargs
        )
    
    def get_basic_details(self, place_id: str, **kwargs) -> Optional[Dict]:
        """
        Get basic information about a place (minimal data)
        
        Args:
            place_id: Google Places ID of the place
            **kwargs: Additional parameters (language_code, region_code)
            
        Returns:
            Dictionary containing basic place details
        """
        # Use basic field mask
        field_mask = kwargs.pop('field_mask', self.field_helper.get_basic_field_mask())
        
        return self.get_details(
            place_id=place_id,
            field_mask=field_mask,
            **kwargs
        )
    
    def get_contact_details(self, place_id: str, **kwargs) -> Optional[Dict]:
        """
        Get contact information about a place
        
        Args:
            place_id: Google Places ID of the place
            **kwargs: Additional parameters (language_code, region_code)
            
        Returns:
            Dictionary containing contact details
        """
        # Use contact field mask
        field_mask = kwargs.pop('field_mask', self.field_helper.get_contact_field_mask())
        
        return self.get_details(
            place_id=place_id,
            field_mask=field_mask,
            **kwargs
        )
    
    def get_reviews_details(self, place_id: str, **kwargs) -> Optional[Dict]:
        """
        Get rating and review information about a place
        
        Args:
            place_id: Google Places ID of the place
            **kwargs: Additional parameters (language_code, region_code)
            
        Returns:
            Dictionary containing reviews and rating details
        """
        # Use reviews field mask
        field_mask = kwargs.pop('field_mask', self.field_helper.get_reviews_field_mask())
        
        return self.get_details(
            place_id=place_id,
            field_mask=field_mask,
            **kwargs
        )
    
    def get_multiple_details(self, place_ids: list, field_mask: Optional[str] = None,
                           **kwargs) -> Dict[str, Optional[Dict]]:
        """
        Get details for multiple places
        
        Args:
            place_ids: List of Google Places IDs
            field_mask: Fields to return for all places
            **kwargs: Additional parameters (language_code, region_code)
            
        Returns:
            Dictionary mapping place_id to details (or None if failed)
        """
        results = {}
        
        for place_id in place_ids:
            details = self.get_details(
                place_id=place_id,
                field_mask=field_mask,
                **kwargs
            )
            results[place_id] = details
        
        return results
