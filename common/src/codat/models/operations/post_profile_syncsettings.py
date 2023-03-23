"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostProfileSyncSettingsRequestBodySyncSetting:
    r"""Describes how often, and how much history, should be fetched for the given data type when a pull operation is queued."""
    
    data_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType') }})  
    fetch_on_first_link: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fetchOnFirstLink') }})
    r"""Whether this data type should be queued after a company has authorized a connection."""  
    sync_order: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncOrder') }})  
    sync_schedule: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncSchedule') }})
    r"""Number of hours after which this data type should be refreshed."""  
    is_locked: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isLocked'), 'exclude': lambda f: f is None }})  
    months_to_sync: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('monthsToSync'), 'exclude': lambda f: f is None }})
    r"""Months of data to fetch, for report data types (`balanceSheet` & `profitAndLoss`) only."""  
    sync_from_utc: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncFromUtc'), 'exclude': lambda f: f is None }})
    r"""Date from which data should be fetched. Set this *or* `syncFromWindow`"""  
    sync_from_window: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncFromWindow'), 'exclude': lambda f: f is None }})
    r"""Number of months of data to be fetched. Set this *or* `syncFromUTC`"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostProfileSyncSettingsRequestBody:
    r"""Include a `syncSetting` object for each data type.
    `syncFromWindow`, `syncFromUTC` & `monthsToSync` only need to be included if you wish to set a value for them.
    """
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})  
    overrides_defaults: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('overridesDefaults') }})  
    settings: list[PostProfileSyncSettingsRequestBodySyncSetting] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settings') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostProfileSyncSettings401ApplicationJSON:
    r"""Your API request was not properly authorized."""
    
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canBeRetried'), 'exclude': lambda f: f is None }})  
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('correlationId'), 'exclude': lambda f: f is None }})  
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})  
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})  
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service'), 'exclude': lambda f: f is None }})  
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class PostProfileSyncSettingsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    post_profile_sync_settings_401_application_json_object: Optional[PostProfileSyncSettings401ApplicationJSON] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    