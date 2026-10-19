from __future__ import annotations

from enum import Enum


class DataIntegrityDataType(str, Enum):
    """Shared OAS parameter enum (lifted from components/parameters/dataIntegrityDataType)."""
    BANKING_ACCOUNTS = 'banking-accounts'
    BANKING_TRANSACTIONS = 'banking-transactions'
    BANK_ACCOUNTS = 'bankAccounts'
    ACCOUNT_TRANSACTIONS = 'accountTransactions'
