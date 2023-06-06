"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from codatbanking import utils
from codatbanking.models import operations, shared
from typing import Optional

class Accounts:
    r"""Where payments are made or received, and bank transactions are recorded."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def get(self, request: operations.GetAccountRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetAccountResponse:
        r"""Get account
        Gets a specified bank account for a given company
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAccountRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/banking-accounts/{accountId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAccountResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Account])
                res.account = out

        return res

    
    def list(self, request: operations.ListAccountsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListAccountsResponse:
        r"""List accounts
        Gets a list of all bank accounts of the SMB, with rich data like balances, account numbers and institutions holdingthe accounts.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListAccountsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/banking-accounts', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListAccountsRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url, params=query_params, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAccountsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Accounts])
                res.accounts = out
        elif http_res.status_code in [400, 401, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Schema])
                res.schema = out
        elif http_res.status_code == 409:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListAccounts409ApplicationJSON])
                res.list_accounts_409_application_json_object = out

        return res

    