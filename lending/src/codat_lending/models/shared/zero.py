from __future__ import annotations

from enum import Enum


class ZeroDataType(str, Enum):
    """Speakeasy-name compat for RecordLineReferenceDataType (matched by value set)."""
    PURCHASE_ORDERS = 'purchaseOrders'
    BILLS = 'bills'
