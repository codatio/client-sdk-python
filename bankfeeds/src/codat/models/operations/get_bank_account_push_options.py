from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class GetBankAccountPushOptionsPathParams:
    account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetBankAccountPushOptionsQueryParams:
    page: float = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetBankAccountPushOptionsSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetBankAccountPushOptionsRequest:
    path_params: GetBankAccountPushOptionsPathParams = dataclasses.field()
    query_params: GetBankAccountPushOptionsQueryParams = dataclasses.field()
    security: GetBankAccountPushOptionsSecurity = dataclasses.field()
    
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoiceOptionTypeEnum(str, Enum):
    ARRAY = "Array"
    OBJECT = "Object"
    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    FILE = "File"
    MULTI_PART = "MultiPart"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('field') }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ref'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfo:
    information: Optional[list[GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('information'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoice:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    type: GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoiceOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    rel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rel'), 'exclude': lambda f: f is None }})
    validation: Optional[GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation'), 'exclude': lambda f: f is None }})
    
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoiceOptionTypeEnum(str, Enum):
    ARRAY = "Array"
    OBJECT = "Object"
    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    FILE = "File"
    MULTI_PART = "MultiPart"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('field') }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ref'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfo:
    information: Optional[list[GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('information'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoice:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    type: GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoiceOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    options: Optional[list[GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options'), 'exclude': lambda f: f is None }})
    rel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rel'), 'exclude': lambda f: f is None }})
    validation: Optional[GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoicePushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation'), 'exclude': lambda f: f is None }})
    
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoiceOptionTypeEnum(str, Enum):
    ARRAY = "Array"
    OBJECT = "Object"
    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    FILE = "File"
    MULTI_PART = "MultiPart"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('field') }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ref'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushValidationInfo:
    information: Optional[list[GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('information'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoice:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    type: GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoiceOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    options: Optional[list[GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options'), 'exclude': lambda f: f is None }})
    rel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rel'), 'exclude': lambda f: f is None }})
    validation: Optional[GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoicePushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation'), 'exclude': lambda f: f is None }})
    
class GetBankAccountPushOptionsPushOptionPushOptionChoiceOptionTypeEnum(str, Enum):
    ARRAY = "Array"
    OBJECT = "Object"
    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    FILE = "File"
    MULTI_PART = "MultiPart"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('field') }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ref'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushOptionChoicePushValidationInfo:
    information: Optional[list[GetBankAccountPushOptionsPushOptionPushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('information'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetBankAccountPushOptionsPushOptionPushOptionChoicePushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushOptionChoice:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    type: GetBankAccountPushOptionsPushOptionPushOptionChoiceOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    options: Optional[list[GetBankAccountPushOptionsPushOptionPushOptionChoicePushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options'), 'exclude': lambda f: f is None }})
    rel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rel'), 'exclude': lambda f: f is None }})
    validation: Optional[GetBankAccountPushOptionsPushOptionPushOptionChoicePushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation'), 'exclude': lambda f: f is None }})
    
class GetBankAccountPushOptionsPushOptionOptionTypeEnum(str, Enum):
    ARRAY = "Array"
    OBJECT = "Object"
    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    FILE = "File"
    MULTI_PART = "MultiPart"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('field') }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ref'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOptionPushValidationInfo:
    information: Optional[list[GetBankAccountPushOptionsPushOptionPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('information'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetBankAccountPushOptionsPushOptionPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountPushOptionsPushOption:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    type: GetBankAccountPushOptionsPushOptionOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    options: Optional[list[GetBankAccountPushOptionsPushOptionPushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options'), 'exclude': lambda f: f is None }})
    rel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rel'), 'exclude': lambda f: f is None }})
    validation: Optional[GetBankAccountPushOptionsPushOptionPushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetBankAccountPushOptionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    push_option: Optional[GetBankAccountPushOptionsPushOption] = dataclasses.field(default=None)
    