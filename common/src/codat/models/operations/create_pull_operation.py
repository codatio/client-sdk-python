from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional

class CreatePullOperationDataTypeEnum(str, Enum):
    ACCOUNT_TRANSACTIONS = "accountTransactions"
    BALANCE_SHEET = "balanceSheet"
    BANK_ACCOUNTS = "bankAccounts"
    BANK_TRANSACTIONS = "bankTransactions"
    BILL_CREDIT_NOTES = "billCreditNotes"
    BILL_PAYMENTS = "billPayments"
    BILLS = "bills"
    CASH_FLOW_STATEMENT = "cashFlowStatement"
    CHART_OF_ACCOUNTS = "chartOfAccounts"
    COMPANY = "company"
    CREDIT_NOTES = "creditNotes"
    CUSTOMERS = "customers"
    DIRECT_COSTS = "directCosts"
    DIRECT_INCOMES = "directIncomes"
    INVOICES = "invoices"
    ITEMS = "items"
    JOURNAL_ENTRIES = "journalEntries"
    JOURNALS = "journals"
    PAYMENT_METHODS = "paymentMethods"
    PAYMENTS = "payments"
    PROFIT_AND_LOSS = "profitAndLoss"
    PROJECTS = "projects"
    PURCHASE_ORDERS = "purchaseOrders"
    SALES_ORDERS = "salesOrders"
    SUPPLIERS = "suppliers"
    TAX_RATES = "taxRates"
    TRACKING_CATEGORIES = "trackingCategories"
    TRANSFERS = "transfers"
    BANKING_ACCOUNT_BALANCES = "banking-accountBalances"
    BANKING_ACCOUNTS = "banking-accounts"
    BANKING_TRANSACTION_CATEGORIES = "banking-transactionCategories"
    BANKING_TRANSACTIONS = "banking-transactions"
    COMMERCE_COMPANY_INFO = "commerce-companyInfo"
    COMMERCE_CUSTOMERS = "commerce-customers"
    COMMERCE_DISPUTES = "commerce-disputes"
    COMMERCE_LOCATIONS = "commerce-locations"
    COMMERCE_ORDERS = "commerce-orders"
    COMMERCE_PAYMENT_METHODS = "commerce-paymentMethods"
    COMMERCE_PAYMENTS = "commerce-payments"
    COMMERCE_PRODUCT_CATEGORIES = "commerce-productCategories"
    COMMERCE_PRODUCTS = "commerce-products"
    COMMERCE_TAX_COMPONENTS = "commerce-taxComponents"
    COMMERCE_TRANSACTIONS = "commerce-transactions"


@dataclasses.dataclass
class CreatePullOperationRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    data_type: CreatePullOperationDataTypeEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'dataType', 'style': 'simple', 'explode': False }})
    connection_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'connectionId', 'style': 'form', 'explode': True }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreatePullOperation404ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canBeRetried'), 'exclude': lambda f: f is None }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('correlationId'), 'exclude': lambda f: f is None }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service'), 'exclude': lambda f: f is None }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreatePullOperation401ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canBeRetried'), 'exclude': lambda f: f is None }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('correlationId'), 'exclude': lambda f: f is None }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service'), 'exclude': lambda f: f is None }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode'), 'exclude': lambda f: f is None }})
    
class CreatePullOperationPullOperationStatusEnum(str, Enum):
    INITIAL = "Initial"
    QUEUED = "Queued"
    FETCHING = "Fetching"
    MAP_QUEUED = "MapQueued"
    MAPPING = "Mapping"
    COMPLETE = "Complete"
    FETCH_ERROR = "FetchError"
    MAP_ERROR = "MapError"
    INTERNAL_ERROR = "InternalError"
    PROCESSING_QUEUED = "ProcessingQueued"
    PROCESSING = "Processing"
    PROCESSING_ERROR = "ProcessingError"
    VALIDATION_QUEUED = "ValidationQueued"
    VALIDATING = "Validating"
    VALIDATION_ERROR = "ValidationError"
    AUTH_ERROR = "AuthError"
    CANCELLED = "Cancelled"
    ROUTING = "Routing"
    ROUTING_ERROR = "RoutingError"
    NOT_SUPPORTED = "NotSupported"
    RATE_LIMIT_ERROR = "RateLimitError"
    PERMISSIONS_ERROR = "PermissionsError"
    PREREQUISITE_NOT_MET = "PrerequisiteNotMet"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreatePullOperationPullOperation:
    r"""CreatePullOperationPullOperation
    Information about a queued, in progress or completed pull operation.
    *Formally called `dataset`*
    """
    
    company_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyId') }})
    connection_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionId') }})
    data_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    is_completed: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isCompleted') }})
    is_errored: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isErrored') }})
    progress: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('progress') }})
    requested: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requested'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: CreatePullOperationPullOperationStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

@dataclasses.dataclass
class CreatePullOperationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_pull_operation_401_application_json_object: Optional[CreatePullOperation401ApplicationJSON] = dataclasses.field(default=None)
    create_pull_operation_404_application_json_object: Optional[CreatePullOperation404ApplicationJSON] = dataclasses.field(default=None)
    pull_operation: Optional[CreatePullOperationPullOperation] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    