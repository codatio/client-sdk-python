"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .accounts import Accounts
from .companies import Companies
from .connections import Connections
from .journal_entries import JournalEntries
from .journals import Journals
from .manage_data import ManageData
from .sdkconfiguration import SDKConfiguration
from .tracking_categories import TrackingCategories
from codatsyncpayroll import utils
from codatsyncpayroll.models import errors, operations, shared
from typing import Optional

class CodatSyncPayroll:
    r"""Sync for Payroll: The API for Sync for Payroll.

    Sync for Payroll is an API and a set of supporting tools built to help integrate your customers' payroll data from their HR and payroll platforms into their accounting platforms and to support its reconciliation.

    [Read More...](https://docs.codat.io/payroll/overview)
    """
    accounts: Accounts
    r"""Accounts"""
    companies: Companies
    r"""Create and manage your Codat companies."""
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
        self.connections = Connections(self.sdk_configuration)
        self.journal_entries = JournalEntries(self.sdk_configuration)
        self.journals = Journals(self.sdk_configuration)
        self.manage_data = ManageData(self.sdk_configuration)
        self.tracking_categories = TrackingCategories(self.sdk_configuration)
    
    def get_accounting_profile(self, request: operations.GetAccountingProfileRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetAccountingProfileResponse:
        r"""Get company accounting profile
        Gets the latest basic info for a company.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAccountingProfileRequest, base_url, '/companies/{companyId}/data/info', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('GET', url, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAccountingProfileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAccountingProfileCompanyInformation])
                res.company_information = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 404, 409, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    