from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationRequestBody:
    property1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('property1'), 'exclude': lambda f: f is None }})
    property2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('property2'), 'exclude': lambda f: f is None }})
    property3: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('property3'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationRequest:
    path_params: GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationPathParams = dataclasses.field()
    request: Optional[GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationConnectionConnectionInfo:
    additional_prop1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp1'), 'exclude': lambda f: f is None }})
    additional_prop2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp2'), 'exclude': lambda f: f is None }})
    additional_prop3: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp3'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationConnectionDataConnectionErrors:
    errored_on_utc: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('erroredOnUtc'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errorMessage'), 'exclude': lambda f: f is None }})
    status_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    status_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusText'), 'exclude': lambda f: f is None }})
    
class GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationConnectionSourceTypeEnum(str, Enum):
    ACCOUNTING = "Accounting"
    BANKING = "Banking"
    COMMERCE = "Commerce"
    OTHER = "Other"
    UNKNOWN = "Unknown"

class GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationConnectionDataConnectionStatusEnum(str, Enum):
    PENDING_AUTH = "PendingAuth"
    LINKED = "Linked"
    UNLINKED = "Unlinked"
    DEAUTHORIZED = "Deauthorized"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationConnection:
    r"""GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationConnection
    A connection represents the link between a `company` and a source of data.
    """
    
    created: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    integration_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationId') }})
    integration_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationKey') }})
    link_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('linkUrl') }})
    platform_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('platformName') }})
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceId') }})
    source_type: GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationConnectionSourceTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType') }})
    status: GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationConnectionDataConnectionStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    connection_info: Optional[GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationConnectionConnectionInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('connectionInfo'), 'exclude': lambda f: f is None }})
    data_connection_errors: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationConnectionDataConnectionErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataConnectionErrors'), 'exclude': lambda f: f is None }})
    last_sync: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lastSync'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connection: Optional[GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationConnection] = dataclasses.field(default=None)
    