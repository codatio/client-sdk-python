from __future__ import annotations

from enum import Enum


class AccountType(str, Enum):
    """AccountType enum (lifted from inline OAS enum)."""
    ASSET = 'Asset'
    EQUITY = 'Equity'
    EXPENSE = 'Expense'
    INCOME = 'Income'
    LIABILITY = 'Liability'
    UNKNOWN = 'Unknown'
