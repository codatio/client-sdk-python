from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheetPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheetQueryParams:
    number_of_periods: int = dataclasses.field(metadata={'query_param': { 'field_name': 'numberOfPeriods', 'style': 'form', 'explode': True }})
    period_length: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodLength', 'style': 'form', 'explode': True }})
    report_date: str = dataclasses.field(metadata={'query_param': { 'field_name': 'reportDate', 'style': 'form', 'explode': True }})
    include_display_names: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'includeDisplayNames', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheetRequest:
    path_params: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheetPathParams = dataclasses.field()
    query_params: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheetQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONDimensionsItems:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONDimensions:
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName'), 'exclude': lambda f: f is None }})
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    items: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONDimensionsItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONErrorsDetails:
    additional_prop1: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp1'), 'exclude': lambda f: f is None }})
    additional_prop2: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp2'), 'exclude': lambda f: f is None }})
    additional_prop3: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp3'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONErrors:
    details: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONErrorsDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('details'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONMeasures:
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName'), 'exclude': lambda f: f is None }})
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    units: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('units'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName'), 'exclude': lambda f: f is None }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasures:
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension'), 'exclude': lambda f: f is None }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName'), 'exclude': lambda f: f is None }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item'), 'exclude': lambda f: f is None }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName'), 'exclude': lambda f: f is None }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName'), 'exclude': lambda f: f is None }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasures:
    components: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components'), 'exclude': lambda f: f is None }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension'), 'exclude': lambda f: f is None }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName'), 'exclude': lambda f: f is None }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item'), 'exclude': lambda f: f is None }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName'), 'exclude': lambda f: f is None }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName'), 'exclude': lambda f: f is None }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasures:
    components: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components'), 'exclude': lambda f: f is None }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension'), 'exclude': lambda f: f is None }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName'), 'exclude': lambda f: f is None }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item'), 'exclude': lambda f: f is None }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName'), 'exclude': lambda f: f is None }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresMeasures:
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    measure_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measureDisplayName'), 'exclude': lambda f: f is None }})
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasures:
    components: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components'), 'exclude': lambda f: f is None }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension'), 'exclude': lambda f: f is None }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName'), 'exclude': lambda f: f is None }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item'), 'exclude': lambda f: f is None }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName'), 'exclude': lambda f: f is None }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasuresMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItems:
    components: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItemsReportComponentMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components'), 'exclude': lambda f: f is None }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimension'), 'exclude': lambda f: f is None }})
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensionDisplayName'), 'exclude': lambda f: f is None }})
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item'), 'exclude': lambda f: f is None }})
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemDisplayName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportInfo:
    additional_prop1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp1'), 'exclude': lambda f: f is None }})
    additional_prop2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp2'), 'exclude': lambda f: f is None }})
    additional_prop3: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalProp3'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSON:
    r"""GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSON
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
    
    dimensions: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONDimensions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dimensions'), 'exclude': lambda f: f is None }})
    errors: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors'), 'exclude': lambda f: f is None }})
    measures: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONMeasures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('measures'), 'exclude': lambda f: f is None }})
    report_data: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportDimensionsItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportData'), 'exclude': lambda f: f is None }})
    report_info: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSONReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportInfo'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_data_companies_company_id_connections_connection_id_assess_enhanced_balance_sheet_200_application_json_object: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSON] = dataclasses.field(default=None)
    