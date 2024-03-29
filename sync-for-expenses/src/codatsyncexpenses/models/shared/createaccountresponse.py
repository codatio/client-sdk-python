"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accountstatus import AccountStatus
from .accounttype import AccountType
from .datatype import DataType
from .pushoperationchange import PushOperationChange
from .pushoperationstatus import PushOperationStatus
from .supplementaldata import SupplementalData
from .validation import Validation
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateAccountResponseMetadata:
    UNSET='__SPEAKEASY_UNSET__'
    is_deleted: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDeleted'), 'exclude': lambda f: f is CreateAccountResponseMetadata.UNSET }})
    r"""Indicates whether the record has been deleted in the third-party system this record originated from."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateAccountResponseValidDataTypeLinks:
    r"""When querying Codat's data model, some data types return `validDatatypeLinks` metadata in the JSON response. This indicates where that object can be used as a reference—a _valid link_—when creating or updating other data.

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
    UNSET='__SPEAKEASY_UNSET__'
    links: Optional[List[str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('links'), 'exclude': lambda f: f is CreateAccountResponseValidDataTypeLinks.UNSET }})
    r"""Supported `dataTypes` that the record can be linked to."""
    property: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('property'), 'exclude': lambda f: f is CreateAccountResponseValidDataTypeLinks.UNSET }})
    r"""The property from the account that can be linked."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountingAccount:
    r"""> **Language tip:** Accounts are also referred to as **chart of accounts**, **nominal accounts**, and **general ledger**.

    View the coverage for accounts in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    Accounts are the categories a business uses to record accounting transactions. From the Accounts endpoints, you can retrieve a list of all accounts for a specified company.

    The categories for an account include:
    * Asset
    * Expense
    * Income
    * Liability
    * Equity.

    The same account may have a different category based on the integration it is used in. For example, a current account (known as checking in the US) should be categorized as `Asset.Current` for Xero, and `Asset.Bank.Checking` for QuickBooks Online.

    At the same time, each integration may have its own requirements to the categories. For example, a Paypal account in Xero is of the `Asset.Bank` category and therefore requires additional properties to be provided.

    To determine the list of allowed categories for a specific integration, you can:
    - Follow our [Create, update, delete data](https://docs.codat.io/using-the-api/push) guide and use the [Get create account model](https://docs.codat.io/sync-for-expenses-api#/operations/get-create-chartOfAccounts-model).
    - Refer to the integration's own documentation.

    > **Accounts with no category**
    >
    > If an account is pulled from the chart of accounts and its nominal code does not lie within the category layout for the company's accounts, then the **type** is `Unknown`. The **fullyQualifiedCategory** and **fullyQualifiedName** fields return `null`.
    >
    > This approach gives a true representation of the company's accounts whilst preventing distorting financials such as a company's profit and loss and balance sheet reports.

    Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    UNSET='__SPEAKEASY_UNSET__'
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction. 

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    current_balance: Optional[Decimal] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currentBalance'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is AccountingAccount.UNSET }})
    r"""Current balance in the account."""
    description: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is AccountingAccount.UNSET }})
    r"""Description for the account."""
    fully_qualified_category: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fullyQualifiedCategory'), 'exclude': lambda f: f is AccountingAccount.UNSET }})
    r"""Full category of the account.

    For example, `Liability.Current` or `Income.Revenue`. To determine a list of possible categories for each integration, see our examples, follow our [Create, update, delete data](https://docs.codat.io/using-the-api/push) guide, or refer to the integration's own documentation.
    """
    fully_qualified_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fullyQualifiedName'), 'exclude': lambda f: f is AccountingAccount.UNSET }})
    r"""Full name of the account, for example:
    - `Cash On Hand`
    - `Rents Held In Trust`
    - `Fixed Asset`
    """
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the account, unique for the company."""
    is_bank_account: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isBankAccount'), 'exclude': lambda f: f is None }})
    r"""Confirms whether the account is a bank account or not."""
    metadata: Optional[CreateAccountResponseMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is AccountingAccount.UNSET }})
    r"""Name of the account."""
    nominal_code: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nominalCode'), 'exclude': lambda f: f is AccountingAccount.UNSET }})
    r"""Reference given to each nominal account for a business. It ensures money is allocated to the correct account. This code isn't a unique identifier in the Codat system."""
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    status: Optional[AccountStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Status of the account"""
    supplemental_data: Optional[SupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplementalData'), 'exclude': lambda f: f is None }})
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting platform. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """
    type: Optional[AccountType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Type of account"""
    valid_datatype_links: Optional[List[CreateAccountResponseValidDataTypeLinks]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validDatatypeLinks'), 'exclude': lambda f: f is AccountingAccount.UNSET }})
    r"""The validDatatypeLinks can be used to determine whether an account can be correctly mapped to another object; for example, accounts with a `type` of `income` might only support being used on an Invoice and Direct Income. For more information, see [Valid Data Type Links](/sync-for-expenses-api#/schemas/ValidDataTypeLinks)."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateAccountResponse:
    UNSET='__SPEAKEASY_UNSET__'
    company_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyId') }})
    r"""Unique identifier for your SMB in Codat."""
    data_connection_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataConnectionKey') }})
    r"""Unique identifier for a company's data connection."""
    push_operation_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pushOperationKey') }})
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""
    requested_on_utc: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestedOnUtc') }})
    r"""In Codat's data model, dates and times are represented using the <a class=\\"external\\" href=\\"https://en.wikipedia.org/wiki/ISO_8601\\" target=\\"_blank\\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```



    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:

    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`

    > Time zones
    > 
    > Not all dates from Codat will contain information about time zones.  
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """
    status: PushOperationStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The current status of the push operation."""
    status_code: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode') }})
    r"""Push status code."""
    changes: Optional[List[PushOperationChange]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changes'), 'exclude': lambda f: f is CreateAccountResponse.UNSET }})
    r"""Contains a single entry that communicates which record has changed and the manner in which it changed."""
    completed_on_utc: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completedOnUtc'), 'exclude': lambda f: f is None }})
    r"""In Codat's data model, dates and times are represented using the <a class=\\"external\\" href=\\"https://en.wikipedia.org/wiki/ISO_8601\\" target=\\"_blank\\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```



    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:

    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`

    > Time zones
    > 
    > Not all dates from Codat will contain information about time zones.  
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """
    data: Optional[AccountingAccount] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is CreateAccountResponse.UNSET }})
    data_type: Optional[DataType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Available data types"""
    error_message: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage'), 'exclude': lambda f: f is CreateAccountResponse.UNSET }})
    r"""A message about the error."""
    timeout_in_minutes: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutInMinutes'), 'exclude': lambda f: f is CreateAccountResponse.UNSET }})
    r"""Number of minutes the push operation must complete within before it times out."""
    timeout_in_seconds: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutInSeconds'), 'exclude': lambda f: f is CreateAccountResponse.UNSET }})
    r"""Number of seconds the push operation must complete within before it times out.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    validation: Optional[Validation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""
    

