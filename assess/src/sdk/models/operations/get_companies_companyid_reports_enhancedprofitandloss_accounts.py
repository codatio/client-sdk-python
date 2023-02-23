import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsQueryParams:
    number_of_periods: int = dataclasses.field(metadata={'query_param': { 'field_name': 'numberOfPeriods', 'style': 'form', 'explode': True }})
    report_date: str = dataclasses.field(metadata={'query_param': { 'field_name': 'reportDate', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsRequest:
    path_params: GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsPathParams = dataclasses.field()
    query_params: GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsQueryParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsEnhancedReportReportInfo:
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyName') }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    generated_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('generatedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    report_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportName') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsEnhancedReportReportItemsAccountCategoryLevels:
    confidence: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('confidence') }})
    level_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('levelName') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsEnhancedReportReportItemsAccountCategory:
    levels: Optional[list[GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsEnhancedReportReportItemsAccountCategoryLevels]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('levels') }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsEnhancedReportReportItems:
    account_category: Optional[GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsEnhancedReportReportItemsAccountCategory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountCategory') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId') }})
    account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountName') }})
    balance: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('balance') }})
    date_: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsEnhancedReport:
    report_info: Optional[GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsEnhancedReportReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportInfo') }})
    report_items: Optional[list[GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsEnhancedReportReportItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportItems') }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    enhanced_report: Optional[GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsEnhancedReport] = dataclasses.field(default=None)
    