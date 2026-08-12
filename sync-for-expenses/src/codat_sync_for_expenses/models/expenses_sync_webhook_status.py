from __future__ import annotations

from enum import Enum


class ExpensesSyncWebhookStatus(str, Enum):
    """ExpensesSyncWebhookStatus enum (lifted from inline OAS enum)."""
    UNKNOWN = 'Unknown'
    PUSH_ERROR = 'PushError'
    COMPLETED = 'Completed'
    FAILED = 'Failed'
    PENDING = 'Pending'
