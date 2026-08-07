from __future__ import annotations

from enum import Enum


class AccountingInvoiceDataType(str, Enum):
    """AccountingInvoiceDataType enum (lifted from inline OAS enum)."""
    SALES_ORDERS = 'salesOrders'
