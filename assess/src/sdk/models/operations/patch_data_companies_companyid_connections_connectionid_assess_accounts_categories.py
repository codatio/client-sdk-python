from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Any, Optional


@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequestBodyCategoriesAccountRef:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequestBodyCategories:
    account_ref: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequestBodyCategoriesAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    confirmed: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('confirmed'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequestBody:
    categories: Optional[list[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequestBodyCategories]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('categories'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequest:
    path_params: PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesPathParams = dataclasses.field()
    request: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccountAccountRef:
    r"""PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccountAccountRef
    An object containing account reference data.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccountModifiedDate:
    detail_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailType'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    subtype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subtype'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccount:
    account_ref: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccountAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    confirmed: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccountModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('confirmed'), 'exclude': lambda f: f is None }})
    suggested: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccountModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('suggested'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    categorised_accounts: Optional[list[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccount]] = dataclasses.field(default=None)
    