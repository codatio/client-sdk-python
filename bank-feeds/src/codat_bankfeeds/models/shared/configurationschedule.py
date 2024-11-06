"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_bankfeeds.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ConfigurationScheduleTypedDict(TypedDict):
    frequency_options: NotRequired[List[str]]
    r"""The available sync frequencies."""
    selected_frequency: NotRequired[str]
    r"""The sync frequency."""
    start_date: NotRequired[str]
    r"""The datetime in UTC you want to start syncing from."""
    sync_hour_utc: NotRequired[int]
    r"""The hour in which the sync is initiated."""
    time_zone_iana_id: NotRequired[str]
    r"""The [IANA](https://www.iana.org/time-zones) time zone ID."""


class ConfigurationSchedule(BaseModel):
    frequency_options: Annotated[
        Optional[List[str]], pydantic.Field(alias="frequencyOptions")
    ] = None
    r"""The available sync frequencies."""

    selected_frequency: Annotated[
        Optional[str], pydantic.Field(alias="selectedFrequency")
    ] = None
    r"""The sync frequency."""

    start_date: Annotated[Optional[str], pydantic.Field(alias="startDate")] = None
    r"""The datetime in UTC you want to start syncing from."""

    sync_hour_utc: Annotated[Optional[int], pydantic.Field(alias="syncHourUtc")] = None
    r"""The hour in which the sync is initiated."""

    time_zone_iana_id: Annotated[
        Optional[str], pydantic.Field(alias="timeZoneIanaId")
    ] = None
    r"""The [IANA](https://www.iana.org/time-zones) time zone ID."""
