import dataclasses
import dateutil.parser
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class PostSyncInfoPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PostSyncInfoSecurity:
    api_key: shared_security.SchemeAPIKey = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PostSyncInfoRequest:
    path_params: PostSyncInfoPathParams = dataclasses.field()
    security: PostSyncInfoSecurity = dataclasses.field()
    
class PostSyncInfo200ApplicationJSONStatusEnum(str, Enum):
    INITIAL = "Initial"
    QUEUED = "Queued"
    FETCHING = "Fetching"
    MAP_QUEUED = "MapQueued"
    MAPPING = "Mapping"
    COMPLETE = "Complete"
    FETCH_ERROR = "FetchError"
    MAP_ERROR = "MapError"
    INTERNAL_ERROR = "InternalError"
    PROCESSING_QUEUED = "ProcessingQueued"
    PROCESSING = "Processing"
    PROCESSING_ERROR = "ProcessingError"
    VALIDATION_QUEUED = "ValidationQueued"
    VALIDATING = "Validating"
    VALIDATION_ERROR = "ValidationError"
    AUTH_ERROR = "AuthError"
    CANCELLED = "Cancelled"
    NOT_SUPPORTED = "NotSupported"
    RATE_LIMIT_ERROR = "RateLimitError"
    PERMISSIONS_ERROR = "PermissionsError"
    PREREQUISITE_NOT_MET = "PrerequisiteNotMet"


@dataclass_json
@dataclasses.dataclass
class PostSyncInfo200ApplicationJSON:
    company_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId') }})
    connection_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('connectionId') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    is_completed: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isCompleted') }})
    is_errored: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isErrored') }})
    progress: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('progress') }})
    requested: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('requested'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: PostSyncInfo200ApplicationJSONStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    completed: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('completed'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    dataset_logs_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('datasetLogsUrl') }})
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType') }})
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errorMessage') }})
    validationinformation_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validationinformationUrl') }})
    

@dataclasses.dataclass
class PostSyncInfoResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    post_sync_info_200_application_json_object: Optional[PostSyncInfo200ApplicationJSON] = dataclasses.field(default=None)
    