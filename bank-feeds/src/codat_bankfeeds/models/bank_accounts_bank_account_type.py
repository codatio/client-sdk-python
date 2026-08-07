from __future__ import annotations

from enum import Enum


class BankAccountsBankAccountType(str, Enum):
    """BankAccountsBankAccountType enum (lifted from inline OAS enum)."""
    UNKNOWN = 'Unknown'
    CREDIT = 'Credit'
    DEBIT = 'Debit'
