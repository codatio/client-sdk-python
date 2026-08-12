from __future__ import annotations

from enum import Enum


class RecordLineReferenceDataType(str, Enum):
    """RecordLineReferenceDataType enum (lifted from inline OAS enum)."""
    PURCHASE_ORDERS = 'purchaseOrders'
    BILLS = 'bills'
