"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountmappinginfo as shared_accountmappinginfo
from ..shared import taxratemappinginfo as shared_taxratemappinginfo
from ..shared import trackingcategorymappinginfo as shared_trackingcategorymappinginfo
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class MappingOptions:
    r"""Success"""
    accounts: Optional[list[shared_accountmappinginfo.AccountMappingInfo]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts'), 'exclude': lambda f: f is None }})
    r"""Array of available accounts for mapping."""
    expense_provider: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expenseProvider'), 'exclude': lambda f: f is None }})
    r"""Name of the expense integration."""
    tax_rates: Optional[list[shared_taxratemappinginfo.TaxRateMappingInfo]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxRates'), 'exclude': lambda f: f is None }})
    r"""Array of available tax rates for mapping."""
    tracking_categories: Optional[list[shared_trackingcategorymappinginfo.TrackingCategoryMappingInfo]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trackingCategories'), 'exclude': lambda f: f is None }})
    r"""Array of available tracking categories for mapping."""
    

