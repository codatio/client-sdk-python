"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .loansummaryreportinfo import LoanSummaryReportInfo
from .loansummaryreportitem import LoanSummaryReportItem
from codatassess import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LoanSummary:
    report_info: Optional[LoanSummaryReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportInfo'), 'exclude': lambda f: f is None }})
    report_items: Optional[List[LoanSummaryReportItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportItems'), 'exclude': lambda f: f is None }})
    r"""Returns a summary of all loan activity for that integration type"""
    

