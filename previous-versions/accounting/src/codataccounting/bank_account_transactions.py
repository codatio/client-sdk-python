"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from codataccounting import utils
from codataccounting.models import errors, operations, shared
from jsonpath import JSONPath
from typing import Any, Dict, Optional

class BankAccountTransactions:
    r"""Bank transactions for bank accounts"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create(self, request: operations.CreateBankTransactionsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.CreateBankTransactionsResponse:
        r"""Create bank account transactions
        The *Create bank account transactions* endpoint creates new [bank account transactions](https://docs.codat.io/accounting-api#/schemas/BankTransactions) for a given company's connection.

        [Bank account transactions](https://docs.codat.io/accounting-api#/schemas/BankTransactions) are records of money that has moved in and out of an SMB's bank account.

        **Integration-specific behaviour**

        Required data may vary by integration. To see what data to post, first call [Get create bank transaction model](https://docs.codat.io/accounting-api#/operations/get-create-bankTransactions-model).

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) for integrations that support creating a bank account transactions.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateBankTransactionsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/bankAccounts/{accountId}/bankTransactions', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "create_bank_transactions", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateBankTransactionsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateBankTransactionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateBankTransactionsResponse])
                res.create_bank_transactions_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 404, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_create_model(self, request: operations.GetCreateBankTransactionsModelRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetCreateBankTransactionsModelResponse:
        r"""Get create bank account transactions model
        The *Get create bank account transactions model* endpoint returns the expected data for the request payload when creating [bank account transactions](https://docs.codat.io/accounting-api#/schemas/BankTransactions) for a given company and integration.

        [Bank account transactions](https://docs.codat.io/accounting-api#/schemas/BankTransactions) are records of money that has moved in and out of an SMB's bank account.

        **Integration-specific behaviour**

        See the *response examples* for integration-specific indicative models.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) for integrations that support creating an bank transaction.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetCreateBankTransactionsModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/bankAccounts/{accountId}/bankTransactions', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('GET', url, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCreateBankTransactionsModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PushOption])
                res.push_option = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 404, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def list(self, request: operations.ListBankAccountTransactionsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListBankAccountTransactionsResponse:
        r"""List bank account transactions
        The *List account bank transactions* endpoint returns a list of [bank account transactions](https://docs.codat.io/accounting-api#/schemas/BankTransactions) for a given company's connection.

        [Bank account transactions](https://docs.codat.io/accounting-api#/schemas/BankTransactions) are records of money that has moved in and out of an SMB's bank account.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) for integrations that support listing bank transactions.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListBankAccountTransactionsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/bankAccounts/{accountId}/bankTransactions', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListBankAccountTransactionsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('GET', url, params=query_params, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')
        
        def next_func() -> Optional[operations.ListBankAccountTransactionsResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            next_cursor = JSONPath("").parse(body)

            if len(next_cursor) == 0:
                return None
            next_cursor = next_cursor[0]

            return self.list(
                request=operations.ListBankAccountTransactionsRequest(
                    account_id=request.account_id,
                    company_id=request.company_id,
                    connection_id=request.connection_id,
                    order_by=request.order_by,
                    page=request.page,
                    page_size=request.page_size,
                    query=request.query,
                ),
                retries=retries,
            )

        res = operations.ListBankAccountTransactionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res, next=next_func)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BankTransactions])
                res.bank_transactions = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 404, 409, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    