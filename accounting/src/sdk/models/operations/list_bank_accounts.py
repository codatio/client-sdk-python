import dataclasses
import dateutil.parser
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class ListBankAccountsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListBankAccountsQueryParams:
    page: float = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListBankAccountsSecurity:
    api_key: shared_security.SchemeAPIKey = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class ListBankAccountsRequest:
    path_params: ListBankAccountsPathParams = dataclasses.field()
    query_params: ListBankAccountsQueryParams = dataclasses.field()
    security: ListBankAccountsSecurity = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class ListBankAccountsLinksLinksCurrent:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json
@dataclasses.dataclass
class ListBankAccountsLinksLinksNext:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json
@dataclasses.dataclass
class ListBankAccountsLinksLinksPrevious:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json
@dataclasses.dataclass
class ListBankAccountsLinksLinksSelf:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json
@dataclasses.dataclass
class ListBankAccountsLinksLinks:
    current: ListBankAccountsLinksLinksCurrent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('current') }})
    self: ListBankAccountsLinksLinksSelf = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('self') }})
    next: Optional[ListBankAccountsLinksLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next') }})
    previous: Optional[ListBankAccountsLinksLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous') }})
    
class ListBankAccountsLinksSourceModifiedDateAccountTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    CREDIT = "Credit"
    DEBIT = "Debit"


@dataclass_json
@dataclasses.dataclass
class ListBankAccountsLinksSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted') }})
    

@dataclass_json
@dataclasses.dataclass
class ListBankAccountsLinksSourceModifiedDate:
    r"""ListBankAccountsLinksSourceModifiedDate
    > **Accessing Bank Accounts through Banking API**
    > 
    > This datatype was originally used for accessing bank account data both in accounting integrations and open banking aggregators. 
    > 
    > To view bank account data through the Banking API, please refer to the new datatype [here](https://docs.codat.io/banking-api#/schemas/Account)
    
    > View the coverage for bank accounts in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A list of bank accounts associated with a company and a specific [data connection](https://api.codat.io/swagger/index.html#/Connection/get_companies__companyId__connections__connectionId_).
    
    Bank accounts data includes:
    * The name and ID of the account in the accounting platform.
    * The currency and balance of the account.
    * The sort code and account number.
    """
    
    account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountName') }})
    account_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountNumber') }})
    account_type: Optional[ListBankAccountsLinksSourceModifiedDateAccountTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountType') }})
    available_balance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('availableBalance') }})
    balance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('balance') }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    i_ban: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('iBan') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    institution: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('institution') }})
    metadata: Optional[ListBankAccountsLinksSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata') }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode') }})
    overdraft_limit: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('overdraftLimit') }})
    sort_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sortCode') }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    

@dataclass_json
@dataclasses.dataclass
class ListBankAccountsLinks:
    r"""ListBankAccountsLinks
    Codat's Paging Model
    """
    
    links: ListBankAccountsLinksLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('_links') }})
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize') }})
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults') }})
    results: Optional[list[ListBankAccountsLinksSourceModifiedDate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    

@dataclasses.dataclass
class ListBankAccountsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    links: Optional[ListBankAccountsLinks] = dataclasses.field(default=None)
    