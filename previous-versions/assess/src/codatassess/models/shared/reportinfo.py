"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatassess import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReportInfo:
    r"""Report additional information, which is specific to Lending API reports."""
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyName'), 'exclude': lambda f: f is None }})
    r"""The name of the company being queried."""
    generated_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generatedDate'), 'exclude': lambda f: f is None }})
    r"""Date the report was generated."""
    page_number: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageNumber'), 'exclude': lambda f: f is None }})
    r"""The number of the page queried."""
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize'), 'exclude': lambda f: f is None }})
    r"""The number of transactions returned per page."""
    report_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportName'), 'exclude': lambda f: f is None }})
    r"""Name of the report."""
    total_results: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalResults'), 'exclude': lambda f: f is None }})
    r"""The total number of transactions available for a company for the period specified in the query string."""
    

