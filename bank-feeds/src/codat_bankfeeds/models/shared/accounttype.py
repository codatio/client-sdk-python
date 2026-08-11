from __future__ import annotations

from enum import Enum


class AccountType(str, Enum):
    """AccountType enum (lifted from inline OAS enum)."""
    CHECKING = 'checking'
    SAVINGS = 'savings'
    LOAN = 'loan'
    CREDIT_CARD = 'creditCard'
    PREPAID_CARD = 'prepaidCard'
