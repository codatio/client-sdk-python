from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
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
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncTransactions200ApplicationJSONHalLink:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    
class GetSyncTransactions200ApplicationJSONResultsIntegrationTypeEnum(str, Enum):
    EXPENSES = "expenses"
    BANKFEEDS = "bankfeeds"

class GetSyncTransactions200ApplicationJSONResultsStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    PENDING = "Pending"
    VALIDATION_ERROR = "ValidationError"
    COMPLETED = "Completed"
    PUSH_ERROR = "PushError"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncTransactions200ApplicationJSONResults:
    integration_type: Optional[GetSyncTransactions200ApplicationJSONResultsIntegrationTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationType'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message'), 'exclude': lambda f: f is None }})
    status: Optional[GetSyncTransactions200ApplicationJSONResultsStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncTransactions200ApplicationJSON:
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize') }})
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults') }})
    links: Optional[dict[str, GetSyncTransactions200ApplicationJSONHalLink]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('links'), 'exclude': lambda f: f is None }})
    results: Optional[list[GetSyncTransactions200ApplicationJSONResults]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetSyncTransactionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_sync_transactions_200_application_json_object: Optional[GetSyncTransactions200ApplicationJSON] = dataclasses.field(default=None)
    