"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from codatsynccommerce import utils
from codatsynccommerce.models import errors, operations, shared
from typing import Optional

class CommerceTransactions:
    r"""Retrieve standardized data from linked commerce platforms."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def get_commerce_transaction(self, request: operations.GetCommerceTransactionRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetCommerceTransactionResponse:
        r"""Get transaction
        The *Get transaction* endpoint returns a single transaction for a given transactionId.

        [Transactions](https://docs.codat.io/commerce-api#/schemas/Transaction) detail all financial affairs recorded in the commerce or point of sale system.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/commerce?view=tab-by-data-type&dataType=commerce-transactions) for integrations that support getting a specific transaction.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-commerce-v1-api#/operations/refresh-company-data).
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetCommerceTransactionRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/commerce-transactions/{transactionId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('GET', url, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCommerceTransactionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CommerceTransaction])
                res.commerce_transaction = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 404, 409, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def list_commerce_transactions(self, request: operations.ListCommerceTransactionsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListCommerceTransactionsResponse:
        r"""List transactions
        The *List transactions* endpoint returns a list of [transactions](https://docs.codat.io/commerce-api#/schemas/Transaction) for a given company's connection.

        [Transactions](https://docs.codat.io/commerce-api#/schemas/Transaction) detail all financial affairs recorded in the commerce or point of sale system.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-commerce-v1-api#/operations/refresh-company-data).
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListCommerceTransactionsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/commerce-transactions', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListCommerceTransactionsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('GET', url, params=query_params, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListCommerceTransactionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CommerceTransactions])
                res.commerce_transactions = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 404, 409, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    