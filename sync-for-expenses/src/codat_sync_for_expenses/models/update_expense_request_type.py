from __future__ import annotations

from enum import Enum


class UpdateExpenseRequestType(str, Enum):
    """UpdateExpenseRequestType enum (lifted from inline OAS enum)."""
    PAYMENT = 'Payment'
    REFUND = 'Refund'
    REWARD = 'Reward'
    CHARGEBACK = 'Chargeback'
