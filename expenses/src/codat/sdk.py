__doc__ = """ SDK Documentation: The API for Sync for Expenses.
Sync for Expenses is an API and a set of supporting tools. It has been built to enable corporate card and expense management platforms to provide high-quality integrations with multiple accounting platforms through a standardized API.

[Read more...](https://docs.codat.io/sync-for-expenses/overview)

[See our OpenAPI spec](https://github.com/codatio/oas)"""
import requests as requests_http
from . import utils
from .configuration import Configuration
from .connections import Connections
from .expenses import Expenses
from .mapping_options import MappingOptions
from .sync import Sync
from .sync_status import SyncStatus
from .transaction_status import TransactionStatus
from codat.models import shared

SERVERS = [
	"https://api.codat.io",
]

class Codat:
    r"""SDK Documentation: The API for Sync for Expenses.
    Sync for Expenses is an API and a set of supporting tools. It has been built to enable corporate card and expense management platforms to provide high-quality integrations with multiple accounting platforms through a standardized API.
    
    [Read more...](https://docs.codat.io/sync-for-expenses/overview)
    
    [See our OpenAPI spec](https://github.com/codatio/oas)"""
    configuration: Configuration
    connections: Connections
    expenses: Expenses
    mapping_options: MappingOptions
    sync: Sync
    sync_status: SyncStatus
    transaction_status: TransactionStatus
    
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.5.0"
    _gen_version: str = "1.12.0"

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
        self.configuration = Configuration(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.connections = Connections(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.expenses = Expenses(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.mapping_options = MappingOptions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.sync = Sync(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.sync_status = SyncStatus(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.transaction_status = TransactionStatus(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    