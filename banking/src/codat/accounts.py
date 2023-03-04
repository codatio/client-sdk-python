import requests
from . import utils
from codat.models import operations
from typing import Optional

class Accounts:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def get_banking_account(self, request: operations.GetBankingAccountRequest) -> operations.GetBankingAccountResponse:
        r"""Get account
        Gets a specified bank account for a given company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/connections/{connectionId}/data/banking-accounts/{accountId}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBankingAccountResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetBankingAccountSourceModifiedDate])
                res.source_modified_date = out

        return res

    def list_banking_accounts(self, request: operations.ListBankingAccountsRequest) -> operations.ListBankingAccountsResponse:
        r"""List accounts
        Gets a list of all bank accounts of the SMB, with rich data like balances, account numbers and institutions holdingthe accounts.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/connections/{connectionId}/data/banking-accounts', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListBankingAccountsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListBankingAccountsLinks])
                res.links = out

        return res

    