"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import loansummaryreportinfo as shared_loansummaryreportinfo
from ..shared import loansummaryreportitem as shared_loansummaryreportitem
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class LoanSummary:
    report_info: Optional[shared_loansummaryreportinfo.LoanSummaryReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportInfo'), 'exclude': lambda f: f is None }})
    report_items: Optional[list[shared_loansummaryreportitem.LoanSummaryReportItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportItems'), 'exclude': lambda f: f is None }})
    r"""Returns a summary of all loan activity for that integration type"""
    

