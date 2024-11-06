"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from enum import Enum
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountTransactionLineRecordRefDataType(str, Enum):
    r"""Name of underlying data type."""

    BANK_TRANSACTIONS = "bankTransactions"
    BILL_CREDIT_NOTES = "billCreditNotes"
    BILL_PAYMENTS = "billPayments"
    BILLS = "bills"
    CREDIT_NOTES = "creditNotes"
    DIRECT_COSTS = "directCosts"
    DIRECT_INCOMES = "directIncomes"
    INVOICES = "invoices"
    JOURNAL_ENTRIES = "journalEntries"
    PAYMENTS = "payments"
    TRANSFERS = "transfers"


class AccountTransactionLineRecordRefTypedDict(TypedDict):
    r"""Links an account transaction line to the underlying record that created it."""

    data_type: NotRequired[AccountTransactionLineRecordRefDataType]
    r"""Name of underlying data type."""
    id: NotRequired[str]
    r"""'id' of the underlying record or data type."""


class AccountTransactionLineRecordRef(BaseModel):
    r"""Links an account transaction line to the underlying record that created it."""

    data_type: Annotated[
        Optional[AccountTransactionLineRecordRefDataType],
        pydantic.Field(alias="dataType"),
    ] = None
    r"""Name of underlying data type."""

    id: Optional[str] = None
    r"""'id' of the underlying record or data type."""
