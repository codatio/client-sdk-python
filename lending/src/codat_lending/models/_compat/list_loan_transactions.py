from __future__ import annotations

from enum import Enum


class ListLoanTransactionsQueryParamSourceType(str, Enum):
    """Operation-parameter enum (lifted from inline OAS enum on list-loan-transactions)."""
    BANKING = 'banking'
    COMMERCE = 'commerce'
    ACCOUNTING = 'accounting'
