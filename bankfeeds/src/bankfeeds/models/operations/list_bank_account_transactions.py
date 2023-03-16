from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from bankfeeds import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class ListBankAccountTransactionsRequest:
    account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    page: float = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankAccountTransactionsLinksLinksCurrent:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankAccountTransactionsLinksLinksNext:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankAccountTransactionsLinksLinksPrevious:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankAccountTransactionsLinksLinksSelf:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankAccountTransactionsLinksLinks:
    current: ListBankAccountTransactionsLinksLinksCurrent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current') }})
    self: ListBankAccountTransactionsLinksLinksSelf = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('self') }})
    next: Optional[ListBankAccountTransactionsLinksLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[ListBankAccountTransactionsLinksLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous'), 'exclude': lambda f: f is None }})
    
class ListBankAccountTransactionsLinksResultsTransactionsTransactionTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    CREDIT = "Credit"
    DEBIT = "Debit"
    INT = "Int"
    DIV = "Div"
    FEE = "Fee"
    SER_CHG = "SerChg"
    DEP = "Dep"
    ATM = "Atm"
    POS = "Pos"
    XFER = "Xfer"
    CHECK = "Check"
    PAYMENT = "Payment"
    CASH = "Cash"
    DIRECT_DEP = "DirectDep"
    DIRECT_DEBIT = "DirectDebit"
    REPEAT_PMT = "RepeatPmt"
    OTHER = "Other"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankAccountTransactionsLinksResultsTransactions:
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    balance: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balance') }})
    date_: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    reconciled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reconciled') }})
    transaction_type: ListBankAccountTransactionsLinksResultsTransactionsTransactionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactionType') }})
    counterparty: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('counterparty'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankAccountTransactionsLinksResults:
    r"""ListBankAccountTransactionsLinksResults
    > **Accessing Bank Accounts through Banking API**
    > 
    > This datatype was originally used for accessing bank account data both in accounting integrations and open banking aggregators. 
    >
    > To view bank account data through the Banking API, please refer to the new datatype [here](https://docs.codat.io/banking-api#/operations/list-all-banking-transactions)
    
    > View the coverage for bank transactions in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    Transactional banking data for a specific company and account.
    
    Bank transactions include the:
    * Amount of the transaction.
    * Current account balance.
    * Transaction type, for example, credit, debit, or transfer.
    """
    
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId'), 'exclude': lambda f: f is None }})
    contract_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contractVersion'), 'exclude': lambda f: f is None }})
    transactions: Optional[list[ListBankAccountTransactionsLinksResultsTransactions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankAccountTransactionsLinks:
    r"""ListBankAccountTransactionsLinks
    Codat's Paging Model
    """
    
    links: ListBankAccountTransactionsLinksLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_links') }})
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageNumber') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize') }})
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalResults') }})
    results: Optional[list[ListBankAccountTransactionsLinksResults]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ListBankAccountTransactionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    links: Optional[ListBankAccountTransactionsLinks] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    