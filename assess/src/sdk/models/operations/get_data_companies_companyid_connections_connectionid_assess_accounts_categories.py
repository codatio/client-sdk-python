from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesQueryParams:
    page: float = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequest:
    path_params: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesPathParams = dataclasses.field()
    query_params: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksLinksCurrent:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksLinksNext:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksLinksPrevious:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksLinksSelf:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksLinks:
    current: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksLinksCurrent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('current') }})
    self: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksLinksSelf = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('self') }})
    next: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksCategorisedAccountAccountRef:
    r"""GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksCategorisedAccountAccountRef
    An object containing account reference data.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksCategorisedAccountModifiedDate:
    detail_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailType'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    subtype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subtype'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksCategorisedAccount:
    account_ref: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksCategorisedAccountAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    confirmed: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksCategorisedAccountModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('confirmed'), 'exclude': lambda f: f is None }})
    suggested: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksCategorisedAccountModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('suggested'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinks:
    r"""GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinks
    Codat's Paging Model
    """
    
    links: GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('_links') }})
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize') }})
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults') }})
    results: Optional[list[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinksCategorisedAccount]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    links: Optional[GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinks] = dataclasses.field(default=None)
    