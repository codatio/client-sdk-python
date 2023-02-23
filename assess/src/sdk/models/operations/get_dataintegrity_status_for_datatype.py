import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional

class GetDataIntegrityStatusForDataTypeDataTypeEnum(str, Enum):
    BANKING_ACCOUNTS = "banking-accounts"
    BANKING_TRANSACTIONS = "banking-transactions"
    BANK_ACCOUNTS = "bankAccounts"
    ACCOUNT_TRANSACTIONS = "accountTransactions"


@dataclasses.dataclass
class GetDataIntegrityStatusForDataTypePathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    data_type: GetDataIntegrityStatusForDataTypeDataTypeEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'dataType', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetDataIntegrityStatusForDataTypeRequest:
    path_params: GetDataIntegrityStatusForDataTypePathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityTypeAmounts:
    r"""GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityTypeAmounts
    Only returned for transactions. For accounts, there is nothing returned.
    """
    
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    max: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('max') }})
    min: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('min') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityTypeConnectionIds:
    source: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source') }})
    target: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityTypeDates:
    r"""GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityTypeDates
    Only returned for transactions. For accounts, there is nothing returned.
    """
    
    max_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('maxDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    max_overlapping_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('maxOverlappingDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    min_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('minDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    min_overlapping_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('minOverlappingDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    
class GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityTypeStatusInfoCurrentStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    DOES_NOT_EXIST = "DoesNotExist"
    ERROR = "Error"
    COMPLETE = "Complete"


@dataclass_json
@dataclasses.dataclass
class GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityTypeStatusInfo:
    current_status: Optional[GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityTypeStatusInfoCurrentStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currentStatus') }})
    last_matched: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lastMatched'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusMessage') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityType:
    amounts: Optional[GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityTypeAmounts] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amounts') }})
    connection_ids: Optional[GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityTypeConnectionIds] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('connectionIds') }})
    dates: Optional[GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityTypeDates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dates') }})
    status_info: Optional[GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityTypeStatusInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusInfo') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataIntegrityStatusForDataType200ApplicationJSON:
    metadata: Optional[list[GetDataIntegrityStatusForDataType200ApplicationJSONDataIntegrityType]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata') }})
    

@dataclasses.dataclass
class GetDataIntegrityStatusForDataTypeResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_data_integrity_status_for_data_type_200_application_json_object: Optional[GetDataIntegrityStatusForDataType200ApplicationJSON] = dataclasses.field(default=None)
    