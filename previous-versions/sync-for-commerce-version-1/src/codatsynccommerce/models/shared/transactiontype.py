"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class TransactionType(str, Enum):
    r"""The type of the platform transaction:
    - `Unknown`  
    - `FailedPayout` — Failed transfer of funds from the seller's merchant account to their bank account.  
    - `Payment` — Credit and debit card payments.  
    - `PaymentFee` — Payment provider's fee on each card payment.  
    - `PaymentFeeRefund` — Payment provider's fee that has been refunded to the seller.  
    - `Payout` — Transfer of funds from the seller's merchant account to their bank account.  
    - `Refund` — Refunds to a customer's credit or debit card.  
    - `Transfer` — Secure transfer of funds to the seller's bank account.
    """
    PAYMENT = 'Payment'
    REFUND = 'Refund'
    PAYOUT = 'Payout'
    FAILED_PAYOUT = 'FailedPayout'
    TRANSFER = 'Transfer'
    PAYMENT_FEE = 'PaymentFee'
    PAYMENT_FEE_REFUND = 'PaymentFeeRefund'
    UNKNOWN = 'Unknown'
