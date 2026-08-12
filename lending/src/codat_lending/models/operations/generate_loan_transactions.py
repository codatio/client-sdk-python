from __future__ import annotations

from enum import Enum


class QueryParamSourceType(str, Enum):
    """Operation-parameter enum (lifted from inline OAS enum on generate-loan-transactions)."""
    BANKING = 'banking'
    COMMERCE = 'commerce'
    ACCOUNTING = 'accounting'
