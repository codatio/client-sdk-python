from __future__ import annotations

from enum import Enum


class BillDataType(str, Enum):
    """BillDataType enum (lifted from inline OAS enum)."""
    TRACKING_CATEGORIES = 'trackingCategories'
    CUSTOMERS = 'customers'
