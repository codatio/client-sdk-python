from __future__ import annotations

from enum import Enum


class JournalLineDataType(str, Enum):
    """Speakeasy-name compat for AccountingJournalEntryDataType (matched by value set)."""
    CUSTOMERS = 'customers'
    SUPPLIERS = 'suppliers'
