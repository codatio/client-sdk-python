"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class ZeroDataType(str, Enum):
    r"""Allowed name of the 'dataType'."""
    PURCHASE_ORDERS = 'purchaseOrders'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Zero:
    r"""Reference to the purchase order line this line was generated from."""
    data_type: Optional[ZeroDataType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Allowed name of the 'dataType'."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' of the underlying record."""
    line_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineNumber'), 'exclude': lambda f: f is None }})
    r"""Line number of the underlying record."""
    

