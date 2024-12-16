"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountinfo import AccountInfo, AccountInfoTypedDict
from .routinginfo import RoutingInfo, RoutingInfoTypedDict
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


class SourceAccountV2AccountType(str, Enum):
    r"""The type of bank account e.g. checking, savings, loan, creditCard, prepaidCard."""

    CHECKING = "checking"
    SAVINGS = "savings"
    LOAN = "loan"
    CREDIT_CARD = "creditCard"
    PREPAID_CARD = "prepaidCard"


class SourceAccountV2Status(str, Enum):
    r"""Status of the source account."""

    PENDING = "pending"
    CONNECTED = "connected"
    CONNECTING = "connecting"
    DISCONNECTED = "disconnected"
    UNKNOWN = "unknown"


class SourceAccountV2TypedDict(TypedDict):
    r"""The target bank account in a supported accounting software for ingestion into a bank feed."""

    account_name: str
    r"""The bank account name."""
    account_number: str
    r"""The account number."""
    account_type: SourceAccountV2AccountType
    r"""The type of bank account e.g. checking, savings, loan, creditCard, prepaidCard."""
    balance: Decimal
    r"""The latest balance for the bank account."""
    currency: str
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    id: str
    r"""Unique ID for the bank account."""
    account_info: NotRequired[Nullable[AccountInfoTypedDict]]
    feed_start_date: NotRequired[Nullable[str]]
    r"""In Codat's data model, dates are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date fields are formatted as strings; for example:
    ```
    2020-10-08
    ```
    """
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
    routing_info: NotRequired[RoutingInfoTypedDict]
    r"""Routing information for the bank. This does not include account number."""
    sort_code: NotRequired[Nullable[str]]
    r"""The sort code."""
    status: NotRequired[Nullable[SourceAccountV2Status]]
    r"""Status of the source account."""


class SourceAccountV2(BaseModel):
    r"""The target bank account in a supported accounting software for ingestion into a bank feed."""

    account_name: Annotated[str, pydantic.Field(alias="accountName")]
    r"""The bank account name."""

    account_number: Annotated[str, pydantic.Field(alias="accountNumber")]
    r"""The account number."""

    account_type: Annotated[
        SourceAccountV2AccountType, pydantic.Field(alias="accountType")
    ]
    r"""The type of bank account e.g. checking, savings, loan, creditCard, prepaidCard."""

    balance: Annotated[
        Decimal,
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ]
    r"""The latest balance for the bank account."""

    currency: str
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    id: str
    r"""Unique ID for the bank account."""

    account_info: Annotated[
        OptionalNullable[AccountInfo], pydantic.Field(alias="accountInfo")
    ] = UNSET

    feed_start_date: Annotated[
        OptionalNullable[str], pydantic.Field(alias="feedStartDate")
    ] = UNSET
    r"""In Codat's data model, dates are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date fields are formatted as strings; for example:
    ```
    2020-10-08
    ```
    """

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

    routing_info: Annotated[
        Optional[RoutingInfo], pydantic.Field(alias="routingInfo")
    ] = None
    r"""Routing information for the bank. This does not include account number."""

    sort_code: Annotated[OptionalNullable[str], pydantic.Field(alias="sortCode")] = (
        UNSET
    )
    r"""The sort code."""

    status: OptionalNullable[SourceAccountV2Status] = UNSET
    r"""Status of the source account."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "accountInfo",
            "feedStartDate",
            "modifiedDate",
            "routingInfo",
            "sortCode",
            "status",
        ]
        nullable_fields = ["accountInfo", "feedStartDate", "sortCode", "status"]
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
