from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Any, Optional


@dataclasses.dataclass
class GetSupplierPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    supplier_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'supplierId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSupplierSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetSupplierRequest:
    path_params: GetSupplierPathParams = dataclasses.field()
    security: GetSupplierSecurity = dataclasses.field()
    
class GetSupplierSourceModifiedDateAddressesTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    BILLING = "Billing"
    DELIVERY = "Delivery"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSupplierSourceModifiedDateAddresses:
    type: GetSupplierSourceModifiedDateAddressesTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('city'), 'exclude': lambda f: f is None }})
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('country'), 'exclude': lambda f: f is None }})
    line1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('line1'), 'exclude': lambda f: f is None }})
    line2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('line2'), 'exclude': lambda f: f is None }})
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('postalCode'), 'exclude': lambda f: f is None }})
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('region'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSupplierSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    
class GetSupplierSourceModifiedDateStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSupplierSourceModifiedDateSupplementalData:
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('content'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSupplierSourceModifiedDate:
    r"""GetSupplierSourceModifiedDate
    > View the coverage for suppliers in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    From the **Suppliers** endpoints, you can retrieve a list of [all the suppliers for a company](https://api.codat.io/swagger/index.html#/Suppliers/get_companies__companyId__data_suppliers). Suppliers' data links to accounts payable [bills](https://docs.codat.io/accounting-api#/schemas/Bill).
    """
    
    status: GetSupplierSourceModifiedDateStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    addresses: Optional[list[GetSupplierSourceModifiedDateAddresses]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('addresses'), 'exclude': lambda f: f is None }})
    contact_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contactName'), 'exclude': lambda f: f is None }})
    default_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('defaultCurrency'), 'exclude': lambda f: f is None }})
    email_address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('emailAddress'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    metadata: Optional[GetSupplierSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('phone'), 'exclude': lambda f: f is None }})
    registration_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('registrationNumber'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    supplemental_data: Optional[GetSupplierSourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplementalData'), 'exclude': lambda f: f is None }})
    supplier_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierName'), 'exclude': lambda f: f is None }})
    tax_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxNumber'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetSupplierResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    source_modified_date: Optional[GetSupplierSourceModifiedDate] = dataclasses.field(default=None)
    