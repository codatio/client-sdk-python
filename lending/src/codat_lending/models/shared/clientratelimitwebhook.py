"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .clientratelimitwebhookpayload import (
    ClientRateLimitWebhookPayload,
    ClientRateLimitWebhookPayloadTypedDict,
)
from codat_lending.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ClientRateLimitWebhookTypedDict(TypedDict):
    event_type: NotRequired[str]
    r"""The type of event."""
    generated_date: NotRequired[str]
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
    id: NotRequired[str]
    r"""Unique identifier of the event."""
    payload: NotRequired[ClientRateLimitWebhookPayloadTypedDict]


class ClientRateLimitWebhook(BaseModel):
    event_type: Annotated[Optional[str], pydantic.Field(alias="eventType")] = None
    r"""The type of event."""

    generated_date: Annotated[Optional[str], pydantic.Field(alias="generatedDate")] = (
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

    id: Optional[str] = None
    r"""Unique identifier of the event."""

    payload: Optional[ClientRateLimitWebhookPayload] = None
