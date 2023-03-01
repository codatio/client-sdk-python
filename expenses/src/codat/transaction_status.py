import requests
from . import utils
from codat.models import operations
from typing import Optional

class TransactionStatus:
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

    
    def get_sync_transaction(self, request: operations.GetSyncTransactionRequest) -> operations.GetSyncTransactionResponse:
        r"""Get Sync Transaction
        Gets the status of a transaction for a sync
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/syncs/{syncId}/transactions/{transactionId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSyncTransactionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[operations.GetSyncTransaction200ApplicationJSON]])
                res.get_sync_transaction_200_application_json_objects = out

        return res

    
    def get_sync_transactions(self, request: operations.GetSyncTransactionsRequest) -> operations.GetSyncTransactionsResponse:
        r"""Get Sync transactions
        Get's the transactions and status for a sync
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/syncs/{syncId}/transactions", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSyncTransactionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetSyncTransactions200ApplicationJSON])
                res.get_sync_transactions_200_application_json_object = out

        return res

    