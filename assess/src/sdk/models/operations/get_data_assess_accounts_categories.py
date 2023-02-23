from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataAssessAccountsCategoriesChartOfAccountCategory:
    detail_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailType'), 'exclude': lambda f: f is None }})
    detail_type_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailTypeDescription'), 'exclude': lambda f: f is None }})
    detail_type_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailTypeDisplayName'), 'exclude': lambda f: f is None }})
    subtype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subtype'), 'exclude': lambda f: f is None }})
    subtype_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subtypeDisplayName'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetDataAssessAccountsCategoriesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_data_assess_accounts_categories_chart_of_account_category_all_ofs: Optional[list[GetDataAssessAccountsCategoriesChartOfAccountCategory]] = dataclasses.field(default=None)
    