from __future__ import annotations

from enum import Enum


class BillLineItemDataType(str, Enum):
    """Compat name for RecordLineReferenceDataType (matched by value set)."""
    PURCHASE_ORDERS = 'purchaseOrders'
    BILLS = 'bills'
