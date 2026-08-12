from __future__ import annotations

from enum import Enum


class BankAccountType(str, Enum):
    """BankAccountType enum (lifted from inline OAS enum)."""
    UNKNOWN = 'Unknown'
    CREDIT = 'Credit'
    DEBIT = 'Debit'
