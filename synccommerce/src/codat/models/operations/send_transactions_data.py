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
class SendTransactionsDataPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    
class SendTransactionsDataRequestBodyTransactionsTransactionSourceRefTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    FEE = "Fee"
    ORDER = "Order"
    PAYMENT = "Payment"
    SERVICE_CHARGE = "ServiceCharge"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SendTransactionsDataRequestBodyTransactionsTransactionSourceRef:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    type: Optional[SendTransactionsDataRequestBodyTransactionsTransactionSourceRefTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    
class SendTransactionsDataRequestBodyTransactionsTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    PAYMENT = "Payment"
    REFUND = "Refund"
    PAYOUT = "Payout"
    FAILED_PAYOUT = "FailedPayout"
    TRANSFER = "Transfer"
    PAYMENT_FEE = "PaymentFee"
    PAYMENT_FEE_REFUND = "PaymentFeeRefund"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SendTransactionsDataRequestBodyTransactions:
    created_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    sub_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subType'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    transaction_source_ref: Optional[SendTransactionsDataRequestBodyTransactionsTransactionSourceRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionSourceRef'), 'exclude': lambda f: f is None }})
    type: Optional[SendTransactionsDataRequestBodyTransactionsTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SendTransactionsDataRequestBody:
    contract_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contractVersion'), 'exclude': lambda f: f is None }})
    transactions: Optional[list[SendTransactionsDataRequestBodyTransactions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactions'), 'exclude': lambda f: f is None }})
    

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


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SendTransactionsData200ApplicationJSONDataTransactionsTransactionSourceRef:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    type: Optional[SendTransactionsData200ApplicationJSONDataTransactionsTransactionSourceRefTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    
class SendTransactionsData200ApplicationJSONDataTransactionsTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    PAYMENT = "Payment"
    REFUND = "Refund"
    PAYOUT = "Payout"
    FAILED_PAYOUT = "FailedPayout"
    TRANSFER = "Transfer"
    PAYMENT_FEE = "PaymentFee"
    PAYMENT_FEE_REFUND = "PaymentFeeRefund"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SendTransactionsData200ApplicationJSONDataTransactions:
    created_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    sub_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subType'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    transaction_source_ref: Optional[SendTransactionsData200ApplicationJSONDataTransactionsTransactionSourceRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionSourceRef'), 'exclude': lambda f: f is None }})
    type: Optional[SendTransactionsData200ApplicationJSONDataTransactionsTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SendTransactionsData200ApplicationJSONData:
    contract_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contractVersion'), 'exclude': lambda f: f is None }})
    transactions: Optional[list[SendTransactionsData200ApplicationJSONDataTransactions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SendTransactionsData200ApplicationJSON:
    data: Optional[SendTransactionsData200ApplicationJSONData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    dataset_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('datasetId'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class SendTransactionsDataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    send_transactions_data_200_application_json_object: Optional[SendTransactionsData200ApplicationJSON] = dataclasses.field(default=None)
    