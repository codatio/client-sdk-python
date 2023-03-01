import requests
from . import utils
from codat.models import operations
from typing import Optional

class BankAccounts:
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

    
    def get_all_bank_account(self, request: operations.GetAllBankAccountRequest) -> operations.GetAllBankAccountResponse:
        r"""Get bank account
        Gets the bank account for given account ID.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/bankAccounts/{accountId}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllBankAccountResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAllBankAccount200ApplicationJSON])
                res.get_all_bank_account_200_application_json_object = out

        return res

    
    def get_bank_account(self, request: operations.GetBankAccountRequest) -> operations.GetBankAccountResponse:
        r"""Get bank account
        Gets the bank account with a given ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/data/bankAccounts/{accountId}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetBankAccountResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetBankAccountSourceModifiedDate])
                res.source_modified_date = out

        return res

    
    def list_bank_accounts(self, request: operations.ListBankAccountsRequest) -> operations.ListBankAccountsResponse:
        r"""List bank accounts
        Gets the list of bank accounts for a given connection
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/data/bankAccounts", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListBankAccountsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListBankAccountsLinks])
                res.links = out

        return res

    
    def post_bank_account(self, request: operations.PostBankAccountRequest) -> operations.PostBankAccountResponse:
        r"""Create bank account
        Posts a new bank account to the accounting package for a given company.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support pushing bank accounts.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/push/bankAccounts", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostBankAccountResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PostBankAccount200ApplicationJSON])
                res.post_bank_account_200_application_json_object = out

        return res

    
    def put_bank_account(self, request: operations.PutBankAccountRequest) -> operations.PutBankAccountResponse:
        r"""Update bank account
        Posts an updated bank account to the accounting package for a given company.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support PUT methods.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/push/bankAccounts/{bankAccountId}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PUT", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PutBankAccountResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PutBankAccount200ApplicationJSON])
                res.put_bank_account_200_application_json_object = out

        return res

    