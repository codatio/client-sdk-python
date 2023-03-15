import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Accounts:
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
        
    def create_account(self, request: operations.CreateAccountRequest) -> operations.CreateAccountResponse:
        r"""Create account
        Creates a new account for a given company.
        
        Required data may vary by integration. To see what data to post, first call [Get create account model](https://docs.codat.io/accounting-api#/operations/get-create-chartOfAccounts-model).
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support creating an account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateAccountRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/accounts', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateAccountRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateAccountResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateAccount200ApplicationJSON])
                res.create_account_200_application_json_object = out

        return res

    def get_account(self, request: operations.GetAccountRequest) -> operations.GetAccountResponse:
        r"""Get account
        Gets a single account corresponding to the given ID.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetAccountRequest, base_url, '/companies/{companyId}/data/accounts/{accountId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAccountResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAccountSourceModifiedDate])
                res.source_modified_date = out

        return res

    def get_accounts(self, request: operations.GetAccountsRequest) -> operations.GetAccountsResponse:
        r"""List accounts
        Gets the latest accounts for a company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetAccountsRequest, base_url, '/companies/{companyId}/data/accounts', request)
        
        query_params = utils.get_query_params(operations.GetAccountsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAccountsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAccountsLinks])
                res.links = out

        return res

    def get_create_chart_of_accounts_model(self, request: operations.GetCreateChartOfAccountsModelRequest) -> operations.GetCreateChartOfAccountsModelResponse:
        r"""Get create account model
        Get create account model. Returns the expected data for the request payload.
        
        See the examples for integration-specific indicative models.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support creating an account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCreateChartOfAccountsModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/chartOfAccounts', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCreateChartOfAccountsModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCreateChartOfAccountsModelPushOption])
                res.push_option = out

        return res

    