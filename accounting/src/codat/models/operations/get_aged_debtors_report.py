from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date, datetime
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class GetAgedDebtorsReportPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetAgedDebtorsReportQueryParams:
    number_of_periods: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'numberOfPeriods', 'style': 'form', 'explode': True }})
    period_length_days: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'periodLengthDays', 'style': 'form', 'explode': True }})
    report_date: Optional[date] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'reportDate', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetAgedDebtorsReportRequest:
    path_params: GetAgedDebtorsReportPathParams = dataclasses.field()
    query_params: GetAgedDebtorsReportQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAgedDebtorsReportAgedDebtorsReportAgedDebtorAgedCurrencyOutstandingAgedOutstandingAmountAmountsOutstandingByDataType:
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAgedDebtorsReportAgedDebtorsReportAgedDebtorAgedCurrencyOutstandingAgedOutstandingAmount:
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount'), 'exclude': lambda f: f is None }})
    details: Optional[list[GetAgedDebtorsReportAgedDebtorsReportAgedDebtorAgedCurrencyOutstandingAgedOutstandingAmountAmountsOutstandingByDataType]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('details'), 'exclude': lambda f: f is None }})
    from_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fromDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    to_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('toDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAgedDebtorsReportAgedDebtorsReportAgedDebtorAgedCurrencyOutstanding:
    aged_outstanding_amounts: Optional[list[GetAgedDebtorsReportAgedDebtorsReportAgedDebtorAgedCurrencyOutstandingAgedOutstandingAmount]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('agedOutstandingAmounts'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAgedDebtorsReportAgedDebtorsReportAgedDebtor:
    aged_currency_outstanding: Optional[list[GetAgedDebtorsReportAgedDebtorsReportAgedDebtorAgedCurrencyOutstanding]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('agedCurrencyOutstanding'), 'exclude': lambda f: f is None }})
    customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerId'), 'exclude': lambda f: f is None }})
    customer_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAgedDebtorsReportAgedDebtorsReport:
    data: Optional[list[GetAgedDebtorsReportAgedDebtorsReportAgedDebtor]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    generated: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('generated'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    report_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetAgedDebtorsReportResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    aged_debtors_report: Optional[GetAgedDebtorsReportAgedDebtorsReport] = dataclasses.field(default=None)
    