import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsQueryParams:
    number_of_periods: int = dataclasses.field(metadata={'query_param': { 'field_name': 'numberOfPeriods', 'style': 'form', 'explode': True }})
    report_date: str = dataclasses.field(metadata={'query_param': { 'field_name': 'reportDate', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsRequest:
    path_params: GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsPathParams = dataclasses.field()
    query_params: GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsQueryParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportInfo:
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyName') }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    generated_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('generatedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    report_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportName') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportItemsAccountCategoryLevels:
    confidence: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('confidence') }})
    level_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('levelName') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportItemsAccountCategory:
    levels: Optional[list[GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportItemsAccountCategoryLevels]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('levels') }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportItems:
    account_category: Optional[GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportItemsAccountCategory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountCategory') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId') }})
    account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountName') }})
    balance: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('balance') }})
    date_: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReport:
    report_info: Optional[GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportInfo') }})
    report_items: Optional[list[GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportItems') }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    enhanced_report: Optional[GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReport] = dataclasses.field(default=None)
    