from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class UpdateDataConnectionPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateDataConnectionRequestBody:
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class UpdateDataConnectionRequest:
    path_params: UpdateDataConnectionPathParams = dataclasses.field()
    request: Optional[UpdateDataConnectionRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateDataConnection200ApplicationJSONDataConnectionErrors:
    errored_on_utc: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('erroredOnUtc'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errorMessage'), 'exclude': lambda f: f is None }})
    status_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    status_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusText'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateDataConnection200ApplicationJSON:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    integration_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationId') }})
    link_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('linkUrl') }})
    platform_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('platformName') }})
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceId') }})
    created: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    data_connection_errors: Optional[list[UpdateDataConnection200ApplicationJSONDataConnectionErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataConnectionErrors'), 'exclude': lambda f: f is None }})
    last_sync: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lastSync'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    source_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType'), 'exclude': lambda f: f is None }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class UpdateDataConnectionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    update_data_connection_200_application_json_object: Optional[UpdateDataConnection200ApplicationJSON] = dataclasses.field(default=None)
    