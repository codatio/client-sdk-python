import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Transactions:
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
        
    def get_banking_transaction(self, request: operations.GetBankingTransactionRequest) -> operations.GetBankingTransactionResponse:
        r"""Get bank transaction
        Gets a specified bank transaction for a given company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetBankingTransactionRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/banking-transactions/{transactionId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBankingTransactionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetBankingTransactionSourceModifiedDate])
                res.source_modified_date = out

        return res

    def list_all_banking_transactions(self, request: operations.ListAllBankingTransactionsRequest) -> operations.ListAllBankingTransactionsResponse:
        r"""List banking transactions
        Gets a list of transactions incurred by a company across all bank accounts.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListAllBankingTransactionsRequest, base_url, '/companies/{companyId}/data/banking-transactions', request)
        
        query_params = utils.get_query_params(operations.ListAllBankingTransactionsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAllBankingTransactionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListAllBankingTransactions200ApplicationJSON])
                res.list_all_banking_transactions_200_application_json_object = out

        return res

    def list_banking_transactions(self, request: operations.ListBankingTransactionsRequest) -> operations.ListBankingTransactionsResponse:
        r"""List bank account transactions
        Gets a list of transactions incurred by a bank account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListBankingTransactionsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/banking-transactions', request)
        
        query_params = utils.get_query_params(operations.ListBankingTransactionsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListBankingTransactionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListBankingTransactions200ApplicationJSON])
                res.list_banking_transactions_200_application_json_object = out

        return res

    