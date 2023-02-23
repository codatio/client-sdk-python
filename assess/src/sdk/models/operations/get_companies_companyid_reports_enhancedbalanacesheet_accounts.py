from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
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
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportInfo:
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyName'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    generated_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('generatedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    report_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportItemsAccountCategoryLevels:
    confidence: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('confidence'), 'exclude': lambda f: f is None }})
    level_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('levelName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportItemsAccountCategory:
    levels: Optional[list[GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportItemsAccountCategoryLevels]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('levels'), 'exclude': lambda f: f is None }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportItems:
    account_category: Optional[GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportItemsAccountCategory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountCategory'), 'exclude': lambda f: f is None }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId'), 'exclude': lambda f: f is None }})
    account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountName'), 'exclude': lambda f: f is None }})
    balance: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('balance'), 'exclude': lambda f: f is None }})
    date_: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReport:
    report_info: Optional[GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportInfo'), 'exclude': lambda f: f is None }})
    report_items: Optional[list[GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReportReportItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportItems'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    enhanced_report: Optional[GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReport] = dataclasses.field(default=None)
    