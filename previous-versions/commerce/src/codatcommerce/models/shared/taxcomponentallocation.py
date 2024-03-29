"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import taxcomponentref as shared_taxcomponentref
from codatcommerce import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxComponentAllocation:
    rate: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rate'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Tax amount on order line sale as available from source commerce platform."""
    tax_component_ref: Optional[shared_taxcomponentref.TaxComponentRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxComponentRef'), 'exclude': lambda f: f is None }})
    r"""Taxes rates reference object depending on the rates being available on source commerce package."""
    

