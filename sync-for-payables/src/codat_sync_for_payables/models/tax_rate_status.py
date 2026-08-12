from __future__ import annotations

from enum import Enum


class TaxRateStatus(str, Enum):
    """TaxRateStatus enum (lifted from inline OAS enum)."""
    ACTIVE = 'Active'
    ARCHIVED = 'Archived'
