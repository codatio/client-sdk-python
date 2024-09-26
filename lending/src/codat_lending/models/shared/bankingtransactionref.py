"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class BankingTransactionRefTypedDict(TypedDict):
    account_id: NotRequired[str]
    r"""Unique identifier of the bank transaction's account."""
    account_name: NotRequired[str]
    r"""Name given to account."""
    amount: NotRequired[Decimal]
    r"""Bank transaction amount."""
    data_connection_id: NotRequired[str]
    r"""Unique identifier of the bank transaction's connection."""
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
    r"""Description given to bank transaction."""
    id: NotRequired[str]
    r"""Unique identifier for the bank transaction."""


class BankingTransactionRef(BaseModel):
    account_id: Annotated[Optional[str], pydantic.Field(alias="accountId")] = None
    r"""Unique identifier of the bank transaction's account."""

    account_name: Annotated[Optional[str], pydantic.Field(alias="accountName")] = None
    r"""Name given to account."""

    amount: Annotated[
        Optional[Decimal],
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ] = None
    r"""Bank transaction amount."""

    data_connection_id: Annotated[
        Optional[str], pydantic.Field(alias="dataConnectionId")
    ] = None
    r"""Unique identifier of the bank transaction's connection."""

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
    r"""Description given to bank transaction."""

    id: Optional[str] = None
    r"""Unique identifier for the bank transaction."""
