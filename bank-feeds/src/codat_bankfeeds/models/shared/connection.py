"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dataconnectionerror import DataConnectionError, DataConnectionErrorTypedDict
from .dataconnectionstatus import DataConnectionStatus
from codat_bankfeeds.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SourceType(str, Enum):
    r"""The type of platform of the connection."""

    ACCOUNTING = "Accounting"
    BANKING = "Banking"
    BANK_FEED = "BankFeed"
    COMMERCE = "Commerce"
    EXPENSE = "Expense"
    OTHER = "Other"
    UNKNOWN = "Unknown"


class ConnectionTypedDict(TypedDict):
    r"""A connection represents a [company's](https://docs.codat.io/bank-feeds-api#/schemas/Company) connection to a data source and allows you to synchronize data (pull and/or push) with that source.

    A company can have multiple data connections depending on the type of data source it is connecting to. For example, a single company can link to:

    - [Accounting data](https://docs.codat.io/accounting-api/overview) - 1 active connection.
    - [Banking data](https://docs.codat.io/banking-api/overview) - Multiple active connections.
    - [Commerce data](https://docs.codat.io/commerce-api/overview) - Multiple active connections.
    Any combination of accounting, banking, and commerce data connections is allowed.

    Before you can use a data connection to pull or push data, the company must grant you access to their business data by [linking the connection](https://docs.codat.io/auth-flow/overview).
    """

    created: str
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
    id: str
    r"""Unique identifier for a company's data connection."""
    integration_id: str
    r"""A Codat ID representing the integration."""
    integration_key: str
    r"""A unique four-character ID that identifies the platform of the company's data connection. This ensures continuity if the platform changes its name in the future."""
    link_url: str
    r"""The link URL your customers can use to authorize access to their business application."""
    platform_name: str
    r"""Name of integration connected to company."""
    source_id: str
    r"""A source-specific ID used to distinguish between different sources originating from the same data connection. In general, a data connection is a single data source. However, for TrueLayer, `sourceId` is associated with a specific bank and has a many-to-one relationship with the `integrationId`."""
    source_type: SourceType
    r"""The type of platform of the connection."""
    status: DataConnectionStatus
    r"""The current authorization status of the data connection."""
    connection_info: NotRequired[Nullable[Dict[str, str]]]
    data_connection_errors: NotRequired[Nullable[List[DataConnectionErrorTypedDict]]]
    last_sync: NotRequired[str]
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


class Connection(BaseModel):
    r"""A connection represents a [company's](https://docs.codat.io/bank-feeds-api#/schemas/Company) connection to a data source and allows you to synchronize data (pull and/or push) with that source.

    A company can have multiple data connections depending on the type of data source it is connecting to. For example, a single company can link to:

    - [Accounting data](https://docs.codat.io/accounting-api/overview) - 1 active connection.
    - [Banking data](https://docs.codat.io/banking-api/overview) - Multiple active connections.
    - [Commerce data](https://docs.codat.io/commerce-api/overview) - Multiple active connections.
    Any combination of accounting, banking, and commerce data connections is allowed.

    Before you can use a data connection to pull or push data, the company must grant you access to their business data by [linking the connection](https://docs.codat.io/auth-flow/overview).
    """

    created: str
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

    id: str
    r"""Unique identifier for a company's data connection."""

    integration_id: Annotated[str, pydantic.Field(alias="integrationId")]
    r"""A Codat ID representing the integration."""

    integration_key: Annotated[str, pydantic.Field(alias="integrationKey")]
    r"""A unique four-character ID that identifies the platform of the company's data connection. This ensures continuity if the platform changes its name in the future."""

    link_url: Annotated[str, pydantic.Field(alias="linkUrl")]
    r"""The link URL your customers can use to authorize access to their business application."""

    platform_name: Annotated[str, pydantic.Field(alias="platformName")]
    r"""Name of integration connected to company."""

    source_id: Annotated[str, pydantic.Field(alias="sourceId")]
    r"""A source-specific ID used to distinguish between different sources originating from the same data connection. In general, a data connection is a single data source. However, for TrueLayer, `sourceId` is associated with a specific bank and has a many-to-one relationship with the `integrationId`."""

    source_type: Annotated[SourceType, pydantic.Field(alias="sourceType")]
    r"""The type of platform of the connection."""

    status: DataConnectionStatus
    r"""The current authorization status of the data connection."""

    connection_info: Annotated[
        OptionalNullable[Dict[str, str]], pydantic.Field(alias="connectionInfo")
    ] = UNSET

    data_connection_errors: Annotated[
        OptionalNullable[List[DataConnectionError]],
        pydantic.Field(alias="dataConnectionErrors"),
    ] = UNSET

    last_sync: Annotated[Optional[str], pydantic.Field(alias="lastSync")] = None
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

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["connectionInfo", "dataConnectionErrors", "lastSync"]
        nullable_fields = ["connectionInfo", "dataConnectionErrors"]
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
