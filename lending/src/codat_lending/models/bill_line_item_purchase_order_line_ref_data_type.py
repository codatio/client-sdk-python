from __future__ import annotations

from enum import Enum


class BillLineItemPurchaseOrderLineRefDataType(str, Enum):
    """BillLineItemPurchaseOrderLineRefDataType enum (lifted from inline OAS enum)."""
    PURCHASE_ORDERS = 'purchaseOrders'
    BILLS = 'bills'
