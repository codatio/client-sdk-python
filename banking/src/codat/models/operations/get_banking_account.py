from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class GetBankingAccountRequest:
    account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankingAccountSourceModifiedDateAccountBalanceAmounts:
    r"""GetBankingAccountSourceModifiedDateAccountBalanceAmounts
    An object containing bank balance data.
    """
    
    available: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('available'), 'exclude': lambda f: f is None }})
    current: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current'), 'exclude': lambda f: f is None }})
    limit: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit'), 'exclude': lambda f: f is None }})
    
class GetBankingAccountSourceModifiedDateAccountIdentifiersTypeEnum(str, Enum):
    ACCOUNT = "Account"
    CARD = "Card"
    CREDIT = "Credit"
    DEPOSITORY = "Depository"
    INVESTMENT = "Investment"
    LOAN = "Loan"
    OTHER = "Other"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankingAccountSourceModifiedDateAccountIdentifiers:
    r"""GetBankingAccountSourceModifiedDateAccountIdentifiers
    An object containing bank account identification information.
    """
    
    type: GetBankingAccountSourceModifiedDateAccountIdentifiersTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    bank_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bankCode'), 'exclude': lambda f: f is None }})
    bic: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bic'), 'exclude': lambda f: f is None }})
    iban: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iban'), 'exclude': lambda f: f is None }})
    masked_account_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maskedAccountNumber'), 'exclude': lambda f: f is None }})
    number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number'), 'exclude': lambda f: f is None }})
    subtype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subtype'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankingAccountSourceModifiedDateAccountInstitution:
    r"""GetBankingAccountSourceModifiedDateAccountInstitution
    The bank or other financial institution providing the account.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    
class GetBankingAccountSourceModifiedDateTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    CREDIT = "Credit"
    DEBIT = "Debit"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankingAccountSourceModifiedDate:
    r"""GetBankingAccountSourceModifiedDate
    An account where payments are made or received, and bank transactions are recorded.
    
    Explore our [data coverage](https://knowledge.codat.io/supported-features/banking?view=tab-by-data-type&dataType=banking-accounts).
    """
    
    balance: GetBankingAccountSourceModifiedDateAccountBalanceAmounts = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balance') }})
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    identifiers: GetBankingAccountSourceModifiedDateAccountIdentifiers = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identifiers') }})
    institution: GetBankingAccountSourceModifiedDateAccountInstitution = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    type: GetBankingAccountSourceModifiedDateTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    holder: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('holder'), 'exclude': lambda f: f is None }})
    informal_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('informalName'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetBankingAccountResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    source_modified_date: Optional[GetBankingAccountSourceModifiedDate] = dataclasses.field(default=None)
    