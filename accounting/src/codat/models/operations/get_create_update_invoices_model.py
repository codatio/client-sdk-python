from __future__ import annotations
import dataclasses
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class GetCreateUpdateInvoicesModelRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionChoiceOptionTypeEnum(str, Enum):
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
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionChoice:
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    type: Optional[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionChoiceOptionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionChoiceOptionTypeEnum(str, Enum):
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
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionChoice:
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    type: Optional[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionChoiceOptionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoiceOptionTypeEnum(str, Enum):
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
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoice:
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    type: Optional[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoiceOptionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoiceOptionTypeEnum(str, Enum):
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
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoice:
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    type: Optional[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoiceOptionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyOptionTypeEnum(str, Enum):
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
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ref'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfo:
    information: Optional[list[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('information'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionProperty:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    type: GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    options: Optional[list[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    validation: Optional[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyOptionTypeEnum(str, Enum):
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
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ref'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfo:
    information: Optional[list[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('information'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionProperty:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    type: GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    options: Optional[list[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    properties: Optional[dict[str, GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionProperty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties'), 'exclude': lambda f: f is None }})
    validation: Optional[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyOptionTypeEnum(str, Enum):
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
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ref'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushValidationInfo:
    information: Optional[list[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('information'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionProperty:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    type: GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    options: Optional[list[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    properties: Optional[dict[str, GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionProperty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties'), 'exclude': lambda f: f is None }})
    validation: Optional[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionPropertyPushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyOptionTypeEnum(str, Enum):
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
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ref'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushValidationInfo:
    information: Optional[list[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('information'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateInvoicesModelPushOptionPushOptionProperty:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    type: GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    options: Optional[list[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    properties: Optional[dict[str, GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushOptionProperty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties'), 'exclude': lambda f: f is None }})
    validation: Optional[GetCreateUpdateInvoicesModelPushOptionPushOptionPropertyPushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateInvoicesModelPushOptionOptionTypeEnum(str, Enum):
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
class GetCreateUpdateInvoicesModelPushOption:
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    type: GetCreateUpdateInvoicesModelPushOptionOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    properties: Optional[dict[str, GetCreateUpdateInvoicesModelPushOptionPushOptionProperty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetCreateUpdateInvoicesModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    push_option: Optional[GetCreateUpdateInvoicesModelPushOption] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    