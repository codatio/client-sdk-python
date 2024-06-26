"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .accounts import Accounts
from .attachments import Attachments
from .companies import Companies
from .configuration import Configuration
from .connections import Connections
from .customers import Customers
from .expenses import Expenses
from .manage_data import ManageData
from .push_operations import PushOperations
from .reimbursements import Reimbursements
from .sdkconfiguration import SDKConfiguration
from .suppliers import Suppliers
from .sync import Sync
from .transaction_status import TransactionStatus
from .transfers import Transfers
from .utils.retries import RetryConfig
from codatsyncexpenses import utils
from codatsyncexpenses._hooks import SDKHooks
from codatsyncexpenses.models import shared
from typing import Callable, Dict, Optional, Union

class CodatSyncExpenses:
    r"""Sync for Expenses: The API for Sync for Expenses.

    Sync for Expenses is an API and a set of supporting tools. It has been built to
    enable corporate card and expense management platforms to provide high-quality
    integrations with multiple accounting platforms through a standardized API.

    [Read more...](https://docs.codat.io/sync-for-expenses/overview)

    [See our OpenAPI spec](https://github.com/codatio/oas)

    Not seeing the endpoints you're expecting? We've [reorganized our products](https://docs.codat.io/updates/230901-new-products), and you may be using a [different version of Sync for Expenses](https://docs.codat.io/sync-for-expenses-v1-api#/).
    """
    companies: Companies
    r"""Create and manage your Codat companies."""
    connections: Connections
    r"""Create and manage partner expense connection."""
    accounts: Accounts
    r"""Accounts"""
    customers: Customers
    r"""Customers"""
    suppliers: Suppliers
    r"""Suppliers"""
    manage_data: ManageData
    r"""Asynchronously retrieve data from an integration to refresh data in Codat."""
    push_operations: PushOperations
    r"""Access create, update and delete operations made to an SMB's data connection."""
    configuration: Configuration
    r"""Manage mapping options and sync configuration."""
    expenses: Expenses
    r"""Create expense transactions."""
    reimbursements: Reimbursements
    r"""Create reimbursable expense transactions."""
    sync: Sync
    r"""Trigger and monitor expense syncs to accounting software."""
    transaction_status: TransactionStatus
    r"""Retrieve the status of transactions within a sync."""
    attachments: Attachments
    r"""Upload attachmens to expenses, transfers and reimbursable expense transactions."""
    transfers: Transfers
    r"""Create transfer transactions."""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: Union[shared.Security,Callable[[], shared.Security]] = None,
                 server_idx: Optional[int] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[RetryConfig] = None
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
        :type retry_config: RetryConfig
        """
        if client is None:
            client = requests_http.Session()

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
    

        self.sdk_configuration = SDKConfiguration(
            client,
            security,
            server_url,
            server_idx,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__['_hooks'] = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.companies = Companies(self.sdk_configuration)
        self.connections = Connections(self.sdk_configuration)
        self.accounts = Accounts(self.sdk_configuration)
        self.customers = Customers(self.sdk_configuration)
        self.suppliers = Suppliers(self.sdk_configuration)
        self.manage_data = ManageData(self.sdk_configuration)
        self.push_operations = PushOperations(self.sdk_configuration)
        self.configuration = Configuration(self.sdk_configuration)
        self.expenses = Expenses(self.sdk_configuration)
        self.reimbursements = Reimbursements(self.sdk_configuration)
        self.sync = Sync(self.sdk_configuration)
        self.transaction_status = TransactionStatus(self.sdk_configuration)
        self.attachments = Attachments(self.sdk_configuration)
        self.transfers = Transfers(self.sdk_configuration)
