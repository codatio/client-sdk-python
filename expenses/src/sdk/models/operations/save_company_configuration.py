import dataclasses
from dataclasses_json import dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class SaveCompanyConfigurationPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationApplicationWildcardPlusJSONBankAccount:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationApplicationWildcardPlusJSONCustomer:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationApplicationWildcardPlusJSONSupplier:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationApplicationWildcardPlusJSON:
    bank_account: Optional[SaveCompanyConfigurationApplicationWildcardPlusJSONBankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bankAccount') }})
    customer: Optional[SaveCompanyConfigurationApplicationWildcardPlusJSONCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customer') }})
    supplier: Optional[SaveCompanyConfigurationApplicationWildcardPlusJSONSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplier') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationApplicationJSONBankAccount:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationApplicationJSONCustomer:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationApplicationJSONSupplier:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationApplicationJSON:
    bank_account: Optional[SaveCompanyConfigurationApplicationJSONBankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bankAccount') }})
    customer: Optional[SaveCompanyConfigurationApplicationJSONCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customer') }})
    supplier: Optional[SaveCompanyConfigurationApplicationJSONSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplier') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationApplicationJSONPatchPlusJSONBankAccount:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationApplicationJSONPatchPlusJSONCustomer:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationApplicationJSONPatchPlusJSONSupplier:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationApplicationJSONPatchPlusJSON:
    bank_account: Optional[SaveCompanyConfigurationApplicationJSONPatchPlusJSONBankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bankAccount') }})
    customer: Optional[SaveCompanyConfigurationApplicationJSONPatchPlusJSONCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customer') }})
    supplier: Optional[SaveCompanyConfigurationApplicationJSONPatchPlusJSONSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplier') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationTextJSONBankAccount:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationTextJSONCustomer:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationTextJSONSupplier:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfigurationTextJSON:
    bank_account: Optional[SaveCompanyConfigurationTextJSONBankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bankAccount') }})
    customer: Optional[SaveCompanyConfigurationTextJSONCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customer') }})
    supplier: Optional[SaveCompanyConfigurationTextJSONSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplier') }})
    

@dataclasses.dataclass
class SaveCompanyConfigurationRequests:
    object: Optional[SaveCompanyConfigurationApplicationWildcardPlusJSON] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/*+json' }})
    object1: Optional[SaveCompanyConfigurationApplicationJSON] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    object2: Optional[SaveCompanyConfigurationApplicationJSONPatchPlusJSON] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json-patch+json' }})
    object3: Optional[SaveCompanyConfigurationTextJSON] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'text/json' }})
    

@dataclasses.dataclass
class SaveCompanyConfigurationRequest:
    path_params: SaveCompanyConfigurationPathParams = dataclasses.field()
    request: Optional[SaveCompanyConfigurationRequests] = dataclasses.field(default=None)
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfiguration400ApplicationJSONValidationErrors:
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemId') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    rule_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ruleId') }})
    validator_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validatorName') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfiguration400ApplicationJSONValidationInternals:
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemId') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    rule_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ruleId') }})
    validator_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validatorName') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfiguration400ApplicationJSONValidationWarnings:
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemId') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    rule_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ruleId') }})
    validator_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validatorName') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfiguration400ApplicationJSONValidation:
    errors: Optional[list[SaveCompanyConfiguration400ApplicationJSONValidationErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors') }})
    has_errors: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hasErrors') }})
    has_internals: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hasInternals') }})
    has_warnings: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hasWarnings') }})
    internals: Optional[list[SaveCompanyConfiguration400ApplicationJSONValidationInternals]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('internals') }})
    warnings: Optional[list[SaveCompanyConfiguration400ApplicationJSONValidationWarnings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfiguration400ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('canBeRetried') }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('correlationId') }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailedErrorCode') }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error') }})
    inner: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('inner') }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('service') }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode') }})
    validation: Optional[SaveCompanyConfiguration400ApplicationJSONValidation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfiguration200TextJSONBankAccount:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfiguration200TextJSONCustomer:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfiguration200TextJSONSupplier:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfiguration200TextJSON:
    bank_account: Optional[SaveCompanyConfiguration200TextJSONBankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bankAccount') }})
    customer: Optional[SaveCompanyConfiguration200TextJSONCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customer') }})
    supplier: Optional[SaveCompanyConfiguration200TextJSONSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplier') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfiguration200ApplicationJSONBankAccount:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfiguration200ApplicationJSONCustomer:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfiguration200ApplicationJSONSupplier:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class SaveCompanyConfiguration200ApplicationJSON:
    bank_account: Optional[SaveCompanyConfiguration200ApplicationJSONBankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bankAccount') }})
    customer: Optional[SaveCompanyConfiguration200ApplicationJSONCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customer') }})
    supplier: Optional[SaveCompanyConfiguration200ApplicationJSONSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplier') }})
    

@dataclasses.dataclass
class SaveCompanyConfigurationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    save_company_configuration_200_application_json_object: Optional[SaveCompanyConfiguration200ApplicationJSON] = dataclasses.field(default=None)
    save_company_configuration_200_text_json_object: Optional[SaveCompanyConfiguration200TextJSON] = dataclasses.field(default=None)
    save_company_configuration_200_text_plain_object: Optional[str] = dataclasses.field(default=None)
    save_company_configuration_400_application_json_object: Optional[SaveCompanyConfiguration400ApplicationJSON] = dataclasses.field(default=None)
    