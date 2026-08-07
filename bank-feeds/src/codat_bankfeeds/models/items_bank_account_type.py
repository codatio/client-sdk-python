from __future__ import annotations

from enum import Enum


class ItemsBankAccountType(str, Enum):
    """ItemsBankAccountType enum (lifted from inline OAS enum)."""
    UNKNOWN = 'Unknown'
    CREDIT = 'Credit'
    DEBIT = 'Debit'
