"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from typing import Any, Optional


@dataclasses.dataclass
class GetDirectCostsRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})  
    page: int = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""Page number. [Read more](https://docs.codat.io/using-the-api/paging)."""  
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    r"""Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results)."""  
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    r"""Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging)."""  
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Codat query string. [Read more](https://docs.codat.io/using-the-api/querying)."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksLinksCurrent:
    
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksLinksNext:
    
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksLinksPrevious:
    
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksLinksSelf:
    
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksLinks:
    
    current: GetDirectCostsLinksLinksCurrent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current') }})  
    self_: GetDirectCostsLinksLinksSelf = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('self') }})  
    next: Optional[GetDirectCostsLinksLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next'), 'exclude': lambda f: f is None }})  
    previous: Optional[GetDirectCostsLinksLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDateContactRef:
    r"""A customer or supplier associated with the direct cost."""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})  
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDateLineItemsAccountRef:
    r"""Reference to the account to which the line item is linked."""
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' from the Accounts data type."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""'name' from the Accounts data type."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDateLineItemsItemRef:
    r"""Reference to the product, service type, or inventory item to which the direct cost is linked."""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDateLineItemsTaxRateRef:
    r"""Reference to the tax rate to which the the line item is linked."""
    
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('effectiveTaxRate'), 'exclude': lambda f: f is None }})
    r"""Applicable tax rate."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' from the 'taxRates' data type."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""'name' from the 'taxRates' data type."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDateLineItemsInvoiceableTrackingInvoiceTo:
    r"""Links to the underlying record or data type.
    
    Found on:
    
    - Journal entries
    - Account transactions
    - Invoices
    - Transfers
    """
    
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Name of the 'dataType'."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' of the underlying record or data type."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDateLineItemsInvoiceableTrackingRecordRefs:
    r"""Links to the underlying record or data type.
    
    Found on:
    
    - Journal entries
    - Account transactions
    - Invoices
    - Transfers
    """
    
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Name of the 'dataType'."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' of the underlying record or data type."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDateLineItemsInvoiceableTracking:
    
    record_refs: list[GetDirectCostsLinksSourceModifiedDateLineItemsInvoiceableTrackingRecordRefs] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRefs') }})  
    invoice_to: Optional[GetDirectCostsLinksSourceModifiedDateLineItemsInvoiceableTrackingInvoiceTo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceTo'), 'exclude': lambda f: f is None }})
    r"""Links to the underlying record or data type.
    
    Found on:
    
    - Journal entries
    - Account transactions
    - Invoices
    - Transfers
    """  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDateLineItemsTrackingCategoryRefs:
    r"""References a category against which the item is tracked."""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDateLineItems:
    
    quantity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})
    r"""Number of units of goods or services received.
    
    Note: If the platform does not provide this information, the quantity will be mapped as 1.
    """  
    unit_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unitAmount') }})
    r"""Price of each unit of goods or services.
    Note: If the platform does not provide this information, the unit amount will be mapped to the total amount.
    """  
    account_ref: Optional[GetDirectCostsLinksSourceModifiedDateLineItemsAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})
    r"""Reference to the account to which the line item is linked."""  
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Friendly name of the goods or services."""  
    discount_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountAmount'), 'exclude': lambda f: f is None }})
    r"""Discount amount for the line before tax."""  
    discount_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountPercentage'), 'exclude': lambda f: f is None }})
    r"""Discount percentage for the line before tax."""  
    item_ref: Optional[GetDirectCostsLinksSourceModifiedDateLineItemsItemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemRef'), 'exclude': lambda f: f is None }})
    r"""Reference to the product, service type, or inventory item to which the direct cost is linked."""  
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subTotal'), 'exclude': lambda f: f is None }})
    r"""Amount of the line, inclusive of discounts but exclusive of tax."""  
    tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxAmount'), 'exclude': lambda f: f is None }})
    r"""Amount of tax for the line."""  
    tax_rate_ref: Optional[GetDirectCostsLinksSourceModifiedDateLineItemsTaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxRateRef'), 'exclude': lambda f: f is None }})
    r"""Reference to the tax rate to which the the line item is linked."""  
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})
    r"""Total amount of the line, including tax."""  
    tracking: Optional[GetDirectCostsLinksSourceModifiedDateLineItemsInvoiceableTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking'), 'exclude': lambda f: f is None }})  
    tracking_category_refs: Optional[list[GetDirectCostsLinksSourceModifiedDateLineItemsTrackingCategoryRefs]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trackingCategoryRefs'), 'exclude': lambda f: f is None }})
    r"""Collection of categories against which this direct cost is tracked."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDateMetadata:
    
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDeleted'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDatePaymentAllocationsAllocation:
    
    allocated_on_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allocatedOnDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date the payment was allocated."""  
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""The currency of the transaction."""  
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencyRate'), 'exclude': lambda f: f is None }})
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.
    
    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.  
    
    Where the currency rate is provided by the underlying accounting platform, it will be available from Codat with the same precision (up to a maximum of 9 decimal places). 
    
    For accounting platforms which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.
    
    ## Examples with base currency of GBP
    
    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |
    
    ## Examples with base currency of USD
    
    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |
    """  
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})
    r"""The total amount that has been allocated."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDatePaymentAllocationsPaymentAccountRef:
    r"""The account that the allocated payment is made from or to."""
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' from the Accounts data type."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""'name' from the Accounts data type."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDatePaymentAllocationsPayment:
    
    account_ref: Optional[GetDirectCostsLinksSourceModifiedDatePaymentAllocationsPaymentAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})
    r"""The account that the allocated payment is made from or to."""  
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""Currency the payment has been made in."""  
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencyRate'), 'exclude': lambda f: f is None }})
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.
    
    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.  
    
    Where the currency rate is provided by the underlying accounting platform, it will be available from Codat with the same precision (up to a maximum of 9 decimal places). 
    
    For accounting platforms which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.
    
    ## Examples with base currency of GBP
    
    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |
    
    ## Examples with base currency of USD
    
    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |
    """  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier of the allocated payment."""  
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('note'), 'exclude': lambda f: f is None }})
    r"""Notes attached to the allocated payment."""  
    paid_on_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paidOnDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date the payment was paid."""  
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference'), 'exclude': lambda f: f is None }})
    r"""Reference to the allocated payment."""  
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})
    r"""Total amount that was paid."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDatePaymentAllocations:
    
    allocation: GetDirectCostsLinksSourceModifiedDatePaymentAllocationsAllocation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allocation') }})  
    payment: GetDirectCostsLinksSourceModifiedDatePaymentAllocationsPayment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDateSupplementalData:
    r"""Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more."""
    
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinksSourceModifiedDate:
    r"""> **Language tip: ** Direct costs may also be referred to as **Spend transactions**, **Spend money transactions**, or **Payments** in various accounting platforms.
    
    > View the coverage for direct costs in the <a className="external" href="https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts" target="_blank">Data coverage explorer</a>.
    
    ## Overview
    
    Direct costs include:
      * Purchasing an item and paying it off at the point of the purchase
      * Receiving cash from a refunded item if the refund is made by the supplier
      * Withdrawing money from a bank account 
      * Writing a cheque
    
    From the Direct Costs endpoints, you can: 
    
      * [Get a list of all direct costs for a specific company ](https://api.codat.io/swagger/index.html#/DirectCosts/get_companies__companyId__connections__connectionId__data_directCosts)
      * [Get a single direct cost for a specific company ](https://api.codat.io/swagger/index.html#/DirectCosts/get_companies__companyId__connections__connectionId__data_directCosts__directCostId_)
      * [Add a new direct cost to a specific company's accounting package](https://api.codat.io/swagger/index.html#/DirectCosts/post_companies__companyId__connections__connectionId__push_directCosts)
    
    Direct costs is a child data type of [account transactions](https://docs.codat.io/accounting-api#/schemas/AccountTransaction).
    """
    
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    r"""Currency of the direct cost."""  
    issue_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issueDate'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""Date of the direct cost as recorded in the accounting platform.Date of the direct cost as recorded in the accounting platform."""  
    line_items: list[GetDirectCostsLinksSourceModifiedDateLineItems] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems') }})
    r"""An array of line items."""  
    payment_allocations: list[GetDirectCostsLinksSourceModifiedDatePaymentAllocations] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentAllocations') }})
    r"""An array of payment allocations."""  
    sub_total: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subTotal') }})
    r"""The total amount of the direct costs, excluding any taxes."""  
    tax_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxAmount') }})
    r"""The total amount of tax on the direct costs."""  
    total_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount') }})
    r"""The amount of the direct costs, inclusive of tax."""  
    contact_ref: Optional[GetDirectCostsLinksSourceModifiedDateContactRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contactRef'), 'exclude': lambda f: f is None }})
    r"""A customer or supplier associated with the direct cost."""  
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencyRate'), 'exclude': lambda f: f is None }})
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.
    
    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.  
    
    Where the currency rate is provided by the underlying accounting platform, it will be available from Codat with the same precision (up to a maximum of 9 decimal places). 
    
    For accounting platforms which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.
    
    ## Examples with base currency of GBP
    
    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |
    
    ## Examples with base currency of USD
    
    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |
    """  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier of the direct cost, unique for the company."""  
    metadata: Optional[GetDirectCostsLinksSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})  
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in Codat."""  
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('note'), 'exclude': lambda f: f is None }})
    r"""A note attached to the direct cost."""  
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference'), 'exclude': lambda f: f is None }})
    r"""User-friendly reference for the direct cost."""  
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in the originating system"""  
    supplemental_data: Optional[GetDirectCostsLinksSourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplementalData'), 'exclude': lambda f: f is None }})
    r"""Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDirectCostsLinks:
    r"""Codat's Paging Model"""
    
    links: GetDirectCostsLinksLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_links') }})  
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageNumber') }})  
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize') }})  
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalResults') }})  
    results: Optional[list[GetDirectCostsLinksSourceModifiedDate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class GetDirectCostsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    links: Optional[GetDirectCostsLinks] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    