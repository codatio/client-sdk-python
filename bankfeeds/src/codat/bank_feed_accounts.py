import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class BankFeedAccounts:
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
        
    def create_bank_feed(self, request: operations.CreateBankFeedRequest) -> operations.CreateBankFeedResponse:
        r"""Create bank feed bank accounts
        Put BankFeed BankAccounts for a single data source connected to a single company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/connections/{connectionId}/connectionInfo/bankFeedAccounts', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateBankFeedResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[operations.CreateBankFeedBankFeedBankAccount]])
                res.bank_feed_bank_accounts = out

        return res

    def get_bank_feeds(self, request: operations.GetBankFeedsRequest) -> operations.GetBankFeedsResponse:
        r"""List bank feed bank accounts
        Get BankFeed BankAccounts for a single data source connected to a single company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/connections/{connectionId}/connectionInfo/bankFeedAccounts', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBankFeedsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[operations.GetBankFeedsBankFeedBankAccount]])
                res.bank_feed_bank_accounts = out

        return res

    def update_bank_feed(self, request: operations.UpdateBankFeedRequest) -> operations.UpdateBankFeedResponse:
        r"""Update bank feed bank account
        Update a single BankFeed BankAccount for a single data source connected to a single company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/connections/{connectionId}/connectionInfo/bankFeedAccounts/{bankAccountId}', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateBankFeedResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateBankFeedBankFeedBankAccount])
                res.bank_feed_bank_account = out

        return res

    