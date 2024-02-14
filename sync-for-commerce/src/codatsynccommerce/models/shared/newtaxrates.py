"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .option import Option
from .taxratemapping import TaxRateMapping
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewTaxRates:
    UNSET='__SPEAKEASY_UNSET__'
    accounting_tax_rate_options: Optional[List[Option]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountingTaxRateOptions'), 'exclude': lambda f: f is NewTaxRates.UNSET }})
    r"""Array of accounting tax rate options."""
    commerce_tax_rate_options: Optional[List[Option]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('commerceTaxRateOptions'), 'exclude': lambda f: f is NewTaxRates.UNSET }})
    r"""Array of tax component options."""
    default_zero_tax_rate_options: Optional[List[Option]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultZeroTaxRateOptions'), 'exclude': lambda f: f is NewTaxRates.UNSET }})
    r"""Default zero tax rate selected for sync."""
    selected_default_zero_tax_rate_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedDefaultZeroTaxRateId'), 'exclude': lambda f: f is NewTaxRates.UNSET }})
    r"""Default tax rate selected for sync."""
    tax_rate_mappings: Optional[List[TaxRateMapping]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxRateMappings'), 'exclude': lambda f: f is NewTaxRates.UNSET }})
    r"""Array of tax component to rate mapppings."""
    

