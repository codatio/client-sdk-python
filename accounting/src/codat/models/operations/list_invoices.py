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
class ListInvoicesPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListInvoicesQueryParams:
    page: float = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListInvoicesSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class ListInvoicesRequest:
    path_params: ListInvoicesPathParams = dataclasses.field()
    query_params: ListInvoicesQueryParams = dataclasses.field()
    security: ListInvoicesSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksLinksCurrent:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksLinksNext:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksLinksPrevious:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksLinksSelf:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksLinks:
    current: ListInvoicesLinksLinksCurrent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('current') }})
    self: ListInvoicesLinksLinksSelf = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('self') }})
    next: Optional[ListInvoicesLinksLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[ListInvoicesLinksLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDateCustomerRef:
    r"""ListInvoicesLinksSourceModifiedDateCustomerRef
    Reference to the customer the invoice has been issued to.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDateLineItemsAccountRef:
    r"""ListInvoicesLinksSourceModifiedDateLineItemsAccountRef
    Reference to the account to which the line item is linked.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDateLineItemsItemRef:
    r"""ListInvoicesLinksSourceModifiedDateLineItemsItemRef
    Reference to the item the line is linked to.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDateLineItemsTaxRateRef:
    r"""ListInvoicesLinksSourceModifiedDateLineItemsTaxRateRef
    Reference to the tax rate to which the line item is linked.
    """
    
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('effectiveTaxRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDateLineItemsTrackingCategoryRefs:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDateLineItemsTrackingCustomerRef:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyName'), 'exclude': lambda f: f is None }})
    
class ListInvoicesLinksSourceModifiedDateLineItemsTrackingIsBilledToEnum(str, Enum):
    UNKNOWN = "Unknown"
    NOT_APPLICABLE = "NotApplicable"
    PROJECT = "Project"

class ListInvoicesLinksSourceModifiedDateLineItemsTrackingIsRebilledToEnum(str, Enum):
    UNKNOWN = "Unknown"
    NOT_APPLICABLE = "NotApplicable"
    PROJECT = "Project"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDateLineItemsTrackingProjectRef:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDateLineItemsTracking:
    category_refs: list[ListInvoicesLinksSourceModifiedDateLineItemsTrackingCategoryRefs] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('categoryRefs') }})
    is_billed_to: ListInvoicesLinksSourceModifiedDateLineItemsTrackingIsBilledToEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isBilledTo') }})
    is_rebilled_to: ListInvoicesLinksSourceModifiedDateLineItemsTrackingIsRebilledToEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isRebilledTo') }})
    customer_ref: Optional[ListInvoicesLinksSourceModifiedDateLineItemsTrackingCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerRef'), 'exclude': lambda f: f is None }})
    project_ref: Optional[ListInvoicesLinksSourceModifiedDateLineItemsTrackingProjectRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('projectRef'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDateLineItems:
    quantity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('quantity') }})
    unit_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('unitAmount') }})
    account_ref: Optional[ListInvoicesLinksSourceModifiedDateLineItemsAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    discount_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountAmount'), 'exclude': lambda f: f is None }})
    discount_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountPercentage'), 'exclude': lambda f: f is None }})
    is_direct_income: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDirectIncome'), 'exclude': lambda f: f is None }})
    item_ref: Optional[ListInvoicesLinksSourceModifiedDateLineItemsItemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemRef'), 'exclude': lambda f: f is None }})
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal'), 'exclude': lambda f: f is None }})
    tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxAmount'), 'exclude': lambda f: f is None }})
    tax_rate_ref: Optional[ListInvoicesLinksSourceModifiedDateLineItemsTaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateRef'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    tracking: Optional[ListInvoicesLinksSourceModifiedDateLineItemsTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tracking'), 'exclude': lambda f: f is None }})
    tracking_category_refs: Optional[list[ListInvoicesLinksSourceModifiedDateLineItemsTrackingCategoryRefs]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('trackingCategoryRefs'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDatePaymentAllocationsAllocation:
    allocated_on_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('allocatedOnDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDatePaymentAllocationsPaymentAccountRef:
    r"""ListInvoicesLinksSourceModifiedDatePaymentAllocationsPaymentAccountRef
    The account that the allocated payment is made from or to.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDatePaymentAllocationsPayment:
    account_ref: Optional[ListInvoicesLinksSourceModifiedDatePaymentAllocationsPaymentAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('note'), 'exclude': lambda f: f is None }})
    paid_on_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('paidOnDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reference'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDatePaymentAllocations:
    allocation: ListInvoicesLinksSourceModifiedDatePaymentAllocationsAllocation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('allocation') }})
    payment: ListInvoicesLinksSourceModifiedDatePaymentAllocationsPayment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('payment') }})
    
class ListInvoicesLinksSourceModifiedDateStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    DRAFT = "Draft"
    SUBMITTED = "Submitted"
    PARTIALLY_PAID = "PartiallyPaid"
    PAID = "Paid"
    VOID = "Void"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDateSupplementalData:
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('content'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDateWithholdingTax:
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinksSourceModifiedDate:
    r"""ListInvoicesLinksSourceModifiedDate
    > View the coverage for invoices in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    An invoice is an itemized record of goods sold or services provided to a [customer](https://docs.codat.io/accounting-api#/schemas/Customer).
    
    In Codat, an invoice contains details of:
    
    - The timeline of the invoice—when it was raised, marked as paid, last edited, and so on.
    - How much the invoice is for, what portion of the invoice is tax or discounts, and what currency the amounts are represented in. 
    - Who the invoice has been raised to; the _customer_.
    - The breakdown of what the invoice is for; the _line items_.
    - Any [payments](https://docs.codat.io/accounting-api#/schemas/Payment) assigned to the invoice; the _payment allocations_.
    
    > **Invoices or bills?**  
    >
    > In Codat, invoices represent accounts receivable only. For accounts payable invoices, see [Bills](https://docs.codat.io/accounting-api#/schemas/Bill).
    
    > **Invoice PDF downloads**  
    >
    > You can <a className=\"external\" href=\"https://api.codat.io/swagger/index.html#/Invoices/get_companies__companyId__data_invoices__invoiceId__pdf\" target=\"_blank\">download a PDF version</a> of an invoice for supported integrations.
    > 
    > The filename will be invoice-{number}.pdf.
    """
    
    amount_due: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('amountDue') }})
    issue_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('issueDate'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: ListInvoicesLinksSourceModifiedDateStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    total_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount') }})
    total_tax_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalTaxAmount') }})
    additional_tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalTaxAmount'), 'exclude': lambda f: f is None }})
    additional_tax_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additionalTaxPercentage'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    customer_ref: Optional[ListInvoicesLinksSourceModifiedDateCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerRef'), 'exclude': lambda f: f is None }})
    discount_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('discountPercentage'), 'exclude': lambda f: f is None }})
    due_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dueDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    invoice_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceNumber'), 'exclude': lambda f: f is None }})
    line_items: Optional[list[ListInvoicesLinksSourceModifiedDateLineItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lineItems'), 'exclude': lambda f: f is None }})
    metadata: Optional[ListInvoicesLinksSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('note'), 'exclude': lambda f: f is None }})
    paid_on_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('paidOnDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    payment_allocations: Optional[list[ListInvoicesLinksSourceModifiedDatePaymentAllocations]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('paymentAllocations'), 'exclude': lambda f: f is None }})
    sales_order_refs: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('salesOrderRefs'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subTotal'), 'exclude': lambda f: f is None }})
    supplemental_data: Optional[ListInvoicesLinksSourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplementalData'), 'exclude': lambda f: f is None }})
    total_discount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalDiscount'), 'exclude': lambda f: f is None }})
    withholding_tax: Optional[list[ListInvoicesLinksSourceModifiedDateWithholdingTax]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('withholdingTax'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListInvoicesLinks:
    r"""ListInvoicesLinks
    Codat's Paging Model
    """
    
    links: ListInvoicesLinksLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('_links') }})
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize') }})
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults') }})
    results: Optional[list[ListInvoicesLinksSourceModifiedDate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ListInvoicesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    links: Optional[ListInvoicesLinks] = dataclasses.field(default=None)
    