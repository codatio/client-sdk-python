import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class CreateExpenseDatasetPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclass_json
@dataclasses.dataclass
class CreateExpenseDatasetRequestBodyItemsLinesRecordRef:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateExpenseDatasetRequestBodyItemsLines:
    account_ref: CreateExpenseDatasetRequestBodyItemsLinesRecordRef = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef') }})
    net_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('netAmount') }})
    tax_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxAmount') }})
    tax_rate_ref: Optional[CreateExpenseDatasetRequestBodyItemsLinesRecordRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateRef') }})
    tracking_refs: Optional[list[CreateExpenseDatasetRequestBodyItemsLinesRecordRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('trackingRefs') }})
    
class CreateExpenseDatasetRequestBodyItemsTypeEnum(str, Enum):
    PAYMENT = "Payment"
    REFUND = "Refund"
    REWARD = "Reward"
    CHARGEBACK = "Chargeback"
    TRANSFER_IN = "TransferIn"
    TRANSFER_OUT = "TransferOut"
    ADJUSTMENT_IN = "AdjustmentIn"
    ADJUSTMENT_OUT = "AdjustmentOut"


@dataclass_json
@dataclasses.dataclass
class CreateExpenseDatasetRequestBodyItems:
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    issue_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('issueDate'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    type: CreateExpenseDatasetRequestBodyItemsTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate') }})
    lines: Optional[list[CreateExpenseDatasetRequestBodyItemsLines]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lines') }})
    merchant_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('merchantName') }})
    notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('notes') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateExpenseDatasetRequestBody:
    items: Optional[list[CreateExpenseDatasetRequestBodyItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items') }})
    

@dataclasses.dataclass
class CreateExpenseDatasetRequest:
    path_params: CreateExpenseDatasetPathParams = dataclasses.field()
    request: Optional[CreateExpenseDatasetRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class CreateExpenseDataset200ApplicationJSON:
    dataset_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('datasetId') }})
    

@dataclasses.dataclass
class CreateExpenseDatasetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_expense_dataset_200_application_json_object: Optional[CreateExpenseDataset200ApplicationJSON] = dataclasses.field(default=None)
    