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
class GetProfitAndLossPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetProfitAndLossQueryParams:
    period_length: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodLength', 'style': 'form', 'explode': True }})
    periods_to_compare: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodsToCompare', 'style': 'form', 'explode': True }})
    start_month: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'startMonth', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetProfitAndLossSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetProfitAndLossRequest:
    path_params: GetProfitAndLossPathParams = dataclasses.field()
    query_params: GetProfitAndLossQueryParams = dataclasses.field()
    security: GetProfitAndLossSecurity = dataclasses.field()
    
class GetProfitAndLoss200ApplicationJSONReportBasisEnum(str, Enum):
    UNKNOWN = "Unknown"
    ACCRUAL = "Accrual"
    CASH = "Cash"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLineReportLineReportLineReportLine:
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLineReportLineReportLine:
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId'), 'exclude': lambda f: f is None }})
    items: Optional[list[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLineReportLineReportLineReportLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLineReportLine:
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId'), 'exclude': lambda f: f is None }})
    items: Optional[list[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLineReportLineReportLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLine:
    r"""GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLine
    ReportLine items for cost of sales in the given date range.
    """
    
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId'), 'exclude': lambda f: f is None }})
    items: Optional[list[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLineReportLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProfitAndLoss200ApplicationJSONProfitAndLossReport:
    r"""GetProfitAndLoss200ApplicationJSONProfitAndLossReport
    > **Language tip:** Profit and loss statement is also referred to as **income statement** under US GAAP (Generally Accepted Accounting Principles).
    
    > View the coverage for profit and loss in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=profitAndLoss\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    The purpose of a profit and loss report is to present the financial performance of a company over a specified time period.
    
    A profit and loss report shows a company's total income and expenses for a specified period of time and whether a profit or loss has been made.
    
    > **Profit and loss or balance sheet?**  
    > Profit and loss reports summarise the total revenue, expenses, and profit or loss over a specified time period. A balance sheet report presents all assets, liability, and equity for a given date.
    
    
    **Structure of this report**  
    This report will reflect the structure and line descriptions that the business has set in their own accounting platform.
    
    **History**  
    By default, Codat pulls (up to) 24 months of profit and loss history for a company. You can adjust this to fetch more history, where available, by updating the `monthsToSync` value for `profitAndLoss` on the [data type settings endpoint](https://docs.codat.io/codat-api#/operations/post-profile-syncSettings).
    
    **Want to pull this in a standardised structure?**  
    Our [Enhanced Financials](https://docs.codat.io/assess/reports/enhanced-financials/financials) endpoints provide the same report under standardized headings, allowing you to pull it in the same format for all of your business customers.
    """
    
    gross_profit: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('grossProfit') }})
    net_operating_profit: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('netOperatingProfit') }})
    net_other_income: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('netOtherIncome') }})
    net_profit: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('netProfit') }})
    cost_of_sales: Optional[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('costOfSales'), 'exclude': lambda f: f is None }})
    expenses: Optional[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('expenses'), 'exclude': lambda f: f is None }})
    from_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fromDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    income: Optional[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('income'), 'exclude': lambda f: f is None }})
    other_expenses: Optional[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('otherExpenses'), 'exclude': lambda f: f is None }})
    other_income: Optional[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('otherIncome'), 'exclude': lambda f: f is None }})
    to_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('toDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProfitAndLoss200ApplicationJSON:
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    report_basis: GetProfitAndLoss200ApplicationJSONReportBasisEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportBasis') }})
    reports: list[GetProfitAndLoss200ApplicationJSONProfitAndLossReport] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('reports') }})
    earliest_available_month: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('earliestAvailableMonth'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    most_recent_available_month: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('mostRecentAvailableMonth'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetProfitAndLossResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_profit_and_loss_200_application_json_object: Optional[GetProfitAndLoss200ApplicationJSON] = dataclasses.field(default=None)
    