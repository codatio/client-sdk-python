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
class GetBankingTransactionPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    transaction_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transactionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetBankingTransactionSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetBankingTransactionRequest:
    path_params: GetBankingTransactionPathParams = dataclasses.field()
    security: GetBankingTransactionSecurity = dataclasses.field()
    
class GetBankingTransactionSourceModifiedDateCodeEnum(str, Enum):
    UNKNOWN = "Unknown"
    FEE = "Fee"
    PAYMENT = "Payment"
    CASH = "Cash"
    TRANSFER = "Transfer"
    INTEREST = "Interest"
    CASHBACK = "Cashback"
    CHEQUE = "Cheque"
    DIRECT_DEBIT = "DirectDebit"
    PURCHASE = "Purchase"
    STANDING_ORDER = "StandingOrder"
    ADJUSTMENT = "Adjustment"
    CREDIT = "Credit"
    OTHER = "Other"
    NOT_SUPPORTED = "NotSupported"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankingTransactionSourceModifiedDateTransactionCategoryRef:
    r"""GetBankingTransactionSourceModifiedDateTransactionCategoryRef
    An object of bank transaction category reference data.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankingTransactionSourceModifiedDate:
    r"""GetBankingTransactionSourceModifiedDate
    The Banking Transactions data type provides an immutable source of up-to-date information on income and expenditure.
    
    View the coverage for banking transactions in the [Data Coverage Explorer](https://knowledge.codat.io/supported-features/banking?view=tab-by-data-type&dataType=banking-transactions).
    """
    
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId') }})
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount'), 'exclude': lambda f: f is None }})
    authorized_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('authorizedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    code: Optional[GetBankingTransactionSourceModifiedDateCodeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    merchant_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('merchantName'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    posted_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('postedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    transaction_category_ref: Optional[GetBankingTransactionSourceModifiedDateTransactionCategoryRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionCategoryRef'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetBankingTransactionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    source_modified_date: Optional[GetBankingTransactionSourceModifiedDate] = dataclasses.field(default=None)
    