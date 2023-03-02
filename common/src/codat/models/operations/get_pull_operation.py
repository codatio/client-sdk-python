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
class GetPullOperationPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'datasetId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetPullOperationRequest:
    path_params: GetPullOperationPathParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPullOperation404ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('canBeRetried'), 'exclude': lambda f: f is None }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('correlationId'), 'exclude': lambda f: f is None }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error'), 'exclude': lambda f: f is None }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('service'), 'exclude': lambda f: f is None }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPullOperation401ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('canBeRetried'), 'exclude': lambda f: f is None }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('correlationId'), 'exclude': lambda f: f is None }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error'), 'exclude': lambda f: f is None }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('service'), 'exclude': lambda f: f is None }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    
class GetPullOperationPullOperationStatusEnum(str, Enum):
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
    ROUTING = "Routing"
    ROUTING_ERROR = "RoutingError"
    NOT_SUPPORTED = "NotSupported"
    RATE_LIMIT_ERROR = "RateLimitError"
    PERMISSIONS_ERROR = "PermissionsError"
    PREREQUISITE_NOT_MET = "PrerequisiteNotMet"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPullOperationPullOperation:
    r"""GetPullOperationPullOperation
    Information about a queued, in progress or completed pull operation.
    *Formally called `dataset`*
    """
    
    company_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId') }})
    connection_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('connectionId') }})
    data_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    is_completed: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isCompleted') }})
    is_errored: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isErrored') }})
    progress: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('progress') }})
    requested: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('requested'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: GetPullOperationPullOperationStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    

@dataclasses.dataclass
class GetPullOperationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_pull_operation_401_application_json_object: Optional[GetPullOperation401ApplicationJSON] = dataclasses.field(default=None)
    get_pull_operation_404_application_json_object: Optional[GetPullOperation404ApplicationJSON] = dataclasses.field(default=None)
    pull_operation: Optional[GetPullOperationPullOperation] = dataclasses.field(default=None)
    