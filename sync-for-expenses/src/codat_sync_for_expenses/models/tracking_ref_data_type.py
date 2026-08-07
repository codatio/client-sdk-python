from __future__ import annotations

from enum import Enum


class TrackingRefDataType(str, Enum):
    """TrackingRefDataType enum (lifted from inline OAS enum)."""
    TRACKING_CATEGORIES = 'trackingCategories'
    CUSTOMERS = 'customers'
