"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from codat_sync_for_payables_version_1 import utils
from codat_sync_for_payables_version_1._hooks import SDKHooks
from codat_sync_for_payables_version_1.accounts import Accounts
from codat_sync_for_payables_version_1.bank_accounts import BankAccounts
from codat_sync_for_payables_version_1.bill_credit_notes import BillCreditNotes
from codat_sync_for_payables_version_1.bill_payments import BillPayments
from codat_sync_for_payables_version_1.bills import Bills
from codat_sync_for_payables_version_1.companies import Companies
from codat_sync_for_payables_version_1.company_info import CompanyInfo
from codat_sync_for_payables_version_1.connections import Connections
from codat_sync_for_payables_version_1.journal_entries import JournalEntries
from codat_sync_for_payables_version_1.journals import Journals
from codat_sync_for_payables_version_1.manage_data import ManageData
from codat_sync_for_payables_version_1.models import shared
from codat_sync_for_payables_version_1.payment_methods import PaymentMethods
from codat_sync_for_payables_version_1.push_operations import PushOperations
from codat_sync_for_payables_version_1.suppliers import Suppliers
from codat_sync_for_payables_version_1.tax_rates import TaxRates
from codat_sync_for_payables_version_1.tracking_categories import TrackingCategories
from codat_sync_for_payables_version_1.types import OptionalNullable, UNSET
import httpx
from typing import Callable, Dict, Optional, Union


class CodatSyncPayables(BaseSDK):
    r"""Sync for Payables: The API for Sync for Payables.

    Sync for Payables is an API and a set of supporting tools built to help integrate with your customers' accounting software, and keep their supplier information, invoices, and payments in sync.

    [Explore product](https://docs.codat.io/payables/overview) | [See OpenAPI spec](https://github.com/codatio/oas)

    ---
    <!-- Start Codat Tags Table -->
    ## Endpoints

    | Endpoints | Description |
    | :- |:- |
    | Companies | Create and manage your SMB users' companies. |
    | Connections | Create new and manage existing data connections for a company. |
    | Accounts | Get, create, and update Accounts. |
    | Bank accounts | Get, create, and update Bank accounts. |
    | Bills | Get, create, and update Bills. |
    | Bill credit notes | Get, create, and update Bill credit notes. |
    | Bill payments | Get, create, and update Bill payments. |
    | Journals | Get, create, and update Journals. |
    | Journal entries | Get, create, and update Journal entries. |
    | Payment methods | Get, create, and update Payment methods. |
    | Suppliers | Get, create, and update Suppliers. |
    | Tax rates | Get, create, and update Tax rates. |
    | Tracking categories | Get, create, and update Tracking categories. |
    | Company info | View company profile from the source platform. |
    | Push operations | View historic push operations. |
    | Manage data | Control how data is retrieved from an integration. |
    <!-- End Codat Tags Table -->
    """

    companies: Companies
    r"""Create and manage your SMB users' companies."""
    connections: Connections
    r"""Create new and manage existing data connections for a company."""
    bills: Bills
    r"""Get, create, and update Bills."""
    bank_accounts: BankAccounts
    r"""Get, create, and update Bank accounts."""
    bill_credit_notes: BillCreditNotes
    r"""Get, create, and update Bill credit notes."""
    bill_payments: BillPayments
    r"""Get, create, and update Bill payments."""
    accounts: Accounts
    r"""Get, create, and update Accounts."""
    journal_entries: JournalEntries
    r"""Get, create, and update Journal entries."""
    journals: Journals
    r"""Get, create, and update Journals."""
    suppliers: Suppliers
    r"""Get, create, and update Suppliers."""
    manage_data: ManageData
    r"""Control how data is retrieved from an integration."""
    company_info: CompanyInfo
    r"""View company profile from the source platform."""
    payment_methods: PaymentMethods
    r"""Get, create, and update Payment methods."""
    tax_rates: TaxRates
    r"""Get, create, and update Tax rates."""
    tracking_categories: TrackingCategories
    r"""Get, create, and update Tracking categories."""
    push_operations: PushOperations
    r"""View historic push operations."""

    def __init__(
        self,
        security: Union[shared.Security, Callable[[], shared.Security]],
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param security: The security details required for authentication
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                async_client=async_client,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, self.sdk_configuration.client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self._init_sdks()

    def _init_sdks(self):
        self.companies = Companies(self.sdk_configuration)
        self.connections = Connections(self.sdk_configuration)
        self.bills = Bills(self.sdk_configuration)
        self.bank_accounts = BankAccounts(self.sdk_configuration)
        self.bill_credit_notes = BillCreditNotes(self.sdk_configuration)
        self.bill_payments = BillPayments(self.sdk_configuration)
        self.accounts = Accounts(self.sdk_configuration)
        self.journal_entries = JournalEntries(self.sdk_configuration)
        self.journals = Journals(self.sdk_configuration)
        self.suppliers = Suppliers(self.sdk_configuration)
        self.manage_data = ManageData(self.sdk_configuration)
        self.company_info = CompanyInfo(self.sdk_configuration)
        self.payment_methods = PaymentMethods(self.sdk_configuration)
        self.tax_rates = TaxRates(self.sdk_configuration)
        self.tracking_categories = TrackingCategories(self.sdk_configuration)
        self.push_operations = PushOperations(self.sdk_configuration)