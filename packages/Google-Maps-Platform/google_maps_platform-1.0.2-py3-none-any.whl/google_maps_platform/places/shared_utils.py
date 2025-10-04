"""
Shared Utilities for Google Places API Modules

This module contains common functionality that can be used across all Google Places API modules
without creating tight coupling through inheritance.
"""

import requests
import json
from typing import Dict, List, Optional
from .field_masks import FieldMaskManager
from ..config import get_api_key


class APIRequestHandler:
    """
    Handles HTTP requests to Google Places API
    
    This class can be instantiated and used by any module that needs to make API requests.
    """
    
    def __init__(self, api_key: str = None):
        """
        Initialize the API request handler
        
        Args:
            api_key: Google Places API key (optional, uses global config if not provided)
        """
        # Use provided API key or get from global config
        if api_key is None:
            api_key = get_api_key()
            if api_key is None:
                raise ValueError(
                    "API key not provided and not set globally. "
                    "Please set the API key using google_maps_platform.set_api_key('your_key') or "
                    "pass it directly to the module constructor."
                )
        
        self.api_key = api_key
        self.base_url = "https://places.googleapis.com/v1"
        
        self.headers = {
            "X-Goog-Api-Key": self.api_key,
            "Content-Type": "application/json"
        }
    
    def make_request(self, url: str, method: str = "GET", data: Optional[Dict] = None, 
                    headers: Optional[Dict] = None) -> Optional[Dict]:
        """
        Make a request to the Google Places API
        
        Args:
            url: The API endpoint URL
            method: HTTP method (GET, POST)
            data: Request body data for POST requests
            headers: Additional headers to include
            
        Returns:
            JSON response as dictionary or None if failed
        """
        request_headers = self.headers.copy()
        if headers:
            request_headers.update(headers)
        
        try:
            if method.upper() == "POST":
                response = requests.post(url, headers=request_headers, data=json.dumps(data))
            else:
                response = requests.get(url, headers=request_headers)
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error making {method} request to {url}: {e}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_details = e.response.json()
                    print(f"Error details: {error_details}")
                except:
                    print(f"Response text: {e.response.text}")
            return None
    
    def build_headers_with_field_mask(self, field_mask: str, 
                                    language_code: Optional[str] = None,
                                    region_code: Optional[str] = None) -> Dict[str, str]:
        """
        Build headers with field mask and optional language/region codes
        
        Args:
            field_mask: Field mask string
            language_code: Optional language code
            region_code: Optional region code
            
        Returns:
            Headers dictionary
        """
        headers = self.headers.copy()
        headers["X-Goog-FieldMask"] = field_mask
        
        if language_code:
            headers["X-Goog-Language-Code"] = language_code
        if region_code:
            headers["X-Goog-Region-Code"] = region_code
            
        return headers


class FieldMaskHelper:
    """
    Helper class for field mask management
    
    This class can be instantiated and used by any module that needs field mask functionality.
    """
    
    def __init__(self):
        """Initialize the field mask helper"""
        self.field_masks = FieldMaskManager()
    
    def get_available_fields(self) -> List[str]:
        """Get all available field masks"""
        return self.field_masks.get_all_fields()
    
    def get_field_categories(self) -> List[Dict]:
        """Get all field mask categories with their fields"""
        return [
            {
                "name": category.name,
                "description": category.description,
                "use_case": category.use_case,
                "fields": category.fields
            }
            for category in self.field_masks.get_categories()
        ]
    
    def search_fields(self, query: str) -> List[str]:
        """Search for fields containing a specific term"""
        return self.field_masks.search_fields(query)
    
    def get_field_info(self, field: str) -> Dict:
        """Get detailed information about a specific field"""
        return self.field_masks.get_field_info(field)
    
    def build_field_mask(self, categories: List[str] = None, fields: List[str] = None) -> str:
        """Build a field mask from categories or specific fields"""
        return self.field_masks.build_field_mask(categories=categories, fields=fields)
    
    def get_predefined_masks(self) -> Dict[str, str]:
        """Get predefined field masks for common use cases"""
        return self.field_masks.get_predefined_masks()
    
    def print_available_fields(self):
        """Print all available fields in a formatted way"""
        self.field_masks.print_all_fields()
    
    def print_field_categories(self):
        """Print all field mask categories"""
        self.field_masks.print_categories()
    
    def print_predefined_masks(self):
        """Print predefined field masks"""
        self.field_masks.print_predefined_masks()
    
    # Convenience methods for common field masks
    def get_restaurant_field_mask(self) -> str:
        """Get field mask optimized for restaurant searches"""
        return self.field_masks.get_predefined_masks()["restaurant"]
    
    def get_hotel_field_mask(self) -> str:
        """Get field mask optimized for hotel searches"""
        return self.field_masks.get_predefined_masks()["hotel"]
    
    def get_attraction_field_mask(self) -> str:
        """Get field mask optimized for attraction searches"""
        return self.field_masks.get_predefined_masks()["attraction"]
    
    def get_basic_field_mask(self) -> str:
        """Get basic field mask with essential fields only"""
        return self.field_masks.get_predefined_masks()["basic"]
    
    def get_contact_field_mask(self) -> str:
        """Get field mask with contact information"""
        return self.field_masks.get_predefined_masks()["contact"]
    
    def get_reviews_field_mask(self) -> str:
        """Get field mask with rating and review information"""
        return self.field_masks.get_predefined_masks()["reviews"]


# Convenience functions for easy access
def create_api_handler(api_key: str) -> APIRequestHandler:
    """Create an API request handler instance"""
    return APIRequestHandler(api_key)


def create_field_mask_helper() -> FieldMaskHelper:
    """Create a field mask helper instance"""
    return FieldMaskHelper()
