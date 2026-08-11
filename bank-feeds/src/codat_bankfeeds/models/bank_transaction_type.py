from __future__ import annotations

from enum import Enum


class BankTransactionType(str, Enum):
    """BankTransactionType enum (lifted from inline OAS enum)."""
    UNKNOWN = 'Unknown'
    CREDIT = 'Credit'
    DEBIT = 'Debit'
    INT = 'Int'
    DIV = 'Div'
    FEE = 'Fee'
    SER_CHG = 'SerChg'
    DEP = 'Dep'
    ATM = 'Atm'
    POS = 'Pos'
    XFER = 'Xfer'
    CHECK = 'Check'
    PAYMENT = 'Payment'
    CASH = 'Cash'
    DIRECT_DEP = 'DirectDep'
    DIRECT_DEBIT = 'DirectDebit'
    REPEAT_PMT = 'RepeatPmt'
    OTHER = 'Other'
