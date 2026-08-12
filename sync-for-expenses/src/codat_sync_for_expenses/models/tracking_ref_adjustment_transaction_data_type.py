from __future__ import annotations

from enum import Enum


class TrackingRefAdjustmentTransactionDataType(str, Enum):
    """TrackingRefAdjustmentTransactionDataType enum (lifted from inline OAS enum)."""
    TRACKING_CATEGORIES = 'trackingCategories'
    CUSTOMERS = 'customers'
    SUPPLIERS = 'suppliers'
