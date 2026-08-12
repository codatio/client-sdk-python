from __future__ import annotations

from enum import Enum


class AccountingJournalEntryDataType(str, Enum):
    """AccountingJournalEntryDataType enum (lifted from inline OAS enum)."""
    CUSTOMERS = 'customers'
    SUPPLIERS = 'suppliers'
