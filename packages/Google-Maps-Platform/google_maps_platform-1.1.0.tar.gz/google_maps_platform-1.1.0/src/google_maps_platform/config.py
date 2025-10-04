"""
Global Configuration Management for Google Maps Platform

This module provides global configuration management for all Google Maps Platform packages.
It allows setting the API key once and using it across all packages (places, routes, environment, etc.).
"""

import os
from typing import Optional, Dict, Any


class GoogleMapsPlatformConfig:
    """
    Global configuration manager for Google Maps Platform
    
    This class manages the global API key and other configuration settings
    that are shared across all Google Maps Platform packages.
    """
    
    _instance = None
    _api_key: Optional[str] = None
    _packages: Dict[str, Any] = {}
    
    def __new__(cls):
        """Singleton pattern to ensure only one configuration instance"""
        if cls._instance is None:
            cls._instance = super(GoogleMapsPlatformConfig, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize the configuration manager"""
        if not hasattr(self, '_initialized'):
            self._api_key = None
            self._packages = {}
            self._initialized = True
    
    def set_api_key(self, api_key: str) -> None:
        """
        Set the global API key for all packages
        
        Args:
            api_key: Google Maps Platform API key
        """
        if not api_key:
            raise ValueError("API key cannot be empty")
        
        self._api_key = api_key
        print(f"✅ Global API key set successfully for all packages")
    
    def get_api_key(self) -> Optional[str]:
        """
        Get the current global API key
        
        Returns:
            Current global API key or None if not set
        """
        return self._api_key
    
    def is_api_key_set(self) -> bool:
        """
        Check if global API key is set
        
        Returns:
            True if API key is set, False otherwise
        """
        return self._api_key is not None
    
    def clear_api_key(self) -> None:
        """Clear the current global API key"""
        self._api_key = None
        print("🗑️ Global API key cleared")
    
    def load_from_environment(self, env_var: str = "GOOGLE_MAPS_API_KEY") -> bool:
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
    
    def register_package(self, package_name: str, package_instance: Any) -> None:
        """
        Register a package with the global configuration
        
        Args:
            package_name: Name of the package (e.g., 'places', 'routes')
            package_instance: Package instance to register
        """
        self._packages[package_name] = package_instance
        print(f"📦 Package '{package_name}' registered with global configuration")
    
    def get_package(self, package_name: str) -> Optional[Any]:
        """
        Get a registered package
        
        Args:
            package_name: Name of the package to get
            
        Returns:
            Package instance or None if not found
        """
        return self._packages.get(package_name)
    
    def get_registered_packages(self) -> Dict[str, Any]:
        """
        Get all registered packages
        
        Returns:
            Dictionary of registered packages
        """
        return self._packages.copy()
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get global configuration status
        
        Returns:
            Dictionary with configuration status
        """
        return {
            "api_key_set": self.is_api_key_set(),
            "api_key_preview": f"{self._api_key[:8]}..." if self._api_key else None,
            "registered_packages": list(self._packages.keys()),
            "total_packages": len(self._packages)
        }
    
    def get_config(self) -> Dict[str, Any]:
        """
        Get complete configuration
        
        Returns:
            Dictionary with complete configuration
        """
        return {
            "api_key": self._api_key,
            "packages": self._packages,
            "status": self.get_status()
        }


# Global configuration instance
config = GoogleMapsPlatformConfig()


def set_api_key(api_key: str) -> None:
    """
    Set the global API key for all packages (convenience function)
    
    Args:
        api_key: Google Maps Platform API key
    """
    config.set_api_key(api_key)


def get_api_key() -> Optional[str]:
    """
    Get the current global API key (convenience function)
    
    Returns:
        Current global API key or None if not set
    """
    return config.get_api_key()


def is_api_key_set() -> bool:
    """
    Check if global API key is set (convenience function)
    
    Returns:
        True if API key is set, False otherwise
    """
    return config.is_api_key_set()


def clear_api_key() -> None:
    """Clear the current global API key (convenience function)"""
    config.clear_api_key()


def load_from_environment(env_var: str = "GOOGLE_MAPS_API_KEY") -> bool:
    """
    Load API key from environment variable (convenience function)
    
    Args:
        env_var: Environment variable name to load from
        
    Returns:
        True if API key was loaded successfully, False otherwise
    """
    return config.load_from_environment(env_var)


def get_status() -> Dict[str, Any]:
    """
    Get global configuration status (convenience function)
    
    Returns:
        Dictionary with configuration status
    """
    return config.get_status()


def get_config() -> Dict[str, Any]:
    """
    Get complete configuration (convenience function)
    
    Returns:
        Dictionary with complete configuration
    """
    return config.get_config()


def register_package(package_name: str, package_instance: Any) -> None:
    """
    Register a package with the global configuration (convenience function)
    
    Args:
        package_name: Name of the package (e.g., 'places', 'routes')
        package_instance: Package instance to register
    """
    config.register_package(package_name, package_instance)


def get_package(package_name: str) -> Optional[Any]:
    """
    Get a registered package (convenience function)
    
    Args:
        package_name: Name of the package to get
        
    Returns:
        Package instance or None if not found
    """
    return config.get_package(package_name)
