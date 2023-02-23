from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class PostSyncLatestPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSyncLatestApplicationWildcardPlusJSON:
    sync_to: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncTo'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSyncLatestApplicationJSON:
    sync_to: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncTo'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSyncLatestApplicationJSONPatchPlusJSON:
    sync_to: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncTo'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSyncLatestTextJSON:
    sync_to: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncTo'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostSyncLatestRequests:
    object: Optional[PostSyncLatestApplicationWildcardPlusJSON] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/*+json' }})
    object1: Optional[PostSyncLatestApplicationJSON] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    object2: Optional[PostSyncLatestApplicationJSONPatchPlusJSON] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json-patch+json' }})
    object3: Optional[PostSyncLatestTextJSON] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'text/json' }})
    

@dataclasses.dataclass
class PostSyncLatestRequest:
    path_params: PostSyncLatestPathParams = dataclasses.field()
    request: Optional[PostSyncLatestRequests] = dataclasses.field(default=None)
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSyncLatest200TextJSONDataConnectionsDataConnectionErrors:
    errored_on_utc: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('erroredOnUtc'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errorMessage'), 'exclude': lambda f: f is None }})
    status_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    status_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusText'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSyncLatest200TextJSONDataConnections:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    integration_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationId') }})
    link_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('linkUrl') }})
    platform_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('platformName') }})
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceId') }})
    created: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    data_connection_errors: Optional[list[PostSyncLatest200TextJSONDataConnectionsDataConnectionErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataConnectionErrors'), 'exclude': lambda f: f is None }})
    last_sync: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lastSync'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    source_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType'), 'exclude': lambda f: f is None }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSyncLatest200TextJSONSyncDateRangeUtc:
    finish: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('finish'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    start: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('start'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSyncLatest200TextJSON:
    commerce_sync_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('commerceSyncId'), 'exclude': lambda f: f is None }})
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId'), 'exclude': lambda f: f is None }})
    data_connections: Optional[list[PostSyncLatest200TextJSONDataConnections]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataConnections'), 'exclude': lambda f: f is None }})
    data_pushed: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataPushed'), 'exclude': lambda f: f is None }})
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errorMessage'), 'exclude': lambda f: f is None }})
    sync_date_range_utc: Optional[PostSyncLatest200TextJSONSyncDateRangeUtc] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncDateRangeUtc'), 'exclude': lambda f: f is None }})
    sync_exception_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncExceptionMessage'), 'exclude': lambda f: f is None }})
    sync_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncStatus'), 'exclude': lambda f: f is None }})
    sync_status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncStatusCode'), 'exclude': lambda f: f is None }})
    sync_utc: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncUtc'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSyncLatest200ApplicationJSONDataConnectionsDataConnectionErrors:
    errored_on_utc: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('erroredOnUtc'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errorMessage'), 'exclude': lambda f: f is None }})
    status_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    status_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusText'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSyncLatest200ApplicationJSONDataConnections:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    integration_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationId') }})
    link_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('linkUrl') }})
    platform_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('platformName') }})
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceId') }})
    created: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    data_connection_errors: Optional[list[PostSyncLatest200ApplicationJSONDataConnectionsDataConnectionErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataConnectionErrors'), 'exclude': lambda f: f is None }})
    last_sync: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lastSync'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    source_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType'), 'exclude': lambda f: f is None }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSyncLatest200ApplicationJSONSyncDateRangeUtc:
    finish: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('finish'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    start: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('start'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSyncLatest200ApplicationJSON:
    commerce_sync_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('commerceSyncId'), 'exclude': lambda f: f is None }})
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId'), 'exclude': lambda f: f is None }})
    data_connections: Optional[list[PostSyncLatest200ApplicationJSONDataConnections]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataConnections'), 'exclude': lambda f: f is None }})
    data_pushed: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataPushed'), 'exclude': lambda f: f is None }})
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errorMessage'), 'exclude': lambda f: f is None }})
    sync_date_range_utc: Optional[PostSyncLatest200ApplicationJSONSyncDateRangeUtc] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncDateRangeUtc'), 'exclude': lambda f: f is None }})
    sync_exception_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncExceptionMessage'), 'exclude': lambda f: f is None }})
    sync_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncStatus'), 'exclude': lambda f: f is None }})
    sync_status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncStatusCode'), 'exclude': lambda f: f is None }})
    sync_utc: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncUtc'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostSyncLatestResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    post_sync_latest_200_application_json_object: Optional[PostSyncLatest200ApplicationJSON] = dataclasses.field(default=None)
    post_sync_latest_200_text_json_object: Optional[PostSyncLatest200TextJSON] = dataclasses.field(default=None)
    post_sync_latest_200_text_plain_object: Optional[str] = dataclasses.field(default=None)
    