from __future__ import annotations

from enum import Enum


class ErrorStatus(str, Enum):
    """ErrorStatus enum (lifted from inline OAS enum)."""
    ACTIVE = 'Active'
    RESOLVED = 'Resolved'
