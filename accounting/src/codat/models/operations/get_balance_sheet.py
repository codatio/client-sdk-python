from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class GetBalanceSheetPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetBalanceSheetQueryParams:
    period_length: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodLength', 'style': 'form', 'explode': True }})
    periods_to_compare: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodsToCompare', 'style': 'form', 'explode': True }})
    start_month: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'startMonth', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetBalanceSheetSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetBalanceSheetRequest:
    path_params: GetBalanceSheetPathParams = dataclasses.field()
    query_params: GetBalanceSheetQueryParams = dataclasses.field()
    security: GetBalanceSheetSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBalanceSheet200ApplicationJSONBalanceSheetReportLineReportLineReportLineReportLine:
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBalanceSheet200ApplicationJSONBalanceSheetReportLineReportLineReportLine:
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId'), 'exclude': lambda f: f is None }})
    items: Optional[list[GetBalanceSheet200ApplicationJSONBalanceSheetReportLineReportLineReportLineReportLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBalanceSheet200ApplicationJSONBalanceSheetReportLineReportLine:
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId'), 'exclude': lambda f: f is None }})
    items: Optional[list[GetBalanceSheet200ApplicationJSONBalanceSheetReportLineReportLineReportLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBalanceSheet200ApplicationJSONBalanceSheetReportLine:
    r"""GetBalanceSheet200ApplicationJSONBalanceSheetReportLine
    ReportLines for assets. For example, fixed and current assets.
    """
    
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId'), 'exclude': lambda f: f is None }})
    items: Optional[list[GetBalanceSheet200ApplicationJSONBalanceSheetReportLineReportLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBalanceSheet200ApplicationJSONBalanceSheet:
    r"""GetBalanceSheet200ApplicationJSONBalanceSheet
    > View the coverage for balance sheet in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=balanceSheet\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    The balance sheet gives interested parties an idea of the company's financial position, in addition to displaying what the company owns and owes.
    
    > **Balance sheet or profit and loss report?**
    >
    > A profit and loss report summarises the total revenue, expenses, and profit or loss during a specified time period. A balance sheet report shows the financial position of a company at a specific moment in time.
    
    **Structure of this report**
    This report will reflect the structure and line descriptions that the business has set in their own accounting platform.
    
    **History**
    By default, Codat pulls (up to) 24 months of balance sheets for a company. You can adjust this to fetch more history, where available, by updating the `monthsToSync` value for `balanceSheet` on the [data type settings endpoint](https://docs.codat.io/codat-api#/operations/post-profile-syncSettings).
    
    **Want to pull this in a standardised structure?**
    Our [Enhanced Financials](https://docs.codat.io/assess/reports/enhanced-financials/financials) endpoints provide the same report under standardized headings, allowing you to pull it in the same format for all of your business customers.
    """
    
    net_assets: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('netAssets') }})
    assets: Optional[GetBalanceSheet200ApplicationJSONBalanceSheetReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('assets'), 'exclude': lambda f: f is None }})
    date_: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    equity: Optional[GetBalanceSheet200ApplicationJSONBalanceSheetReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('equity'), 'exclude': lambda f: f is None }})
    liabilities: Optional[GetBalanceSheet200ApplicationJSONBalanceSheetReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('liabilities'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBalanceSheet200ApplicationJSON:
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    reports: list[GetBalanceSheet200ApplicationJSONBalanceSheet] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('reports') }})
    earliest_available_month: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('earliestAvailableMonth'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    most_recent_available_month: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('mostRecentAvailableMonth'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetBalanceSheetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_balance_sheet_200_application_json_object: Optional[GetBalanceSheet200ApplicationJSON] = dataclasses.field(default=None)
    