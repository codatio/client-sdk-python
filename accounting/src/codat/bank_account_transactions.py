import requests
from . import utils
from codat.models import operations
from typing import Optional

class BankAccountTransactions:
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

    
    def get_bank_account_push_options(self, request: operations.GetBankAccountPushOptionsRequest) -> operations.GetBankAccountPushOptionsResponse:
        r"""List push options for bank account bank transactions
        Gets the options of pushing bank account transactions.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/options/bankAccounts/{accountId}/bankTransactions", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetBankAccountPushOptionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetBankAccountPushOptionsPushOption])
                res.push_option = out

        return res

    
    def list_all_bank_transactionscount(self, request: operations.ListAllBankTransactionscountRequest) -> operations.ListAllBankTransactionscountResponse:
        r"""List bank transactions for bank account
        Gets bank transactions for a given bank account ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/data/bankAccounts/{accountId}/bankTransactions", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListAllBankTransactionscountResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListAllBankTransactionscountLinks])
                res.links = out

        return res

    
    def list_bank_transactions(self, request: operations.ListBankTransactionsRequest) -> operations.ListBankTransactionsResponse:
        r"""List all bank transactions
        Gets the latest bank transactions for given account ID and company. Doesn't require connection ID.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/bankAccounts/{accountId}/transactions", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListBankTransactionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListBankTransactionsLinks])
                res.links = out

        return res

    
    def post_bank_transactions(self, request: operations.PostBankTransactionsRequest) -> operations.PostBankTransactionsResponse:
        r"""Create bank transactions
        Posts bank transactions to the accounting package for a given company.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) for integrations that support POST methods.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/push/bankAccounts/{accountId}/bankTransactions", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostBankTransactionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PostBankTransactions200ApplicationJSON])
                res.post_bank_transactions_200_application_json_object = out

        return res

    