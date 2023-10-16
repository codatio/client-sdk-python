"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .advanced_controls import AdvancedControls
from .connections import Connections
from .integrations import Integrations
from .sdkconfiguration import SDKConfiguration
from .sync import Sync
from .sync_flow_settings import SyncFlowSettings
from codatsynccommerce import utils
from codatsynccommerce.models import shared

class CodatSyncCommerce:
    r"""Sync for Commerce: The API for Sync for Commerce.

    Sync for Commerce automatically replicates and reconciles sales data from a merchant’s source PoS, Payments, and eCommerce systems into their accounting software. This eliminates manual processing by merchants and transforms their ability to run and grow their business.

    [Read More...](https://docs.codat.io/commerce/overview)

    Not seeing the endpoints you're expecting? We've [reorganized our products](https://docs.codat.io/updates/230901-new-products), and you may be using a [different version of Sync for Commerce](https://docs.codat.io/sync-for-commerce-v1-api#/).
    """
    advanced_controls: AdvancedControls
    r"""Advanced company management and sync preferences."""
    connections: Connections
    r"""Create new and manage existing Sync for Commerce connections using the Sync flow UI."""
    integrations: Integrations
    r"""View useful information about codat's integrations."""
    sync: Sync
    r"""Initiate and monitor the sync of company data into accounting software."""
    sync_flow_settings: SyncFlowSettings
    r"""Configure preferences for any given Sync for Commerce company using sync flow."""

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
        self.advanced_controls = AdvancedControls(self.sdk_configuration)
        self.connections = Connections(self.sdk_configuration)
        self.integrations = Integrations(self.sdk_configuration)
        self.sync = Sync(self.sdk_configuration)
        self.sync_flow_settings = SyncFlowSettings(self.sdk_configuration)
    