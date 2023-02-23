import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesPathParams:
    account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclass_json
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesRequestBodyChartOfAccountCategory:
    detail_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailType') }})
    subtype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subtype') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesRequestBody:
    confirmed: PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesRequestBodyChartOfAccountCategory = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('confirmed') }})
    

@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesRequest:
    path_params: PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesPathParams = dataclasses.field()
    request: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesCategorisedAccountAccountRef:
    r"""PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesCategorisedAccountAccountRef
    An object containing account reference data.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesCategorisedAccountModifiedDate:
    detail_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailType') }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    subtype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subtype') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesCategorisedAccount:
    account_ref: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesCategorisedAccountAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef') }})
    confirmed: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesCategorisedAccountModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('confirmed') }})
    suggested: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesCategorisedAccountModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('suggested') }})
    

@dataclasses.dataclass
class PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    categorised_account: Optional[PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesCategorisedAccount] = dataclasses.field(default=None)
    