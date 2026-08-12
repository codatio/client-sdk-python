from __future__ import annotations

from enum import Enum


class AccountingAccountTransactionDataType(str, Enum):
    """AccountingAccountTransactionDataType enum (lifted from inline OAS enum)."""
    BANK_TRANSACTIONS = 'bankTransactions'
    BILL_CREDIT_NOTES = 'billCreditNotes'
    BILL_PAYMENTS = 'billPayments'
    BILLS = 'bills'
    CREDIT_NOTES = 'creditNotes'
    DIRECT_COSTS = 'directCosts'
    DIRECT_INCOMES = 'directIncomes'
    INVOICES = 'invoices'
    JOURNAL_ENTRIES = 'journalEntries'
    PAYMENTS = 'payments'
    TRANSFERS = 'transfers'
