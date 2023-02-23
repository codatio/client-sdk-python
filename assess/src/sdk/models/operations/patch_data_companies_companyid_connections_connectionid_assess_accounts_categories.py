import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Any, Optional


@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclass_json
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequestBodyCategoriesAccountRef:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequestBodyCategories:
    account_ref: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequestBodyCategoriesAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef') }})
    confirmed: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('confirmed') }})
    

@dataclass_json
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequestBody:
    categories: Optional[list[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequestBodyCategories]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('categories') }})
    

@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequest:
    path_params: PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesPathParams = dataclasses.field()
    request: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccountAccountRef:
    r"""PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccountAccountRef
    An object containing account reference data.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccountModifiedDate:
    detail_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailType') }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    subtype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subtype') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccount:
    account_ref: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccountAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef') }})
    confirmed: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccountModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('confirmed') }})
    suggested: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccountModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('suggested') }})
    

@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    categorised_accounts: Optional[list[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccount]] = dataclasses.field(default=None)
    