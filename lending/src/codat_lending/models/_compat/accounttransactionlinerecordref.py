from __future__ import annotations

from enum import Enum


class AccountTransactionLineRecordRefDataType(str, Enum):
    """Speakeasy-name compat for JournalEntryRecordRefDataType (matched by value set)."""
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
