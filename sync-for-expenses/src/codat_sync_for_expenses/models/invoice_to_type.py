from __future__ import annotations

from enum import Enum


class InvoiceToType(str, Enum):
    """InvoiceToType enum (lifted from inline OAS enum)."""
    CUSTOMER = 'customer'
