"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class AccountTypeEnum(str, Enum):
    r"""Type of account"""
    UNKNOWN = 'Unknown'
    ASSET = 'Asset'
    EXPENSE = 'Expense'
    INCOME = 'Income'
    LIABILITY = 'Liability'
    EQUITY = 'Equity'