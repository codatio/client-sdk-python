"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountref import AccountRef, AccountRefTypedDict
from .sourceref import SourceRef, SourceRefTypedDict
from .transactioncategory import TransactionCategory, TransactionCategoryTypedDict
from codat_lending.types import BaseModel
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CashFlowTransactionTypedDict(TypedDict):
    account_ref: NotRequired[AccountRefTypedDict]
    r"""An account reference containing the account id and name."""
    amount: NotRequired[Decimal]
    r"""The bank transaction amount."""
    counterparty_names: NotRequired[List[str]]
    r"""An array of counterparty names involved in the transaction."""
    currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    date_: NotRequired[str]
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
    description: NotRequired[str]
    r"""The description of the bank transaction."""
    id: NotRequired[str]
    r"""The unique identifier of the bank transaction."""
    modified_date: NotRequired[str]
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
    platform_name: NotRequired[str]
    r"""Returns the payment processor responsible for the transaction."""
    source_ref: NotRequired[SourceRefTypedDict]
    r"""A source reference containing the `sourceType` object \"Banking\"."""
    transaction_category: NotRequired[TransactionCategoryTypedDict]


class CashFlowTransaction(BaseModel):
    account_ref: Annotated[Optional[AccountRef], pydantic.Field(alias="accountRef")] = (
        None
    )
    r"""An account reference containing the account id and name."""

    amount: Annotated[
        Optional[Decimal],
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ] = None
    r"""The bank transaction amount."""

    counterparty_names: Annotated[
        Optional[List[str]], pydantic.Field(alias="counterpartyNames")
    ] = None
    r"""An array of counterparty names involved in the transaction."""

    currency: Optional[str] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    date_: Annotated[Optional[str], pydantic.Field(alias="date")] = None
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

    description: Optional[str] = None
    r"""The description of the bank transaction."""

    id: Optional[str] = None
    r"""The unique identifier of the bank transaction."""

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None
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

    platform_name: Annotated[Optional[str], pydantic.Field(alias="platformName")] = None
    r"""Returns the payment processor responsible for the transaction."""

    source_ref: Annotated[Optional[SourceRef], pydantic.Field(alias="sourceRef")] = None
    r"""A source reference containing the `sourceType` object \"Banking\"."""

    transaction_category: Annotated[
        Optional[TransactionCategory], pydantic.Field(alias="transactionCategory")
    ] = None


class EnhancedCashFlowItemTypedDict(TypedDict):
    transactions: NotRequired[List[CashFlowTransactionTypedDict]]
    r"""An array of transaction data."""


class EnhancedCashFlowItem(BaseModel):
    transactions: Optional[List[CashFlowTransaction]] = None
    r"""An array of transaction data."""
