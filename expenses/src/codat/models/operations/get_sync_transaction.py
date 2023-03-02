from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class GetSyncTransactionPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    sync_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'syncId', 'style': 'simple', 'explode': False }})
    transaction_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transactionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSyncTransactionRequest:
    path_params: GetSyncTransactionPathParams = dataclasses.field()
    
class GetSyncTransaction200ApplicationJSONIntegrationTypeEnum(str, Enum):
    EXPENSES = "expenses"
    BANKFEEDS = "bankfeeds"

class GetSyncTransaction200ApplicationJSONStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    PENDING = "Pending"
    VALIDATION_ERROR = "ValidationError"
    COMPLETED = "Completed"
    PUSH_ERROR = "PushError"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncTransaction200ApplicationJSON:
    integration_type: Optional[GetSyncTransaction200ApplicationJSONIntegrationTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationType'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message'), 'exclude': lambda f: f is None }})
    status: Optional[GetSyncTransaction200ApplicationJSONStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionId'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetSyncTransactionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_sync_transaction_200_application_json_objects: Optional[list[GetSyncTransaction200ApplicationJSON]] = dataclasses.field(default=None)
    