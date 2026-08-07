from __future__ import annotations

from enum import Enum


class ExpenseContactRefType(str, Enum):
    """Speakeasy-name compat for Type (matched by value set)."""
    SUPPLIER = 'Supplier'
