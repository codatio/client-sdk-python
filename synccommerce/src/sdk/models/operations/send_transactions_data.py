import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class SendTransactionsDataPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    
class SendTransactionsDataRequestBodyTransactionsTransactionSourceRefTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    FEE = "Fee"
    ORDER = "Order"
    PAYMENT = "Payment"
    SERVICE_CHARGE = "ServiceCharge"


@dataclass_json
@dataclasses.dataclass
class SendTransactionsDataRequestBodyTransactionsTransactionSourceRef:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: Optional[SendTransactionsDataRequestBodyTransactionsTransactionSourceRefTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    
class SendTransactionsDataRequestBodyTransactionsTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    PAYMENT = "Payment"
    REFUND = "Refund"
    PAYOUT = "Payout"
    FAILED_PAYOUT = "FailedPayout"
    TRANSFER = "Transfer"
    PAYMENT_FEE = "PaymentFee"
    PAYMENT_FEE_REFUND = "PaymentFeeRefund"


@dataclass_json
@dataclasses.dataclass
class SendTransactionsDataRequestBodyTransactions:
    created_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    sub_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subType') }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount') }})
    transaction_source_ref: Optional[SendTransactionsDataRequestBodyTransactionsTransactionSourceRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionSourceRef') }})
    type: Optional[SendTransactionsDataRequestBodyTransactionsTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class SendTransactionsDataRequestBody:
    contract_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contractVersion') }})
    transactions: Optional[list[SendTransactionsDataRequestBodyTransactions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactions') }})
    

@dataclasses.dataclass
class SendTransactionsDataRequest:
    path_params: SendTransactionsDataPathParams = dataclasses.field()
    request: Optional[SendTransactionsDataRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    
class SendTransactionsData200ApplicationJSONDataTransactionsTransactionSourceRefTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    FEE = "Fee"
    ORDER = "Order"
    PAYMENT = "Payment"
    SERVICE_CHARGE = "ServiceCharge"


@dataclass_json
@dataclasses.dataclass
class SendTransactionsData200ApplicationJSONDataTransactionsTransactionSourceRef:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: Optional[SendTransactionsData200ApplicationJSONDataTransactionsTransactionSourceRefTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    
class SendTransactionsData200ApplicationJSONDataTransactionsTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    PAYMENT = "Payment"
    REFUND = "Refund"
    PAYOUT = "Payout"
    FAILED_PAYOUT = "FailedPayout"
    TRANSFER = "Transfer"
    PAYMENT_FEE = "PaymentFee"
    PAYMENT_FEE_REFUND = "PaymentFeeRefund"


@dataclass_json
@dataclasses.dataclass
class SendTransactionsData200ApplicationJSONDataTransactions:
    created_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    sub_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subType') }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount') }})
    transaction_source_ref: Optional[SendTransactionsData200ApplicationJSONDataTransactionsTransactionSourceRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionSourceRef') }})
    type: Optional[SendTransactionsData200ApplicationJSONDataTransactionsTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class SendTransactionsData200ApplicationJSONData:
    contract_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contractVersion') }})
    transactions: Optional[list[SendTransactionsData200ApplicationJSONDataTransactions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactions') }})
    

@dataclass_json
@dataclasses.dataclass
class SendTransactionsData200ApplicationJSON:
    data: Optional[SendTransactionsData200ApplicationJSONData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    dataset_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('datasetId') }})
    

@dataclasses.dataclass
class SendTransactionsDataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    send_transactions_data_200_application_json_object: Optional[SendTransactionsData200ApplicationJSON] = dataclasses.field(default=None)
    