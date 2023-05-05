"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .company_info import CompanyInfo
from .customers import Customers
from .disputes import Disputes
from .locations import Locations
from .orders import Orders
from .payments import Payments
from .products import Products
from .tax_components import TaxComponents
from .transactions import Transactions
from codatcommerce.models import shared

SERVERS = [
    "https://api.codat.io",
    r"""Production"""
]
"""Contains the list of servers available to the SDK"""

class CodatCommerce:
    r"""Codat's standardized API for accessing commerce data
    Codat's Commerce API allows you to access standardised data from over 11 commerce and POS systems.
    
    Standardize how you connect to your customers’ payment, PoS, and eCommerce systems. Retrieve orders, payouts, payments, and product data in the same way for all the leading commerce platforms.
    
    [Read more...](https://docs.codat.io/commerce-api/overview)
    
    [See our OpenAPI spec](https://github.com/codatio/oas)
    """
    company_info: CompanyInfo
    r"""Retrieve standardized data from linked commerce platforms."""
    customers: Customers
    r"""Retrieve standardized data from linked commerce platforms."""
    disputes: Disputes
    r"""Retrieve standardized data from linked commerce platforms."""
    locations: Locations
    r"""Retrieve standardized data from linked commerce platforms."""
    orders: Orders
    r"""Retrieve standardized data from linked commerce platforms."""
    payments: Payments
    r"""Retrieve standardized data from linked commerce platforms."""
    products: Products
    r"""Retrieve standardized data from linked commerce platforms."""
    tax_components: TaxComponents
    r"""Retrieve standardized data from linked commerce platforms."""
    transactions: Transactions
    r"""Retrieve standardized data from linked commerce platforms."""

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.16.0"
    _gen_version: str = "2.26.0"

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
        self.company_info = CompanyInfo(
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
        
        self.disputes = Disputes(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.locations = Locations(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.orders = Orders(
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
        
        self.products = Products(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.tax_components = TaxComponents(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.transactions = Transactions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    