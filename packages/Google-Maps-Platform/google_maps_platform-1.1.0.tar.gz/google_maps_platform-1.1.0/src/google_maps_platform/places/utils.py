"""
Utilities for Google Places API Client

This module contains utility functions that are not part of the core Google Places API
but provide convenient functionality for working with the API responses.
"""

from typing import Dict, List


def format_places_data(places_data: List[Dict]) -> List[Dict]:
    """
    Format places data for easier consumption
    
    Args:
        places_data: Raw places data from API
        
    Returns:
        List of formatted place dictionaries
    """
    formatted_places = []
    for place in places_data:
        formatted_place = {
            'id': place.get('id', ''),
            'name': place.get('displayName', {}).get('text', 'N/A'),
            'address': place.get('formattedAddress', 'N/A'),
            'rating': place.get('rating', 'N/A'),
            'user_rating_count': place.get('userRatingCount', 'N/A'),
            'price_level': place.get('priceLevel', 'N/A'),
            'types': place.get('types', []),
            'website': place.get('websiteUri', 'N/A'),
            'phone': place.get('internationalPhoneNumber', 'N/A')
        }
        formatted_places.append(formatted_place)
    
    return formatted_places


def search_places_formatted(api, search_query: str, location: str, 
                           radius_meters: int = 5000, max_results: int = 20) -> List[Dict]:
    """
    Search for places and return formatted results
    
    Args:
        api: GooglePlacesAPI instance
        search_query: Text query to search for
        location: Location to search around
        radius_meters: Search radius in meters
        max_results: Maximum number of results to return
        
    Returns:
        List of formatted place dictionaries
    """
    from .parameter_builders import LocationBuilder
    
    # Create location builder to get coordinates
    location_builder = LocationBuilder(api.api_key)
    coords = location_builder.geocode_place(location)
    if coords is None:
        return []
    
    # Use nearby search with the coordinates
    result = api.nearby_search(
        location={"latitude": coords['latitude'], "longitude": coords['longitude']},
        radius=radius_meters,
        max_result_count=max_results
    )
    
    if result is None:
        return []
    
    places_data = result.get('places', [])
    return format_places_data(places_data)


def filter_places_by_rating(places: List[Dict], min_rating: float = 4.0) -> List[Dict]:
    """
    Filter places by minimum rating
    
    Args:
        places: List of place dictionaries
        min_rating: Minimum rating threshold
        
    Returns:
        Filtered list of places
    """
    filtered_places = []
    for place in places:
        rating = place.get('rating', 'N/A')
        if rating != 'N/A' and float(rating) >= min_rating:
            filtered_places.append(place)
    
    return filtered_places


def filter_places_by_price_level(places: List[Dict], max_price_level: str) -> List[Dict]:
    """
    Filter places by maximum price level
    
    Args:
        places: List of place dictionaries
        max_price_level: Maximum price level (e.g., 'PRICE_LEVEL_MODERATE')
        
    Returns:
        Filtered list of places
    """
    price_levels = {
        'PRICE_LEVEL_INEXPENSIVE': 1,
        'PRICE_LEVEL_MODERATE': 2,
        'PRICE_LEVEL_EXPENSIVE': 3,
        'PRICE_LEVEL_VERY_EXPENSIVE': 4
    }
    
    max_level = price_levels.get(max_price_level, 4)
    
    filtered_places = []
    for place in places:
        price_level = place.get('price_level', 'N/A')
        if price_level == 'N/A':
            filtered_places.append(place)
        else:
            place_level = price_levels.get(price_level, 4)
            if place_level <= max_level:
                filtered_places.append(place)
    
    return filtered_places


def sort_places_by_rating(places: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Sort places by rating
    
    Args:
        places: List of place dictionaries
        descending: If True, sort in descending order (highest first)
        
    Returns:
        Sorted list of places
    """
    def get_rating(place):
        rating = place.get('rating', 'N/A')
        return float(rating) if rating != 'N/A' else 0.0
    
    return sorted(places, key=get_rating, reverse=descending)


def get_place_summary(place: Dict) -> str:
    """
    Get a formatted summary string for a place
    
    Args:
        place: Place dictionary
        
    Returns:
        Formatted summary string
    """
    name = place.get('name', 'N/A')
    rating = place.get('rating', 'N/A')
    address = place.get('address', 'N/A')
    price_level = place.get('price_level', 'N/A')
    
    summary = f"{name}"
    if rating != 'N/A':
        summary += f" (⭐ {rating})"
    if price_level != 'N/A':
        price_symbols = {
            'PRICE_LEVEL_INEXPENSIVE': '$',
            'PRICE_LEVEL_MODERATE': '$$',
            'PRICE_LEVEL_EXPENSIVE': '$$$',
            'PRICE_LEVEL_VERY_EXPENSIVE': '$$$$'
        }
        price_symbol = price_symbols.get(price_level, price_level)
        summary += f" {price_symbol}"
    
    return summary
