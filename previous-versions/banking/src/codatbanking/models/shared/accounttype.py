"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class AccountType(str, Enum):
    r"""The type of transactions and balances on the account.
    For Credit accounts, positive balances are liabilities, and positive transactions **reduce** liabilities.  
    For Debit accounts, positive balances are assets, and positive transactions **increase** assets.
    """
    UNKNOWN = 'Unknown'
    CREDIT = 'Credit'
    DEBIT = 'Debit'
