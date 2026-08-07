from __future__ import annotations

from enum import Enum


class BankAccountCreateResponseBankAccountType(str, Enum):
    """BankAccountCreateResponseBankAccountType enum (lifted from inline OAS enum)."""
    UNKNOWN = 'Unknown'
    CREDIT = 'Credit'
    DEBIT = 'Debit'
