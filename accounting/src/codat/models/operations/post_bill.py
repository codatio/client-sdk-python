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
class PostBillPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PostBillQueryParams:
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDateLineItemsAccountRef:
    r"""PostBillSourceModifiedDateLineItemsAccountRef
    Reference to the account to which the line item is linked.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDateLineItemsItemRef:
    r"""PostBillSourceModifiedDateLineItemsItemRef
    Reference to the product, service type, or inventory item to which the line item is linked.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDateLineItemsTaxRateRef:
    r"""PostBillSourceModifiedDateLineItemsTaxRateRef
    Reference to the tax rate to which the line item is linked.
    """
    
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('effectiveTaxRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDateLineItemsTrackingCategoryRefs:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDateLineItemsTrackingCustomerRef:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyName'), 'exclude': lambda f: f is None }})
    
class PostBillSourceModifiedDateLineItemsTrackingIsBilledToEnum(str, Enum):
    UNKNOWN = "Unknown"
    NOT_APPLICABLE = "NotApplicable"
    CUSTOMER = "Customer"
    PROJECT = "Project"

class PostBillSourceModifiedDateLineItemsTrackingIsRebilledToEnum(str, Enum):
    UNKNOWN = "Unknown"
    NOT_APPLICABLE = "NotApplicable"
    CUSTOMER = "Customer"
    PROJECT = "Project"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDateLineItemsTrackingProjectRef:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDateLineItemsTracking:
    category_refs: list[PostBillSourceModifiedDateLineItemsTrackingCategoryRefs] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('categoryRefs') }})
    is_billed_to: PostBillSourceModifiedDateLineItemsTrackingIsBilledToEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isBilledTo') }})
    is_rebilled_to: PostBillSourceModifiedDateLineItemsTrackingIsRebilledToEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isRebilledTo') }})
    customer_ref: Optional[PostBillSourceModifiedDateLineItemsTrackingCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerRef'), 'exclude': lambda f: f is None }})
    project_ref: Optional[PostBillSourceModifiedDateLineItemsTrackingProjectRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('projectRef'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDateLineItems:
    quantity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('quantity') }})
    unit_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('unitAmount') }})
    account_ref: Optional[PostBillSourceModifiedDateLineItemsAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    discount_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountAmount'), 'exclude': lambda f: f is None }})
    discount_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountPercentage'), 'exclude': lambda f: f is None }})
    is_direct_cost: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDirectCost'), 'exclude': lambda f: f is None }})
    item_ref: Optional[PostBillSourceModifiedDateLineItemsItemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemRef'), 'exclude': lambda f: f is None }})
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal'), 'exclude': lambda f: f is None }})
    tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxAmount'), 'exclude': lambda f: f is None }})
    tax_rate_ref: Optional[PostBillSourceModifiedDateLineItemsTaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateRef'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    tracking: Optional[PostBillSourceModifiedDateLineItemsTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tracking'), 'exclude': lambda f: f is None }})
    tracking_category_refs: Optional[list[PostBillSourceModifiedDateLineItemsTrackingCategoryRefs]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('trackingCategoryRefs'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDatePaymentAllocationsAllocation:
    allocated_on_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('allocatedOnDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDatePaymentAllocationsPaymentAccountRef:
    r"""PostBillSourceModifiedDatePaymentAllocationsPaymentAccountRef
    The account that the allocated payment is made from or to.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDatePaymentAllocationsPayment:
    account_ref: Optional[PostBillSourceModifiedDatePaymentAllocationsPaymentAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('note'), 'exclude': lambda f: f is None }})
    paid_on_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('paidOnDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reference'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDatePaymentAllocations:
    allocation: PostBillSourceModifiedDatePaymentAllocationsAllocation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('allocation') }})
    payment: PostBillSourceModifiedDatePaymentAllocationsPayment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('payment') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDatePurchaseOrderRefs:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    purchase_order_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('purchaseOrderNumber'), 'exclude': lambda f: f is None }})
    
class PostBillSourceModifiedDateStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    OPEN = "Open"
    PARTIALLY_PAID = "PartiallyPaid"
    PAID = "Paid"
    VOID = "Void"
    DRAFT = "Draft"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDateSupplementalData:
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('content'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDateSupplierRef:
    r"""PostBillSourceModifiedDateSupplierRef
    Reference to the supplier the bill was received from.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    supplier_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDateWithholdingTax:
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBillSourceModifiedDate:
    r"""PostBillSourceModifiedDate
    > **Invoices or bills?**
    >
    > In Codat, bills are for accounts payable only. For the accounts receivable equivalent of bills, see [Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice).
    
    View the coverage for bills in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    In Codat, a bill contains details of:
    * When the bill was recorded in the accounting system.
    * How much the bill is for and the currency of the amount.
    * Who the bill was received from — the *supplier*.
    * What the bill is for — the *line items*.
    
    Some accounting platforms give a separate name to purchases where the payment is made immediately, such as something bought with a credit card or online payment. One example of this would be QuickBooks Online's *expenses*.
    
    You can find these types of transactions in our [Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) data model.
    """
    
    issue_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('issueDate'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: PostBillSourceModifiedDateStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    sub_total: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal') }})
    tax_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxAmount') }})
    total_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount') }})
    amount_due: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amountDue'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    due_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dueDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    line_items: Optional[list[PostBillSourceModifiedDateLineItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lineItems'), 'exclude': lambda f: f is None }})
    metadata: Optional[PostBillSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('note'), 'exclude': lambda f: f is None }})
    payment_allocations: Optional[list[PostBillSourceModifiedDatePaymentAllocations]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('paymentAllocations'), 'exclude': lambda f: f is None }})
    purchase_order_refs: Optional[list[PostBillSourceModifiedDatePurchaseOrderRefs]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('purchaseOrderRefs'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reference'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    supplemental_data: Optional[PostBillSourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplementalData'), 'exclude': lambda f: f is None }})
    supplier_ref: Optional[PostBillSourceModifiedDateSupplierRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierRef'), 'exclude': lambda f: f is None }})
    withholding_tax: Optional[list[PostBillSourceModifiedDateWithholdingTax]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('withholdingTax'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostBillSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class PostBillRequest:
    path_params: PostBillPathParams = dataclasses.field()
    query_params: PostBillQueryParams = dataclasses.field()
    security: PostBillSecurity = dataclasses.field()
    request: Optional[PostBillSourceModifiedDate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONChangesPushOperationRecordRef:
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    
class PostBill200ApplicationJSONChangesTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    CREATED = "Created"
    MODIFIED = "Modified"
    DELETED = "Deleted"
    ATTACHMENT_UPLOADED = "AttachmentUploaded"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONChanges:
    attachment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attachmentId'), 'exclude': lambda f: f is None }})
    record_ref: Optional[PostBill200ApplicationJSONChangesPushOperationRecordRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('recordRef'), 'exclude': lambda f: f is None }})
    type: Optional[PostBill200ApplicationJSONChangesTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDateLineItemsAccountRef:
    r"""PostBill200ApplicationJSONSourceModifiedDateLineItemsAccountRef
    Reference to the account to which the line item is linked.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDateLineItemsItemRef:
    r"""PostBill200ApplicationJSONSourceModifiedDateLineItemsItemRef
    Reference to the product, service type, or inventory item to which the line item is linked.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDateLineItemsTaxRateRef:
    r"""PostBill200ApplicationJSONSourceModifiedDateLineItemsTaxRateRef
    Reference to the tax rate to which the line item is linked.
    """
    
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('effectiveTaxRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDateLineItemsTrackingCategoryRefs:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDateLineItemsTrackingCustomerRef:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyName'), 'exclude': lambda f: f is None }})
    
class PostBill200ApplicationJSONSourceModifiedDateLineItemsTrackingIsBilledToEnum(str, Enum):
    UNKNOWN = "Unknown"
    NOT_APPLICABLE = "NotApplicable"
    CUSTOMER = "Customer"
    PROJECT = "Project"

class PostBill200ApplicationJSONSourceModifiedDateLineItemsTrackingIsRebilledToEnum(str, Enum):
    UNKNOWN = "Unknown"
    NOT_APPLICABLE = "NotApplicable"
    CUSTOMER = "Customer"
    PROJECT = "Project"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDateLineItemsTrackingProjectRef:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDateLineItemsTracking:
    category_refs: list[PostBill200ApplicationJSONSourceModifiedDateLineItemsTrackingCategoryRefs] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('categoryRefs') }})
    is_billed_to: PostBill200ApplicationJSONSourceModifiedDateLineItemsTrackingIsBilledToEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isBilledTo') }})
    is_rebilled_to: PostBill200ApplicationJSONSourceModifiedDateLineItemsTrackingIsRebilledToEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isRebilledTo') }})
    customer_ref: Optional[PostBill200ApplicationJSONSourceModifiedDateLineItemsTrackingCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerRef'), 'exclude': lambda f: f is None }})
    project_ref: Optional[PostBill200ApplicationJSONSourceModifiedDateLineItemsTrackingProjectRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('projectRef'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDateLineItems:
    quantity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('quantity') }})
    unit_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('unitAmount') }})
    account_ref: Optional[PostBill200ApplicationJSONSourceModifiedDateLineItemsAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    discount_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountAmount'), 'exclude': lambda f: f is None }})
    discount_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountPercentage'), 'exclude': lambda f: f is None }})
    is_direct_cost: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDirectCost'), 'exclude': lambda f: f is None }})
    item_ref: Optional[PostBill200ApplicationJSONSourceModifiedDateLineItemsItemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemRef'), 'exclude': lambda f: f is None }})
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal'), 'exclude': lambda f: f is None }})
    tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxAmount'), 'exclude': lambda f: f is None }})
    tax_rate_ref: Optional[PostBill200ApplicationJSONSourceModifiedDateLineItemsTaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateRef'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    tracking: Optional[PostBill200ApplicationJSONSourceModifiedDateLineItemsTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tracking'), 'exclude': lambda f: f is None }})
    tracking_category_refs: Optional[list[PostBill200ApplicationJSONSourceModifiedDateLineItemsTrackingCategoryRefs]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('trackingCategoryRefs'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDatePaymentAllocationsAllocation:
    allocated_on_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('allocatedOnDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDatePaymentAllocationsPaymentAccountRef:
    r"""PostBill200ApplicationJSONSourceModifiedDatePaymentAllocationsPaymentAccountRef
    The account that the allocated payment is made from or to.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDatePaymentAllocationsPayment:
    account_ref: Optional[PostBill200ApplicationJSONSourceModifiedDatePaymentAllocationsPaymentAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('note'), 'exclude': lambda f: f is None }})
    paid_on_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('paidOnDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reference'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDatePaymentAllocations:
    allocation: PostBill200ApplicationJSONSourceModifiedDatePaymentAllocationsAllocation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('allocation') }})
    payment: PostBill200ApplicationJSONSourceModifiedDatePaymentAllocationsPayment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('payment') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDatePurchaseOrderRefs:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    purchase_order_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('purchaseOrderNumber'), 'exclude': lambda f: f is None }})
    
class PostBill200ApplicationJSONSourceModifiedDateStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    OPEN = "Open"
    PARTIALLY_PAID = "PartiallyPaid"
    PAID = "Paid"
    VOID = "Void"
    DRAFT = "Draft"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDateSupplementalData:
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('content'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDateSupplierRef:
    r"""PostBill200ApplicationJSONSourceModifiedDateSupplierRef
    Reference to the supplier the bill was received from.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    supplier_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDateWithholdingTax:
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONSourceModifiedDate:
    r"""PostBill200ApplicationJSONSourceModifiedDate
    > **Invoices or bills?**
    >
    > In Codat, bills are for accounts payable only. For the accounts receivable equivalent of bills, see [Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice).
    
    View the coverage for bills in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    In Codat, a bill contains details of:
    * When the bill was recorded in the accounting system.
    * How much the bill is for and the currency of the amount.
    * Who the bill was received from — the *supplier*.
    * What the bill is for — the *line items*.
    
    Some accounting platforms give a separate name to purchases where the payment is made immediately, such as something bought with a credit card or online payment. One example of this would be QuickBooks Online's *expenses*.
    
    You can find these types of transactions in our [Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) data model.
    """
    
    issue_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('issueDate'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: PostBill200ApplicationJSONSourceModifiedDateStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    sub_total: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal') }})
    tax_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxAmount') }})
    total_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount') }})
    amount_due: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amountDue'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    due_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dueDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    line_items: Optional[list[PostBill200ApplicationJSONSourceModifiedDateLineItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lineItems'), 'exclude': lambda f: f is None }})
    metadata: Optional[PostBill200ApplicationJSONSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('note'), 'exclude': lambda f: f is None }})
    payment_allocations: Optional[list[PostBill200ApplicationJSONSourceModifiedDatePaymentAllocations]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('paymentAllocations'), 'exclude': lambda f: f is None }})
    purchase_order_refs: Optional[list[PostBill200ApplicationJSONSourceModifiedDatePurchaseOrderRefs]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('purchaseOrderRefs'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reference'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    supplemental_data: Optional[PostBill200ApplicationJSONSourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplementalData'), 'exclude': lambda f: f is None }})
    supplier_ref: Optional[PostBill200ApplicationJSONSourceModifiedDateSupplierRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierRef'), 'exclude': lambda f: f is None }})
    withholding_tax: Optional[list[PostBill200ApplicationJSONSourceModifiedDateWithholdingTax]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('withholdingTax'), 'exclude': lambda f: f is None }})
    
class PostBill200ApplicationJSONStatusEnum(str, Enum):
    PENDING = "Pending"
    FAILED = "Failed"
    SUCCESS = "Success"
    TIMED_OUT = "TimedOut"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONValidationValidationItem:
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemId'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message'), 'exclude': lambda f: f is None }})
    validator_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validatorName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSONValidation:
    r"""PostBill200ApplicationJSONValidation
    A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here.
    """
    
    errors: Optional[list[PostBill200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[PostBill200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBill200ApplicationJSON:
    company_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId') }})
    data_connection_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataConnectionKey') }})
    push_operation_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pushOperationKey') }})
    requested_on_utc: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('requestedOnUtc'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: PostBill200ApplicationJSONStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    status_code: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode') }})
    changes: Optional[list[PostBill200ApplicationJSONChanges]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('changes'), 'exclude': lambda f: f is None }})
    completed_on_utc: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('completedOnUtc'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    data: Optional[PostBill200ApplicationJSONSourceModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType'), 'exclude': lambda f: f is None }})
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errorMessage'), 'exclude': lambda f: f is None }})
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeoutInMinutes'), 'exclude': lambda f: f is None }})
    timeout_in_seconds: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeoutInSeconds'), 'exclude': lambda f: f is None }})
    validation: Optional[PostBill200ApplicationJSONValidation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostBillResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    post_bill_200_application_json_object: Optional[PostBill200ApplicationJSON] = dataclasses.field(default=None)
    