from __future__ import annotations

from enum import Enum


class CreateBankAccountResponseBankAccountType(str, Enum):
    """Compat name for BankAccountType (matched by value set)."""
    UNKNOWN = 'Unknown'
    CREDIT = 'Credit'
    DEBIT = 'Debit'
