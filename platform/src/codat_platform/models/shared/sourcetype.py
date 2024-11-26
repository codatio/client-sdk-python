"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class SourceType(str, Enum):
    r"""The type of platform of the connection."""

    ACCOUNTING = "Accounting"
    BANKING = "Banking"
    BANK_FEED = "BankFeed"
    COMMERCE = "Commerce"
    EXPENSE = "Expense"
    OTHER = "Other"
    UNKNOWN = "Unknown"