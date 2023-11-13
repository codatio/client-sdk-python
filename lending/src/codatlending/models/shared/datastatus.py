"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DataTypes(str, Enum):
    r"""Available Data types"""
    ACCOUNT_TRANSACTIONS = 'accountTransactions'
    BALANCE_SHEET = 'balanceSheet'
    BANK_ACCOUNTS = 'bankAccounts'
    BANK_TRANSACTIONS = 'bankTransactions'
    BILL_CREDIT_NOTES = 'billCreditNotes'
    BILL_PAYMENTS = 'billPayments'
    BILLS = 'bills'
    CASH_FLOW_STATEMENT = 'cashFlowStatement'
    CHART_OF_ACCOUNTS = 'chartOfAccounts'
    COMPANY = 'company'
    CREDIT_NOTES = 'creditNotes'
    CUSTOMERS = 'customers'
    DIRECT_COSTS = 'directCosts'
    DIRECT_INCOMES = 'directIncomes'
    INVOICES = 'invoices'
    ITEMS = 'items'
    JOURNAL_ENTRIES = 'journalEntries'
    JOURNALS = 'journals'
    PAYMENT_METHODS = 'paymentMethods'
    PAYMENTS = 'payments'
    PROFIT_AND_LOSS = 'profitAndLoss'
    PURCHASE_ORDERS = 'purchaseOrders'
    SALES_ORDERS = 'salesOrders'
    SUPPLIERS = 'suppliers'
    TAX_RATES = 'taxRates'
    TRACKING_CATEGORIES = 'trackingCategories'
    TRANSFERS = 'transfers'
    BANKING_ACCOUNT_BALANCES = 'banking-accountBalances'
    BANKING_ACCOUNTS = 'banking-accounts'
    BANKING_TRANSACTION_CATEGORIES = 'banking-transactionCategories'
    BANKING_TRANSACTIONS = 'banking-transactions'
    COMMERCE_COMPANY_INFO = 'commerce-companyInfo'
    COMMERCE_CUSTOMERS = 'commerce-customers'
    COMMERCE_DISPUTES = 'commerce-disputes'
    COMMERCE_LOCATIONS = 'commerce-locations'
    COMMERCE_ORDERS = 'commerce-orders'
    COMMERCE_PAYMENT_METHODS = 'commerce-paymentMethods'
    COMMERCE_PAYMENTS = 'commerce-payments'
    COMMERCE_PRODUCT_CATEGORIES = 'commerce-productCategories'
    COMMERCE_PRODUCTS = 'commerce-products'
    COMMERCE_TAX_COMPONENTS = 'commerce-taxComponents'
    COMMERCE_TRANSACTIONS = 'commerce-transactions'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DataStatus:
    r"""Describes the state of data in the Codat cache for a company and data type"""
    current_status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currentStatus') }})
    r"""The current status of the dataset in Codat's cache."""
    data_type: DataTypes = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType') }})
    r"""Available Data types"""
    last_successful_sync: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastSuccessfulSync') }})
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
    latest_successful_sync_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('latestSuccessfulSyncId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for the most recent successful sync of data type."""
    latest_sync_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('latestSyncId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for most recent sync of data type."""
    

