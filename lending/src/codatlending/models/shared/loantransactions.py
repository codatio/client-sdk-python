"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import loantransactionsreportinfo as shared_loantransactionsreportinfo
from ..shared import reportitems as shared_reportitems
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class LoanTransactions:
    r"""OK"""
    errors: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    r"""If there are no errors, an empty array is returned."""
    report_info: Optional[shared_loantransactionsreportinfo.LoanTransactionsReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportInfo'), 'exclude': lambda f: f is None }})
    report_items: Optional[list[shared_reportitems.ReportItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportItems'), 'exclude': lambda f: f is None }})
    r"""Contains object of reporting properties. The loan ref will reference a different object depending on the integration type."""
    
