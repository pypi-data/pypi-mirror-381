"""
Field Masks for Google Places API

This module provides comprehensive field mask information and utilities
for the Google Places API (New) text search and nearby search endpoints.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class FieldMaskCategory:
    """Represents a category of field masks"""
    name: str
    description: str
    fields: List[str]
    use_case: str


class FieldMaskManager:
    """
    Manager for Google Places API field masks
    
    Provides utilities to view, categorize, and build field masks
    for different use cases.
    """
    
    def __init__(self):
        """Initialize the field mask manager with all available fields"""
        self.all_fields = [
            "places.attributions",
            "places.id",
            "places.name*",
            "nextPageToken",
            "places.accessibilityOptions",
            "places.addressComponents",
            "places.addressDescriptor*",
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
            "routingSummaries*",
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
        
        self.categories = self._create_categories()
    
    def _create_categories(self) -> List[FieldMaskCategory]:
        """Create categorized field masks"""
        return [
            FieldMaskCategory(
                name="Basic Information",
                description="Essential place information",
                fields=[
                    "places.id",
                    "places.displayName",
                    "places.formattedAddress",
                    "places.location",
                    "places.types",
                    "places.primaryType",
                    "places.primaryTypeDisplayName"
                ],
                use_case="Basic place identification and location"
            ),
            FieldMaskCategory(
                name="Contact Information",
                description="Contact details and communication",
                fields=[
                    "places.internationalPhoneNumber",
                    "places.nationalPhoneNumber",
                    "places.websiteUri",
                    "places.googleMapsUri",
                    "places.googleMapsLinks"
                ],
                use_case="Getting contact information and directions"
            ),
            FieldMaskCategory(
                name="Ratings & Reviews",
                description="User ratings and review information",
                fields=[
                    "places.rating",
                    "places.userRatingCount",
                    "places.reviews",
                    "places.reviewSummary",
                    "places.editorialSummary",
                    "places.generativeSummary"
                ],
                use_case="Understanding place quality and user feedback"
            ),
            FieldMaskCategory(
                name="Pricing Information",
                description="Price levels and cost information",
                fields=[
                    "places.priceLevel",
                    "places.priceRange"
                ],
                use_case="Budget planning and cost estimation"
            ),
            FieldMaskCategory(
                name="Operating Hours",
                description="Business hours and availability",
                fields=[
                    "places.currentOpeningHours",
                    "places.currentSecondaryOpeningHours",
                    "places.regularOpeningHours",
                    "places.regularSecondaryOpeningHours",
                    "places.utcOffsetMinutes"
                ],
                use_case="Checking when places are open"
            ),
            FieldMaskCategory(
                name="Visual Content",
                description="Photos and visual information",
                fields=[
                    "places.photos",
                    "places.iconBackgroundColor",
                    "places.iconMaskBaseUri"
                ],
                use_case="Displaying visual content and place icons"
            ),
            FieldMaskCategory(
                name="Address Details",
                description="Detailed address information",
                fields=[
                    "places.addressComponents",
                    "places.addressDescriptor*",
                    "places.adrFormatAddress",
                    "places.postalAddress",
                    "places.shortFormattedAddress",
                    "places.plusCode",
                    "places.viewport"
                ],
                use_case="Detailed address parsing and mapping"
            ),
            FieldMaskCategory(
                name="Business Information",
                description="Business status and characteristics",
                fields=[
                    "places.businessStatus",
                    "places.pureServiceAreaBusiness",
                    "places.containingPlaces",
                    "places.subDestinations"
                ],
                use_case="Understanding business operations and relationships"
            ),
            FieldMaskCategory(
                name="Dining & Food Services",
                description="Restaurant and food service features",
                fields=[
                    "places.servesBreakfast",
                    "places.servesBrunch",
                    "places.servesLunch",
                    "places.servesDinner",
                    "places.servesCoffee",
                    "places.servesDessert",
                    "places.servesVegetarianFood",
                    "places.servesBeer",
                    "places.servesWine",
                    "places.servesCocktails",
                    "places.menuForChildren",
                    "places.dineIn",
                    "places.takeout",
                    "places.delivery",
                    "places.curbsidePickup"
                ],
                use_case="Restaurant and food service planning"
            ),
            FieldMaskCategory(
                name="Amenities & Features",
                description="Place amenities and special features",
                fields=[
                    "places.outdoorSeating",
                    "places.parkingOptions",
                    "places.restroom",
                    "places.allowsDogs",
                    "places.goodForChildren",
                    "places.goodForGroups",
                    "places.goodForWatchingSports",
                    "places.liveMusic",
                    "places.reservable"
                ],
                use_case="Understanding place amenities and features"
            ),
            FieldMaskCategory(
                name="Payment & Services",
                description="Payment methods and service options",
                fields=[
                    "places.paymentOptions"
                ],
                use_case="Payment and service planning"
            ),
            FieldMaskCategory(
                name="Electric Vehicle Support",
                description="EV charging and fuel options",
                fields=[
                    "places.evChargeOptions",
                    "places.evChargeAmenitySummary",
                    "places.fuelOptions"
                ],
                use_case="Electric vehicle trip planning"
            ),
            FieldMaskCategory(
                name="Location Context",
                description="Neighborhood and area information",
                fields=[
                    "places.neighborhoodSummary"
                ],
                use_case="Understanding local context and area"
            ),
            FieldMaskCategory(
                name="System Fields",
                description="System and pagination fields",
                fields=[
                    "places.attributions",
                    "nextPageToken",
                    "routingSummaries*"
                ],
                use_case="System requirements and pagination"
            )
        ]
    
    def get_all_fields(self) -> List[str]:
        """Get all available field masks"""
        return self.all_fields.copy()
    
    def get_categories(self) -> List[FieldMaskCategory]:
        """Get all field mask categories"""
        return self.categories.copy()
    
    def get_fields_by_category(self, category_name: str) -> Optional[List[str]]:
        """Get fields for a specific category"""
        for category in self.categories:
            if category.name.lower() == category_name.lower():
                return category.fields.copy()
        return None
    
    def get_category_info(self, category_name: str) -> Optional[FieldMaskCategory]:
        """Get full category information"""
        for category in self.categories:
            if category.name.lower() == category_name.lower():
                return category
        return None
    
    def build_field_mask(self, categories: List[str] = None, fields: List[str] = None) -> str:
        """
        Build a field mask from categories or specific fields
        
        Args:
            categories: List of category names to include
            fields: List of specific fields to include
            
        Returns:
            Comma-separated field mask string
        """
        selected_fields = set()
        
        if categories:
            for category_name in categories:
                category_fields = self.get_fields_by_category(category_name)
                if category_fields:
                    selected_fields.update(category_fields)
        
        if fields:
            selected_fields.update(fields)
        
        return ",".join(sorted(selected_fields))
    
    def get_predefined_masks(self) -> Dict[str, str]:
        """Get predefined field masks for common use cases"""
        return {
            "basic": self.build_field_mask(categories=["Basic Information"]),
            "contact": self.build_field_mask(categories=["Basic Information", "Contact Information"]),
            "reviews": self.build_field_mask(categories=["Basic Information", "Ratings & Reviews"]),
            "restaurant": self.build_field_mask(categories=[
                "Basic Information", "Contact Information", "Ratings & Reviews", 
                "Pricing Information", "Operating Hours", "Dining & Food Services",
                "Amenities & Features"
            ]),
            "hotel": self.build_field_mask(categories=[
                "Basic Information", "Contact Information", "Ratings & Reviews",
                "Pricing Information", "Operating Hours", "Amenities & Features",
                "Payment & Services"
            ]),
            "attraction": self.build_field_mask(categories=[
                "Basic Information", "Contact Information", "Ratings & Reviews",
                "Operating Hours", "Visual Content", "Amenities & Features"
            ]),
            "comprehensive": self.build_field_mask(fields=self.all_fields)
        }
    
    def print_all_fields(self):
        """Print all available fields in a formatted way"""
        print("🔍 Google Places API Field Masks")
        print("=" * 50)
        print(f"Total fields available: {len(self.all_fields)}")
        print()
        
        for i, field in enumerate(self.all_fields, 1):
            print(f"{i:2d}. {field}")
    
    def print_categories(self):
        """Print all categories with their fields"""
        print("📂 Field Mask Categories")
        print("=" * 50)
        
        for category in self.categories:
            print(f"\n📁 {category.name}")
            print(f"   Description: {category.description}")
            print(f"   Use Case: {category.use_case}")
            print(f"   Fields ({len(category.fields)}):")
            for field in category.fields:
                print(f"     • {field}")
    
    def print_predefined_masks(self):
        """Print predefined field masks"""
        print("🎯 Predefined Field Masks")
        print("=" * 50)
        
        masks = self.get_predefined_masks()
        for name, mask in masks.items():
            print(f"\n{name.upper()}:")
            print(f"  {mask}")
    
    def search_fields(self, query: str) -> List[str]:
        """Search for fields containing a specific term"""
        query_lower = query.lower()
        matching_fields = []
        
        for field in self.all_fields:
            if query_lower in field.lower():
                matching_fields.append(field)
        
        return matching_fields
    
    def get_field_info(self, field: str) -> Dict[str, str]:
        """Get information about a specific field"""
        # Find which category contains this field
        for category in self.categories:
            if field in category.fields:
                return {
                    "field": field,
                    "category": category.name,
                    "description": category.description,
                    "use_case": category.use_case
                }
        
        return {
            "field": field,
            "category": "Unknown",
            "description": "Field not found in categories",
            "use_case": "Unknown"
        }


# Convenience functions
def get_field_mask_manager() -> FieldMaskManager:
    """Get a FieldMaskManager instance"""
    return FieldMaskManager()


def print_field_masks():
    """Print all field masks in a formatted way"""
    manager = get_field_mask_manager()
    manager.print_all_fields()


def print_field_categories():
    """Print all field mask categories"""
    manager = get_field_mask_manager()
    manager.print_categories()


def get_restaurant_field_mask() -> str:
    """Get field mask optimized for restaurant searches"""
    manager = get_field_mask_manager()
    return manager.get_predefined_masks()["restaurant"]


def get_hotel_field_mask() -> str:
    """Get field mask optimized for hotel searches"""
    manager = get_field_mask_manager()
    return manager.get_predefined_masks()["hotel"]


def get_attraction_field_mask() -> str:
    """Get field mask optimized for attraction searches"""
    manager = get_field_mask_manager()
    return manager.get_predefined_masks()["attraction"]
