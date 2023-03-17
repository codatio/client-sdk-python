__doc__ = """ SDK Documentation: A flexible API for pulling accounting data, normalized and aggregated from 20 accounting integrations.

Standardize how you connect to your customers’ accounting software. View, create, update, and delete data in the same way for all the leading accounting platforms.

[Read more...](https://docs.codat.io/accounting-api/overview)

[See our OpenAPI spec](https://github.com/codatio/oas)    """
import requests as requests_http
from . import utils
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
from .financials import Financials
from .invoices import Invoices
from .items import Items
from .journal_entries import JournalEntries
from .journals import Journals
from .payment_methods import PaymentMethods
from .payments import Payments
from .purchase_orders import PurchaseOrders
from .reports import Reports
from .sales_orders import SalesOrders
from .suppliers import Suppliers
from .tax_rates import TaxRates
from .tracking_categories import TrackingCategories
from .transfers import Transfers
from codat.models import shared

SERVERS = [
	"https://api.codat.io",
]

class Codat:
    r"""SDK Documentation: A flexible API for pulling accounting data, normalized and aggregated from 20 accounting integrations.
    
    Standardize how you connect to your customers’ accounting software. View, create, update, and delete data in the same way for all the leading accounting platforms.
    
    [Read more...](https://docs.codat.io/accounting-api/overview)
    
    [See our OpenAPI spec](https://github.com/codatio/oas)    """
    account_transactions: AccountTransactions
    accounts: Accounts
    bank_account_transactions: BankAccountTransactions
    bank_accounts: BankAccounts
    bill_credit_notes: BillCreditNotes
    bill_payments: BillPayments
    bills: Bills
    company_info: CompanyInfo
    credit_notes: CreditNotes
    customers: Customers
    direct_costs: DirectCosts
    direct_incomes: DirectIncomes
    financials: Financials
    invoices: Invoices
    items: Items
    journal_entries: JournalEntries
    journals: Journals
    payment_methods: PaymentMethods
    payments: Payments
    purchase_orders: PurchaseOrders
    reports: Reports
    sales_orders: SalesOrders
    suppliers: Suppliers
    tax_rates: TaxRates
    tracking_categories: TrackingCategories
    transfers: Transfers
    
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.5.1"
    _gen_version: str = "1.12.1"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = utils.configure_security_client(self._client, security)
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.account_transactions = AccountTransactions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.accounts = Accounts(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.bank_account_transactions = BankAccountTransactions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.bank_accounts = BankAccounts(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.bill_credit_notes = BillCreditNotes(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.bill_payments = BillPayments(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.bills = Bills(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.company_info = CompanyInfo(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.credit_notes = CreditNotes(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.customers = Customers(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.direct_costs = DirectCosts(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.direct_incomes = DirectIncomes(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.financials = Financials(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.invoices = Invoices(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.items = Items(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.journal_entries = JournalEntries(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.journals = Journals(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.payment_methods = PaymentMethods(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.payments = Payments(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.purchase_orders = PurchaseOrders(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.reports = Reports(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.sales_orders = SalesOrders(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.suppliers = Suppliers(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.tax_rates = TaxRates(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.tracking_categories = TrackingCategories(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.transfers = Transfers(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    