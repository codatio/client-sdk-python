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
class GetPurchaseOrderPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    purchase_order_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'purchaseOrderId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetPurchaseOrderSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetPurchaseOrderRequest:
    path_params: GetPurchaseOrderPathParams = dataclasses.field()
    security: GetPurchaseOrderSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPurchaseOrderSourceModifiedDateLineItemsAccountRef:
    r"""GetPurchaseOrderSourceModifiedDateLineItemsAccountRef
    Reference to the account to which the line item is linked.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPurchaseOrderSourceModifiedDateLineItemsItemRef:
    r"""GetPurchaseOrderSourceModifiedDateLineItemsItemRef
    Reference to the product or inventory item to which the line item is linked.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPurchaseOrderSourceModifiedDateLineItemsTaxRateRef:
    r"""GetPurchaseOrderSourceModifiedDateLineItemsTaxRateRef
    Reference to the tax rate to which the line item is linked.
    """
    
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('effectiveTaxRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPurchaseOrderSourceModifiedDateLineItemsTrackingCategoryRefs:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPurchaseOrderSourceModifiedDateLineItems:
    account_ref: Optional[GetPurchaseOrderSourceModifiedDateLineItemsAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    discount_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountAmount'), 'exclude': lambda f: f is None }})
    discount_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountPercentage'), 'exclude': lambda f: f is None }})
    item_ref: Optional[GetPurchaseOrderSourceModifiedDateLineItemsItemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemRef'), 'exclude': lambda f: f is None }})
    quantity: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('quantity'), 'exclude': lambda f: f is None }})
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal'), 'exclude': lambda f: f is None }})
    tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxAmount'), 'exclude': lambda f: f is None }})
    tax_rate_ref: Optional[GetPurchaseOrderSourceModifiedDateLineItemsTaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateRef'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    tracking_category_refs: Optional[list[GetPurchaseOrderSourceModifiedDateLineItemsTrackingCategoryRefs]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('trackingCategoryRefs'), 'exclude': lambda f: f is None }})
    unit_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unitAmount'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPurchaseOrderSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    
class GetPurchaseOrderSourceModifiedDateShipToAddressTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    BILLING = "Billing"
    DELIVERY = "Delivery"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPurchaseOrderSourceModifiedDateShipToAddress:
    r"""GetPurchaseOrderSourceModifiedDateShipToAddress
    Delivery address for any goods that have been ordered.
    """
    
    type: GetPurchaseOrderSourceModifiedDateShipToAddressTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('city'), 'exclude': lambda f: f is None }})
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('country'), 'exclude': lambda f: f is None }})
    line1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('line1'), 'exclude': lambda f: f is None }})
    line2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('line2'), 'exclude': lambda f: f is None }})
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('postalCode'), 'exclude': lambda f: f is None }})
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('region'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPurchaseOrderSourceModifiedDateShipToContact:
    r"""GetPurchaseOrderSourceModifiedDateShipToContact
    Details of the named contact at the delivery address.
    """
    
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('email'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('phone'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPurchaseOrderSourceModifiedDateShipTo:
    r"""GetPurchaseOrderSourceModifiedDateShipTo
    Delivery details for any goods that have been ordered.
    """
    
    address: Optional[GetPurchaseOrderSourceModifiedDateShipToAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('address'), 'exclude': lambda f: f is None }})
    contact: Optional[GetPurchaseOrderSourceModifiedDateShipToContact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contact'), 'exclude': lambda f: f is None }})
    
class GetPurchaseOrderSourceModifiedDateStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    DRAFT = "Draft"
    OPEN = "Open"
    CLOSED = "Closed"
    VOID = "Void"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPurchaseOrderSourceModifiedDateSupplierRef:
    r"""GetPurchaseOrderSourceModifiedDateSupplierRef
    Supplier that the purchase order is recorded against in the accounting system.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    supplier_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPurchaseOrderSourceModifiedDate:
    r"""GetPurchaseOrderSourceModifiedDate
    > View the coverage for purchase orders in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    Purchase orders represent a business's intent to purchase goods or services from a supplier and normally include information such as expected delivery dates and shipping details.  
    
    This information can be used to provide visibility on a business's expected payables and to track a purchase through the full procurement process.
    """
    
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    delivery_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deliveryDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    expected_delivery_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('expectedDeliveryDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    issue_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('issueDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    line_items: Optional[list[GetPurchaseOrderSourceModifiedDateLineItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lineItems'), 'exclude': lambda f: f is None }})
    metadata: Optional[GetPurchaseOrderSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('note'), 'exclude': lambda f: f is None }})
    payment_due_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('paymentDueDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    purchase_order_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('purchaseOrderNumber'), 'exclude': lambda f: f is None }})
    ship_to: Optional[GetPurchaseOrderSourceModifiedDateShipTo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('shipTo'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    status: Optional[GetPurchaseOrderSourceModifiedDateStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal'), 'exclude': lambda f: f is None }})
    supplier_ref: Optional[GetPurchaseOrderSourceModifiedDateSupplierRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierRef'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    total_discount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalDiscount'), 'exclude': lambda f: f is None }})
    total_tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalTaxAmount'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetPurchaseOrderResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    source_modified_date: Optional[GetPurchaseOrderSourceModifiedDate] = dataclasses.field(default=None)
    