"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .expensecontactref import ExpenseContactRef, ExpenseContactRefTypedDict
from .expensetransactionline import (
    ExpenseTransactionLine,
    ExpenseTransactionLineTypedDict,
)
from codat_sync_for_expenses.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_sync_for_expenses.utils import serialize_decimal, validate_decimal
from decimal import Decimal
from enum import Enum
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BankAccountReferenceTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Identifier of the bank account."""


class BankAccountReference(BaseModel):
    id: Optional[str] = None
    r"""Identifier of the bank account."""


class ExpenseTransactionType(str, Enum):
    r"""The type of transaction."""

    PAYMENT = "Payment"
    REFUND = "Refund"
    REWARD = "Reward"
    CHARGEBACK = "Chargeback"


class ExpenseTransactionTypedDict(TypedDict):
    currency: str
    r"""Currency the transaction was recorded in."""
    id: str
    r"""Your unique identifier for the transaction."""
    issue_date: str
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```



    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:

    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`

    > Time zones
    >
    > Not all dates from Codat will contain information about time zones.
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """
    type: ExpenseTransactionType
    r"""The type of transaction."""
    bank_account_ref: NotRequired[BankAccountReferenceTypedDict]
    contact_ref: NotRequired[ExpenseContactRefTypedDict]
    currency_rate: NotRequired[Nullable[Decimal]]
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.

    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.

    It is not possible to perform the currency conversion with two or more non-base currencies participating in the transaction. For example, if a company's base currency is USD, and it has a bill issued in EUR, then the bill payment must happen in USD or EUR.

    Where the currency rate is provided by the underlying accounting software, it will be available from Codat with the same precision (up to a maximum of 9 decimal places).

    For accounting software which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.

    ## Examples with base currency of GBP

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |

    ## Examples with base currency of USD

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |


    ### Integration-specific details

    | Integration       | Scenario                                        | System behavior                                                                                                                                                      |
    |-------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | QuickBooks Online | Transaction currency differs from base currency | If currency rate value is left `null`, a rate of 1 will be used by QBO by default. To override this, specify a currencyRate in the request body.  |
    """
    lines: NotRequired[List[ExpenseTransactionLineTypedDict]]
    r"""Array of transaction lines."""
    merchant_name: NotRequired[str]
    r"""Name of the merchant where the purchase took place"""
    notes: NotRequired[str]
    r"""Any private, company notes about the transaction."""
    post_as_draft: NotRequired[Nullable[bool]]
    r"""This optional property, when set to true, posts the transaction to a drafted state. Note that postAsDraft is only supported in Microsoft Dynamics 365 Business Central."""
    reference: NotRequired[Nullable[str]]
    r"""User-friendly reference for the expense transaction."""


class ExpenseTransaction(BaseModel):
    currency: str
    r"""Currency the transaction was recorded in."""

    id: str
    r"""Your unique identifier for the transaction."""

    issue_date: Annotated[str, pydantic.Field(alias="issueDate")]
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```



    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:

    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`

    > Time zones
    >
    > Not all dates from Codat will contain information about time zones.
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """

    type: ExpenseTransactionType
    r"""The type of transaction."""

    bank_account_ref: Annotated[
        Optional[BankAccountReference], pydantic.Field(alias="bankAccountRef")
    ] = None

    contact_ref: Annotated[
        Optional[ExpenseContactRef], pydantic.Field(alias="contactRef")
    ] = None

    currency_rate: Annotated[
        Annotated[
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="currencyRate"),
    ] = UNSET
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.

    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.

    It is not possible to perform the currency conversion with two or more non-base currencies participating in the transaction. For example, if a company's base currency is USD, and it has a bill issued in EUR, then the bill payment must happen in USD or EUR.

    Where the currency rate is provided by the underlying accounting software, it will be available from Codat with the same precision (up to a maximum of 9 decimal places).

    For accounting software which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.

    ## Examples with base currency of GBP

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |

    ## Examples with base currency of USD

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |


    ### Integration-specific details

    | Integration       | Scenario                                        | System behavior                                                                                                                                                      |
    |-------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | QuickBooks Online | Transaction currency differs from base currency | If currency rate value is left `null`, a rate of 1 will be used by QBO by default. To override this, specify a currencyRate in the request body.  |
    """

    lines: Optional[List[ExpenseTransactionLine]] = None
    r"""Array of transaction lines."""

    merchant_name: Annotated[Optional[str], pydantic.Field(alias="merchantName")] = None
    r"""Name of the merchant where the purchase took place"""

    notes: Optional[str] = None
    r"""Any private, company notes about the transaction."""

    post_as_draft: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="postAsDraft")
    ] = UNSET
    r"""This optional property, when set to true, posts the transaction to a drafted state. Note that postAsDraft is only supported in Microsoft Dynamics 365 Business Central."""

    reference: OptionalNullable[str] = UNSET
    r"""User-friendly reference for the expense transaction."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "bankAccountRef",
            "contactRef",
            "currencyRate",
            "lines",
            "merchantName",
            "notes",
            "postAsDraft",
            "reference",
        ]
        nullable_fields = ["currencyRate", "postAsDraft", "reference"]
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
