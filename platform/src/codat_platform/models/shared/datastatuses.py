"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .datastatus import DataStatus, DataStatusTypedDict
from codat_platform.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DataStatusesTypedDict(TypedDict):
    account_transactions: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    balance_sheet: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    bank_accounts: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    bank_transactions: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    banking_account_balances: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    banking_accounts: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    banking_transaction_categories: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    banking_transactions: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    bill_credit_notes: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    bill_payments: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    bills: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    cash_flow_statement: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    chart_of_accounts: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    commerce_company_info: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    commerce_customers: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    commerce_disputes: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    commerce_locations: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    commerce_orders: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    commerce_payment_methods: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    commerce_payments: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    commerce_product_categories: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    commerce_products: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    commerce_tax_components: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    commerce_transactions: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    company: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    credit_notes: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    customers: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    direct_costs: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    direct_incomes: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    invoices: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    item_receipts: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    items: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    journal_entries: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    journals: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    payment_methods: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    payments: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    profit_and_loss: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    purchase_orders: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    sales_orders: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    suppliers: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    tax_rates: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    tracking_categories: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""
    transfers: NotRequired[DataStatusTypedDict]
    r"""Describes the state of data in the Codat cache for a company and data type"""


class DataStatuses(BaseModel):
    account_transactions: Annotated[
        Optional[DataStatus], pydantic.Field(alias="accountTransactions")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    balance_sheet: Annotated[
        Optional[DataStatus], pydantic.Field(alias="balanceSheet")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    bank_accounts: Annotated[
        Optional[DataStatus], pydantic.Field(alias="bankAccounts")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    bank_transactions: Annotated[
        Optional[DataStatus], pydantic.Field(alias="bankTransactions")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    banking_account_balances: Annotated[
        Optional[DataStatus], pydantic.Field(alias="banking-accountBalances")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    banking_accounts: Annotated[
        Optional[DataStatus], pydantic.Field(alias="banking-accounts")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    banking_transaction_categories: Annotated[
        Optional[DataStatus], pydantic.Field(alias="banking-transactionCategories")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    banking_transactions: Annotated[
        Optional[DataStatus], pydantic.Field(alias="banking-transactions")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    bill_credit_notes: Annotated[
        Optional[DataStatus], pydantic.Field(alias="billCreditNotes")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    bill_payments: Annotated[
        Optional[DataStatus], pydantic.Field(alias="billPayments")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    bills: Optional[DataStatus] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    cash_flow_statement: Annotated[
        Optional[DataStatus], pydantic.Field(alias="cashFlowStatement")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    chart_of_accounts: Annotated[
        Optional[DataStatus], pydantic.Field(alias="chartOfAccounts")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    commerce_company_info: Annotated[
        Optional[DataStatus], pydantic.Field(alias="commerce-companyInfo")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    commerce_customers: Annotated[
        Optional[DataStatus], pydantic.Field(alias="commerce-customers")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    commerce_disputes: Annotated[
        Optional[DataStatus], pydantic.Field(alias="commerce-disputes")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    commerce_locations: Annotated[
        Optional[DataStatus], pydantic.Field(alias="commerce-locations")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    commerce_orders: Annotated[
        Optional[DataStatus], pydantic.Field(alias="commerce-orders")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    commerce_payment_methods: Annotated[
        Optional[DataStatus], pydantic.Field(alias="commerce-paymentMethods")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    commerce_payments: Annotated[
        Optional[DataStatus], pydantic.Field(alias="commerce-payments")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    commerce_product_categories: Annotated[
        Optional[DataStatus], pydantic.Field(alias="commerce-productCategories")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    commerce_products: Annotated[
        Optional[DataStatus], pydantic.Field(alias="commerce-products")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    commerce_tax_components: Annotated[
        Optional[DataStatus], pydantic.Field(alias="commerce-taxComponents")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    commerce_transactions: Annotated[
        Optional[DataStatus], pydantic.Field(alias="commerce-transactions")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    company: Optional[DataStatus] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    credit_notes: Annotated[
        Optional[DataStatus], pydantic.Field(alias="creditNotes")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    customers: Optional[DataStatus] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    direct_costs: Annotated[
        Optional[DataStatus], pydantic.Field(alias="directCosts")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    direct_incomes: Annotated[
        Optional[DataStatus], pydantic.Field(alias="directIncomes")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    invoices: Optional[DataStatus] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    item_receipts: Annotated[
        Optional[DataStatus], pydantic.Field(alias="itemReceipts")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    items: Optional[DataStatus] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    journal_entries: Annotated[
        Optional[DataStatus], pydantic.Field(alias="journalEntries")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    journals: Optional[DataStatus] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    payment_methods: Annotated[
        Optional[DataStatus], pydantic.Field(alias="paymentMethods")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    payments: Optional[DataStatus] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    profit_and_loss: Annotated[
        Optional[DataStatus], pydantic.Field(alias="profitAndLoss")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    purchase_orders: Annotated[
        Optional[DataStatus], pydantic.Field(alias="purchaseOrders")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    sales_orders: Annotated[
        Optional[DataStatus], pydantic.Field(alias="salesOrders")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    suppliers: Optional[DataStatus] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    tax_rates: Annotated[Optional[DataStatus], pydantic.Field(alias="taxRates")] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    tracking_categories: Annotated[
        Optional[DataStatus], pydantic.Field(alias="trackingCategories")
    ] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""

    transfers: Optional[DataStatus] = None
    r"""Describes the state of data in the Codat cache for a company and data type"""
