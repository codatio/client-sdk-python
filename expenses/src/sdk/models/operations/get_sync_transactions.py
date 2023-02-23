import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetSyncTransactionsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    sync_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'syncId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSyncTransactionsQueryParams:
    page: float = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetSyncTransactionsRequest:
    path_params: GetSyncTransactionsPathParams = dataclasses.field()
    query_params: GetSyncTransactionsQueryParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetSyncTransactions200TextJSONHalLink:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    
class GetSyncTransactions200TextJSONResultsIntegrationTypeEnum(str, Enum):
    EXPENSES = "expenses"
    BANKFEEDS = "bankfeeds"

class GetSyncTransactions200TextJSONResultsStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    PENDING = "Pending"
    VALIDATION_ERROR = "ValidationError"
    COMPLETED = "Completed"
    PUSH_ERROR = "PushError"


@dataclass_json
@dataclasses.dataclass
class GetSyncTransactions200TextJSONResults:
    integration_type: Optional[GetSyncTransactions200TextJSONResultsIntegrationTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationType') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    status: Optional[GetSyncTransactions200TextJSONResultsStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionId') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncTransactions200TextJSON:
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize') }})
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults') }})
    links: Optional[dict[str, GetSyncTransactions200TextJSONHalLink]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('links') }})
    results: Optional[list[GetSyncTransactions200TextJSONResults]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncTransactions200ApplicationJSONHalLink:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    
class GetSyncTransactions200ApplicationJSONResultsIntegrationTypeEnum(str, Enum):
    EXPENSES = "expenses"
    BANKFEEDS = "bankfeeds"

class GetSyncTransactions200ApplicationJSONResultsStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    PENDING = "Pending"
    VALIDATION_ERROR = "ValidationError"
    COMPLETED = "Completed"
    PUSH_ERROR = "PushError"


@dataclass_json
@dataclasses.dataclass
class GetSyncTransactions200ApplicationJSONResults:
    integration_type: Optional[GetSyncTransactions200ApplicationJSONResultsIntegrationTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationType') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    status: Optional[GetSyncTransactions200ApplicationJSONResultsStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionId') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncTransactions200ApplicationJSON:
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize') }})
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults') }})
    links: Optional[dict[str, GetSyncTransactions200ApplicationJSONHalLink]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('links') }})
    results: Optional[list[GetSyncTransactions200ApplicationJSONResults]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    

@dataclasses.dataclass
class GetSyncTransactionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_sync_transactions_200_application_json_object: Optional[GetSyncTransactions200ApplicationJSON] = dataclasses.field(default=None)
    get_sync_transactions_200_text_json_object: Optional[GetSyncTransactions200TextJSON] = dataclasses.field(default=None)
    get_sync_transactions_200_text_plain_object: Optional[str] = dataclasses.field(default=None)
    