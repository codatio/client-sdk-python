from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostProfileSyncSettingsRequestBodySyncSetting:
    r"""PostProfileSyncSettingsRequestBodySyncSetting
    Describes how often, and how much history, should be fetched for the given data type when a pull operation is queued.
    """
    
    data_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType') }})
    fetch_on_first_link: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('fetchOnFirstLink') }})
    sync_order: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncOrder') }})
    sync_schedule: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncSchedule') }})
    is_locked: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isLocked'), 'exclude': lambda f: f is None }})
    months_to_sync: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('monthsToSync'), 'exclude': lambda f: f is None }})
    sync_from_utc: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncFromUtc'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    sync_from_window: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncFromWindow'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostProfileSyncSettingsRequestBody:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('clientId') }})
    overrides_defaults: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('overridesDefaults') }})
    settings: list[PostProfileSyncSettingsRequestBodySyncSetting] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('settings') }})
    

@dataclasses.dataclass
class PostProfileSyncSettingsRequest:
    request: Optional[PostProfileSyncSettingsRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostProfileSyncSettings401ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('canBeRetried'), 'exclude': lambda f: f is None }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('correlationId'), 'exclude': lambda f: f is None }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error'), 'exclude': lambda f: f is None }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('service'), 'exclude': lambda f: f is None }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostProfileSyncSettingsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    post_profile_sync_settings_401_application_json_object: Optional[PostProfileSyncSettings401ApplicationJSON] = dataclasses.field(default=None)
    