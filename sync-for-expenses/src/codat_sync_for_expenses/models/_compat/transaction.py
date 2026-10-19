from __future__ import annotations

from enum import Enum


class TransactionDefinitionsStatus(str, Enum):
    """Compat name for ExpensesSyncWebhookStatus (matched by value set)."""
    UNKNOWN = 'Unknown'
    PUSH_ERROR = 'PushError'
    COMPLETED = 'Completed'
    FAILED = 'Failed'
    PENDING = 'Pending'
