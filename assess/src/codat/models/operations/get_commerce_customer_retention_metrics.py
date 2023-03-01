from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class GetCommerceCustomerRetentionMetricsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    
class GetCommerceCustomerRetentionMetricsPeriodUnitEnum(str, Enum):
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"


@dataclasses.dataclass
class GetCommerceCustomerRetentionMetricsQueryParams:
    number_of_periods: int = dataclasses.field(metadata={'query_param': { 'field_name': 'numberOfPeriods', 'style': 'form', 'explode': True }})
    period_length: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodLength', 'style': 'form', 'explode': True }})
    period_unit: GetCommerceCustomerRetentionMetricsPeriodUnitEnum = dataclasses.field(metadata={'query_param': { 'field_name': 'periodUnit', 'style': 'form', 'explode': True }})
    report_date: str = dataclasses.field(metadata={'query_param': { 'field_name': 'reportDate', 'style': 'form', 'explode': True }})
    include_display_names: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'includeDisplayNames', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetCommerceCustomerRetentionMetricsRequest:
    path_params: GetCommerceCustomerRetentionMetricsPathParams = dataclasses.field()
    query_params: GetCommerceCustomerRetentionMetricsQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONDimensionsItems:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONDimensions:
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName'), 'exclude': lambda f: f is None }})
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    items: Optional[list[GetCommerceCustomerRetentionMetrics200ApplicationJSONDimensionsItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONErrorsDetails:
    additional_prop1: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp1'), 'exclude': lambda f: f is None }})
    additional_prop2: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp2'), 'exclude': lambda f: f is None }})
    additional_prop3: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp3'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONErrors:
    details: Optional[GetCommerceCustomerRetentionMetrics200ApplicationJSONErrorsDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('details'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONMeasures:
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName'), 'exclude': lambda f: f is None }})
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    units: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('units'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName'), 'exclude': lambda f: f is None }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasures:
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension'), 'exclude': lambda f: f is None }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName'), 'exclude': lambda f: f is None }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item'), 'exclude': lambda f: f is None }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName'), 'exclude': lambda f: f is None }})
    measures: Optional[list[GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName'), 'exclude': lambda f: f is None }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasures:
    components: Optional[list[GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components'), 'exclude': lambda f: f is None }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension'), 'exclude': lambda f: f is None }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName'), 'exclude': lambda f: f is None }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item'), 'exclude': lambda f: f is None }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName'), 'exclude': lambda f: f is None }})
    measures: Optional[list[GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName'), 'exclude': lambda f: f is None }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasures:
    components: Optional[list[GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components'), 'exclude': lambda f: f is None }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension'), 'exclude': lambda f: f is None }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName'), 'exclude': lambda f: f is None }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item'), 'exclude': lambda f: f is None }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName'), 'exclude': lambda f: f is None }})
    measures: Optional[list[GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName'), 'exclude': lambda f: f is None }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasures:
    components: Optional[list[GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components'), 'exclude': lambda f: f is None }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension'), 'exclude': lambda f: f is None }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName'), 'exclude': lambda f: f is None }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item'), 'exclude': lambda f: f is None }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName'), 'exclude': lambda f: f is None }})
    measures: Optional[list[GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItems:
    components: Optional[list[GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItemsReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components'), 'exclude': lambda f: f is None }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension'), 'exclude': lambda f: f is None }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName'), 'exclude': lambda f: f is None }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item'), 'exclude': lambda f: f is None }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSONReportInfo:
    additional_prop1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp1'), 'exclude': lambda f: f is None }})
    additional_prop2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp2'), 'exclude': lambda f: f is None }})
    additional_prop3: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp3'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCommerceCustomerRetentionMetrics200ApplicationJSON:
    r"""GetCommerceCustomerRetentionMetrics200ApplicationJSON
    Assess reports follow a consistent structure. Reports contain four sections of information:
    
    1. Report definition information such as:
      a. The report info (e.g. enhanced_profit_and_loss).
      b. The display name of the report (e.g. Enhanced Profit and Loss).
    2. Information about the dimension contained in the reports such as:
      a. The type of dimension (e.g. datetime, recordRef).
      b. The display name of the dimension (e.g. Period, Category type, Category sub type).
      c. The details about each item within the dimension (e.g. displayName:\"Jan 2022\", start:\"...\", end:\"...\", id:\"...\", name:\"...\").
    3. Information about the measures contained in the report such as:
      a. The display name of the measure (e.g. value of account, percentage change).
      b. The type of the measure (e.g. currency, percentage).
      c. The unit of the measure (e.g. %, GBP).
    4. The data for the report. When the *includeDisplayName* parameter is set to *true*, it shows the *dimensionDisplayName* and *itemDisplayName* to make the data human-readable. The default setting for *includeDisplayName* is *false*.
    
    Reports can be rendered as follows (ordering is implicit rather than explicit):
    
    ![A table showing an example of how a report can be rendered](https://files.readme.io/1fa20ca-Report1.png)
    
    # Data model
    
    ## Dimensions
    """
    
    dimensions: Optional[list[GetCommerceCustomerRetentionMetrics200ApplicationJSONDimensions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensions'), 'exclude': lambda f: f is None }})
    errors: Optional[list[GetCommerceCustomerRetentionMetrics200ApplicationJSONErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors'), 'exclude': lambda f: f is None }})
    measures: Optional[list[GetCommerceCustomerRetentionMetrics200ApplicationJSONMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures'), 'exclude': lambda f: f is None }})
    report_data: Optional[list[GetCommerceCustomerRetentionMetrics200ApplicationJSONReportDimensionsItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportData'), 'exclude': lambda f: f is None }})
    report_info: Optional[GetCommerceCustomerRetentionMetrics200ApplicationJSONReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportInfo'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetCommerceCustomerRetentionMetricsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_commerce_customer_retention_metrics_200_application_json_object: Optional[GetCommerceCustomerRetentionMetrics200ApplicationJSON] = dataclasses.field(default=None)
    