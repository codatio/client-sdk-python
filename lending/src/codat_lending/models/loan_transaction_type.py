from __future__ import annotations

from enum import Enum


class LoanTransactionType(str, Enum):
    """LoanTransactionType enum (lifted from inline OAS enum)."""
    INVESTMENT = 'Investment'
    REPAYMENT = 'Repayment'
    INTEREST = 'Interest'
    ACCURED_INTEREST = 'AccuredInterest'
