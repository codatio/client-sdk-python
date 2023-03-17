__doc__ = """ SDK Documentation: Bank Feeds API enables your SMB users to set up bank feeds from accounts in your application to supported accounting platforms.

A bank feed is a connection between a source bank account—in your application—and a target bank account in a supported accounting package.

[Read more...](https://docs.codat.io/bank-feeds-api/overview)

[See our OpenAPI spec](https://github.com/codatio/oas) """
import requests as requests_http
from . import utils
from bankfeeds.models import operations, shared
from typing import Optional

SERVERS = [
	"https://api.codat.io",
]

class BankFeeds:
    r"""SDK Documentation: Bank Feeds API enables your SMB users to set up bank feeds from accounts in your application to supported accounting platforms.
    
    A bank feed is a connection between a source bank account—in your application—and a target bank account in a supported accounting package.
    
    [Read more...](https://docs.codat.io/bank-feeds-api/overview)
    
    [See our OpenAPI spec](https://github.com/codatio/oas) """
    
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.5.3"
    _gen_version: str = "1.12.1"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = utils.configure_security_client(self._client, security)
        

        
    
    
    def create_bank_feed(self, request: operations.CreateBankFeedRequest) -> operations.CreateBankFeedResponse:
        r"""Create bank feed bank accounts
        Put BankFeed BankAccounts for a single data source connected to a single company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateBankFeedRequest, base_url, '/companies/{companyId}/connections/{connectionId}/connectionInfo/bankFeedAccounts', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
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

    def get_bank_account_push_options(self, request: operations.GetBankAccountPushOptionsRequest) -> operations.GetBankAccountPushOptionsResponse:
        r"""List push options for bank account bank transactions
        Gets the options of pushing bank account transactions.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetBankAccountPushOptionsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/bankAccounts/{accountId}/bankTransactions', request)
        
        query_params = utils.get_query_params(operations.GetBankAccountPushOptionsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBankAccountPushOptionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetBankAccountPushOptionsPushOption])
                res.push_option = out

        return res

    def get_bank_feeds(self, request: operations.GetBankFeedsRequest) -> operations.GetBankFeedsResponse:
        r"""List bank feed bank accounts
        Get BankFeed BankAccounts for a single data source connected to a single company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetBankFeedsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/connectionInfo/bankFeedAccounts', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBankFeedsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[operations.GetBankFeedsBankFeedBankAccount]])
                res.bank_feed_bank_accounts = out

        return res

    def list_bank_account_transactions(self, request: operations.ListBankAccountTransactionsRequest) -> operations.ListBankAccountTransactionsResponse:
        r"""List bank transactions for bank account
        Gets bank transactions for a given bank account ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListBankAccountTransactionsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/bankAccounts/{accountId}/bankTransactions', request)
        
        query_params = utils.get_query_params(operations.ListBankAccountTransactionsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListBankAccountTransactionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListBankAccountTransactionsLinks])
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
        
        url = utils.generate_url(operations.PostBankTransactionsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/bankAccounts/{accountId}}/bankTransactions', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.PostBankTransactionsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostBankTransactionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostBankTransactions200ApplicationJSON])
                res.post_bank_transactions_200_application_json_object = out

        return res

    def update_bank_feed(self, request: operations.UpdateBankFeedRequest) -> operations.UpdateBankFeedResponse:
        r"""Update bank feed bank account
        Update a single BankFeed BankAccount for a single data source connected to a single company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateBankFeedRequest, base_url, '/companies/{companyId}/connections/{connectionId}/connectionInfo/bankFeedAccounts/{bankAccountId}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
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

    