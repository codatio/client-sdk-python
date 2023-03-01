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
class GetCompaniesCompanyIDPushPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDPushQueryParams:
    page: float = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDPushRequest:
    path_params: GetCompaniesCompanyIDPushPathParams = dataclasses.field()
    query_params: GetCompaniesCompanyIDPushQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDPushLinksLinksCurrent:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDPushLinksLinksNext:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDPushLinksLinksPrevious:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDPushLinksLinksSelf:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDPushLinksLinks:
    current: GetCompaniesCompanyIDPushLinksLinksCurrent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('current') }})
    self: GetCompaniesCompanyIDPushLinksLinksSelf = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('self') }})
    next: Optional[GetCompaniesCompanyIDPushLinksLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[GetCompaniesCompanyIDPushLinksLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDPushLinksResultsChangesPushOperationRecordRef:
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    
class GetCompaniesCompanyIDPushLinksResultsChangesTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    CREATED = "Created"
    MODIFIED = "Modified"
    DELETED = "Deleted"
    ATTACHMENT_UPLOADED = "AttachmentUploaded"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDPushLinksResultsChanges:
    attachment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attachmentId'), 'exclude': lambda f: f is None }})
    record_ref: Optional[GetCompaniesCompanyIDPushLinksResultsChangesPushOperationRecordRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('recordRef'), 'exclude': lambda f: f is None }})
    type: Optional[GetCompaniesCompanyIDPushLinksResultsChangesTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    
class GetCompaniesCompanyIDPushLinksResultsStatusEnum(str, Enum):
    PENDING = "Pending"
    FAILED = "Failed"
    SUCCESS = "Success"
    TIMED_OUT = "TimedOut"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDPushLinksResultsValidationValidationItem:
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemId'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message'), 'exclude': lambda f: f is None }})
    validator_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validatorName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDPushLinksResultsValidation:
    r"""GetCompaniesCompanyIDPushLinksResultsValidation
    A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here.
    """
    
    errors: Optional[list[GetCompaniesCompanyIDPushLinksResultsValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetCompaniesCompanyIDPushLinksResultsValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDPushLinksResults:
    company_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId') }})
    data_connection_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataConnectionKey') }})
    push_operation_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pushOperationKey') }})
    requested_on_utc: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('requestedOnUtc'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: GetCompaniesCompanyIDPushLinksResultsStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    status_code: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode') }})
    changes: Optional[list[GetCompaniesCompanyIDPushLinksResultsChanges]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('changes'), 'exclude': lambda f: f is None }})
    completed_on_utc: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('completedOnUtc'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType'), 'exclude': lambda f: f is None }})
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errorMessage'), 'exclude': lambda f: f is None }})
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeoutInMinutes'), 'exclude': lambda f: f is None }})
    timeout_in_seconds: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeoutInSeconds'), 'exclude': lambda f: f is None }})
    validation: Optional[GetCompaniesCompanyIDPushLinksResultsValidation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDPushLinks:
    r"""GetCompaniesCompanyIDPushLinks
    Codat's Paging Model
    """
    
    links: GetCompaniesCompanyIDPushLinksLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('_links') }})
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize') }})
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults') }})
    results: Optional[list[GetCompaniesCompanyIDPushLinksResults]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDPushResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    links: Optional[GetCompaniesCompanyIDPushLinks] = dataclasses.field(default=None)
    