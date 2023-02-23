import dataclasses
import dateutil.parser
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class ListBankingTransactionsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListBankingTransactionsQueryParams:
    page: float = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListBankingTransactionsSecurity:
    api_key: shared_security.SchemeAPIKey = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class ListBankingTransactionsRequest:
    path_params: ListBankingTransactionsPathParams = dataclasses.field()
    query_params: ListBankingTransactionsQueryParams = dataclasses.field()
    security: ListBankingTransactionsSecurity = dataclasses.field()
    
class ListBankingTransactions200ApplicationJSONSourceModifiedDateCodeEnum(str, Enum):
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


@dataclass_json
@dataclasses.dataclass
class ListBankingTransactions200ApplicationJSONSourceModifiedDateTransactionCategoryRef:
    r"""ListBankingTransactions200ApplicationJSONSourceModifiedDateTransactionCategoryRef
    An object of bank transaction category reference data.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ListBankingTransactions200ApplicationJSONSourceModifiedDate:
    r"""ListBankingTransactions200ApplicationJSONSourceModifiedDate
    The Banking Transactions data type provides an immutable source of up-to-date information on income and expenditure.
    
    View the coverage for banking transactions in the [Data Coverage Explorer](https://knowledge.codat.io/supported-features/banking?view=tab-by-data-type&dataType=banking-transactions).
    """
    
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId') }})
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount') }})
    authorized_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('authorizedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    code: Optional[ListBankingTransactions200ApplicationJSONSourceModifiedDateCodeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    merchant_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('merchantName') }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    posted_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('postedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    transaction_category_ref: Optional[ListBankingTransactions200ApplicationJSONSourceModifiedDateTransactionCategoryRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionCategoryRef') }})
    

@dataclass_json
@dataclasses.dataclass
class ListBankingTransactions200ApplicationJSON:
    results: Optional[ListBankingTransactions200ApplicationJSONSourceModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    

@dataclasses.dataclass
class ListBankingTransactionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_banking_transactions_200_application_json_object: Optional[ListBankingTransactions200ApplicationJSON] = dataclasses.field(default=None)
    