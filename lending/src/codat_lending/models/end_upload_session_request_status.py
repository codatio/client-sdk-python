from __future__ import annotations

from enum import Enum


class EndUploadSessionRequestStatus(str, Enum):
    """EndUploadSessionRequestStatus enum (lifted from inline OAS enum)."""
    CANCEL = 'Cancel'
    PROCESS = 'Process'
