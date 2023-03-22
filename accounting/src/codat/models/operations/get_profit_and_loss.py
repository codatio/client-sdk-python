"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

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


@dataclasses.dataclass
class GetProfitAndLossRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    period_length: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodLength', 'style': 'form', 'explode': True }})  
    periods_to_compare: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodsToCompare', 'style': 'form', 'explode': True }})  
    start_month: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'startMonth', 'style': 'form', 'explode': True }})  
    
class GetProfitAndLoss200ApplicationJSONReportBasisEnum(str, Enum):
    r"""The basis of a report."""
    UNKNOWN = "Unknown"
    ACCRUAL = "Accrual"
    CASH = "Cash"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLineReportLineReportLineReportLine:
    
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Numerical value of the line item."""  
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId'), 'exclude': lambda f: f is None }})
    r"""Identifier for the account, unique for the company in the accounting platform."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the report line item."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLineReportLineReportLine:
    
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Numerical value of the line item."""  
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId'), 'exclude': lambda f: f is None }})
    r"""Identifier for the account, unique for the company in the accounting platform."""  
    items: Optional[list[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLineReportLineReportLineReportLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items'), 'exclude': lambda f: f is None }})
    r"""An array of ReportLine items."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the report line item."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLineReportLine:
    
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Numerical value of the line item."""  
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId'), 'exclude': lambda f: f is None }})
    r"""Identifier for the account, unique for the company in the accounting platform."""  
    items: Optional[list[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLineReportLineReportLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items'), 'exclude': lambda f: f is None }})
    r"""An array of ReportLine items."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the report line item."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLine:
    r"""ReportLine items for cost of sales in the given date range."""
    
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""Numerical value of the line item."""  
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId'), 'exclude': lambda f: f is None }})
    r"""Identifier for the account, unique for the company in the accounting platform."""  
    items: Optional[list[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLineReportLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items'), 'exclude': lambda f: f is None }})
    r"""An array of ReportLine items."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the report line item."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProfitAndLoss200ApplicationJSONProfitAndLossReport:
    r"""> **Language tip:** Profit and loss statement is also referred to as **income statement** under US GAAP (Generally Accepted Accounting Principles).
    
    > View the coverage for profit and loss in the <a className="external" href="https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=profitAndLoss" target="_blank">Data coverage explorer</a>.
    
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
    
    gross_profit: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grossProfit') }})
    r"""Gross profit of the company in the given date range."""  
    net_operating_profit: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('netOperatingProfit') }})
    r"""Net operating profit of the company in the given date range."""  
    net_other_income: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('netOtherIncome') }})
    r"""Net other income of the company in the given date range."""  
    net_profit: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('netProfit') }})
    r"""Net profit of the company in the given date range."""  
    cost_of_sales: Optional[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('costOfSales'), 'exclude': lambda f: f is None }})
    r"""ReportLine items for cost of sales in the given date range."""  
    expenses: Optional[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expenses'), 'exclude': lambda f: f is None }})
    r"""ReportLine items for expenses in the given date range."""  
    from_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fromDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Date from which the report data begins."""  
    income: Optional[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('income'), 'exclude': lambda f: f is None }})
    r"""ReportLine items for income in the given date range."""  
    other_expenses: Optional[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('otherExpenses'), 'exclude': lambda f: f is None }})
    r"""ReportLine items for other expenses in the given date range."""  
    other_income: Optional[GetProfitAndLoss200ApplicationJSONProfitAndLossReportReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('otherIncome'), 'exclude': lambda f: f is None }})
    r"""ReportLine items for other income in the given date range."""  
    to_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('toDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Date on which the report data ends."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProfitAndLoss200ApplicationJSON:
    r"""Success"""
    
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    r"""Base currency of the company in which the profit and loss report is presented."""  
    report_basis: GetProfitAndLoss200ApplicationJSONReportBasisEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportBasis') }})
    r"""The basis of a report."""  
    reports: list[GetProfitAndLoss200ApplicationJSONProfitAndLossReport] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reports') }})
    r"""An array of ProfitAndLossReports."""  
    earliest_available_month: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('earliestAvailableMonth'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Earliest available monthly report data."""  
    most_recent_available_month: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mostRecentAvailableMonth'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Most recent available monthly report data."""  
    

@dataclasses.dataclass
class GetProfitAndLossResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    get_profit_and_loss_200_application_json_object: Optional[GetProfitAndLoss200ApplicationJSON] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    