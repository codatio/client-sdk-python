"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .companies import Companies
from .connections import Connections
from .data_status import DataStatus
from .integrations import Integrations
from .push_data import PushData
from .refresh_data import RefreshData
from .settings import Settings
from .webhooks import Webhooks
from codatcommon.models import shared

SERVERS = [
    "https://api.codat.io",
    r"""Production"""
]
"""Contains the list of servers available to the SDK"""

class CodatCommon:
    r"""Common API
    An API for the common components of all of Codat's products.
    
    These end points cover creating and managing your companies, data connections, and integrations.
    
    [Read about the building blocks of Codat...](https://docs.codat.io/core-concepts/companies)
    
    [See our OpenAPI spec](https://github.com/codatio/oas)
    """
    companies: Companies
    r"""Create and manage your Codat companies."""
    connections: Connections
    r"""Manage your companies' data connections."""
    data_status: DataStatus
    r"""Understand the state of data within Codat."""
    integrations: Integrations
    r"""View and manage your available integrations in Codat."""
    push_data: PushData
    r"""View push options and get push statuses."""
    refresh_data: RefreshData
    r"""Queue pull operations to refresh data in Codat."""
    settings: Settings
    r"""Manage your Codat instance."""
    webhooks: Webhooks
    r"""Manage webhooks, rules and alerts."""

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.10.0"
    _gen_version: str = "2.20.1"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
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
        self.companies = Companies(
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
        
        self.data_status = DataStatus(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.integrations = Integrations(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.push_data = PushData(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.refresh_data = RefreshData(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.settings = Settings(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.webhooks = Webhooks(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    