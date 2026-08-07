from __future__ import annotations

from enum import Enum


class AccountingTransferStatus(str, Enum):
    """AccountingTransferStatus enum (lifted from inline OAS enum)."""
    UNKNOWN = 'Unknown'
    UNRECONCILED = 'Unreconciled'
    RECONCILED = 'Reconciled'
    VOID = 'Void'
