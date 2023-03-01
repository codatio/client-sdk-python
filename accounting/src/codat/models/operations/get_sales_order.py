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
class GetSalesOrderPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    sales_order_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'salesOrderId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSalesOrderSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetSalesOrderRequest:
    path_params: GetSalesOrderPathParams = dataclasses.field()
    security: GetSalesOrderSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateCustomerRef:
    r"""GetSalesOrderSourceModifiedDateCustomerRef
    The customer that the sales order is recorded against in the accounting system.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyName'), 'exclude': lambda f: f is None }})
    
class GetSalesOrderSourceModifiedDateInvoicingStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    PARTIALLY_INVOICED = "PartiallyInvoiced"
    INVOICED = "Invoiced"
    NOT_INVOICED = "NotInvoiced"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateLineItemsAccountRef:
    r"""GetSalesOrderSourceModifiedDateLineItemsAccountRef
    Reference to the account to which the line item is linked.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateLineItemsItemRef:
    r"""GetSalesOrderSourceModifiedDateLineItemsItemRef
    Reference to the product or inventory item to which the line item is linked.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateLineItemsTaxRateRef:
    r"""GetSalesOrderSourceModifiedDateLineItemsTaxRateRef
    Reference to the tax rate to which the line item is linked.
    """
    
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('effectiveTaxRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateLineItemsTracking:
    record_refs: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('recordRefs'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateLineItems:
    account_ref: Optional[GetSalesOrderSourceModifiedDateLineItemsAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    discount_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountAmount'), 'exclude': lambda f: f is None }})
    discount_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountPercentage'), 'exclude': lambda f: f is None }})
    item_ref: Optional[GetSalesOrderSourceModifiedDateLineItemsItemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemRef'), 'exclude': lambda f: f is None }})
    quantity: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('quantity'), 'exclude': lambda f: f is None }})
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal'), 'exclude': lambda f: f is None }})
    tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxAmount'), 'exclude': lambda f: f is None }})
    tax_rate_ref: Optional[GetSalesOrderSourceModifiedDateLineItemsTaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateRef'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    tracking: Optional[GetSalesOrderSourceModifiedDateLineItemsTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tracking'), 'exclude': lambda f: f is None }})
    unit_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unitAmount'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    
class GetSalesOrderSourceModifiedDateShipToAddressTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    BILLING = "Billing"
    DELIVERY = "Delivery"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateShipToAddress:
    r"""GetSalesOrderSourceModifiedDateShipToAddress
    Delivery address for any goods that have been ordered.
    """
    
    type: GetSalesOrderSourceModifiedDateShipToAddressTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('city'), 'exclude': lambda f: f is None }})
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('country'), 'exclude': lambda f: f is None }})
    line1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('line1'), 'exclude': lambda f: f is None }})
    line2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('line2'), 'exclude': lambda f: f is None }})
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('postalCode'), 'exclude': lambda f: f is None }})
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('region'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateShipToContact:
    r"""GetSalesOrderSourceModifiedDateShipToContact
    Details of the named contact at the delivery address.
    """
    
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('email'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('phone'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateShipTo:
    r"""GetSalesOrderSourceModifiedDateShipTo
    Delivery details for any goods that have been ordered.
    """
    
    address: Optional[GetSalesOrderSourceModifiedDateShipToAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('address'), 'exclude': lambda f: f is None }})
    contact: Optional[GetSalesOrderSourceModifiedDateShipToContact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contact'), 'exclude': lambda f: f is None }})
    
class GetSalesOrderSourceModifiedDateStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    DRAFT = "Draft"
    OPEN = "Open"
    CLOSED = "Closed"
    VOID = "Void"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDate:
    r"""GetSalesOrderSourceModifiedDate
    > View the coverage for sales orders in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=salesOrders\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A sales order represents a customer's intention to purchase goods or services from a seller and usually includes information such as the expected delivery date and shipping details. This information can be used to provide visibility on a business's expected receivables and to track sales through the full procurement process.
    
    A sales order is typically converted to an [invoice](https://docs.codat.io/accounting-api#/schemas/Invoice) after approval.
    """
    
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    customer_purchase_order_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerPurchaseOrderNumber'), 'exclude': lambda f: f is None }})
    customer_ref: Optional[GetSalesOrderSourceModifiedDateCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerRef'), 'exclude': lambda f: f is None }})
    expected_delivery_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('expectedDeliveryDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    invoicing_status: Optional[GetSalesOrderSourceModifiedDateInvoicingStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoicingStatus'), 'exclude': lambda f: f is None }})
    issue_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('issueDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    line_items: Optional[list[GetSalesOrderSourceModifiedDateLineItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lineItems'), 'exclude': lambda f: f is None }})
    metadata: Optional[GetSalesOrderSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('note'), 'exclude': lambda f: f is None }})
    sales_order_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('salesOrderNumber'), 'exclude': lambda f: f is None }})
    ship_to: Optional[GetSalesOrderSourceModifiedDateShipTo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('shipTo'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    status: Optional[GetSalesOrderSourceModifiedDateStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    total_discount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalDiscount'), 'exclude': lambda f: f is None }})
    total_tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalTaxAmount'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetSalesOrderResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    source_modified_date: Optional[GetSalesOrderSourceModifiedDate] = dataclasses.field(default=None)
    