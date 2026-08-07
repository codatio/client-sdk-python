from __future__ import annotations

from enum import Enum


class ReportOperationStatus(str, Enum):
    """ReportOperationStatus enum (lifted from inline OAS enum)."""
    IN_PROGRESS = 'InProgress'
    COMPLETE = 'Complete'
    ERROR = 'Error'
