from __future__ import annotations

from enum import Enum


class AccountingCreateTransferResponseStatus(str, Enum):
    """Compat name for AccountingTransferStatus (matched by value set)."""
    UNKNOWN = 'Unknown'
    UNRECONCILED = 'Unreconciled'
    RECONCILED = 'Reconciled'
    VOID = 'Void'
