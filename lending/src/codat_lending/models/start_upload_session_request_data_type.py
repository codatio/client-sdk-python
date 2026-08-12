from __future__ import annotations

from enum import Enum


class StartUploadSessionRequestDataType(str, Enum):
    """StartUploadSessionRequestDataType enum (lifted from inline OAS enum)."""
    BANKING_ACCOUNTS = 'banking-accounts'
    BANKING_TRANSACTIONS = 'banking-transactions'
