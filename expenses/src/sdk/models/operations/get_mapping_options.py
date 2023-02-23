import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetMappingOptionsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetMappingOptionsRequest:
    path_params: GetMappingOptionsPathParams = dataclasses.field()
    
class GetMappingOptions200TextJSONAccountsAccountTypeEnum(str, Enum):
    ASSET = "Asset"
    LIABILITY = "Liability"
    INCOME = "Income"
    EXPENSE = "Expense"
    EQUITY = "Equity"

class GetMappingOptions200TextJSONAccountsValidTransactionTypesEnum(str, Enum):
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
class GetMappingOptions200TextJSONAccounts:
    account_type: Optional[GetMappingOptions200TextJSONAccountsAccountTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountType') }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    valid_transaction_types: Optional[list[GetMappingOptions200TextJSONAccountsValidTransactionTypesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validTransactionTypes') }})
    
class GetMappingOptions200TextJSONTaxRatesValidTransactionTypesEnum(str, Enum):
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
class GetMappingOptions200TextJSONTaxRates:
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('effectiveTaxRate') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    total_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalTaxRate') }})
    valid_transaction_types: Optional[list[GetMappingOptions200TextJSONTaxRatesValidTransactionTypesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validTransactionTypes') }})
    

@dataclass_json
@dataclasses.dataclass
class GetMappingOptions200TextJSONTrackingCategories:
    has_children: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hasChildren') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    parent_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('parentId') }})
    

@dataclass_json
@dataclasses.dataclass
class GetMappingOptions200TextJSON:
    accounts: Optional[list[GetMappingOptions200TextJSONAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    expense_provider: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('expenseProvider') }})
    tax_rates: Optional[list[GetMappingOptions200TextJSONTaxRates]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRates') }})
    tracking_categories: Optional[list[GetMappingOptions200TextJSONTrackingCategories]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('trackingCategories') }})
    
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


@dataclass_json
@dataclasses.dataclass
class GetMappingOptions200ApplicationJSONAccounts:
    account_type: Optional[GetMappingOptions200ApplicationJSONAccountsAccountTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountType') }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    valid_transaction_types: Optional[list[GetMappingOptions200ApplicationJSONAccountsValidTransactionTypesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validTransactionTypes') }})
    
class GetMappingOptions200ApplicationJSONTaxRatesValidTransactionTypesEnum(str, Enum):
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
class GetMappingOptions200ApplicationJSONTaxRates:
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('effectiveTaxRate') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    total_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalTaxRate') }})
    valid_transaction_types: Optional[list[GetMappingOptions200ApplicationJSONTaxRatesValidTransactionTypesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validTransactionTypes') }})
    

@dataclass_json
@dataclasses.dataclass
class GetMappingOptions200ApplicationJSONTrackingCategories:
    has_children: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hasChildren') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    parent_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('parentId') }})
    

@dataclass_json
@dataclasses.dataclass
class GetMappingOptions200ApplicationJSON:
    accounts: Optional[list[GetMappingOptions200ApplicationJSONAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    expense_provider: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('expenseProvider') }})
    tax_rates: Optional[list[GetMappingOptions200ApplicationJSONTaxRates]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRates') }})
    tracking_categories: Optional[list[GetMappingOptions200ApplicationJSONTrackingCategories]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('trackingCategories') }})
    

@dataclasses.dataclass
class GetMappingOptionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_mapping_options_200_application_json_object: Optional[GetMappingOptions200ApplicationJSON] = dataclasses.field(default=None)
    get_mapping_options_200_text_json_object: Optional[GetMappingOptions200TextJSON] = dataclasses.field(default=None)
    get_mapping_options_200_text_plain_object: Optional[str] = dataclasses.field(default=None)
    