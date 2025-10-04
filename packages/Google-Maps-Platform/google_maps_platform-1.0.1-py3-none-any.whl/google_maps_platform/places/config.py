"""
Configuration Management for Google Places API

This module provides global configuration management for the Google Places API client.
It allows setting the API key once and using it across all modules.
"""

import os
from typing import Optional


class APIConfig:
    """
    Global API configuration manager
    
    This class manages the global API key and other configuration settings
    that are shared across all Google Places API modules.
    """
    
    _instance = None
    _api_key: Optional[str] = None
    
    def __new__(cls):
        """Singleton pattern to ensure only one configuration instance"""
        if cls._instance is None:
            cls._instance = super(APIConfig, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize the configuration manager"""
        if not hasattr(self, '_initialized'):
            self._api_key = None
            self._initialized = True
    
    def set_api_key(self, api_key: str) -> None:
        """
        Set the global API key
        
        Args:
            api_key: Google Places API key
        """
        if not api_key:
            raise ValueError("API key cannot be empty")
        
        self._api_key = api_key
        print(f"✅ API key set successfully")
    
    def get_api_key(self) -> Optional[str]:
        """
        Get the current API key
        
        Returns:
            Current API key or None if not set
        """
        return self._api_key
    
    def is_api_key_set(self) -> bool:
        """
        Check if API key is set
        
        Returns:
            True if API key is set, False otherwise
        """
        return self._api_key is not None
    
    def clear_api_key(self) -> None:
        """Clear the current API key"""
        self._api_key = None
        print("🗑️ API key cleared")
    
    def load_from_environment(self, env_var: str = "GOOGLE_PLACES_API_KEY") -> bool:
        """
        Load API key from environment variable
        
        Args:
            env_var: Environment variable name to load from
            
        Returns:
            True if API key was loaded successfully, False otherwise
        """
        api_key = os.getenv(env_var)
        if api_key:
            self.set_api_key(api_key)
            return True
        return False
    
    def get_status(self) -> dict:
        """
        Get configuration status
        
        Returns:
            Dictionary with configuration status
        """
        return {
            "api_key_set": self.is_api_key_set(),
            "api_key_preview": f"{self._api_key[:8]}..." if self._api_key else None
        }


# Global configuration instance
config = APIConfig()


def set_api_key(api_key: str) -> None:
    """
    Set the global API key (convenience function)
    
    Args:
        api_key: Google Places API key
    """
    config.set_api_key(api_key)


def get_api_key() -> Optional[str]:
    """
    Get the current API key (convenience function)
    
    Returns:
        Current API key or None if not set
    """
    return config.get_api_key()


def is_api_key_set() -> bool:
    """
    Check if API key is set (convenience function)
    
    Returns:
        True if API key is set, False otherwise
    """
    return config.is_api_key_set()


def clear_api_key() -> None:
    """Clear the current API key (convenience function)"""
    config.clear_api_key()


def load_from_environment(env_var: str = "GOOGLE_PLACES_API_KEY") -> bool:
    """
    Load API key from environment variable (convenience function)
    
    Args:
        env_var: Environment variable name to load from
        
    Returns:
        True if API key was loaded successfully, False otherwise
    """
    return config.load_from_environment(env_var)


def get_status() -> dict:
    """
    Get configuration status (convenience function)
    
    Returns:
        Dictionary with configuration status
    """
    return config.get_status()
