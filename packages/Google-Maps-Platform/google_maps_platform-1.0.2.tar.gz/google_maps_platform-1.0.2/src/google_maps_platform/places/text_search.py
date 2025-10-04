"""
Text Search Module for Google Places API

This module contains the Text Search functionality for Google Places API (New).
It implements the searchText endpoint for searching places using text queries.

This module is completely independent and can be used standalone.
"""

from typing import Dict, List, Optional
from .shared_utils import APIRequestHandler, FieldMaskHelper


class TextSearch:
    """
    Text Search functionality for Google Places API (New)
    
    This class provides text-based search capabilities for finding places
    using natural language queries.
    """
    
    # All available field masks for text search
    AVAILABLE_FIELD_MASKS = [
        "places.attributions",
        "places.id",
        "places.name",
        "nextPageToken",
        "places.accessibilityOptions",
        "places.addressComponents",
        "places.addressDescriptor",
        "places.adrFormatAddress",
        "places.businessStatus",
        "places.containingPlaces",
        "places.displayName",
        "places.formattedAddress",
        "places.googleMapsLinks",
        "places.googleMapsUri",
        "places.iconBackgroundColor",
        "places.iconMaskBaseUri",
        "places.location",
        "places.photos",
        "places.plusCode",
        "places.postalAddress",
        "places.primaryType",
        "places.primaryTypeDisplayName",
        "places.pureServiceAreaBusiness",
        "places.shortFormattedAddress",
        "places.subDestinations",
        "places.types",
        "places.utcOffsetMinutes",
        "places.viewport",
        "places.currentOpeningHours",
        "places.currentSecondaryOpeningHours",
        "places.internationalPhoneNumber",
        "places.nationalPhoneNumber",
        "places.priceLevel",
        "places.priceRange",
        "places.rating",
        "places.regularOpeningHours",
        "places.regularSecondaryOpeningHours",
        "places.userRatingCount",
        "places.websiteUri",
        "places.allowsDogs",
        "places.curbsidePickup",
        "places.delivery",
        "places.dineIn",
        "places.editorialSummary",
        "places.evChargeAmenitySummary",
        "places.evChargeOptions",
        "places.fuelOptions",
        "places.generativeSummary",
        "places.goodForChildren",
        "places.goodForGroups",
        "places.goodForWatchingSports",
        "places.liveMusic",
        "places.menuForChildren",
        "places.neighborhoodSummary",
        "places.parkingOptions",
        "places.paymentOptions",
        "places.outdoorSeating",
        "places.reservable",
        "places.restroom",
        "places.reviews",
        "places.reviewSummary",
        "routingSummaries",
        "places.servesBeer",
        "places.servesBreakfast",
        "places.servesBrunch",
        "places.servesCocktails",
        "places.servesCoffee",
        "places.servesDessert",
        "places.servesDinner",
        "places.servesLunch",
        "places.servesVegetarianFood",
        "places.servesWine",
        "places.takeout"
    ]
    
    def __init__(self, api_key: str = None):
        """
        Initialize the Text Search client
        
        Args:
            api_key: Google Places API key (optional, uses global config if not provided)
        """
        self.api_handler = APIRequestHandler(api_key)
        self.field_helper = FieldMaskHelper()
        self.search_url = f"{self.api_handler.base_url}/places:searchText"
    
    def list_field_masks(self) -> None:
        """
        Print all available field masks for text search
        """
        print("Available field masks for text search:")
        print("=" * 50)
        for i, field_mask in enumerate(self.AVAILABLE_FIELD_MASKS, 1):
            print(f"{i:2d}. {field_mask}")
        print(f"\nTotal: {len(self.AVAILABLE_FIELD_MASKS)} field masks")
    
    def validate_field_mask(self, field_mask: str) -> str:
        """
        Validate field mask and return cleaned version
        
        Args:
            field_mask: Field mask to validate (spaces around commas will be removed)
            
        Returns:
            Cleaned and validated field mask (no spaces around commas)
            
        Raises:
            ValueError: If field mask contains invalid fields
        """
        if not field_mask:
            return ""
        
        # Split by comma and clean each field
        fields = [field.strip() for field in field_mask.split(',')]
        valid_fields = []
        invalid_fields = []
        
        for field in fields:
            if field in self.AVAILABLE_FIELD_MASKS:
                valid_fields.append(field)
            else:
                invalid_fields.append(field)
        
        if invalid_fields:
            raise ValueError(
                f"Invalid field masks: {', '.join(invalid_fields)}\n"
                f"Available field masks: {', '.join(self.AVAILABLE_FIELD_MASKS[:10])}..."
            )
        
        # Return without spaces around commas (Google API requirement)
        return ','.join(valid_fields)
    
    def search(
        self,
        text_query: str,
        field_mask: Optional[str] = None,
        included_type: Optional[str] = None,
        include_pure_service_area_businesses: Optional[bool] = None,
        language_code: Optional[str] = None,
        location_bias: Optional[Dict] = None,
        location_restriction: Optional[Dict] = None,
        ev_options: Optional[Dict] = None,
        min_rating: Optional[float] = None,
        open_now: Optional[bool] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        price_levels: Optional[List[str]] = None,
        rank_preference: Optional[str] = None,
        region_code: Optional[str] = None,
        strict_type_filtering: Optional[bool] = None
    ) -> Optional[Dict]:
        """
        Search places using text query
        
        Args:
            text_query: The text query to search for (required)
            field_mask: Fields to return (optional, uses default if None)
            included_type: Filter by place type (optional)
            include_pure_service_area_businesses: Include service area businesses (optional)
            language_code: Language for results (optional)
            location_bias: Bias results toward a location (optional)
            location_restriction: Restrict results to a specific area (optional)
            ev_options: Electric vehicle charging options (optional)
            min_rating: Minimum rating filter (optional)
            open_now: Filter for places currently open (optional)
            page_size: Number of results per page (optional, max 20)
            page_token: Token for pagination (optional)
            price_levels: Price level filters (optional)
            rank_preference: How to rank results (optional)
            region_code: Region code for results (optional)
            strict_type_filtering: Strict type filtering (optional)
            
        Returns:
            Dictionary containing search results or None if failed
            
        Example:
            # Basic text search
            text_search = TextSearch("your_api_key")
            results = text_search.search("restaurants in San Francisco")
            
            # Advanced text search with filters
            results = text_search.search(
                text_query="Italian restaurants in San Francisco",
                field_mask=text_search.get_restaurant_field_mask(),
                min_rating=4.0,
                price_levels=["PRICE_LEVEL_MODERATE"],
                page_size=10
            )
        """
        # Set default field mask if not provided
        if field_mask is None:
            field_mask = "places.attributions,places.id,places.displayName,nextPageToken"
        else:
            # Validate field mask if provided
            field_mask = self.validate_field_mask(field_mask)
        
        # Build request body with required parameters
        request_body = {
            "textQuery": text_query
        }
        
        # Add optional parameters if provided
        if included_type:
            request_body["includedType"] = included_type
        if include_pure_service_area_businesses is not None:
            request_body["includePureServiceAreaBusinesses"] = include_pure_service_area_businesses
        if language_code:
            request_body["languageCode"] = language_code
        if location_bias:
            request_body["locationBias"] = location_bias
        if location_restriction:
            request_body["locationRestriction"] = location_restriction
        if ev_options:
            request_body["evOptions"] = ev_options
        if min_rating is not None:
            request_body["minRating"] = min_rating
        if open_now is not None:
            request_body["openNow"] = open_now
        if page_size is not None:
            request_body["pageSize"] = min(page_size, 20)  # API limit
        if page_token:
            request_body["pageToken"] = page_token
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
    
