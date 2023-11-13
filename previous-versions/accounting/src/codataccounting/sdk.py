"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .account_transactions import AccountTransactions
from .accounts import Accounts
from .bank_account_transactions import BankAccountTransactions
from .bank_accounts import BankAccounts
from .bill_credit_notes import BillCreditNotes
from .bill_payments import BillPayments
from .bills import Bills
from .company_info import CompanyInfo
from .credit_notes import CreditNotes
from .customers import Customers
from .direct_costs import DirectCosts
from .direct_incomes import DirectIncomes
from .invoices import Invoices
from .items import Items
from .journal_entries import JournalEntries
from .journals import Journals
from .payment_methods import PaymentMethods
from .payments import Payments
from .purchase_orders import PurchaseOrders
from .reports import Reports
from .sales_orders import SalesOrders
from .sdkconfiguration import SDKConfiguration
from .suppliers import Suppliers
from .tax_rates import TaxRates
from .tracking_categories import TrackingCategories
from .transfers import Transfers
from codataccounting import utils
from codataccounting.models import shared
from typing import Callable, Dict, Union

class CodatAccounting:
    r"""Accounting API: A flexible API for pulling accounting data, normalized and aggregated from 20 accounting integrations.

    Standardize how you connect to your customers’ accounting software. View, create, update, and delete data in the same way for all the leading accounting platforms.

    [Read more...](https://docs.codat.io/accounting-api/overview)

    [See our OpenAPI spec](https://github.com/codatio/oas)
    """
    account_transactions: AccountTransactions
    r"""Account transactions"""
    bank_accounts: BankAccounts
    r"""Bank accounts"""
    bank_account_transactions: BankAccountTransactions
    r"""Bank transactions for bank accounts"""
    bills: Bills
    r"""Bills"""
    customers: Customers
    r"""Customers"""
    direct_costs: DirectCosts
    r"""Direct costs"""
    direct_incomes: DirectIncomes
    r"""Direct incomes"""
    invoices: Invoices
    r"""Invoices"""
    purchase_orders: PurchaseOrders
    r"""Purchase orders"""
    suppliers: Suppliers
    r"""Suppliers"""
    transfers: Transfers
    r"""Transfers"""
    bill_credit_notes: BillCreditNotes
    r"""Bill credit notes"""
    bill_payments: BillPayments
    r"""Bill payments"""
    accounts: Accounts
    r"""Accounts"""
    credit_notes: CreditNotes
    r"""Credit notes"""
    items: Items
    r"""Items"""
    journal_entries: JournalEntries
    r"""Journal entries"""
    journals: Journals
    r"""Journals"""
    payments: Payments
    r"""Payments"""
    reports: Reports
    r"""Reports"""
    company_info: CompanyInfo
    r"""Company info"""
    payment_methods: PaymentMethods
    r"""Payment methods"""
    sales_orders: SalesOrders
    r"""Sales orders"""
    tax_rates: TaxRates
    r"""Tax rates"""
    tracking_categories: TrackingCategories
    r"""Tracking categories"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: Union[shared.Security,Callable[[], shared.Security]] = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: Union[shared.Security,Callable[[], shared.Security]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.account_transactions = AccountTransactions(self.sdk_configuration)
        self.bank_accounts = BankAccounts(self.sdk_configuration)
        self.bank_account_transactions = BankAccountTransactions(self.sdk_configuration)
        self.bills = Bills(self.sdk_configuration)
        self.customers = Customers(self.sdk_configuration)
        self.direct_costs = DirectCosts(self.sdk_configuration)
        self.direct_incomes = DirectIncomes(self.sdk_configuration)
        self.invoices = Invoices(self.sdk_configuration)
        self.purchase_orders = PurchaseOrders(self.sdk_configuration)
        self.suppliers = Suppliers(self.sdk_configuration)
        self.transfers = Transfers(self.sdk_configuration)
        self.bill_credit_notes = BillCreditNotes(self.sdk_configuration)
        self.bill_payments = BillPayments(self.sdk_configuration)
        self.accounts = Accounts(self.sdk_configuration)
        self.credit_notes = CreditNotes(self.sdk_configuration)
        self.items = Items(self.sdk_configuration)
        self.journal_entries = JournalEntries(self.sdk_configuration)
        self.journals = Journals(self.sdk_configuration)
        self.payments = Payments(self.sdk_configuration)
        self.reports = Reports(self.sdk_configuration)
        self.company_info = CompanyInfo(self.sdk_configuration)
        self.payment_methods = PaymentMethods(self.sdk_configuration)
        self.sales_orders = SalesOrders(self.sdk_configuration)
        self.tax_rates = TaxRates(self.sdk_configuration)
        self.tracking_categories = TrackingCategories(self.sdk_configuration)
    