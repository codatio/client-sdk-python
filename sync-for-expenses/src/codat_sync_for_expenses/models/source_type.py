from __future__ import annotations

from enum import Enum


class SourceType(str, Enum):
    """SourceType enum (lifted from inline OAS enum)."""
    ACCOUNTING = 'Accounting'
    BANKING = 'Banking'
    BANK_FEED = 'BankFeed'
    COMMERCE = 'Commerce'
    EXPENSE = 'Expense'
    OTHER = 'Other'
    UNKNOWN = 'Unknown'
