"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import orderdiscountallocation as shared_orderdiscountallocation
from ..shared import productref as shared_productref
from ..shared import productvariantref as shared_productvariantref
from ..shared import taxcomponentallocation as shared_taxcomponentallocation
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrderLineItem:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""A unique, persistent identifier for this record"""
    discount_allocations: Optional[list[shared_orderdiscountallocation.OrderDiscountAllocation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountAllocations'), 'exclude': lambda f: f is None }})
    product_ref: Optional[shared_productref.ProductRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productRef'), 'exclude': lambda f: f is None }})
    r"""Reference that links the line item to the correct product details."""
    product_variant_ref: Optional[shared_productvariantref.ProductVariantRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productVariantRef'), 'exclude': lambda f: f is None }})
    r"""Reference that links the line item to the specific version of product that has been ordered."""
    quantity: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity'), 'exclude': lambda f: f is None }})
    r"""Number of units of the product sold.
    For refunds, quantity is a negative value.
    """
    taxes: Optional[list[shared_taxcomponentallocation.TaxComponentAllocation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxes'), 'exclude': lambda f: f is None }})
    r"""Taxes breakdown as applied to order lines."""
    tax_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxPercentage'), 'exclude': lambda f: f is None }})
    r"""Percentage rate (from 0 to 100) of any sale tax applied to the unit amount."""
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})
    r"""Total price of the line item, including discounts, tax and minus any refunds."""
    total_tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalTaxAmount'), 'exclude': lambda f: f is None }})
    r"""Total amount of tax applied to the line item."""
    unit_price: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unitPrice'), 'exclude': lambda f: f is None }})
    r"""Price per unit of goods or service."""
    

