from __future__ import annotations

from enum import Enum


class SourceType(str, Enum):
    """Operation-parameter enum (lifted from inline OAS enum on generate-loan-summary)."""
    BANKING = 'banking'
    COMMERCE = 'commerce'
    ACCOUNTING = 'accounting'
