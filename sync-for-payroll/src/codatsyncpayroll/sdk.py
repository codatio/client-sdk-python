"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .accounts import Accounts
from .companies import Companies
from .company_info import CompanyInfo
from .connections import Connections
from .journal_entries import JournalEntries
from .journals import Journals
from .manage_data import ManageData
from .sdkconfiguration import SDKConfiguration
from .tracking_categories import TrackingCategories
from codatsyncpayroll import utils
from codatsyncpayroll.models import shared

class CodatSyncPayroll:
    r"""Sync for Payroll: The API for Sync for Payroll.

    Sync for Payroll is an API and a set of supporting tools built to help integrate your customers' payroll data from their HR and payroll platforms into their accounting platforms and to support its reconciliation.

    [Explore product](https://docs.codat.io/payroll/overview) | [See OpenAPI spec](https://github.com/codatio/oas)

    ---

    ## Endpoints

    | Endpoints            | Description                                                                                                |
    |:---------------------|:-----------------------------------------------------------------------------------------------------------|
    | Companies            | Create and manage your SMB users' companies.                                                               |
    | Connections          | Create new and manage existing data connections for a company.                                             |
    | Accounts             | Get, create, and update Accounts.                                                           |
    | Journal entries      | Get, create, and update Journal entries.                                                           |
    | Journals             | Get, create, and update Journals.                                                           |
    | Tracking categories  | Get, create, and update Tracking Categories for additional categorization of payroll components.                                                           |
    | Company info         | View company profile from the source platform.                                                             |
    | Manage data          | Control how data is retrieved from an integration.                                                         |
    """
    accounts: Accounts
    r"""Accounts"""
    companies: Companies
    r"""Create and manage your Codat companies."""
    company_info: CompanyInfo
    r"""View company information fetched from the source platform."""
    connections: Connections
    r"""Manage your companies' data connections."""
    journal_entries: JournalEntries
    r"""Journal entries"""
    journals: Journals
    r"""Journals"""
    manage_data: ManageData
    r"""Asynchronously retrieve data from an integration to refresh data in Codat."""
    tracking_categories: TrackingCategories
    r"""Tracking categories"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: shared.Security = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        security_client = utils.configure_security_client(client, security)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.accounts = Accounts(self.sdk_configuration)
        self.companies = Companies(self.sdk_configuration)
        self.company_info = CompanyInfo(self.sdk_configuration)
        self.connections = Connections(self.sdk_configuration)
        self.journal_entries = JournalEntries(self.sdk_configuration)
        self.journals = Journals(self.sdk_configuration)
        self.manage_data = ManageData(self.sdk_configuration)
        self.tracking_categories = TrackingCategories(self.sdk_configuration)
    