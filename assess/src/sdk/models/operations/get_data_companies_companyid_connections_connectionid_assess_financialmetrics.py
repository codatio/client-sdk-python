from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetricsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetricsQueryParams:
    number_of_periods: int = dataclasses.field(metadata={'query_param': { 'field_name': 'numberOfPeriods', 'style': 'form', 'explode': True }})
    period_length: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodLength', 'style': 'form', 'explode': True }})
    report_date: str = dataclasses.field(metadata={'query_param': { 'field_name': 'reportDate', 'style': 'form', 'explode': True }})
    show_metric_inputs: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'showMetricInputs', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetricsRequest:
    path_params: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetricsPathParams = dataclasses.field()
    query_params: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetricsQueryParams = dataclasses.field()
    
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONErrorsTypeEnum(str, Enum):
    DATA_NOT_SYNCED = "DataNotSynced"
    DATA_NOT_SUPPORTED = "DataNotSupported"
    DATA_SYNC_FAILED = "DataSyncFailed"
    DATA_TYPE_NOT_ENABLED = "DataTypeNotEnabled"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONErrors:
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message'), 'exclude': lambda f: f is None }})
    type: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONErrorsTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricErrorsAssessErrorDetails:
    r"""GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricErrorsAssessErrorDetails
    Dictionary list outlining the missing properties or allowed values.
    """
    
    property_detail1: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('propertyDetail1'), 'exclude': lambda f: f is None }})
    property_detail2: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('propertyDetail2'), 'exclude': lambda f: f is None }})
    property_detail_n: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('propertyDetailN'), 'exclude': lambda f: f is None }})
    
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricErrorsTypeEnum(str, Enum):
    UNCATEGORIZED_ACCOUNTS = "UncategorizedAccounts"
    MISSING_INPUT_DATA = "MissingInputData"
    INPUT_DATA_ERROR = "InputDataError"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricErrors:
    details: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricErrorsAssessErrorDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('details'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message'), 'exclude': lambda f: f is None }})
    type: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricErrorsTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricKeyEnum(str, Enum):
    UNKNOWN = "Unknown"
    EBITDA = "EBITDA"
    DEBT_SERVICE_COVERAGE_RATIO = "DebtServiceCoverageRatio"
    CURRENT_RATIO_QUICK_RATIO = "CurrentRatio QuickRatio"
    GROSS_PROFIT_MARGIN = "GrossProfitMargin"
    FIXED_CHARGE_COVERAGE_RATIO = "FixedChargeCoverageRatio"
    WORKING_CAPITAL = "WorkingCapital"
    FREE_CASH_FLOW = "FreeCashFlow"
    NET_PROFIT_MARGIN = "NetProfitMargin"
    RETURN_ON_ASSETS_RATIO = "ReturnOnAssetsRatio"
    RETURN_ON_EQUITY_RATIO = "ReturnOnEquityRatio"
    OPERATING_PROFIT_MARGIN = "OperatingProfitMargin"
    DEPT_TO_EQUITY = "DeptToEquity"
    DEBT_TO_ASSETS = "DebtToAssets"
    INTEREST_COVERAGE_RATIO = "InterestCoverageRatio"
    CASH_RATIO = "CashRatio"
    INVENTORY_TURNOVER_RATIO = "InventoryTurnoverRatio"
    ASSET_TURNOVER_RATIO = "AssetTurnoverRatio"
    WORKING_CAPITAL_TURNOVER_RATIO = "WorkingCapitalTurnoverRatio"
    DAYS_SALES_OUTSTANDING = "DaysSalesOutstanding"
    DAYS_PAYABLES_OUTSTANDING = "DaysPayablesOutstanding"

class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricMetricUnitEnum(str, Enum):
    RATIO = "Ratio"
    MONEY = "Money"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricPeriodsErrorsAssessErrorDetails:
    r"""GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricPeriodsErrorsAssessErrorDetails
    Dictionary list outlining the missing properties or allowed values.
    """
    
    property_detail1: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('propertyDetail1'), 'exclude': lambda f: f is None }})
    property_detail2: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('propertyDetail2'), 'exclude': lambda f: f is None }})
    property_detail_n: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('propertyDetailN'), 'exclude': lambda f: f is None }})
    
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricPeriodsErrorsTypeEnum(str, Enum):
    MISSING_ACCOUNT_DATA = "MissingAccountData"
    DATES_OUT_OF_RANGE = "DatesOutOfRange"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricPeriodsErrors:
    details: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricPeriodsErrorsAssessErrorDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('details'), 'exclude': lambda f: f is None }})
    massage: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('massage'), 'exclude': lambda f: f is None }})
    type: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricPeriodsErrorsTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricPeriodsInputs:
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricPeriods:
    errors: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricPeriodsErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors'), 'exclude': lambda f: f is None }})
    from_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fromDate'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    inputs: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricPeriodsInputs]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('inputs'), 'exclude': lambda f: f is None }})
    to_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('toDate'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetric:
    errors: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors'), 'exclude': lambda f: f is None }})
    key: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricKeyEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('key'), 'exclude': lambda f: f is None }})
    metric_unit: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricMetricUnitEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metricUnit'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    periods: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetricPeriods]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('periods'), 'exclude': lambda f: f is None }})
    
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONPeriodUnitEnum(str, Enum):
    MONTH = "Month"
    WEEK = "Week"
    DAY = "Day"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSON:
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    errors: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors'), 'exclude': lambda f: f is None }})
    metrics: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONFinancialMetric]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metrics'), 'exclude': lambda f: f is None }})
    period_unit: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSONPeriodUnitEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('periodUnit'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetricsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_data_companies_company_id_connections_connection_id_assess_financial_metrics_200_application_json_object: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSON] = dataclasses.field(default=None)
    