from __future__ import annotations

from enum import Enum


class ReportType(str, Enum):
    """Shared OAS parameter enum (lifted from components/parameters/reportType)."""
    CATEGORIZED_BANK_STATEMENT = 'categorizedBankStatement'
    CREDIT_MODEL = 'creditModel'
