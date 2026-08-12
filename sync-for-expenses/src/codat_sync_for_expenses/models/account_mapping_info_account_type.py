from __future__ import annotations

from enum import Enum


class AccountMappingInfoAccountType(str, Enum):
    """AccountMappingInfoAccountType enum (lifted from inline OAS enum)."""
    ASSET = 'Asset'
    LIABILITY = 'Liability'
    INCOME = 'Income'
    EXPENSE = 'Expense'
    EQUITY = 'Equity'
