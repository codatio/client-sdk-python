"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from codatlending import utils
from codatlending.models import errors, operations, shared
from enum import Enum
from typing import Optional

class DownloadAttachmentAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    APPLICATION_OCTET_STREAM = "application/octet-stream"

class AccountsPayableBills:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def download_attachment(self, request: operations.DownloadAccountingBillAttachmentRequest, retries: Optional[utils.RetryConfig] = None, accept_header_override: Optional[DownloadAttachmentAcceptEnum] = None) -> operations.DownloadAccountingBillAttachmentResponse:
        r"""Download bill attachment
        The *Download bill attachment* endpoint downloads a specific attachment for a given `billId` and `attachmentId`.

        [Bills](https://docs.codat.io/lending-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support downloading a bill attachment.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DownloadAccountingBillAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments/{attachmentId}/download', request)
        headers = {}
        if accept_header_override is not None:
            headers['Accept'] = accept_header_override.value
        else:
            headers['Accept'] = 'application/json;q=1, application/octet-stream;q=0'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
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

        res = operations.DownloadAccountingBillAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/octet-stream'):
                res.data = http_res
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get(self, request: operations.GetAccountingBillRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetAccountingBillResponse:
        r"""Get bill
        The *Get bill* endpoint returns a single bill for a given billId.

        [Bills](https://docs.codat.io/lending-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support getting a specific bill.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAccountingBillRequest, base_url, '/companies/{companyId}/data/bills/{billId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
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

        res = operations.GetAccountingBillResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AccountingBill])
                res.accounting_bill = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 402, 403, 404, 409, 429, 500, 503]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_attachment(self, request: operations.GetAccountingBillAttachmentRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetAccountingBillAttachmentResponse:
        r"""Get bill attachment
        The *Get bill attachment* endpoint returns a specific attachment for a given `billId` and `attachmentId`.

        [Bills](https://docs.codat.io/lending-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support getting a bill attachment.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAccountingBillAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments/{attachmentId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
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

        res = operations.GetAccountingBillAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AccountingAttachment])
                res.accounting_attachment = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def list(self, request: operations.ListAccountingBillsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListAccountingBillsResponse:
        r"""List bills
        The *List bills* endpoint returns a list of [bills](https://docs.codat.io/lending-api#/schemas/Bill) for a given company's connection.

        [Bills](https://docs.codat.io/lending-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListAccountingBillsRequest, base_url, '/companies/{companyId}/data/bills', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListAccountingBillsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
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

        res = operations.ListAccountingBillsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AccountingBills])
                res.accounting_bills = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 404, 409, 429, 500, 503]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def list_attachments(self, request: operations.ListAccountingBillAttachmentsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListAccountingBillAttachmentsResponse:
        r"""List bill attachments
        The *List bill attachments* endpoint returns a list of attachments available to download for a given `billId`.

        [Bills](https://docs.codat.io/lending-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support listing bill attachments.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListAccountingBillAttachmentsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
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

        res = operations.ListAccountingBillAttachmentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Attachments])
                res.attachments = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 402, 403, 404, 409, 429, 500, 503]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    