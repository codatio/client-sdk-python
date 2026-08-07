from __future__ import annotations

from enum import Enum


class AccountingAccountTransactionStatus(str, Enum):
    """AccountingAccountTransactionStatus enum (lifted from inline OAS enum)."""
    UNKNOWN = 'Unknown'
    UNRECONCILED = 'Unreconciled'
    RECONCILED = 'Reconciled'
    VOID = 'Void'
