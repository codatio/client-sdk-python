import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class GetCompaniesCompanyIDConnectionsConnectionIDPushDataTypeEnum(str, Enum):
    INVOICES = "invoices"
    ACCOUNTS = "accounts"
    COMMERCE_PAYMENTS = "commerce-payments"
    BANKING_ACCOUNTS = "banking-accounts"
    COMPANY = "company"
    PROFIT_AND_LOSS = "profitAndLoss"
    COMMERCE_TRANSACTIONS = "commerce-transactions"
    BILLS = "bills"
    CUSTOMERS = "customers"


@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    data_type: GetCompaniesCompanyIDConnectionsConnectionIDPushDataTypeEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'dataType', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushRequest:
    path_params: GetCompaniesCompanyIDConnectionsConnectionIDPushPathParams = dataclasses.field()
    
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoiceOptionTypeEnum(str, Enum):
    ARRAY = "Array"
    OBJECT = "Object"
    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    FILE = "File"
    MULTI_PART = "MultiPart"


@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('field') }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ref') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfo:
    information: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('information') }})
    warnings: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoice:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    type: GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoiceOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    rel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rel') }})
    validation: Optional[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation') }})
    
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoiceOptionTypeEnum(str, Enum):
    ARRAY = "Array"
    OBJECT = "Object"
    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    FILE = "File"
    MULTI_PART = "MultiPart"


@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('field') }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ref') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfo:
    information: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('information') }})
    warnings: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoice:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    type: GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoiceOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    options: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options') }})
    rel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rel') }})
    validation: Optional[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation') }})
    
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoiceOptionTypeEnum(str, Enum):
    ARRAY = "Array"
    OBJECT = "Object"
    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    FILE = "File"
    MULTI_PART = "MultiPart"


@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('field') }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ref') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushValidationInfo:
    information: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('information') }})
    warnings: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoice:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    type: GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoiceOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    options: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options') }})
    rel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rel') }})
    validation: Optional[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoicePushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation') }})
    
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoiceOptionTypeEnum(str, Enum):
    ARRAY = "Array"
    OBJECT = "Object"
    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    FILE = "File"
    MULTI_PART = "MultiPart"


@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('field') }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ref') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushValidationInfo:
    information: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('information') }})
    warnings: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoice:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    type: GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoiceOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    options: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options') }})
    rel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rel') }})
    validation: Optional[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoicePushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation') }})
    
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionOptionTypeEnum(str, Enum):
    ARRAY = "Array"
    OBJECT = "Object"
    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    FILE = "File"
    MULTI_PART = "MultiPart"


@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('field') }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ref') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushValidationInfo:
    information: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('information') }})
    warnings: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushPushOption:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    type: GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    options: Optional[list[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options') }})
    rel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rel') }})
    validation: Optional[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOptionPushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation') }})
    

@dataclasses.dataclass
class GetCompaniesCompanyIDConnectionsConnectionIDPushResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    push_option: Optional[GetCompaniesCompanyIDConnectionsConnectionIDPushPushOption] = dataclasses.field(default=None)
    