"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class IntegrationType(str, Enum):
    r"""Type of transaction that has been processed e.g. Expense or Bank Feed."""
    EXPENSES = 'expenses'
    BANKFEEDS = 'bankfeeds'
