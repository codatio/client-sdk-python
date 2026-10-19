from __future__ import annotations

from enum import Enum


class TrackingRecordRefDataType(str, Enum):
    """Compat name for JournalLineTrackingDataType (matched by value set)."""
    CUSTOMERS = 'customers'
    SUPPLIERS = 'suppliers'
    TRACKING_CATEGORIES = 'trackingCategories'
