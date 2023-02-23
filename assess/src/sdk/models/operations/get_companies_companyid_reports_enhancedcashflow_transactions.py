from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsQueryParams:
    page: float = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsRequest:
    path_params: GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsPathParams = dataclasses.field()
    query_params: GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsDataSourcesAccountsReportSourceRef:
    source_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsDataSourcesAccounts:
    account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountName'), 'exclude': lambda f: f is None }})
    account_provider: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountProvider'), 'exclude': lambda f: f is None }})
    account_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountType'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    current_balance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currentBalance'), 'exclude': lambda f: f is None }})
    platform_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('platformName'), 'exclude': lambda f: f is None }})
    source_ref: Optional[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsDataSourcesAccountsReportSourceRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceRef'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsDataSources:
    accounts: Optional[list[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsDataSourcesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportInfo:
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyName'), 'exclude': lambda f: f is None }})
    generated_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('generatedDate'), 'exclude': lambda f: f is None }})
    page_number: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber'), 'exclude': lambda f: f is None }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize'), 'exclude': lambda f: f is None }})
    report_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportName'), 'exclude': lambda f: f is None }})
    total_results: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItemsTransactionsReportSourceRef:
    source_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItemsTransactionsTransactionCategory:
    confidence: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('confidence'), 'exclude': lambda f: f is None }})
    levels: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('levels'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItemsTransactions:
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    date_: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    source_ref: Optional[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItemsTransactionsReportSourceRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceRef'), 'exclude': lambda f: f is None }})
    transaction_category: Optional[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItemsTransactionsTransactionCategory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionCategory'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItems:
    transactions: Optional[list[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItemsTransactions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactions:
    data_sources: Optional[list[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsDataSources]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataSources'), 'exclude': lambda f: f is None }})
    report_info: Optional[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportInfo'), 'exclude': lambda f: f is None }})
    report_items: Optional[list[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportItems'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    enhanced_cash_flow_transactions: Optional[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactions] = dataclasses.field(default=None)
    