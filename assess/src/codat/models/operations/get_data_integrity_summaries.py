from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class GetDataIntegritySummariesDataTypeEnum(str, Enum):
    BANKING_ACCOUNTS = "banking-accounts"
    BANKING_TRANSACTIONS = "banking-transactions"
    BANK_ACCOUNTS = "bankAccounts"
    ACCOUNT_TRANSACTIONS = "accountTransactions"


@dataclasses.dataclass
class GetDataIntegritySummariesPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    data_type: GetDataIntegritySummariesDataTypeEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'dataType', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetDataIntegritySummariesQueryParams:
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetDataIntegritySummariesRequest:
    path_params: GetDataIntegritySummariesPathParams = dataclasses.field()
    query_params: GetDataIntegritySummariesQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataIntegritySummaries200ApplicationJSONDataIntegrityTypeByAmount:
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    matched: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('matched'), 'exclude': lambda f: f is None }})
    match_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('matchPercentage'), 'exclude': lambda f: f is None }})
    total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('total'), 'exclude': lambda f: f is None }})
    unmatched: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unmatched'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataIntegritySummaries200ApplicationJSONDataIntegrityTypeByCount:
    matched: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('matched'), 'exclude': lambda f: f is None }})
    match_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('matchPercentage'), 'exclude': lambda f: f is None }})
    total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('total'), 'exclude': lambda f: f is None }})
    unmatched: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unmatched'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataIntegritySummaries200ApplicationJSONDataIntegrityType:
    by_amount: Optional[GetDataIntegritySummaries200ApplicationJSONDataIntegrityTypeByAmount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('byAmount'), 'exclude': lambda f: f is None }})
    by_count: Optional[GetDataIntegritySummaries200ApplicationJSONDataIntegrityTypeByCount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('byCount'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataIntegritySummaries200ApplicationJSON:
    summaries: Optional[list[GetDataIntegritySummaries200ApplicationJSONDataIntegrityType]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('summaries'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetDataIntegritySummariesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_data_integrity_summaries_200_application_json_object: Optional[GetDataIntegritySummaries200ApplicationJSON] = dataclasses.field(default=None)
    