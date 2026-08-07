from __future__ import annotations

from enum import Enum


class ValidTransactionTypes(str, Enum):
    """Top-level OAS enum schema (components/schemas/validTransactionTypes)."""
    PAYMENT = 'Payment'
    REFUND = 'Refund'
    REWARD = 'Reward'
    CHARGEBACK = 'Chargeback'
