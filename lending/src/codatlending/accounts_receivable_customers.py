"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from codatlending import utils
from codatlending.models import errors, operations, shared
from enum import Enum
from jsonpath import JSONPath
from typing import Any, Dict, Optional

class DownloadAttachmentAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    APPLICATION_OCTET_STREAM = "application/octet-stream"

class AccountsReceivableCustomers:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def download_attachment(self, request: operations.DownloadAccountingCustomerAttachmentRequest, retries: Optional[utils.RetryConfig] = None, accept_header_override: Optional[DownloadAttachmentAcceptEnum] = None) -> operations.DownloadAccountingCustomerAttachmentResponse:
        r"""Download customer attachment
        The *Download customer attachment* endpoint downloads a specific attachment for a given `customerId` and `attachmentId`.

        [Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support downloading a customer attachment.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DownloadAccountingCustomerAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments/{attachmentId}/download', request)
        headers = {}
        if accept_header_override is not None:
            headers['Accept'] = accept_header_override.value
        else:
            headers['Accept'] = 'application/json;q=1, application/octet-stream;q=0'
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

        res = operations.DownloadAccountingCustomerAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/octet-stream'):
                res.data = http_res.content
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 404, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get(self, request: operations.GetAccountingCustomerRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetAccountingCustomerResponse:
        r"""Get customer
        The *Get customer* endpoint returns a single customer for a given customerId.

        [Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support getting a specific customer.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAccountingCustomerRequest, base_url, '/companies/{companyId}/data/customers/{customerId}', request)
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

        res = operations.GetAccountingCustomerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AccountingCustomer])
                res.accounting_customer = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 404, 409, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_attachment(self, request: operations.GetAccountingCustomerAttachmentRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetAccountingCustomerAttachmentResponse:
        r"""Get customer attachment
        The *Get customer attachment* endpoint returns a specific attachment for a given `customerId` and `attachmentId`.

        [Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support getting a customer attachment.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAccountingCustomerAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments/{attachmentId}', request)
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

        res = operations.GetAccountingCustomerAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AccountingAttachment])
                res.accounting_attachment = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 404, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def list(self, request: operations.ListAccountingCustomersRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListAccountingCustomersResponse:
        r"""List customers
        The *List customers* endpoint returns a list of [customers](https://docs.codat.io/accounting-api#/schemas/Customer) for a given company's connection.

        [Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListAccountingCustomersRequest, base_url, '/companies/{companyId}/data/customers', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListAccountingCustomersRequest, request)
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
        
        def next_func() -> Optional[operations.ListAccountingCustomersResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            next_cursor = JSONPath("").parse(body)

            if len(next_cursor) == 0:
                return None
            next_cursor = next_cursor[0]

            return self.list(
                request=operations.ListAccountingCustomersRequest(
                    company_id=request.company_id,
                    order_by=request.order_by,
                    page=request.page,
                    page_size=request.page_size,
                    query=request.query,
                ),
                retries=retries,
            )

        res = operations.ListAccountingCustomersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res, next=next_func)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AccountingCustomers])
                res.accounting_customers = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 404, 409]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def list_attachments(self, request: operations.ListAccountingCustomerAttachmentsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListAccountingCustomerAttachmentsResponse:
        r"""List customer attachments
        The *List customer attachments* endpoint returns a list of attachments avialable to download for given `customerId`.

        [Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support listing customer attachments.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListAccountingCustomerAttachmentsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments', request)
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

        res = operations.ListAccountingCustomerAttachmentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Attachments])
                res.attachments = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 404, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    