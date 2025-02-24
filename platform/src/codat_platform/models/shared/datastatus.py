"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .status import Status
from codat_platform.types import BaseModel
from enum import Enum
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DataTypes(str, Enum):
    r"""Available data types"""

    ACCOUNT_TRANSACTIONS = "accountTransactions"
    BALANCE_SHEET = "balanceSheet"
    BANK_ACCOUNTS = "bankAccounts"
    BANK_TRANSACTIONS = "bankTransactions"
    BILL_CREDIT_NOTES = "billCreditNotes"
    BILL_PAYMENTS = "billPayments"
    BILLS = "bills"
    CASH_FLOW_STATEMENT = "cashFlowStatement"
    CHART_OF_ACCOUNTS = "chartOfAccounts"
    COMPANY = "company"
    CREDIT_NOTES = "creditNotes"
    CUSTOMERS = "customers"
    DIRECT_COSTS = "directCosts"
    DIRECT_INCOMES = "directIncomes"
    INVOICES = "invoices"
    ITEM_RECEIPTS = "itemReceipts"
    ITEMS = "items"
    JOURNAL_ENTRIES = "journalEntries"
    JOURNALS = "journals"
    PAYMENT_METHODS = "paymentMethods"
    PAYMENTS = "payments"
    PROFIT_AND_LOSS = "profitAndLoss"
    PURCHASE_ORDERS = "purchaseOrders"
    SALES_ORDERS = "salesOrders"
    SUPPLIERS = "suppliers"
    TAX_RATES = "taxRates"
    TRACKING_CATEGORIES = "trackingCategories"
    TRANSFERS = "transfers"
    BANKING_ACCOUNT_BALANCES = "banking-accountBalances"
    BANKING_ACCOUNTS = "banking-accounts"
    BANKING_TRANSACTION_CATEGORIES = "banking-transactionCategories"
    BANKING_TRANSACTIONS = "banking-transactions"
    COMMERCE_COMPANY_INFO = "commerce-companyInfo"
    COMMERCE_CUSTOMERS = "commerce-customers"
    COMMERCE_DISPUTES = "commerce-disputes"
    COMMERCE_LOCATIONS = "commerce-locations"
    COMMERCE_ORDERS = "commerce-orders"
    COMMERCE_PAYMENT_METHODS = "commerce-paymentMethods"
    COMMERCE_PAYMENTS = "commerce-payments"
    COMMERCE_PRODUCT_CATEGORIES = "commerce-productCategories"
    COMMERCE_PRODUCTS = "commerce-products"
    COMMERCE_TAX_COMPONENTS = "commerce-taxComponents"
    COMMERCE_TRANSACTIONS = "commerce-transactions"


class DataStatusTypedDict(TypedDict):
    r"""Describes the state of data in the Codat cache for a company and data type"""

    current_status: Status
    r"""The current status of the dataset."""
    data_type: DataTypes
    r"""Available data types"""
    last_successful_sync: str
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

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
    latest_successful_sync_id: NotRequired[str]
    r"""Unique identifier for the most recent successful sync of data type."""
    latest_sync_id: NotRequired[str]
    r"""Unique identifier for most recent sync of data type."""


class DataStatus(BaseModel):
    r"""Describes the state of data in the Codat cache for a company and data type"""

    current_status: Annotated[Status, pydantic.Field(alias="currentStatus")]
    r"""The current status of the dataset."""

    data_type: Annotated[DataTypes, pydantic.Field(alias="dataType")]
    r"""Available data types"""

    last_successful_sync: Annotated[str, pydantic.Field(alias="lastSuccessfulSync")]
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

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

    latest_successful_sync_id: Annotated[
        Optional[str], pydantic.Field(alias="latestSuccessfulSyncId")
    ] = None
    r"""Unique identifier for the most recent successful sync of data type."""

    latest_sync_id: Annotated[Optional[str], pydantic.Field(alias="latestSyncId")] = (
        None
    )
    r"""Unique identifier for most recent sync of data type."""
