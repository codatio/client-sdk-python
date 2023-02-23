import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetSyncTransactionPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    sync_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'syncId', 'style': 'simple', 'explode': False }})
    transaction_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transactionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSyncTransactionRequest:
    path_params: GetSyncTransactionPathParams = dataclasses.field()
    
class GetSyncTransaction200TextJSONIntegrationTypeEnum(str, Enum):
    EXPENSES = "expenses"
    BANKFEEDS = "bankfeeds"

class GetSyncTransaction200TextJSONStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    PENDING = "Pending"
    VALIDATION_ERROR = "ValidationError"
    COMPLETED = "Completed"
    PUSH_ERROR = "PushError"


@dataclass_json
@dataclasses.dataclass
class GetSyncTransaction200TextJSON:
    integration_type: Optional[GetSyncTransaction200TextJSONIntegrationTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationType') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    status: Optional[GetSyncTransaction200TextJSONStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionId') }})
    
class GetSyncTransaction200ApplicationJSONIntegrationTypeEnum(str, Enum):
    EXPENSES = "expenses"
    BANKFEEDS = "bankfeeds"

class GetSyncTransaction200ApplicationJSONStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    PENDING = "Pending"
    VALIDATION_ERROR = "ValidationError"
    COMPLETED = "Completed"
    PUSH_ERROR = "PushError"


@dataclass_json
@dataclasses.dataclass
class GetSyncTransaction200ApplicationJSON:
    integration_type: Optional[GetSyncTransaction200ApplicationJSONIntegrationTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationType') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    status: Optional[GetSyncTransaction200ApplicationJSONStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionId') }})
    

@dataclasses.dataclass
class GetSyncTransactionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_sync_transaction_200_application_json_objects: Optional[list[GetSyncTransaction200ApplicationJSON]] = dataclasses.field(default=None)
    get_sync_transaction_200_text_json_objects: Optional[list[GetSyncTransaction200TextJSON]] = dataclasses.field(default=None)
    get_sync_transaction_200_text_plain_array: Optional[str] = dataclasses.field(default=None)
    