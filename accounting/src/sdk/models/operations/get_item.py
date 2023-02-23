import dataclasses
import dateutil.parser
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetItemPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    item_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'itemId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetItemSecurity:
    api_key: shared_security.SchemeAPIKey = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetItemRequest:
    path_params: GetItemPathParams = dataclasses.field()
    security: GetItemSecurity = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetItemSourceModifiedDateBillItemAccountRef:
    r"""GetItemSourceModifiedDateBillItemAccountRef
    Reference of the account to which the item is linked.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class GetItemSourceModifiedDateBillItemTaxRateRef:
    r"""GetItemSourceModifiedDateBillItemTaxRateRef
    Reference of the tax rate to which the item is linked.
    """
    
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('effectiveTaxRate') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class GetItemSourceModifiedDateBillItem:
    r"""GetItemSourceModifiedDateBillItem
    Item details that are only for bills.
    """
    
    account_ref: Optional[GetItemSourceModifiedDateBillItemAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    tax_rate_ref: Optional[GetItemSourceModifiedDateBillItemTaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateRef') }})
    unit_price: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unitPrice') }})
    

@dataclass_json
@dataclasses.dataclass
class GetItemSourceModifiedDateInvoiceItemAccountRef:
    r"""GetItemSourceModifiedDateInvoiceItemAccountRef
    Reference of the account to which the item is linked.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class GetItemSourceModifiedDateInvoiceItemTaxRateRef:
    r"""GetItemSourceModifiedDateInvoiceItemTaxRateRef
    Reference of the tax rate to which the item is linked.
    """
    
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('effectiveTaxRate') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class GetItemSourceModifiedDateInvoiceItem:
    r"""GetItemSourceModifiedDateInvoiceItem
    Item details that are only for bills.
    """
    
    account_ref: Optional[GetItemSourceModifiedDateInvoiceItemAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    tax_rate_ref: Optional[GetItemSourceModifiedDateInvoiceItemTaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateRef') }})
    unit_price: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unitPrice') }})
    
class GetItemSourceModifiedDateItemStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"


@dataclass_json
@dataclasses.dataclass
class GetItemSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted') }})
    
class GetItemSourceModifiedDateTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    INVENTORY = "Inventory"
    NON_INVENTORY = "NonInventory"
    SERVICE = "Service"


@dataclass_json
@dataclasses.dataclass
class GetItemSourceModifiedDate:
    r"""GetItemSourceModifiedDate
    > View the coverage for items in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    **Items** allow your customers to save and track details of the products and services that they buy and sell.
    
    """
    
    is_bill_item: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isBillItem') }})
    is_invoice_item: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isInvoiceItem') }})
    item_status: GetItemSourceModifiedDateItemStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemStatus') }})
    type: GetItemSourceModifiedDateTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    bill_item: Optional[GetItemSourceModifiedDateBillItem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('billItem') }})
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    invoice_item: Optional[GetItemSourceModifiedDateInvoiceItem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceItem') }})
    metadata: Optional[GetItemSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata') }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    

@dataclasses.dataclass
class GetItemResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    source_modified_date: Optional[GetItemSourceModifiedDate] = dataclasses.field(default=None)
    