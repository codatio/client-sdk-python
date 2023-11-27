"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .reportcomponentmeasure import ReportComponentMeasure
from codatassess import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CommerceReportComponent:
    components: Optional[List[CommerceReportComponent]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('components'), 'exclude': lambda f: f is None }})
    dimension: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dimension'), 'exclude': lambda f: f is None }})
    r"""The component's dimension."""
    dimension_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dimensionDisplayName'), 'exclude': lambda f: f is None }})
    r"""The component's display name."""
    item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item'), 'exclude': lambda f: f is None }})
    r"""The component's item number."""
    item_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemDisplayName'), 'exclude': lambda f: f is None }})
    r"""The component's item display name."""
    measures: Optional[List[ReportComponentMeasure]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('measures'), 'exclude': lambda f: f is None }})
    

