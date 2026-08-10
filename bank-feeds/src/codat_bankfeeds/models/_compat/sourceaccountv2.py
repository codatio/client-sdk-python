from __future__ import annotations

from enum import Enum


class SourceAccountV2AccountType(str, Enum):
    """Speakeasy-name compat for AccountType (matched by value set)."""
    CHECKING = 'checking'
    SAVINGS = 'savings'
    LOAN = 'loan'
    CREDIT_CARD = 'creditCard'
    PREPAID_CARD = 'prepaidCard'
