"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Any, Optional


@dataclasses.dataclass
class ListCommerceOrdersRequest:
    
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
class ListCommerceOrdersLinksLinksCurrent:
    
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCommerceOrdersLinksLinksNext:
    
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCommerceOrdersLinksLinksPrevious:
    
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCommerceOrdersLinksLinksSelf:
    
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCommerceOrdersLinksLinks:
    
    current: ListCommerceOrdersLinksLinksCurrent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current') }})  
    self_: ListCommerceOrdersLinksLinksSelf = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('self') }})  
    next: Optional[ListCommerceOrdersLinksLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next'), 'exclude': lambda f: f is None }})  
    previous: Optional[ListCommerceOrdersLinksLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCommerceOrdersLinksSourceModifiedDateNameRef:
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique identitifer of the record being referenced"""  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the record being referenced."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCommerceOrdersLinksSourceModifiedDateOrderLineItemsDiscountAllocations:
    
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the discount in the commerce or point of sale platform."""  
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})
    r"""Total amount of discount applied."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCommerceOrdersLinksSourceModifiedDateOrderLineItemsNameRef:
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique identitifer of the record being referenced"""  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the record being referenced."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCommerceOrdersLinksSourceModifiedDateOrderLineItems:
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""A unique, persistent identifier for this record"""  
    discount_allocations: Optional[list[ListCommerceOrdersLinksSourceModifiedDateOrderLineItemsDiscountAllocations]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountAllocations'), 'exclude': lambda f: f is None }})  
    product_ref: Optional[ListCommerceOrdersLinksSourceModifiedDateOrderLineItemsNameRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productRef'), 'exclude': lambda f: f is None }})  
    product_variant_ref: Optional[ListCommerceOrdersLinksSourceModifiedDateOrderLineItemsNameRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productVariantRef'), 'exclude': lambda f: f is None }})  
    quantity: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity'), 'exclude': lambda f: f is None }})
    r"""Number of units of the product sold.
    For refunds, quantity is a negative value.
    
    """  
    taxes: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxes'), 'exclude': lambda f: f is None }})
    r"""Taxes breakdown as applied to order lines."""  
    tax_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxPercentage'), 'exclude': lambda f: f is None }})
    r"""Percentage rate (from 0 to 100) of any sale tax applied to the unit amount."""  
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})
    r"""Total price of the line item, including discounts, tax and minus any refunds."""  
    total_tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalTaxAmount'), 'exclude': lambda f: f is None }})
    r"""Total amount of tax applied to the line item."""  
    unit_price: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unitPrice'), 'exclude': lambda f: f is None }})
    r"""Price per unit of goods or service."""  
    
class ListCommerceOrdersLinksSourceModifiedDateSourceModifiedDateStatusEnum(str, Enum):
    r"""Status of the payment"""
    PENDING = "Pending"
    AUTHORIZED = "Authorized"
    PAID = "Paid"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    UNKNOWN = "Unknown"

class ListCommerceOrdersLinksSourceModifiedDateSourceModifiedDateTypeEnum(str, Enum):
    r"""Status of the payment"""
    CASH = "Cash"
    CARD = "Card"
    INVOICE = "Invoice"
    ONLINE_CARD = "OnlineCard"
    SWISH = "Swish"
    VIPPS = "Vipps"
    MOBILE = "Mobile"
    STORE_CREDIT = "StoreCredit"
    PAYPAL = "Paypal"
    CUSTOM = "Custom"
    PREPAID = "Prepaid"
    UNKNOWN = "Unknown"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCommerceOrdersLinksSourceModifiedDateSourceModifiedDate:
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""A unique, persistent identifier for this record"""  
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    r"""Payment Amount (including gratuity)."""  
    created_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date the entity was created."""  
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""Currency in which the payment was made."""  
    due_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Date by which payment must be made"""  
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in Codat."""  
    payment_provider: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentProvider'), 'exclude': lambda f: f is None }})
    r"""Service provider of the payment, if applicable."""  
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in the originating system"""  
    status: Optional[ListCommerceOrdersLinksSourceModifiedDateSourceModifiedDateStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Status of the payment"""  
    type: Optional[ListCommerceOrdersLinksSourceModifiedDateSourceModifiedDateTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Status of the payment"""  
    
class ListCommerceOrdersLinksSourceModifiedDateServiceChargesTypeEnum(str, Enum):
    r"""The type of the service charge."""
    GENERIC = "Generic"
    SHIPPING = "Shipping"
    OVERPAYMENT = "Overpayment"
    UNKNOWN = "Unknown"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCommerceOrdersLinksSourceModifiedDateServiceCharges:
    
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Service charges for this order."""  
    quantity: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity'), 'exclude': lambda f: f is None }})
    r"""The number of times the charge is charged."""  
    tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxAmount'), 'exclude': lambda f: f is None }})
    r"""Amount of the service charge that is tax."""  
    taxes: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxes'), 'exclude': lambda f: f is None }})
    r"""Taxes breakdown as applied to service charges."""  
    tax_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxPercentage'), 'exclude': lambda f: f is None }})
    r"""Percentage rate (from 0 to 100) of any tax applied to the service charge."""  
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})
    r"""Total service charge, including taxes."""  
    type: Optional[ListCommerceOrdersLinksSourceModifiedDateServiceChargesTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The type of the service charge."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCommerceOrdersLinksSourceModifiedDate:
    r"""Orders contain the transaction details for all products sold by the company, and include details of any payments, service charges, or refunds related to each order.
    
    From the Orders endpoints you can retrieve:
    
    A list of all the orders for a commerce company:
    `GET /companies/{companyId}/connections/{connectionId}/data/commerce-orders`.
    The details of an individual order:
    `GET /companies/{companyId}/connections/{connectionId}/data/commerce-orders/{orderId}`.
    Note that for refunds `quantity` is a negative value and `unitPrice` is a positive value.
    
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""A unique, persistent identifier for this record"""  
    closed_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('closedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Date on which order was closed after the product was shipped, paid for, and any refund period had elapsed."""  
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""The Codat country property is returned as it was provided in the underlying platform by the company without any formatting on our part.
    
    Depending on the platform the value of this property will either be an <a href=\"https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes\" target=\"_blank\">ISO 3166</a> code (2-alpha or 3-alpha) or free-form text returned as a string name in our model. 
    
    For POST operations against platforms that demand a specific format for the country code, we have documented accepted values in the [options](https://docs.codat.io/codat-api#/operations/get-companies-companyId-connections-connectionId-push) endpoint.
    """  
    created_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date the entity was created."""  
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})  
    customer_ref: Optional[ListCommerceOrdersLinksSourceModifiedDateNameRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerRef'), 'exclude': lambda f: f is None }})  
    location_ref: Optional[ListCommerceOrdersLinksSourceModifiedDateNameRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('locationRef'), 'exclude': lambda f: f is None }})  
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in Codat."""  
    order_line_items: Optional[list[ListCommerceOrdersLinksSourceModifiedDateOrderLineItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orderLineItems'), 'exclude': lambda f: f is None }})  
    order_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orderNumber'), 'exclude': lambda f: f is None }})
    r"""Friendly reference for the order in the commerce or point of sale platform."""  
    payments: Optional[list[ListCommerceOrdersLinksSourceModifiedDateSourceModifiedDate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payments'), 'exclude': lambda f: f is None }})  
    service_charges: Optional[list[ListCommerceOrdersLinksSourceModifiedDateServiceCharges]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('serviceCharges'), 'exclude': lambda f: f is None }})  
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in the originating system"""  
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})
    r"""Total amount of the order, including tax, net of any discounts and refunds."""  
    total_discount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalDiscount'), 'exclude': lambda f: f is None }})
    r"""Total amount of discount applied to the order."""  
    total_gratuity: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalGratuity'), 'exclude': lambda f: f is None }})
    r"""Extra amount added to a bill."""  
    total_refund: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalRefund'), 'exclude': lambda f: f is None }})
    r"""Total amount refunded issued by a merchant on an order (always a negative value)."""  
    total_tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalTaxAmount'), 'exclude': lambda f: f is None }})
    r"""Total amount of tax applied to the order."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCommerceOrdersLinks:
    r"""Codat's Paging Model"""
    
    links: ListCommerceOrdersLinksLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_links') }})  
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageNumber') }})  
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize') }})  
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalResults') }})  
    results: Optional[list[ListCommerceOrdersLinksSourceModifiedDate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class ListCommerceOrdersResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    links: Optional[ListCommerceOrdersLinks] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    