from __future__ import annotations

from enum import Enum


class ExpenseTransactionType(str, Enum):
    """ExpenseTransactionType enum (lifted from inline OAS enum)."""
    PAYMENT = 'Payment'
    REFUND = 'Refund'
    REWARD = 'Reward'
    CHARGEBACK = 'Chargeback'
