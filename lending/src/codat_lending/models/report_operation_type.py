from __future__ import annotations

from enum import Enum


class ReportOperationType(str, Enum):
    """ReportOperationType enum (lifted from inline OAS enum)."""
    CATEGORIZED_BANK_STATEMENT = 'categorizedBankStatement'
    CREDIT_MODEL = 'creditModel'
    SPEND_ANALYSIS = 'spendAnalysis'
