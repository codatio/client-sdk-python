"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import billitem as shared_billitem
from ..shared import invoiceitem as shared_invoiceitem
from ..shared import itemstatus as shared_itemstatus
from ..shared import itemtype as shared_itemtype
from ..shared import metadata as shared_metadata
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Item:
    r"""> View the coverage for items in the <a className=\\"external\\" href=\\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items\\" target=\\"_blank\\">Data coverage explorer</a>.
    
    ## Overview
    
    **Items** allow your customers to save and track details of the products and services that they buy and sell.
    """
    is_bill_item: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isBillItem') }})
    r"""Whether you can use this item for bills."""
    is_invoice_item: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isInvoiceItem') }})
    r"""Whether you can use this item for invoices."""
    item_status: shared_itemstatus.ItemStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemStatus') }})
    r"""Current state of the item, either:
    
    - `Active`: Available for use
    - `Archived`: Unavailable
    - `Unknown`
    
    Due to a [limitation in Xero's API](https://docs.codat.io/integrations/accounting/xero/xero-faq#why-do-all-of-my-items-from-xero-have-their-status-as-unknown), all items from Xero are mapped as `Unknown`.
    """
    type: shared_itemtype.ItemType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Type of the item."""
    bill_item: Optional[shared_billitem.BillItem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billItem'), 'exclude': lambda f: f is None }})
    r"""Item details that are only for bills."""
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""Friendly reference for the item."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the item that is unique to a company in the accounting platform."""
    invoice_item: Optional[shared_invoiceitem.InvoiceItem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceItem'), 'exclude': lambda f: f is None }})
    r"""Item details that are only for bills."""
    metadata: Optional[shared_metadata.Metadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the item in the accounting platform."""
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    
