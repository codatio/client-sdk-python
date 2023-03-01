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
class GetAccountPathParams:
    account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetAccountSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetAccountRequest:
    path_params: GetAccountPathParams = dataclasses.field()
    security: GetAccountSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAccountSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    
class GetAccountSourceModifiedDateStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"
    PENDING = "Pending"

class GetAccountSourceModifiedDateTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    ASSET = "Asset"
    EXPENSE = "Expense"
    INCOME = "Income"
    LIABILITY = "Liability"
    EQUITY = "Equity"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAccountSourceModifiedDateValidDataTypeLinks:
    r"""GetAccountSourceModifiedDateValidDataTypeLinks
    When querying Codat's data model, some data types return `validDatatypeLinks` metadata in the JSON response. This indicates where that object can be used as a reference—a _valid link_—when creating or updating other data.
    
    For example, `validDatatypeLinks` might indicate the following references:
    
    - Which tax rates are valid to use on the line item of a bill.
    - Which items can be used when creating an invoice. 
    
    You can use `validDatatypeLinks` to present your SMB customers with only valid choices when selecting objects from a list, for example.
    
    ## `validDatatypeLinks` example
    
    The following example uses the `Accounting.Accounts` data type. It shows that, on the linked integration, this account is valid as the account on a payment or bill payment; and as the account referenced on the line item of a direct income or direct cost. Because there is no valid link to Invoices or Bills, using this account on those data types will result in an error.
    
    ```json validDatatypeLinks for an account
    {
                \"id\": \"bd9e85e0-0478-433d-ae9f-0b3c4f04bfe4\",
                \"nominalCode\": \"090\",
                \"name\": \"Business Bank Account\",
                #...
                \"validDatatypeLinks\": [
                    {
                        \"property\": \"Id\",
                        \"links\": [
                            \"Payment.AccountRef.Id\",
                            \"BillPayment.AccountRef.Id\",
                            \"DirectIncome.LineItems.AccountRef.Id\",
                            \"DirectCost.LineItems.AccountRef.Id\"
                        ]
                    }
                ]
            }
    ```
    
    
    
    ## Support for `validDatatypeLinks`
    
    Codat currently supports `validDatatypeLinks` for some data types on our Xero, QuickBooks Online, QuickBooks Desktop, Exact (NL), and Sage Business Cloud integrations. 
    
    If you'd like us to extend support to more data types or integrations, suggest or vote for this on our <a href=\"https://portal.productboard.com/codat/5-product-roadmap\">Product Roadmap</a>.
    """
    
    links: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('links'), 'exclude': lambda f: f is None }})
    property: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('property'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAccountSourceModifiedDate:
    r"""GetAccountSourceModifiedDate
    > **Language tip:** Accounts are also referred to as **chart of accounts**, **nominal accounts**, and **general ledger**.
    
    Explore the <a className=\"external\" href=\"https://api.codat.io/swagger/index.html#/Accounts\" target=\"_blank\">Accounts</a> endpoints in Swagger.
    
    View the coverage for accounts in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    Accounts are the categories a business uses to record accounting transactions. From the Accounts endpoints, you can retrieve [a list of all accounts for a specified company](https://api.codat.io/swagger/index.html#/Accounts/Accounts_List). 
    
    The categories for an account include:
      * Asset
      * Expense
      * Income
      * Liability
      * Equity.
    
    > **Accounts with no category**
    > 
    > If an account is pulled from the chart of accounts and its nominal code does not lie within the category layout for the company's accounts, then the **type** is `Unknown`. The **fullyQualifiedCategory** and **fullyQualifiedName** fields return `null`.
    > 
    > This approach gives a true representation of the company's accounts whilst preventing distorting financials such as a company's profit and loss and balance sheet reports.
    """
    
    is_bank_account: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isBankAccount') }})
    status: GetAccountSourceModifiedDateStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    type: GetAccountSourceModifiedDateTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    current_balance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currentBalance'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    fully_qualified_category: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fullyQualifiedCategory'), 'exclude': lambda f: f is None }})
    fully_qualified_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fullyQualifiedName'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    metadata: Optional[GetAccountSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    valid_datatype_links: Optional[list[GetAccountSourceModifiedDateValidDataTypeLinks]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validDatatypeLinks'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetAccountResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    source_modified_date: Optional[GetAccountSourceModifiedDate] = dataclasses.field(default=None)
    