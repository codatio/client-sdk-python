import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
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
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsDataSourcesAccountsReportSourceRef:
    source_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsDataSourcesAccounts:
    account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountName') }})
    account_provider: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountProvider') }})
    account_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountType') }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    current_balance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currentBalance') }})
    platform_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('platformName') }})
    source_ref: Optional[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsDataSourcesAccountsReportSourceRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceRef') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsDataSources:
    accounts: Optional[list[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsDataSourcesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportInfo:
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyName') }})
    generated_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('generatedDate') }})
    page_number: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber') }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize') }})
    report_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportName') }})
    total_results: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItemsTransactionsReportSourceRef:
    source_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItemsTransactionsTransactionCategory:
    confidence: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('confidence') }})
    levels: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('levels') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItemsTransactions:
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount') }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    date_: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    source_ref: Optional[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItemsTransactionsReportSourceRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceRef') }})
    transaction_category: Optional[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItemsTransactionsTransactionCategory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionCategory') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItems:
    transactions: Optional[list[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItemsTransactions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactions') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactions:
    data_sources: Optional[list[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsDataSources]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataSources') }})
    report_info: Optional[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportInfo') }})
    report_items: Optional[list[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactionsReportItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportItems') }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    enhanced_cash_flow_transactions: Optional[GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactions] = dataclasses.field(default=None)
    