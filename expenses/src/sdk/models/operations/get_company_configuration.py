import dataclasses
from dataclasses_json import dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetCompanyConfigurationPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetCompanyConfigurationRequest:
    path_params: GetCompanyConfigurationPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetCompanyConfiguration200TextJSONBankAccount:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompanyConfiguration200TextJSONCustomer:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompanyConfiguration200TextJSONSupplier:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompanyConfiguration200TextJSON:
    bank_account: Optional[GetCompanyConfiguration200TextJSONBankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bankAccount') }})
    customer: Optional[GetCompanyConfiguration200TextJSONCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customer') }})
    supplier: Optional[GetCompanyConfiguration200TextJSONSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplier') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompanyConfiguration200ApplicationJSONBankAccount:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompanyConfiguration200ApplicationJSONCustomer:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompanyConfiguration200ApplicationJSONSupplier:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class GetCompanyConfiguration200ApplicationJSON:
    bank_account: Optional[GetCompanyConfiguration200ApplicationJSONBankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bankAccount') }})
    customer: Optional[GetCompanyConfiguration200ApplicationJSONCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customer') }})
    supplier: Optional[GetCompanyConfiguration200ApplicationJSONSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplier') }})
    

@dataclasses.dataclass
class GetCompanyConfigurationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_company_configuration_200_application_json_object: Optional[GetCompanyConfiguration200ApplicationJSON] = dataclasses.field(default=None)
    get_company_configuration_200_text_json_object: Optional[GetCompanyConfiguration200TextJSON] = dataclasses.field(default=None)
    get_company_configuration_200_text_plain_object: Optional[str] = dataclasses.field(default=None)
    