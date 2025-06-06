"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bankaccountstatus import BankAccountStatus
from codat_bankfeeds.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_bankfeeds.utils import serialize_decimal, validate_decimal
from decimal import Decimal
from enum import Enum
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
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


class BankAccountPrototypeTypedDict(TypedDict):
    account_name: NotRequired[Nullable[str]]
    r"""Name of the bank account in the accounting software."""
    account_number: NotRequired[Nullable[str]]
    r"""Account number for the bank account.

    Xero integrations
    Only a UK account number shows for bank accounts with GBP currency and a combined total of sort code and account number that equals 14 digits, For non-GBP accounts, the full bank account number is populated.

    FreeAgent integrations
    For Credit accounts, only the last four digits are required. For other types, the field is optional.
    """
    account_type: NotRequired[BankAccountType]
    r"""The type of transactions and balances on the account.
    For Credit accounts, positive balances are liabilities, and positive transactions **reduce** liabilities.
    For Debit accounts, positive balances are assets, and positive transactions **increase** assets.
    """
    available_balance: NotRequired[Nullable[Decimal]]
    r"""Total available balance of the bank account as reported by the underlying data source. This may take into account overdrafts or pending transactions for example."""
    balance: NotRequired[Nullable[Decimal]]
    r"""Balance of the bank account."""
    currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    i_ban: NotRequired[Nullable[str]]
    r"""International bank account number of the account. Often used when making or receiving international payments."""
    institution: NotRequired[Nullable[str]]
    r"""The institution of the bank account."""
    nominal_code: NotRequired[Nullable[str]]
    r"""Code used to identify each nominal account for a business."""
    overdraft_limit: NotRequired[Nullable[Decimal]]
    r"""Pre-arranged overdraft limit of the account.

    The value is always positive. For example, an overdraftLimit of `1000` means that the balance of the account can go down to `-1000`.
    """
    sort_code: NotRequired[Nullable[str]]
    r"""Sort code for the bank account.

    Xero integrations
    The sort code is only displayed when the currency = GBP and the sort code and account number sum to 14 digits. For non-GBP accounts, this field is not populated.
    """
    status: NotRequired[BankAccountStatus]
    r"""Status of the bank account."""


class BankAccountPrototype(BaseModel):
    account_name: Annotated[
        OptionalNullable[str], pydantic.Field(alias="accountName")
    ] = UNSET
    r"""Name of the bank account in the accounting software."""

    account_number: Annotated[
        OptionalNullable[str], pydantic.Field(alias="accountNumber")
    ] = UNSET
    r"""Account number for the bank account.

    Xero integrations
    Only a UK account number shows for bank accounts with GBP currency and a combined total of sort code and account number that equals 14 digits, For non-GBP accounts, the full bank account number is populated.

    FreeAgent integrations
    For Credit accounts, only the last four digits are required. For other types, the field is optional.
    """

    account_type: Annotated[
        Optional[BankAccountType], pydantic.Field(alias="accountType")
    ] = None
    r"""The type of transactions and balances on the account.
    For Credit accounts, positive balances are liabilities, and positive transactions **reduce** liabilities.
    For Debit accounts, positive balances are assets, and positive transactions **increase** assets.
    """

    available_balance: Annotated[
        Annotated[
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="availableBalance"),
    ] = UNSET
    r"""Total available balance of the bank account as reported by the underlying data source. This may take into account overdrafts or pending transactions for example."""

    balance: Annotated[
        OptionalNullable[Decimal],
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ] = UNSET
    r"""Balance of the bank account."""

    currency: Optional[str] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    i_ban: Annotated[OptionalNullable[str], pydantic.Field(alias="iBan")] = UNSET
    r"""International bank account number of the account. Often used when making or receiving international payments."""

    institution: OptionalNullable[str] = UNSET
    r"""The institution of the bank account."""

    nominal_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="nominalCode")
    ] = UNSET
    r"""Code used to identify each nominal account for a business."""

    overdraft_limit: Annotated[
        Annotated[
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="overdraftLimit"),
    ] = UNSET
    r"""Pre-arranged overdraft limit of the account.

    The value is always positive. For example, an overdraftLimit of `1000` means that the balance of the account can go down to `-1000`.
    """

    sort_code: Annotated[OptionalNullable[str], pydantic.Field(alias="sortCode")] = (
        UNSET
    )
    r"""Sort code for the bank account.

    Xero integrations
    The sort code is only displayed when the currency = GBP and the sort code and account number sum to 14 digits. For non-GBP accounts, this field is not populated.
    """

    status: Optional[BankAccountStatus] = None
    r"""Status of the bank account."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "accountName",
            "accountNumber",
            "accountType",
            "availableBalance",
            "balance",
            "currency",
            "iBan",
            "institution",
            "nominalCode",
            "overdraftLimit",
            "sortCode",
            "status",
        ]
        nullable_fields = [
            "accountName",
            "accountNumber",
            "availableBalance",
            "balance",
            "iBan",
            "institution",
            "nominalCode",
            "overdraftLimit",
            "sortCode",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
