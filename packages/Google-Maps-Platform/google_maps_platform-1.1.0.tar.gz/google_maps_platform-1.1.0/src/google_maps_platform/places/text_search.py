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
    using natural language queries with built-in pagination support.
    """
    
    # Constants
    MAX_PAGE_SIZE = 20  # Google Places API limit
    ALL_PAGES = -1  # Special value to fetch all available pages
    NEXT_PAGE_TOKEN_FIELD = "nextPageToken"
    
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
    
    def _prepare_field_mask_for_pagination(self, field_mask: str) -> str:
        """
        Prepare field mask for pagination by ensuring nextPageToken is included.
        
        Args:
            field_mask: The original field mask
            
        Returns:
            Field mask with nextPageToken included if not already present
        """
        # Validate and clean field mask
        field_mask = self.validate_field_mask(field_mask)
        
        # Ensure nextPageToken is included for pagination
        if self.NEXT_PAGE_TOKEN_FIELD not in field_mask:
            field_mask = f"{field_mask},{self.NEXT_PAGE_TOKEN_FIELD}"
        
        return field_mask
    
    def _validate_pagination_params(self, number_of_pages: int) -> None:
        """
        Validate pagination parameters.
        
        Args:
            number_of_pages: Number of pages to fetch
            
        Raises:
            ValueError: If pagination parameters are invalid
        """
        if number_of_pages == 0:
            raise ValueError("number_of_pages must be greater than 0 or -1 for all pages")
        
        if number_of_pages < self.ALL_PAGES:
            raise ValueError(f"number_of_pages must be {self.ALL_PAGES} (all pages) or a positive integer")
    
    def _build_request_body(
        self,
        text_query: str,
        page_token: Optional[str] = None,
        included_type: Optional[str] = None,
        include_pure_service_area_businesses: Optional[bool] = None,
        language_code: Optional[str] = None,
        location_bias: Optional[Dict] = None,
        location_restriction: Optional[Dict] = None,
        ev_options: Optional[Dict] = None,
        min_rating: Optional[float] = None,
        open_now: Optional[bool] = None,
        page_size: Optional[int] = None,
        price_levels: Optional[List[str]] = None,
        rank_preference: Optional[str] = None,
        region_code: Optional[str] = None,
        strict_type_filtering: Optional[bool] = None
    ) -> Dict:
        """
        Build request body for a single page request.
        
        Args:
            text_query: The text query to search for
            page_token: Token for pagination (optional)
            **kwargs: Other optional parameters
            
        Returns:
            Request body dictionary
        """
        request_body = {"textQuery": text_query}
        
        # Add pagination token if available
        if page_token:
            request_body["pageToken"] = page_token
        
        # Add optional parameters if provided
        optional_params = {
            "includedType": included_type,
            "includePureServiceAreaBusinesses": include_pure_service_area_businesses,
            "languageCode": language_code,
            "locationBias": location_bias,
            "locationRestriction": location_restriction,
            "evOptions": ev_options,
            "minRating": min_rating,
            "openNow": open_now,
            "pageSize": min(page_size, self.MAX_PAGE_SIZE) if page_size else None,
            "priceLevels": price_levels,
            "rankPreference": rank_preference,
            "regionCode": region_code,
            "strictTypeFiltering": strict_type_filtering
        }
        
        # Add non-None parameters
        for key, value in optional_params.items():
            if value is not None:
                request_body[key] = value
        
        return request_body
    
    def _fetch_single_page(
        self,
        text_query: str,
        field_mask: str,
        page_token: Optional[str] = None,
        language_code: Optional[str] = None,
        region_code: Optional[str] = None,
        **kwargs
    ) -> Optional[Dict]:
        """
        Fetch a single page of results.
        
        Args:
            text_query: The text query to search for
            field_mask: Fields to return
            page_token: Token for pagination (optional)
            language_code: Language for results (optional)
            region_code: Region code for results (optional)
            **kwargs: Other optional parameters
            
        Returns:
            Single page result or None if failed
        """
        # Build request body
        request_body = self._build_request_body(
            text_query=text_query,
            page_token=page_token,
            **kwargs
        )
        
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
    
    def _extract_page_data(self, page_result: Dict) -> tuple[List[Dict], List[Dict], Optional[str]]:
        """
        Extract places, attributions, and next page token from a page result.
        
        Args:
            page_result: The result from a single page request
            
        Returns:
            Tuple of (places, attributions, next_page_token)
        """
        places = page_result.get("places", [])
        attributions = page_result.get("attributions", [])
        next_page_token = page_result.get(self.NEXT_PAGE_TOKEN_FIELD)
        
        return places, attributions, next_page_token
    
    def _build_final_result(
        self,
        all_places: List[Dict],
        all_attributions: List[Dict],
        page_count: int,
        has_more_pages: bool
    ) -> Optional[Dict]:
        """
        Build the final result dictionary.
        
        Args:
            all_places: All places from all pages
            all_attributions: All attributions from all pages
            page_count: Number of pages fetched
            has_more_pages: Whether more pages are available
            
        Returns:
            Final result dictionary or None if no places found
        """
        if not all_places:
            return None
        
        result = {"places": all_places}
        
        # Add attributions if any
        if all_attributions:
            result["attributions"] = all_attributions
        
        # Add pagination info
        result["pagination_info"] = {
            "pages_fetched": page_count,
            "total_places": len(all_places),
            "has_more_pages": has_more_pages
        }
        
        return result
    
    def _execute_paginated_search(
        self,
        text_query: str,
        field_mask: str,
        number_of_pages: int,
        **kwargs
    ) -> Optional[Dict]:
        """
        Execute the paginated search logic.
        
        Args:
            text_query: The text query to search for
            field_mask: Fields to return
            number_of_pages: Number of pages to fetch
            **kwargs: Other optional parameters
            
        Returns:
            Combined results from all pages or None if failed
        """
        # Initialize results storage
        all_places = []
        all_attributions = []
        page_count = 0
        next_page_token = None
        
        # Determine pagination strategy
        max_pages = number_of_pages if number_of_pages > 0 else float('inf')
        fetch_all_pages = (number_of_pages == self.ALL_PAGES)
        
        # Fetch pages
        while page_count < max_pages:
            # Fetch single page
            page_result = self._fetch_single_page(
                text_query=text_query,
                field_mask=field_mask,
                page_token=next_page_token,
                **kwargs
            )
            
            # Check if request failed
            if page_result is None:
                break
            
            # Extract data from current page
            places, attributions, next_page_token = self._extract_page_data(page_result)
            
            # Add to accumulated results
            all_places.extend(places)
            all_attributions.extend(attributions)
            page_count += 1
            
            # Break if no more pages or reached desired count
            if not next_page_token or (not fetch_all_pages and page_count >= number_of_pages):
                break
        
        # Build and return final result
        return self._build_final_result(
            all_places=all_places,
            all_attributions=all_attributions,
            page_count=page_count,
            has_more_pages=next_page_token is not None
        )
    
    def search(
        self,
        text_query: str,
        field_mask: str,
        number_of_pages: int = 1,
        included_type: Optional[str] = None,
        include_pure_service_area_businesses: Optional[bool] = None,
        language_code: Optional[str] = None,
        location_bias: Optional[Dict] = None,
        location_restriction: Optional[Dict] = None,
        ev_options: Optional[Dict] = None,
        min_rating: Optional[float] = None,
        open_now: Optional[bool] = None,
        page_size: Optional[int] = None,
        price_levels: Optional[List[str]] = None,
        rank_preference: Optional[str] = None,
        region_code: Optional[str] = None,
        strict_type_filtering: Optional[bool] = None
    ) -> Optional[Dict]:
        """
        Search places using text query with pagination support
        
        Args:
            text_query: The text query to search for (required)
            field_mask: Fields to return (required) - nextPageToken is automatically added
            number_of_pages: Number of pages to fetch (default: 1, use -1 for all pages)
            included_type: Filter by place type (optional)
            include_pure_service_area_businesses: Include service area businesses (optional)
            language_code: Language for results (optional)
            location_bias: Bias results toward a location (optional)
            location_restriction: Restrict results to a specific area (optional)
            ev_options: Electric vehicle charging options (optional)
            min_rating: Minimum rating filter (optional)
            open_now: Filter for places currently open (optional)
            page_size: Number of results per page (optional, max 20)
            price_levels: Price level filters (optional)
            rank_preference: How to rank results (optional)
            region_code: Region code for results (optional)
            strict_type_filtering: Strict type filtering (optional)
            
        Returns:
            Dictionary containing search results with all pages combined or None if failed
            
        Example:
            # Basic text search (single page)
            text_search = TextSearch()
            results = text_search.search(
                text_query="restaurants in San Francisco",
                field_mask="places.id,places.displayName,places.rating"
            )
            
            # Multi-page search
            results = text_search.search(
                text_query="pizza in New York",
                field_mask="places.id,places.displayName,places.rating,places.priceLevel",
                number_of_pages=3,
                page_size=20
            )
            
            # Get all available pages
            results = text_search.search(
                text_query="coffee shops",
                field_mask="places.id,places.displayName",
                number_of_pages=-1  # -1 means all pages
            )
        """
        # Validate and prepare field mask
        field_mask = self._prepare_field_mask_for_pagination(field_mask)
        
        # Validate pagination parameters
        self._validate_pagination_params(number_of_pages)
        
        # Execute paginated search
        return self._execute_paginated_search(
            text_query=text_query,
            field_mask=field_mask,
            number_of_pages=number_of_pages,
            included_type=included_type,
            include_pure_service_area_businesses=include_pure_service_area_businesses,
            language_code=language_code,
            location_bias=location_bias,
            location_restriction=location_restriction,
            ev_options=ev_options,
            min_rating=min_rating,
            open_now=open_now,
            page_size=page_size,
            price_levels=price_levels,
            rank_preference=rank_preference,
            region_code=region_code,
            strict_type_filtering=strict_type_filtering
        )
    
