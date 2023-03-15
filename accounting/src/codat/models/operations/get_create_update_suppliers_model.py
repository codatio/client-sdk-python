from __future__ import annotations
import dataclasses
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class GetCreateUpdateSuppliersModelRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionChoiceOptionTypeEnum(str, Enum):
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
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionChoice:
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    type: Optional[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionChoiceOptionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionChoiceOptionTypeEnum(str, Enum):
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
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionChoice:
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    type: Optional[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionChoiceOptionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoiceOptionTypeEnum(str, Enum):
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
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoice:
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    type: Optional[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoiceOptionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoiceOptionTypeEnum(str, Enum):
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
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoice:
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    type: Optional[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoiceOptionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyOptionTypeEnum(str, Enum):
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
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ref'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfo:
    information: Optional[list[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('information'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionProperty:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    type: GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    options: Optional[list[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    validation: Optional[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyOptionTypeEnum(str, Enum):
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
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ref'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfo:
    information: Optional[list[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('information'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionProperty:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    type: GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    options: Optional[list[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    properties: Optional[dict[str, GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushOptionProperty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties'), 'exclude': lambda f: f is None }})
    validation: Optional[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionPropertyPushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyOptionTypeEnum(str, Enum):
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
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ref'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushValidationInfo:
    information: Optional[list[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('information'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionProperty:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    type: GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    options: Optional[list[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    properties: Optional[dict[str, GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushOptionProperty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties'), 'exclude': lambda f: f is None }})
    validation: Optional[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionPropertyPushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyOptionTypeEnum(str, Enum):
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
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushValidationInfoPushFieldValidation:
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ref'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushValidationInfo:
    information: Optional[list[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('information'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushValidationInfoPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreateUpdateSuppliersModelPushOptionPushOptionProperty:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    type: GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    options: Optional[list[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    properties: Optional[dict[str, GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushOptionProperty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties'), 'exclude': lambda f: f is None }})
    validation: Optional[GetCreateUpdateSuppliersModelPushOptionPushOptionPropertyPushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    
class GetCreateUpdateSuppliersModelPushOptionOptionTypeEnum(str, Enum):
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
class GetCreateUpdateSuppliersModelPushOption:
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    type: GetCreateUpdateSuppliersModelPushOptionOptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    properties: Optional[dict[str, GetCreateUpdateSuppliersModelPushOptionPushOptionProperty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetCreateUpdateSuppliersModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    push_option: Optional[GetCreateUpdateSuppliersModelPushOption] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    