"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .option import Option
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxRateAmount:
    UNSET='__SPEAKEASY_UNSET__'
    selected_tax_rate_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedTaxRateId'), 'exclude': lambda f: f is TaxRateAmount.UNSET }})
    r"""Selected tax rate id from the list of tax rates on the accounting software."""
    tax_rate_options: Optional[List[Option]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxRateOptions'), 'exclude': lambda f: f is TaxRateAmount.UNSET }})
    r"""Array of tax rate options object."""
    

