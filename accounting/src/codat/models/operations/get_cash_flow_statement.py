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
class GetCashFlowStatementPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetCashFlowStatementQueryParams:
    period_length: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodLength', 'style': 'form', 'explode': True }})
    periods_to_compare: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodsToCompare', 'style': 'form', 'explode': True }})
    start_month: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'startMonth', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetCashFlowStatementSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetCashFlowStatementRequest:
    path_params: GetCashFlowStatementPathParams = dataclasses.field()
    query_params: GetCashFlowStatementQueryParams = dataclasses.field()
    security: GetCashFlowStatementSecurity = dataclasses.field()
    
class GetCashFlowStatement200ApplicationJSONReportBasisEnum(str, Enum):
    UNKNOWN = "Unknown"
    ACCRUAL = "Accrual"
    CASH = "Cash"

class GetCashFlowStatement200ApplicationJSONReportInputEnum(str, Enum):
    UNKNOWN = "Unknown"
    INDIRECT = "Indirect"
    DIRECT = "Direct"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCashFlowStatement200ApplicationJSONCashFlowStatementReportLineReportLineReportLineReportLine:
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCashFlowStatement200ApplicationJSONCashFlowStatementReportLineReportLineReportLine:
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId'), 'exclude': lambda f: f is None }})
    items: Optional[list[GetCashFlowStatement200ApplicationJSONCashFlowStatementReportLineReportLineReportLineReportLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCashFlowStatement200ApplicationJSONCashFlowStatementReportLineReportLine:
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId'), 'exclude': lambda f: f is None }})
    items: Optional[list[GetCashFlowStatement200ApplicationJSONCashFlowStatementReportLineReportLineReportLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCashFlowStatement200ApplicationJSONCashFlowStatementReportLine:
    r"""GetCashFlowStatement200ApplicationJSONCashFlowStatementReportLine
    ReportLines for cash payments to suppliers for the purchase of goods or services.
    """
    
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId'), 'exclude': lambda f: f is None }})
    items: Optional[list[GetCashFlowStatement200ApplicationJSONCashFlowStatementReportLineReportLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCashFlowStatement200ApplicationJSONCashFlowStatement:
    r"""GetCashFlowStatement200ApplicationJSONCashFlowStatement
    > View the coverage for cash flow statement in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=cashFlowStatement\" target=\"_blank\">Data coverage explorer</a>.
    
    > ** Operating activities only**  
    > 
    > Currently, the cash flow statement shows cash that flows into and out of the company from operating activities *only*. Operating activities generate cash from the sale of goods or services.
    
    ## Overview
    
    A cash flow statement is a financial report that records all cash that is received or spent by a company during a given period. It gives you a clearer picture of the company’s performance, and their ability to pay creditors and finance growth.
    
    > **Cash flow statement or balance sheet?**
    > 
    > Look at the cash flow statement to understand a company's ability to pay its bills. Although the balance sheet may show healthy earnings at a specific point in time, the cash flow statement allows you to see whether the company is meeting its financial commitments, such as paying creditors or its employees.
    """
    
    cash_payments: Optional[GetCashFlowStatement200ApplicationJSONCashFlowStatementReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('cashPayments'), 'exclude': lambda f: f is None }})
    cash_receipts: Optional[GetCashFlowStatement200ApplicationJSONCashFlowStatementReportLine] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('cashReceipts'), 'exclude': lambda f: f is None }})
    from_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fromDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    to_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('toDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCashFlowStatement200ApplicationJSON:
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    report_basis: GetCashFlowStatement200ApplicationJSONReportBasisEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportBasis') }})
    report_input: GetCashFlowStatement200ApplicationJSONReportInputEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportInput') }})
    reports: list[GetCashFlowStatement200ApplicationJSONCashFlowStatement] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('reports') }})
    earliest_available_month: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('earliestAvailableMonth'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    most_recent_available_month: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('mostRecentAvailableMonth'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetCashFlowStatementResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_cash_flow_statement_200_application_json_object: Optional[GetCashFlowStatement200ApplicationJSON] = dataclasses.field(default=None)
    