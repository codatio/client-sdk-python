import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class TransactionStatus:
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
        
    def get_sync_transaction(self, request: operations.GetSyncTransactionRequest) -> operations.GetSyncTransactionResponse:
        r"""Get Sync Transaction
        Gets the status of a transaction for a sync
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetSyncTransactionRequest, base_url, '/companies/{companyId}/sync/expenses/syncs/{syncId}/transactions/{transactionId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSyncTransactionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[operations.GetSyncTransaction200ApplicationJSON]])
                res.get_sync_transaction_200_application_json_objects = out

        return res

    def get_sync_transactions(self, request: operations.GetSyncTransactionsRequest) -> operations.GetSyncTransactionsResponse:
        r"""Get Sync transactions
        Get's the transactions and status for a sync
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetSyncTransactionsRequest, base_url, '/companies/{companyId}/sync/expenses/syncs/{syncId}/transactions', request)
        
        query_params = utils.get_query_params(operations.GetSyncTransactionsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSyncTransactionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetSyncTransactions200ApplicationJSON])
                res.get_sync_transactions_200_application_json_object = out

        return res

    