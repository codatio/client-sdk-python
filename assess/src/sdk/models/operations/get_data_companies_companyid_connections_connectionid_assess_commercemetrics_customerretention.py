import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetentionPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetentionPeriodUnitEnum(str, Enum):
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"


@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetentionQueryParams:
    number_of_periods: int = dataclasses.field(metadata={'query_param': { 'field_name': 'numberOfPeriods', 'style': 'form', 'explode': True }})
    period_length: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodLength', 'style': 'form', 'explode': True }})
    period_unit: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetentionPeriodUnitEnum = dataclasses.field(metadata={'query_param': { 'field_name': 'periodUnit', 'style': 'form', 'explode': True }})
    report_date: str = dataclasses.field(metadata={'query_param': { 'field_name': 'reportDate', 'style': 'form', 'explode': True }})
    include_display_names: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'includeDisplayNames', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetentionRequest:
    path_params: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetentionPathParams = dataclasses.field()
    query_params: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetentionQueryParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONDimensionsItems:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONDimensions:
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    items: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONDimensionsItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONErrorsDetails:
    additional_prop1: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp1') }})
    additional_prop2: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp2') }})
    additional_prop3: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp3') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONErrors:
    details: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONErrorsDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONMeasures:
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    units: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('units') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName') }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasures:
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension') }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName') }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item') }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName') }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName') }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasures:
    components: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components') }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension') }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName') }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item') }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName') }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName') }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasures:
    components: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components') }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension') }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName') }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item') }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName') }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName') }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasures:
    components: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components') }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension') }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName') }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item') }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName') }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItems:
    components: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItemsReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components') }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension') }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName') }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item') }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportInfo:
    additional_prop1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp1') }})
    additional_prop2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp2') }})
    additional_prop3: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp3') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSON:
    r"""GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSON
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
    
    dimensions: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONDimensions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensions') }})
    errors: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors') }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures') }})
    report_data: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportDimensionsItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportData') }})
    report_info: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSONReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportInfo') }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetentionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_data_companies_company_id_connections_connection_id_assess_commerce_metrics_customer_retention_200_application_json_object: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSON] = dataclasses.field(default=None)
    