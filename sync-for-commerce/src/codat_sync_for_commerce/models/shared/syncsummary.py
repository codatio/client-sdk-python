"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .connection import Connection, ConnectionTypedDict
from codat_sync_for_commerce.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SyncDateRangeUtcTypedDict(TypedDict):
    finish: NotRequired[str]
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
    start: NotRequired[str]
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


class SyncDateRangeUtc(BaseModel):
    finish: Optional[str] = None
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

    start: Optional[str] = None
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


class SyncSummaryTypedDict(TypedDict):
    commerce_sync_id: NotRequired[str]
    r"""Unique identifier for the sync in Codat."""
    company_id: NotRequired[str]
    r"""Unique identifier for your SMB in Codat."""
    data_connections: NotRequired[Nullable[List[ConnectionTypedDict]]]
    r"""Array of containing objects data connection information for the company."""
    data_pushed: NotRequired[bool]
    r"""Boolean indicator for data being pushed during a sync operation."""
    error_message: NotRequired[Nullable[str]]
    r"""Friendly error message for the sync operation."""
    sync_date_range_utc: NotRequired[SyncDateRangeUtcTypedDict]
    sync_exception_message: NotRequired[Nullable[str]]
    r"""Exception message for the sync operation."""
    sync_status: NotRequired[Nullable[str]]
    r"""Status of the sync of the company data. This is linked to status code."""
    sync_status_code: NotRequired[int]
    r"""Numerical status code sync of the company data."""
    sync_utc: NotRequired[str]
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


class SyncSummary(BaseModel):
    commerce_sync_id: Annotated[
        Optional[str], pydantic.Field(alias="commerceSyncId")
    ] = None
    r"""Unique identifier for the sync in Codat."""

    company_id: Annotated[Optional[str], pydantic.Field(alias="companyId")] = None
    r"""Unique identifier for your SMB in Codat."""

    data_connections: Annotated[
        OptionalNullable[List[Connection]], pydantic.Field(alias="dataConnections")
    ] = UNSET
    r"""Array of containing objects data connection information for the company."""

    data_pushed: Annotated[Optional[bool], pydantic.Field(alias="dataPushed")] = None
    r"""Boolean indicator for data being pushed during a sync operation."""

    error_message: Annotated[
        OptionalNullable[str], pydantic.Field(alias="errorMessage")
    ] = UNSET
    r"""Friendly error message for the sync operation."""

    sync_date_range_utc: Annotated[
        Optional[SyncDateRangeUtc], pydantic.Field(alias="syncDateRangeUtc")
    ] = None

    sync_exception_message: Annotated[
        OptionalNullable[str], pydantic.Field(alias="syncExceptionMessage")
    ] = UNSET
    r"""Exception message for the sync operation."""

    sync_status: Annotated[
        OptionalNullable[str], pydantic.Field(alias="syncStatus")
    ] = UNSET
    r"""Status of the sync of the company data. This is linked to status code."""

    sync_status_code: Annotated[
        Optional[int], pydantic.Field(alias="syncStatusCode")
    ] = None
    r"""Numerical status code sync of the company data."""

    sync_utc: Annotated[Optional[str], pydantic.Field(alias="syncUtc")] = None
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
        optional_fields = [
            "commerceSyncId",
            "companyId",
            "dataConnections",
            "dataPushed",
            "errorMessage",
            "syncDateRangeUtc",
            "syncExceptionMessage",
            "syncStatus",
            "syncStatusCode",
            "syncUtc",
        ]
        nullable_fields = [
            "dataConnections",
            "errorMessage",
            "syncExceptionMessage",
            "syncStatus",
        ]
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
