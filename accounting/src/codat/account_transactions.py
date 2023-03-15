import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class AccountTransactions:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def get_create_update_account_transactions_model(self, request: operations.GetCreateUpdateAccountTransactionsModelRequest) -> operations.GetCreateUpdateAccountTransactionsModelResponse:
        r"""Get account transaction
        Get create/update account transactions model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCreateUpdateAccountTransactionsModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/accountTransactions/{accountTransactionId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCreateUpdateAccountTransactionsModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCreateUpdateAccountTransactionsModelSourceModifiedDate])
                res.source_modified_date = out

        return res

    def list_account_transactions(self, request: operations.ListAccountTransactionsRequest) -> operations.ListAccountTransactionsResponse:
        r"""List account transactions
        Gets the account transactions for a given company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListAccountTransactionsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/accountTransactions', request)
        
        query_params = utils.get_query_params(operations.ListAccountTransactionsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAccountTransactionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListAccountTransactionsLinks])
                res.links = out

        return res

    