"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bankaccountstatus import BankAccountStatus
from codat_sync_for_payables.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BankAccountType(str, Enum):
    r"""The type of transactions and balances on the account.
    For Credit accounts, positive balances are liabilities, and positive transactions **reduce** liabilities.
    For Debit accounts, positive balances are assets, and positive transactions **increase** assets.
    """

    UNKNOWN = "Unknown"
    CREDIT = "Credit"
    DEBIT = "Debit"


class BankAccountTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Identifier for the bank account, unique for the company in the accounting software."""
    nominal_code: NotRequired[Nullable[str]]
    r"""Code used to identify each nominal account for a business."""
    name: NotRequired[Nullable[str]]
    r"""Name of the bank account in the accounting software."""
    account_type: NotRequired[BankAccountType]
    r"""The type of transactions and balances on the account.
    For Credit accounts, positive balances are liabilities, and positive transactions **reduce** liabilities.
    For Debit accounts, positive balances are assets, and positive transactions **increase** assets.
    """
    account_number: NotRequired[Nullable[str]]
    r"""Account number for the bank account.

    Xero integrations
    Only a UK account number shows for bank accounts with GBP currency and a combined total of sort code and account number that equals 14 digits, For non-GBP accounts, the full bank account number is populated.
    """
    sort_code: NotRequired[Nullable[str]]
    r"""Sort code for the bank account. This is relevant to UK bank accounts.

    Xero integrations
    The sort code is only displayed when the currency = GBP and the sort code and account number sum to 14 digits. For non-GBP accounts, this field is not populated.
    """
    currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    status: NotRequired[BankAccountStatus]
    r"""The current status of the bank account."""
    source_modified_date: NotRequired[str]


class BankAccount(BaseModel):
    id: Optional[str] = None
    r"""Identifier for the bank account, unique for the company in the accounting software."""

    nominal_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="nominalCode")
    ] = UNSET
    r"""Code used to identify each nominal account for a business."""

    name: OptionalNullable[str] = UNSET
    r"""Name of the bank account in the accounting software."""

    account_type: Annotated[
        Optional[BankAccountType], pydantic.Field(alias="accountType")
    ] = None
    r"""The type of transactions and balances on the account.
    For Credit accounts, positive balances are liabilities, and positive transactions **reduce** liabilities.
    For Debit accounts, positive balances are assets, and positive transactions **increase** assets.
    """

    account_number: Annotated[
        OptionalNullable[str], pydantic.Field(alias="accountNumber")
    ] = UNSET
    r"""Account number for the bank account.

    Xero integrations
    Only a UK account number shows for bank accounts with GBP currency and a combined total of sort code and account number that equals 14 digits, For non-GBP accounts, the full bank account number is populated.
    """

    sort_code: Annotated[OptionalNullable[str], pydantic.Field(alias="sortCode")] = (
        UNSET
    )
    r"""Sort code for the bank account. This is relevant to UK bank accounts.

    Xero integrations
    The sort code is only displayed when the currency = GBP and the sort code and account number sum to 14 digits. For non-GBP accounts, this field is not populated.
    """

    currency: Optional[str] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    status: Optional[BankAccountStatus] = None
    r"""The current status of the bank account."""

    source_modified_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceModifiedDate")
    ] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "nominalCode",
            "name",
            "accountType",
            "accountNumber",
            "sortCode",
            "currency",
            "status",
            "sourceModifiedDate",
        ]
        nullable_fields = ["nominalCode", "name", "accountNumber", "sortCode"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
