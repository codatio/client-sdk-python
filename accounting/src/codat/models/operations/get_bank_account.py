from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class GetBankAccountPathParams:
    account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetBankAccountSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetBankAccountRequest:
    path_params: GetBankAccountPathParams = dataclasses.field()
    security: GetBankAccountSecurity = dataclasses.field()
    
class GetBankAccountSourceModifiedDateAccountTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    CREDIT = "Credit"
    DEBIT = "Debit"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBankAccountSourceModifiedDate:
    r"""GetBankAccountSourceModifiedDate
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
    
    account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountName'), 'exclude': lambda f: f is None }})
    account_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountNumber'), 'exclude': lambda f: f is None }})
    account_type: Optional[GetBankAccountSourceModifiedDateAccountTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountType'), 'exclude': lambda f: f is None }})
    available_balance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('availableBalance'), 'exclude': lambda f: f is None }})
    balance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('balance'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    i_ban: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('iBan'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    institution: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('institution'), 'exclude': lambda f: f is None }})
    metadata: Optional[GetBankAccountSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    overdraft_limit: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('overdraftLimit'), 'exclude': lambda f: f is None }})
    sort_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sortCode'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetBankAccountResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    source_modified_date: Optional[GetBankAccountSourceModifiedDate] = dataclasses.field(default=None)
    