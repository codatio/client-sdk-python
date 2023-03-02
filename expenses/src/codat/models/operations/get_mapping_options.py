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
class GetMappingOptionsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetMappingOptionsRequest:
    path_params: GetMappingOptionsPathParams = dataclasses.field()
    
class GetMappingOptions200ApplicationJSONAccountsAccountTypeEnum(str, Enum):
    ASSET = "Asset"
    LIABILITY = "Liability"
    INCOME = "Income"
    EXPENSE = "Expense"
    EQUITY = "Equity"

class GetMappingOptions200ApplicationJSONAccountsValidTransactionTypesEnum(str, Enum):
    PAYMENT = "Payment"
    REFUND = "Refund"
    REWARD = "Reward"
    CHARGEBACK = "Chargeback"
    TRANSFER_IN = "TransferIn"
    TRANSFER_OUT = "TransferOut"
    ADJUSTMENT_IN = "AdjustmentIn"
    ADJUSTMENT_OUT = "AdjustmentOut"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetMappingOptions200ApplicationJSONAccounts:
    account_type: Optional[GetMappingOptions200ApplicationJSONAccountsAccountTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountType'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    valid_transaction_types: Optional[list[GetMappingOptions200ApplicationJSONAccountsValidTransactionTypesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validTransactionTypes'), 'exclude': lambda f: f is None }})
    
class GetMappingOptions200ApplicationJSONTaxRatesValidTransactionTypesEnum(str, Enum):
    PAYMENT = "Payment"
    REFUND = "Refund"
    REWARD = "Reward"
    CHARGEBACK = "Chargeback"
    TRANSFER_IN = "TransferIn"
    TRANSFER_OUT = "TransferOut"
    ADJUSTMENT_IN = "AdjustmentIn"
    ADJUSTMENT_OUT = "AdjustmentOut"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetMappingOptions200ApplicationJSONTaxRates:
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code'), 'exclude': lambda f: f is None }})
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('effectiveTaxRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    total_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalTaxRate'), 'exclude': lambda f: f is None }})
    valid_transaction_types: Optional[list[GetMappingOptions200ApplicationJSONTaxRatesValidTransactionTypesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validTransactionTypes'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetMappingOptions200ApplicationJSONTrackingCategories:
    has_children: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hasChildren'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    parent_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('parentId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetMappingOptions200ApplicationJSON:
    accounts: Optional[list[GetMappingOptions200ApplicationJSONAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    expense_provider: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('expenseProvider'), 'exclude': lambda f: f is None }})
    tax_rates: Optional[list[GetMappingOptions200ApplicationJSONTaxRates]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRates'), 'exclude': lambda f: f is None }})
    tracking_categories: Optional[list[GetMappingOptions200ApplicationJSONTrackingCategories]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('trackingCategories'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetMappingOptionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_mapping_options_200_application_json_object: Optional[GetMappingOptions200ApplicationJSON] = dataclasses.field(default=None)
    