"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_payables.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ClientRateLimitWebhookPayloadTypedDict(TypedDict):
    daily_quota: NotRequired[int]
    r"""The number of available requests per day."""
    quota_remaining: NotRequired[int]
    r"""Total number of requests remaining for your client."""
    expiry_date: NotRequired[str]
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


class ClientRateLimitWebhookPayload(BaseModel):
    daily_quota: Annotated[Optional[int], pydantic.Field(alias="dailyQuota")] = None
    r"""The number of available requests per day."""

    quota_remaining: Annotated[
        Optional[int], pydantic.Field(alias="quotaRemaining")
    ] = None
    r"""Total number of requests remaining for your client."""

    expiry_date: Annotated[Optional[str], pydantic.Field(alias="expiryDate")] = None
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
