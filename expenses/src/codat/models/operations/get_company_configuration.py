from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class GetCompanyConfigurationPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetCompanyConfigurationRequest:
    path_params: GetCompanyConfigurationPathParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompanyConfiguration200ApplicationJSONBankAccount:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompanyConfiguration200ApplicationJSONCustomer:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompanyConfiguration200ApplicationJSONSupplier:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompanyConfiguration200ApplicationJSON:
    bank_account: Optional[GetCompanyConfiguration200ApplicationJSONBankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bankAccount'), 'exclude': lambda f: f is None }})
    customer: Optional[GetCompanyConfiguration200ApplicationJSONCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customer'), 'exclude': lambda f: f is None }})
    supplier: Optional[GetCompanyConfiguration200ApplicationJSONSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplier'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetCompanyConfigurationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_company_configuration_200_application_json_object: Optional[GetCompanyConfiguration200ApplicationJSON] = dataclasses.field(default=None)
    