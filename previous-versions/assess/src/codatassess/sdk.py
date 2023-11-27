"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .data_integrity import DataIntegrity
from .excel_reports import ExcelReports
from .reports import Reports
from .sdkconfiguration import SDKConfiguration
from codatassess import utils
from codatassess.models import shared
from typing import Callable, Dict, Union

class CodatAssess:
    r"""Assess API: Codat's financial insights API
    Check that you have enabled the [data types required by Assess](https://docs.codat.io/assess/get-started#prerequisites) for all of its features to work.  

    [Read more...](https://www.docs.codat.io/assess/)

    [See our OpenAPI spec](https://github.com/codatio/oas)
    """
    reports: Reports
    r"""Enriched reports and analyses of financial data"""
    data_integrity: DataIntegrity
    r"""Match mutable accounting data with immutable banking data to increase confidence in financial data"""
    excel_reports: ExcelReports
    r"""Downloadable reports"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 auth_header: Union[str,Callable[[], str]],
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param auth_header: The auth_header required for authentication
        :type auth_header: Union[str,Callable[[], str]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        security = shared.Security(auth_header = auth_header)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.reports = Reports(self.sdk_configuration)
        self.data_integrity = DataIntegrity(self.sdk_configuration)
        self.excel_reports = ExcelReports(self.sdk_configuration)
    