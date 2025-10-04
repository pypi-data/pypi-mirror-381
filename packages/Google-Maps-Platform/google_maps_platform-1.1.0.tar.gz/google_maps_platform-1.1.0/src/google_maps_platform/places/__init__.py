"""
Google Maps Platform - Places API Client

An unofficial Python client library for Google Places API (New) with independent
modular components and comprehensive field mask management.

Independent Modules:
- TextSearch: Text Search (searchText endpoint)
- NearbySearch: Nearby Search (searchNearby endpoint)
- PlaceDetails: Place Details (places/{place_id} endpoint)

Advanced Features:
- Completely Independent Modules
- Shared Utilities (APIRequestHandler, FieldMaskHelper)
- Parameter Builders for Complex Scenarios
- Utility Functions for Data Processing
- Type Hints and Error Handling
"""

# Independent modular components
from .text_search import TextSearch
from .nearby_search import NearbySearch
from .place_details import PlaceDetails

# Shared utilities
from .shared_utils import APIRequestHandler, FieldMaskHelper

# Configuration management
from .config import (
    set_api_key,
    get_api_key,
    is_api_key_set,
    clear_api_key,
    load_from_environment,
    get_status
)

# Parameter builders
from .parameter_builders import LocationBuilder, TextSearchBuilder, NearbySearchBuilder

# Field mask management
from .field_masks import FieldMaskManager

# Utility functions
from .utils import (
    format_places_data,
    search_places_formatted,
    filter_places_by_rating,
    filter_places_by_price_level,
    sort_places_by_rating,
    get_place_summary
)


__version__ = "1.0.0"
__author__ = "Chandan Gowda"
__email__ = "chandangowdatk23@gmail.com"

__all__ = [
    # Independent modular components
    "TextSearch",
    "NearbySearch", 
    "PlaceDetails",
    
    # Shared utilities
    "APIRequestHandler",
    "FieldMaskHelper",
    
    # Configuration management
    "set_api_key",
    "get_api_key",
    "is_api_key_set",
    "clear_api_key",
    "load_from_environment",
    "get_status",
    
    # Parameter builders
    "LocationBuilder",
    "TextSearchBuilder",
    "NearbySearchBuilder",
    
    # Field mask management
    "FieldMaskManager",
    
    # Utility functions
    "format_places_data",
    "search_places_formatted",
    "filter_places_by_rating",
    "filter_places_by_price_level",
    "sort_places_by_rating",
    "get_place_summary"
]
