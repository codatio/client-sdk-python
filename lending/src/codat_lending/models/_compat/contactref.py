from __future__ import annotations

from enum import Enum


class ContactRefDataType(str, Enum):
    """Compat name for AccountingJournalEntryDataType (matched by value set)."""
    CUSTOMERS = 'customers'
    SUPPLIERS = 'suppliers'
