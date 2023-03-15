import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class BankAccounts:
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
        
    def create_bank_account(self, request: operations.CreateBankAccountRequest) -> operations.CreateBankAccountResponse:
        r"""Create bank account
        Posts a new bank account to the accounting package for a given company.
        
        Required data may vary by integration. To see what data to post, first call []().
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating bank accounts.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateBankAccountRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/bankAccounts', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateBankAccountRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateBankAccountResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateBankAccount200ApplicationJSON])
                res.create_bank_account_200_application_json_object = out

        return res

    def get_all_bank_account(self, request: operations.GetAllBankAccountRequest) -> operations.GetAllBankAccountResponse:
        r"""Get bank account
        Gets the bank account for given account ID.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetAllBankAccountRequest, base_url, '/companies/{companyId}/data/bankAccounts/{accountId}', request)
        
        query_params = utils.get_query_params(operations.GetAllBankAccountRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAllBankAccountResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAllBankAccount200ApplicationJSON])
                res.get_all_bank_account_200_application_json_object = out

        return res

    def get_bank_account(self, request: operations.GetBankAccountRequest) -> operations.GetBankAccountResponse:
        r"""Get bank account
        Gets the bank account with a given ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetBankAccountRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/bankAccounts/{accountId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBankAccountResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetBankAccountSourceModifiedDate])
                res.source_modified_date = out

        return res

    def get_create_update_bank_accounts_model(self, request: operations.GetCreateUpdateBankAccountsModelRequest) -> operations.GetCreateUpdateBankAccountsModelResponse:
        r"""Get create/update bank account model
        Get create/update bank account model. Returns the expected data for the request payload.
        
        See the examples for integration-specific indicative models.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating and updating bank accounts.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCreateUpdateBankAccountsModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/bankAccounts', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCreateUpdateBankAccountsModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCreateUpdateBankAccountsModelPushOption])
                res.push_option = out

        return res

    def list_bank_accounts(self, request: operations.ListBankAccountsRequest) -> operations.ListBankAccountsResponse:
        r"""List bank accounts
        Gets the list of bank accounts for a given connection
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListBankAccountsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/bankAccounts', request)
        
        query_params = utils.get_query_params(operations.ListBankAccountsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListBankAccountsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListBankAccountsLinks])
                res.links = out

        return res

    def put_bank_account(self, request: operations.PutBankAccountRequest) -> operations.PutBankAccountResponse:
        r"""Update bank account
        Posts an updated bank account to the accounting package for a given company.
        
        Required data may vary by integration. To see what data to post, first call []().
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support updating bank accounts.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.PutBankAccountRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/bankAccounts/{bankAccountId}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.PutBankAccountRequest, request)
        
        client = self._security_client
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutBankAccountResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PutBankAccount200ApplicationJSON])
                res.put_bank_account_200_application_json_object = out

        return res

    