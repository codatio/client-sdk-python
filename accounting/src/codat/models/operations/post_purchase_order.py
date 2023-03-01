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
class PostPurchaseOrderPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PostPurchaseOrderQueryParams:
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrderSourceModifiedDateLineItemsAccountRef:
    r"""PostPurchaseOrderSourceModifiedDateLineItemsAccountRef
    Reference to the account to which the line item is linked.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrderSourceModifiedDateLineItemsItemRef:
    r"""PostPurchaseOrderSourceModifiedDateLineItemsItemRef
    Reference to the product or inventory item to which the line item is linked.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrderSourceModifiedDateLineItemsTaxRateRef:
    r"""PostPurchaseOrderSourceModifiedDateLineItemsTaxRateRef
    Reference to the tax rate to which the line item is linked.
    """
    
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('effectiveTaxRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrderSourceModifiedDateLineItemsTrackingCategoryRefs:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrderSourceModifiedDateLineItems:
    account_ref: Optional[PostPurchaseOrderSourceModifiedDateLineItemsAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    discount_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountAmount'), 'exclude': lambda f: f is None }})
    discount_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountPercentage'), 'exclude': lambda f: f is None }})
    item_ref: Optional[PostPurchaseOrderSourceModifiedDateLineItemsItemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemRef'), 'exclude': lambda f: f is None }})
    quantity: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('quantity'), 'exclude': lambda f: f is None }})
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal'), 'exclude': lambda f: f is None }})
    tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxAmount'), 'exclude': lambda f: f is None }})
    tax_rate_ref: Optional[PostPurchaseOrderSourceModifiedDateLineItemsTaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateRef'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    tracking_category_refs: Optional[list[PostPurchaseOrderSourceModifiedDateLineItemsTrackingCategoryRefs]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('trackingCategoryRefs'), 'exclude': lambda f: f is None }})
    unit_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unitAmount'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrderSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    
class PostPurchaseOrderSourceModifiedDateShipToAddressTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    BILLING = "Billing"
    DELIVERY = "Delivery"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrderSourceModifiedDateShipToAddress:
    r"""PostPurchaseOrderSourceModifiedDateShipToAddress
    Delivery address for any goods that have been ordered.
    """
    
    type: PostPurchaseOrderSourceModifiedDateShipToAddressTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('city'), 'exclude': lambda f: f is None }})
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('country'), 'exclude': lambda f: f is None }})
    line1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('line1'), 'exclude': lambda f: f is None }})
    line2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('line2'), 'exclude': lambda f: f is None }})
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('postalCode'), 'exclude': lambda f: f is None }})
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('region'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrderSourceModifiedDateShipToContact:
    r"""PostPurchaseOrderSourceModifiedDateShipToContact
    Details of the named contact at the delivery address.
    """
    
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('email'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('phone'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrderSourceModifiedDateShipTo:
    r"""PostPurchaseOrderSourceModifiedDateShipTo
    Delivery details for any goods that have been ordered.
    """
    
    address: Optional[PostPurchaseOrderSourceModifiedDateShipToAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('address'), 'exclude': lambda f: f is None }})
    contact: Optional[PostPurchaseOrderSourceModifiedDateShipToContact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contact'), 'exclude': lambda f: f is None }})
    
class PostPurchaseOrderSourceModifiedDateStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    DRAFT = "Draft"
    OPEN = "Open"
    CLOSED = "Closed"
    VOID = "Void"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrderSourceModifiedDateSupplierRef:
    r"""PostPurchaseOrderSourceModifiedDateSupplierRef
    Supplier that the purchase order is recorded against in the accounting system.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    supplier_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrderSourceModifiedDate:
    r"""PostPurchaseOrderSourceModifiedDate
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
    line_items: Optional[list[PostPurchaseOrderSourceModifiedDateLineItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lineItems'), 'exclude': lambda f: f is None }})
    metadata: Optional[PostPurchaseOrderSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('note'), 'exclude': lambda f: f is None }})
    payment_due_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('paymentDueDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    purchase_order_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('purchaseOrderNumber'), 'exclude': lambda f: f is None }})
    ship_to: Optional[PostPurchaseOrderSourceModifiedDateShipTo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('shipTo'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    status: Optional[PostPurchaseOrderSourceModifiedDateStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal'), 'exclude': lambda f: f is None }})
    supplier_ref: Optional[PostPurchaseOrderSourceModifiedDateSupplierRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierRef'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    total_discount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalDiscount'), 'exclude': lambda f: f is None }})
    total_tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalTaxAmount'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostPurchaseOrderSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class PostPurchaseOrderRequest:
    path_params: PostPurchaseOrderPathParams = dataclasses.field()
    query_params: PostPurchaseOrderQueryParams = dataclasses.field()
    security: PostPurchaseOrderSecurity = dataclasses.field()
    request: Optional[PostPurchaseOrderSourceModifiedDate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONChangesPushOperationRecordRef:
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    
class PostPurchaseOrder200ApplicationJSONChangesTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    CREATED = "Created"
    MODIFIED = "Modified"
    DELETED = "Deleted"
    ATTACHMENT_UPLOADED = "AttachmentUploaded"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONChanges:
    attachment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attachmentId'), 'exclude': lambda f: f is None }})
    record_ref: Optional[PostPurchaseOrder200ApplicationJSONChangesPushOperationRecordRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('recordRef'), 'exclude': lambda f: f is None }})
    type: Optional[PostPurchaseOrder200ApplicationJSONChangesTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONSourceModifiedDateLineItemsAccountRef:
    r"""PostPurchaseOrder200ApplicationJSONSourceModifiedDateLineItemsAccountRef
    Reference to the account to which the line item is linked.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONSourceModifiedDateLineItemsItemRef:
    r"""PostPurchaseOrder200ApplicationJSONSourceModifiedDateLineItemsItemRef
    Reference to the product or inventory item to which the line item is linked.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONSourceModifiedDateLineItemsTaxRateRef:
    r"""PostPurchaseOrder200ApplicationJSONSourceModifiedDateLineItemsTaxRateRef
    Reference to the tax rate to which the line item is linked.
    """
    
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('effectiveTaxRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONSourceModifiedDateLineItemsTrackingCategoryRefs:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONSourceModifiedDateLineItems:
    account_ref: Optional[PostPurchaseOrder200ApplicationJSONSourceModifiedDateLineItemsAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    discount_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountAmount'), 'exclude': lambda f: f is None }})
    discount_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountPercentage'), 'exclude': lambda f: f is None }})
    item_ref: Optional[PostPurchaseOrder200ApplicationJSONSourceModifiedDateLineItemsItemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemRef'), 'exclude': lambda f: f is None }})
    quantity: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('quantity'), 'exclude': lambda f: f is None }})
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal'), 'exclude': lambda f: f is None }})
    tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxAmount'), 'exclude': lambda f: f is None }})
    tax_rate_ref: Optional[PostPurchaseOrder200ApplicationJSONSourceModifiedDateLineItemsTaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateRef'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    tracking_category_refs: Optional[list[PostPurchaseOrder200ApplicationJSONSourceModifiedDateLineItemsTrackingCategoryRefs]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('trackingCategoryRefs'), 'exclude': lambda f: f is None }})
    unit_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unitAmount'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    
class PostPurchaseOrder200ApplicationJSONSourceModifiedDateShipToAddressTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    BILLING = "Billing"
    DELIVERY = "Delivery"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONSourceModifiedDateShipToAddress:
    r"""PostPurchaseOrder200ApplicationJSONSourceModifiedDateShipToAddress
    Delivery address for any goods that have been ordered.
    """
    
    type: PostPurchaseOrder200ApplicationJSONSourceModifiedDateShipToAddressTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('city'), 'exclude': lambda f: f is None }})
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('country'), 'exclude': lambda f: f is None }})
    line1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('line1'), 'exclude': lambda f: f is None }})
    line2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('line2'), 'exclude': lambda f: f is None }})
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('postalCode'), 'exclude': lambda f: f is None }})
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('region'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONSourceModifiedDateShipToContact:
    r"""PostPurchaseOrder200ApplicationJSONSourceModifiedDateShipToContact
    Details of the named contact at the delivery address.
    """
    
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('email'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('phone'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONSourceModifiedDateShipTo:
    r"""PostPurchaseOrder200ApplicationJSONSourceModifiedDateShipTo
    Delivery details for any goods that have been ordered.
    """
    
    address: Optional[PostPurchaseOrder200ApplicationJSONSourceModifiedDateShipToAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('address'), 'exclude': lambda f: f is None }})
    contact: Optional[PostPurchaseOrder200ApplicationJSONSourceModifiedDateShipToContact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contact'), 'exclude': lambda f: f is None }})
    
class PostPurchaseOrder200ApplicationJSONSourceModifiedDateStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    DRAFT = "Draft"
    OPEN = "Open"
    CLOSED = "Closed"
    VOID = "Void"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONSourceModifiedDateSupplierRef:
    r"""PostPurchaseOrder200ApplicationJSONSourceModifiedDateSupplierRef
    Supplier that the purchase order is recorded against in the accounting system.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    supplier_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONSourceModifiedDate:
    r"""PostPurchaseOrder200ApplicationJSONSourceModifiedDate
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
    line_items: Optional[list[PostPurchaseOrder200ApplicationJSONSourceModifiedDateLineItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lineItems'), 'exclude': lambda f: f is None }})
    metadata: Optional[PostPurchaseOrder200ApplicationJSONSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('note'), 'exclude': lambda f: f is None }})
    payment_due_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('paymentDueDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    purchase_order_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('purchaseOrderNumber'), 'exclude': lambda f: f is None }})
    ship_to: Optional[PostPurchaseOrder200ApplicationJSONSourceModifiedDateShipTo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('shipTo'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    status: Optional[PostPurchaseOrder200ApplicationJSONSourceModifiedDateStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal'), 'exclude': lambda f: f is None }})
    supplier_ref: Optional[PostPurchaseOrder200ApplicationJSONSourceModifiedDateSupplierRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierRef'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    total_discount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalDiscount'), 'exclude': lambda f: f is None }})
    total_tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalTaxAmount'), 'exclude': lambda f: f is None }})
    
class PostPurchaseOrder200ApplicationJSONStatusEnum(str, Enum):
    PENDING = "Pending"
    FAILED = "Failed"
    SUCCESS = "Success"
    TIMED_OUT = "TimedOut"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONValidationValidationItem:
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemId'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message'), 'exclude': lambda f: f is None }})
    validator_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validatorName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSONValidation:
    r"""PostPurchaseOrder200ApplicationJSONValidation
    A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here.
    """
    
    errors: Optional[list[PostPurchaseOrder200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[PostPurchaseOrder200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPurchaseOrder200ApplicationJSON:
    company_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId') }})
    data_connection_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataConnectionKey') }})
    push_operation_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pushOperationKey') }})
    requested_on_utc: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('requestedOnUtc'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: PostPurchaseOrder200ApplicationJSONStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    status_code: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode') }})
    changes: Optional[list[PostPurchaseOrder200ApplicationJSONChanges]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('changes'), 'exclude': lambda f: f is None }})
    completed_on_utc: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('completedOnUtc'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    data: Optional[PostPurchaseOrder200ApplicationJSONSourceModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType'), 'exclude': lambda f: f is None }})
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errorMessage'), 'exclude': lambda f: f is None }})
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeoutInMinutes'), 'exclude': lambda f: f is None }})
    timeout_in_seconds: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeoutInSeconds'), 'exclude': lambda f: f is None }})
    validation: Optional[PostPurchaseOrder200ApplicationJSONValidation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostPurchaseOrderResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    post_purchase_order_200_application_json_object: Optional[PostPurchaseOrder200ApplicationJSON] = dataclasses.field(default=None)
    