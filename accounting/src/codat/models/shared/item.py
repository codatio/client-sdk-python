"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import billitem as shared_billitem
from ..shared import invoiceitem as shared_invoiceitem
from ..shared import itemstatus_enum as shared_itemstatus_enum
from ..shared import metadata as shared_metadata
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Item:
    r"""> View the coverage for items in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    **Items** allow your customers to save and track details of the products and services that they buy and sell.
    
    """
    
    is_bill_item: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isBillItem') }})
    r"""Whether you can use this item for bills."""  
    is_invoice_item: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isInvoiceItem') }})
    r"""Whether you can use this item for invoices."""  
    item_status: shared_itemstatus_enum.ItemStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemStatus') }})
    r"""Current state of the item, either:
    
    - `Active`: Available for use
    - `Archived`: Unavailable
    - `Unknown`
    
    Due to a [limitation in Xero's API](https://docs.codat.io/integrations/accounting/xero/xero-faq#why-do-all-of-my-items-from-xero-have-their-status-as-unknown), all items from Xero are mapped as `Unknown`.
    """  
    type: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})  
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
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:
    
    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```
    
    
    
    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:
    
    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`
    
    > Time zones
    > 
    > Not all dates from Codat will contain information about time zones.  
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the item in the accounting platform."""  
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:
    
    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```
    
    
    
    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:
    
    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`
    
    > Time zones
    > 
    > Not all dates from Codat will contain information about time zones.  
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """  
    