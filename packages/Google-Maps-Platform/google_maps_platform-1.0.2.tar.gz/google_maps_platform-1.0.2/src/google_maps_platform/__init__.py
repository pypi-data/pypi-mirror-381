"""
Google Maps Platform - Root Library

A comprehensive Python client library for Google Maps Platform APIs with
global configuration management across all packages.

Packages:
- places: Google Places API (New) client
- routes: Google Routes API client (coming soon)
- environment: Google Environment API client (coming soon)
- ... and more

Global Configuration:
- Set API key once for all packages
- Environment variable support
- Configuration management
- Error handling
"""

# Global configuration management
from .config import (
    set_api_key,
    get_api_key,
    is_api_key_set,
    clear_api_key,
    load_from_environment,
    get_status,
    get_config
)

# Package imports
from . import places

# Version information
__version__ = "1.0.2"
__author__ = "Chandan Gowda"
__email__ = "chandangowdatk23@gmail.com"

# Package exports
__all__ = [
    # Global configuration
    "set_api_key",
    "get_api_key", 
    "is_api_key_set",
    "clear_api_key",
    "load_from_environment",
    "get_status",
    "get_config",
    
    # Packages
    "places",
    
    # Version info
    "__version__",
    "__author__",
    "__email__"
]
