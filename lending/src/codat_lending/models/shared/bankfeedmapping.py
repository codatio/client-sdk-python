"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .targetaccountoption import TargetAccountOption, TargetAccountOptionTypedDict
from codat_lending.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BankFeedMappingTypedDict(TypedDict):
    r"""A bank feed connection between a source account and a target account, including potential target accounts."""

    feed_start_date: NotRequired[str]
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
    source_account_id: NotRequired[str]
    r"""Unique ID for the source account."""
    source_account_name: NotRequired[str]
    r"""Name for the source account."""
    source_account_number: NotRequired[str]
    r"""Account number for the source account."""
    source_balance: NotRequired[Decimal]
    r"""Balance for the source account."""
    source_currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    status: NotRequired[str]
    r"""The status."""
    target_account_id: NotRequired[Nullable[str]]
    r"""Unique ID for the target account in the accounting software."""
    target_account_name: NotRequired[str]
    r"""Name for the target account in the accounting software."""
    target_account_options: NotRequired[Nullable[List[TargetAccountOptionTypedDict]]]
    r"""An array of potential target accounts."""


class BankFeedMapping(BaseModel):
    r"""A bank feed connection between a source account and a target account, including potential target accounts."""

    feed_start_date: Annotated[Optional[str], pydantic.Field(alias="feedStartDate")] = (
        None
    )
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

    source_account_id: Annotated[
        Optional[str], pydantic.Field(alias="sourceAccountId")
    ] = None
    r"""Unique ID for the source account."""

    source_account_name: Annotated[
        Optional[str], pydantic.Field(alias="sourceAccountName")
    ] = None
    r"""Name for the source account."""

    source_account_number: Annotated[
        Optional[str], pydantic.Field(alias="sourceAccountNumber")
    ] = None
    r"""Account number for the source account."""

    source_balance: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="sourceBalance"),
    ] = None
    r"""Balance for the source account."""

    source_currency: Annotated[
        Optional[str], pydantic.Field(alias="sourceCurrency")
    ] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    status: Optional[str] = None
    r"""The status."""

    target_account_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="targetAccountId")
    ] = UNSET
    r"""Unique ID for the target account in the accounting software."""

    target_account_name: Annotated[
        Optional[str], pydantic.Field(alias="targetAccountName")
    ] = None
    r"""Name for the target account in the accounting software."""

    target_account_options: Annotated[
        OptionalNullable[List[TargetAccountOption]],
        pydantic.Field(alias="targetAccountOptions"),
    ] = UNSET
    r"""An array of potential target accounts."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "feedStartDate",
            "sourceAccountId",
            "sourceAccountName",
            "sourceAccountNumber",
            "sourceBalance",
            "sourceCurrency",
            "status",
            "targetAccountId",
            "targetAccountName",
            "targetAccountOptions",
        ]
        nullable_fields = ["targetAccountId", "targetAccountOptions"]
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
