import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummariesDataTypeEnum(str, Enum):
    BANKING_ACCOUNTS = "banking-accounts"
    BANKING_TRANSACTIONS = "banking-transactions"
    BANK_ACCOUNTS = "bankAccounts"
    ACCOUNT_TRANSACTIONS = "accountTransactions"


@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummariesPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    data_type: GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummariesDataTypeEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'dataType', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummariesQueryParams:
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummariesRequest:
    path_params: GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummariesPathParams = dataclasses.field()
    query_params: GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummariesQueryParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummaries200ApplicationJSONDataIntegrityTypeByAmount:
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    matched: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('matched') }})
    match_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('matchPercentage') }})
    total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('total') }})
    unmatched: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unmatched') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummaries200ApplicationJSONDataIntegrityTypeByCount:
    matched: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('matched') }})
    match_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('matchPercentage') }})
    total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('total') }})
    unmatched: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unmatched') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummaries200ApplicationJSONDataIntegrityType:
    by_amount: Optional[GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummaries200ApplicationJSONDataIntegrityTypeByAmount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('byAmount') }})
    by_count: Optional[GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummaries200ApplicationJSONDataIntegrityTypeByCount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('byCount') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummaries200ApplicationJSON:
    summaries: Optional[list[GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummaries200ApplicationJSONDataIntegrityType]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('summaries') }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummariesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_data_companies_company_id_assess_data_types_data_type_data_integrity_summaries_200_application_json_object: Optional[GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegritySummaries200ApplicationJSON] = dataclasses.field(default=None)
    