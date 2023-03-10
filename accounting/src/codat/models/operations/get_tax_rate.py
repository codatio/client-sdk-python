from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class GetTaxRatePathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    tax_rate_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'taxRateId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetTaxRateSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetTaxRateRequest:
    path_params: GetTaxRatePathParams = dataclasses.field()
    security: GetTaxRateSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetTaxRate200ApplicationJSONComponents:
    is_compound: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isCompound') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rate'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetTaxRate200ApplicationJSONMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    
class GetTaxRate200ApplicationJSONStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetTaxRate200ApplicationJSONValidDataTypeLinks:
    r"""GetTaxRate200ApplicationJSONValidDataTypeLinks
    When querying Codat's data model, some data types return `validDatatypeLinks` metadata in the JSON response. This indicates where that object can be used as a reference???a _valid link_???when creating or updating other data.
    
    For example, `validDatatypeLinks` might indicate the following references:
    
    - Which tax rates are valid to use on the line item of a bill.
    - Which items can be used when creating an invoice. 
    
    You can use `validDatatypeLinks` to present your SMB customers with only valid choices when selecting objects from a list, for example.
    
    ## `validDatatypeLinks` example
    
    The following example uses the `Accounting.Accounts` data type. It shows that, on the linked integration, this account is valid as the account on a payment or bill payment; and as the account referenced on the line item of a direct income or direct cost. Because there is no valid link to Invoices or Bills, using this account on those data types will result in an error.
    
    ```json validDatatypeLinks for an account
    {
                \"id\": \"bd9e85e0-0478-433d-ae9f-0b3c4f04bfe4\",
                \"nominalCode\": \"090\",
                \"name\": \"Business Bank Account\",
                #...
                \"validDatatypeLinks\": [
                    {
                        \"property\": \"Id\",
                        \"links\": [
                            \"Payment.AccountRef.Id\",
                            \"BillPayment.AccountRef.Id\",
                            \"DirectIncome.LineItems.AccountRef.Id\",
                            \"DirectCost.LineItems.AccountRef.Id\"
                        ]
                    }
                ]
            }
    ```
    
    
    
    ## Support for `validDatatypeLinks`
    
    Codat currently supports `validDatatypeLinks` for some data types on our Xero, QuickBooks Online, QuickBooks Desktop, Exact (NL), and Sage Business Cloud integrations. 
    
    If you'd like us to extend support to more data types or integrations, suggest or vote for this on our <a href=\"https://portal.productboard.com/codat/5-product-roadmap\">Product Roadmap</a>.
    """
    
    links: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('links'), 'exclude': lambda f: f is None }})
    property: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('property'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetTaxRate200ApplicationJSON:
    r"""GetTaxRate200ApplicationJSON
    > View the coverage for tax rates in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=taxRates\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    Accounting systems typically store a set of taxes and associated rates within the accounting package. This means that users don't have to look up or remember the rates for each type of tax. For example: Applying the tax \"UK sales VAT\" to line items of an invoice adds the correct rate of 20%. 
    
    ### Tax components
    
    In some cases, a tax is made up of multiple sub taxes, often called _components_ of the tax.  For example: You may have an item that is charged a tax rate called \"City import tax (8%)\" that has two components: 
    
    - A city tax of 5%. 
    - An import tax of 3%.
    
    > **Effective tax rates**  
    > Where there are multiple components of a tax, each component may be calculated on the original amount and added together. Alternatively, one tax may be calculated on the sub-total of the original amount plus another tax, which is referred to as _compounding_. When there is compounding, the effective tax rate is the rate that, if applied to the original amount, would result in the total amount of tax with compounding.  
    >
    > **Example:**  
    > A tax has two components. Both components have a rate of 10%, and one component is compound. In this case, there is a total tax rate of 20% but an effective tax rate of 21%. [Also see _Compound tax example_](#section-compound-tax-example).
    > - For QuickBooks Online, Codat doesn't use compound rates. Instead, the calculated effective tax rate for each component is shown. This means that the effective and total rates are the same because the total tax rate is a sum of the component rates.
    """
    
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code'), 'exclude': lambda f: f is None }})
    components: Optional[list[GetTaxRate200ApplicationJSONComponents]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('components'), 'exclude': lambda f: f is None }})
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('effectiveTaxRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    metadata: Optional[GetTaxRate200ApplicationJSONMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    status: Optional[GetTaxRate200ApplicationJSONStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    total_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalTaxRate'), 'exclude': lambda f: f is None }})
    valid_datatype_links: Optional[list[GetTaxRate200ApplicationJSONValidDataTypeLinks]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validDatatypeLinks'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetTaxRateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_tax_rate_200_application_json_object: Optional[GetTaxRate200ApplicationJSON] = dataclasses.field(default=None)
    