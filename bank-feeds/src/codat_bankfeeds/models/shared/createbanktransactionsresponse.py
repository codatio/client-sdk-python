"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createbanktransactions import (
    CreateBankTransactions,
    CreateBankTransactionsTypedDict,
)
from .datatype import DataType
from .pushoperationchange import PushOperationChange, PushOperationChangeTypedDict
from .pushoperationstatus import PushOperationStatus
from .validation import Validation, ValidationTypedDict
from codat_bankfeeds.types import (
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


class CreateBankTransactionsResponseTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for your SMB in Codat."""
    data_connection_key: str
    r"""Unique identifier for a company's data connection."""
    push_operation_key: str
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""
    requested_on_utc: str
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
    status: PushOperationStatus
    r"""The current status of the push operation."""
    status_code: int
    r"""Push status code."""
    changes: NotRequired[Nullable[List[PushOperationChangeTypedDict]]]
    r"""Contains a single entry that communicates which record has changed and the manner in which it changed."""
    completed_on_utc: NotRequired[str]
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
    data: NotRequired[CreateBankTransactionsTypedDict]
    data_type: NotRequired[DataType]
    r"""Available data types"""
    error_message: NotRequired[Nullable[str]]
    r"""A message about the error."""
    timeout_in_minutes: NotRequired[Nullable[int]]
    r"""Number of minutes the push operation must complete within before it times out."""
    timeout_in_seconds: NotRequired[Nullable[int]]
    r"""Number of seconds the push operation must complete within before it times out."""
    validation: NotRequired[ValidationTypedDict]
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""


class CreateBankTransactionsResponse(BaseModel):
    company_id: Annotated[str, pydantic.Field(alias="companyId")]
    r"""Unique identifier for your SMB in Codat."""

    data_connection_key: Annotated[str, pydantic.Field(alias="dataConnectionKey")]
    r"""Unique identifier for a company's data connection."""

    push_operation_key: Annotated[str, pydantic.Field(alias="pushOperationKey")]
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""

    requested_on_utc: Annotated[str, pydantic.Field(alias="requestedOnUtc")]
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

    status: PushOperationStatus
    r"""The current status of the push operation."""

    status_code: Annotated[int, pydantic.Field(alias="statusCode")]
    r"""Push status code."""

    changes: OptionalNullable[List[PushOperationChange]] = UNSET
    r"""Contains a single entry that communicates which record has changed and the manner in which it changed."""

    completed_on_utc: Annotated[
        Optional[str], pydantic.Field(alias="completedOnUtc")
    ] = None
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

    data: Optional[CreateBankTransactions] = None

    data_type: Annotated[Optional[DataType], pydantic.Field(alias="dataType")] = None
    r"""Available data types"""

    error_message: Annotated[
        OptionalNullable[str], pydantic.Field(alias="errorMessage")
    ] = UNSET
    r"""A message about the error."""

    timeout_in_minutes: Annotated[
        OptionalNullable[int], pydantic.Field(alias="timeoutInMinutes")
    ] = UNSET
    r"""Number of minutes the push operation must complete within before it times out."""

    timeout_in_seconds: Annotated[
        OptionalNullable[int],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="timeoutInSeconds",
        ),
    ] = UNSET
    r"""Number of seconds the push operation must complete within before it times out."""

    validation: Optional[Validation] = None
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "changes",
            "completedOnUtc",
            "data",
            "dataType",
            "errorMessage",
            "timeoutInMinutes",
            "timeoutInSeconds",
            "validation",
        ]
        nullable_fields = [
            "changes",
            "errorMessage",
            "timeoutInMinutes",
            "timeoutInSeconds",
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
