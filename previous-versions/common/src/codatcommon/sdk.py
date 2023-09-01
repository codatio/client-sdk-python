"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .companies import Companies
from .connections import Connections
from .integrations import Integrations
from .push_data import PushData
from .refresh_data import RefreshData
from .sdkconfiguration import SDKConfiguration
from .settings import Settings
from .supplemental_data import SupplementalData
from .webhooks import Webhooks
from codatcommon import utils
from codatcommon.models import shared

class CodatCommon:
    r"""Common API: Common API
    An API for the common components of all of Codat's products.

    These end points cover creating and managing your companies, data connections, and integrations.

    [Read about the building blocks of Codat...](https://docs.codat.io/core-concepts/companies)

    [See our OpenAPI spec](https://github.com/codatio/oas)
    """
    companies: Companies
    r"""Create and manage your Codat companies."""
    connections: Connections
    r"""Manage your companies' data connections."""
    integrations: Integrations
    r"""View and manage your available integrations in Codat."""
    push_data: PushData
    r"""View push options and get push statuses."""
    refresh_data: RefreshData
    r"""Asynchronously retrieve data from an integration to refresh data in Codat."""
    settings: Settings
    r"""Manage your Codat instance."""
    supplemental_data: SupplementalData
    r"""View and configure supplemental data for supported data types."""
    webhooks: Webhooks
    r"""Manage webhooks, rules, and events."""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: shared.Security = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
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
        """
        if client is None:
            client = requests_http.Session()
        
        security_client = utils.configure_security_client(client, security)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.companies = Companies(self.sdk_configuration)
        self.connections = Connections(self.sdk_configuration)
        self.integrations = Integrations(self.sdk_configuration)
        self.push_data = PushData(self.sdk_configuration)
        self.refresh_data = RefreshData(self.sdk_configuration)
        self.settings = Settings(self.sdk_configuration)
        self.supplemental_data = SupplementalData(self.sdk_configuration)
        self.webhooks = Webhooks(self.sdk_configuration)
    