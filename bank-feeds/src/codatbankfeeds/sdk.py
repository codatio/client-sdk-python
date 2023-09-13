"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .account_mapping import AccountMapping
from .companies import Companies
from .connections import Connections
from .sdkconfiguration import SDKConfiguration
from .source_accounts import SourceAccounts
from .transactions import Transactions
from codatbankfeeds import utils
from codatbankfeeds.models import shared

class CodatBankFeeds:
    r"""Bank Feeds API: Bank Feeds API enables your SMB users to set up bank feeds from accounts in your application to supported accounting platforms.

    A bank feed is a connection between a source bank account in your application and a target bank account in a supported accounting package.

    [Explore product](https://docs.codat.io/bank-feeds-api/overview) | [See OpenAPI spec](https://github.com/codatio/oas)

    ---

    ## Endpoints

    | Endpoints | Description |
    | :- | :- |
    | Companies | Create and manage your SMB users' companies. |
    | Connections | Create new and manage existing data connections for a company. |
    | Source accounts | Provide and manage lists of source bank accounts.   |
    | Transactions | Create new bank account transactions for a company's connections, and see previous operations. |
    | Account mapping | Extra functionality for building an account management UI |
    """
    account_mapping: AccountMapping
    r"""Bank feed bank account mapping."""
    companies: Companies
    r"""Create and manage your Codat companies."""
    connections: Connections
    r"""Manage your companies' data connections."""
    source_accounts: SourceAccounts
    r"""Source accounts act as a bridge to bank accounts in accounting software."""
    transactions: Transactions
    r"""Transactions represent debits and credits from a source account."""

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
        self.account_mapping = AccountMapping(self.sdk_configuration)
        self.companies = Companies(self.sdk_configuration)
        self.connections = Connections(self.sdk_configuration)
        self.source_accounts = SourceAccounts(self.sdk_configuration)
        self.transactions = Transactions(self.sdk_configuration)
    