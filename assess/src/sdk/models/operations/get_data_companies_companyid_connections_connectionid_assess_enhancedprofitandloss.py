import dataclasses
from dataclasses_json import dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLossPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLossQueryParams:
    number_of_periods: int = dataclasses.field(metadata={'query_param': { 'field_name': 'numberOfPeriods', 'style': 'form', 'explode': True }})
    period_length: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodLength', 'style': 'form', 'explode': True }})
    report_date: str = dataclasses.field(metadata={'query_param': { 'field_name': 'reportDate', 'style': 'form', 'explode': True }})
    include_display_names: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'includeDisplayNames', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLossRequest:
    path_params: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLossPathParams = dataclasses.field()
    query_params: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLossQueryParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONDimensionsItems:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONDimensions:
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    items: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONDimensionsItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONErrorsDetails:
    additional_prop1: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp1') }})
    additional_prop2: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp2') }})
    additional_prop3: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp3') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONErrors:
    details: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONErrorsDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONMeasures:
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    units: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('units') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName') }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasures:
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension') }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName') }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item') }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName') }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName') }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasures:
    components: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components') }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension') }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName') }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item') }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName') }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName') }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasures:
    components: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components') }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension') }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName') }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item') }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName') }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName') }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasures:
    components: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components') }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension') }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName') }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item') }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName') }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItems:
    components: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItemsReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components') }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension') }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName') }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item') }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportInfo:
    additional_prop1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp1') }})
    additional_prop2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp2') }})
    additional_prop3: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp3') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSON:
    r"""GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSON
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
    
    dimensions: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONDimensions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensions') }})
    errors: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors') }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures') }})
    report_data: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportDimensionsItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportData') }})
    report_info: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSONReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportInfo') }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLossResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_data_companies_company_id_connections_connection_id_assess_enhanced_profit_and_loss_200_application_json_object: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSON] = dataclasses.field(default=None)
    