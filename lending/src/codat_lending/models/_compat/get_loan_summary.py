from __future__ import annotations

from enum import Enum


class GetLoanSummaryQueryParamSourceType(str, Enum):
    """Operation-parameter enum (lifted from inline OAS enum on get-loan-summary)."""
    BANKING = 'banking'
    COMMERCE = 'commerce'
    ACCOUNTING = 'accounting'
