from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class ListBankingAccountBalancesPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListBankingAccountBalancesQueryParams:
    page: float = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListBankingAccountBalancesSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class ListBankingAccountBalancesRequest:
    path_params: ListBankingAccountBalancesPathParams = dataclasses.field()
    query_params: ListBankingAccountBalancesQueryParams = dataclasses.field()
    security: ListBankingAccountBalancesSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankingAccountBalancesLinksLinksCurrent:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankingAccountBalancesLinksLinksNext:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankingAccountBalancesLinksLinksPrevious:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankingAccountBalancesLinksLinksSelf:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankingAccountBalancesLinksLinks:
    current: ListBankingAccountBalancesLinksLinksCurrent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('current') }})
    self: ListBankingAccountBalancesLinksLinksSelf = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('self') }})
    next: Optional[ListBankingAccountBalancesLinksLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[ListBankingAccountBalancesLinksLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankingAccountBalancesLinksSourceModifiedDateBalance:
    r"""ListBankingAccountBalancesLinksSourceModifiedDateBalance
    An object containing bank balance data.
    """
    
    current: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('current') }})
    available: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('available'), 'exclude': lambda f: f is None }})
    limit: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('limit'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankingAccountBalancesLinksSourceModifiedDate:
    r"""ListBankingAccountBalancesLinksSourceModifiedDate
    The Banking Account Balances data type provides a list of balances for a bank account including end-of-day batch balance or running balances per transaction.
    """
    
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId') }})
    balance: ListBankingAccountBalancesLinksSourceModifiedDateBalance = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('balance') }})
    date_: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankingAccountBalancesLinks:
    r"""ListBankingAccountBalancesLinks
    Codat's Paging Model
    """
    
    links: ListBankingAccountBalancesLinksLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('_links') }})
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize') }})
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults') }})
    results: Optional[ListBankingAccountBalancesLinksSourceModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ListBankingAccountBalancesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    links: Optional[ListBankingAccountBalancesLinks] = dataclasses.field(default=None)
    