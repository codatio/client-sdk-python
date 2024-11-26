"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bankaccounttype import BankAccountType
from codat_sync_for_payables.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class BankAccountPrototypeTypedDict(TypedDict):
    name: Nullable[str]
    r"""Name of the bank account in the accounting software."""
    account_type: BankAccountType
    r"""The type of transactions and balances on the account.
    For Credit accounts, positive balances are liabilities, and positive transactions **reduce** liabilities.
    For Debit accounts, positive balances are assets, and positive transactions **increase** assets.
    """
    account_number: Nullable[str]
    r"""Account number for the bank account.

    Xero integrations
    Only a UK account number shows for bank accounts with GBP currency and a combined total of sort code and account number that equals 14 digits, For non-GBP accounts, the full bank account number is populated.
    """
    currency: str
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    nominal_code: NotRequired[Nullable[str]]
    r"""Code used to identify each nominal account for a business."""
    sort_code: NotRequired[Nullable[str]]
    r"""Sort code for the bank account. This is relevant to UK bank accounts.

    Xero integrations
    The sort code is only displayed when the currency = GBP and the sort code and account number sum to 14 digits. For non-GBP accounts, this field is not populated.
    """


class BankAccountPrototype(BaseModel):
    name: Nullable[str]
    r"""Name of the bank account in the accounting software."""

    account_type: Annotated[BankAccountType, pydantic.Field(alias="accountType")]
    r"""The type of transactions and balances on the account.
    For Credit accounts, positive balances are liabilities, and positive transactions **reduce** liabilities.
    For Debit accounts, positive balances are assets, and positive transactions **increase** assets.
    """

    account_number: Annotated[Nullable[str], pydantic.Field(alias="accountNumber")]
    r"""Account number for the bank account.

    Xero integrations
    Only a UK account number shows for bank accounts with GBP currency and a combined total of sort code and account number that equals 14 digits, For non-GBP accounts, the full bank account number is populated.
    """

    currency: str
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    nominal_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="nominalCode")
    ] = UNSET
    r"""Code used to identify each nominal account for a business."""

    sort_code: Annotated[OptionalNullable[str], pydantic.Field(alias="sortCode")] = (
        UNSET
    )
    r"""Sort code for the bank account. This is relevant to UK bank accounts.

    Xero integrations
    The sort code is only displayed when the currency = GBP and the sort code and account number sum to 14 digits. For non-GBP accounts, this field is not populated.
    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["nominalCode", "sortCode"]
        nullable_fields = ["name", "accountNumber", "nominalCode", "sortCode"]
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