from __future__ import annotations

from enum import Enum


class JournalLineTrackingDataType(str, Enum):
    """JournalLineTrackingDataType enum (lifted from inline OAS enum)."""
    CUSTOMERS = 'customers'
    SUPPLIERS = 'suppliers'
    TRACKING_CATEGORIES = 'trackingCategories'
