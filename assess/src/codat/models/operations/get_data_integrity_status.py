from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional

class GetDataIntegrityStatusDataTypeEnum(str, Enum):
    BANKING_ACCOUNTS = "banking-accounts"
    BANKING_TRANSACTIONS = "banking-transactions"
    BANK_ACCOUNTS = "bankAccounts"
    ACCOUNT_TRANSACTIONS = "accountTransactions"


@dataclasses.dataclass
class GetDataIntegrityStatusPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    data_type: GetDataIntegrityStatusDataTypeEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'dataType', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetDataIntegrityStatusRequest:
    path_params: GetDataIntegrityStatusPathParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataIntegrityStatus200ApplicationJSONDataIntegrityTypeAmounts:
    r"""GetDataIntegrityStatus200ApplicationJSONDataIntegrityTypeAmounts
    Only returned for transactions. For accounts, there is nothing returned.
    """
    
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    max: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('max'), 'exclude': lambda f: f is None }})
    min: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('min'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataIntegrityStatus200ApplicationJSONDataIntegrityTypeConnectionIds:
    source: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source'), 'exclude': lambda f: f is None }})
    target: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataIntegrityStatus200ApplicationJSONDataIntegrityTypeDates:
    r"""GetDataIntegrityStatus200ApplicationJSONDataIntegrityTypeDates
    Only returned for transactions. For accounts, there is nothing returned.
    """
    
    max_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('maxDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    max_overlapping_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('maxOverlappingDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    min_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('minDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    min_overlapping_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('minOverlappingDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    
class GetDataIntegrityStatus200ApplicationJSONDataIntegrityTypeStatusInfoCurrentStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    DOES_NOT_EXIST = "DoesNotExist"
    ERROR = "Error"
    COMPLETE = "Complete"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataIntegrityStatus200ApplicationJSONDataIntegrityTypeStatusInfo:
    current_status: Optional[GetDataIntegrityStatus200ApplicationJSONDataIntegrityTypeStatusInfoCurrentStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currentStatus'), 'exclude': lambda f: f is None }})
    last_matched: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lastMatched'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    status_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusMessage'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataIntegrityStatus200ApplicationJSONDataIntegrityType:
    amounts: Optional[GetDataIntegrityStatus200ApplicationJSONDataIntegrityTypeAmounts] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amounts'), 'exclude': lambda f: f is None }})
    connection_ids: Optional[GetDataIntegrityStatus200ApplicationJSONDataIntegrityTypeConnectionIds] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('connectionIds'), 'exclude': lambda f: f is None }})
    dates: Optional[GetDataIntegrityStatus200ApplicationJSONDataIntegrityTypeDates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dates'), 'exclude': lambda f: f is None }})
    status_info: Optional[GetDataIntegrityStatus200ApplicationJSONDataIntegrityTypeStatusInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusInfo'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataIntegrityStatus200ApplicationJSON:
    metadata: Optional[list[GetDataIntegrityStatus200ApplicationJSONDataIntegrityType]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetDataIntegrityStatusResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_data_integrity_status_200_application_json_object: Optional[GetDataIntegrityStatus200ApplicationJSON] = dataclasses.field(default=None)
    