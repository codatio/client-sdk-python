"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from codatsyncexpenses import utils
from codatsyncexpenses._hooks import HookContext
from codatsyncexpenses.models import errors, operations, shared
from typing import Optional

class Expenses:
    r"""Create expense datasets and upload receipts."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def create(self, request: operations.CreateExpenseTransactionRequest, retries: Optional[utils.RetryConfig] = None) -> operations.CreateExpenseTransactionResponse:
        r"""Create expense transaction
        The *Create expense* endpoint creates an [expense transaction](https://docs.codat.io/sync-for-expenses-api#/schemas/ExpenseTransaction) in the accounting platform for a given company's connection. 

        [Expense transactions](https://docs.codat.io/sync-for-expenses-api#/schemas/ExpenseTransaction) represent transactions made with a company debit or credit card. 


        **Integration-specific behaviour**

        Some accounting platforms support the option of pushing transactions to a draft state. This can be done by setting the postAsDraft property on the transaction to true. For platforms without this feature, the postAsDraft property should be ignored or set to false.

        | Integration | Draft State | Details                                                                                                      |  
        |-------------|-------------|--------------------------------------------------------------------------------------------------------------|
        | Dynamics 365 Business Central | Yes   | Setting postAsDraft to true will push the transactions to a drafted state rather than posting directly to the ledger. For transactions in a draft state, they can then be approved and posted within the accounting platform. |
        | Quickbooks Online | No | -  |
        | Xero | No | - |
        | NetSuite | No | - |
        """
        hook_ctx = HookContext(operation_id='create-expense-transaction', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateExpenseTransactionRequest, base_url, '/companies/{companyId}/sync/expenses/data/expense-transactions', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        req_content_type, data, form = utils.serialize_request_body(request, operations.CreateExpenseTransactionRequest, "create_expense_request", False, True, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['400','401','402','403','404','429','4XX','500','503','5XX'], http_res.status_code):
                http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
                if e:
                    raise e
            else:
                result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
                if isinstance(result, Exception):
                    raise result
                http_res = result

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        
        
        res = operations.CreateExpenseTransactionResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateExpenseResponse])
                res.create_expense_response = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.ErrorMessage)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def update(self, request: operations.UpdateExpenseTransactionRequest, retries: Optional[utils.RetryConfig] = None) -> operations.UpdateExpenseTransactionResponse:
        r"""Update expense transactions
        The *Update expense* endpoint updates an existing [expense transaction](https://docs.codat.io/sync-for-expenses-api#/schemas/ExpenseTransaction) in the accounting platform for a given company's connection. 

        [Expense transactions](https://docs.codat.io/sync-for-expenses-api#/schemas/ExpenseTransaction) represent transactions made with a company debit or credit card. 


        **Integration-specific behaviour**

        At the moment you can update expenses only for Xero ([Payment](https://docs.codat.io/expenses/sync-process/expense-transactions#transaction-types) transaction type only).
        """
        hook_ctx = HookContext(operation_id='update-expense-transaction', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateExpenseTransactionRequest, base_url, '/companies/{companyId}/sync/expenses/expense-transactions/{transactionId}', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        req_content_type, data, form = utils.serialize_request_body(request, operations.UpdateExpenseTransactionRequest, "update_expense_request", False, True, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('PUT', url, params=query_params, data=data, files=form, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['400','401','402','403','404','422','429','4XX','500','503','5XX'], http_res.status_code):
                http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
                if e:
                    raise e
            else:
                result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
                if isinstance(result, Exception):
                    raise result
                http_res = result

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        
        
        res = operations.UpdateExpenseTransactionResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 202:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[shared.UpdateExpenseResponse])
                res.update_expense_response = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 404, 422, 429, 500, 503]:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.ErrorMessage)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def upload_attachment(self, request: operations.UploadExpenseAttachmentRequest, retries: Optional[utils.RetryConfig] = None) -> operations.UploadExpenseAttachmentResponse:
        r"""Upload attachment
        The *Upload attachment* endpoint uploads an attachment in the accounting software against the given transactionId. 

        [Expense transactions](https://docs.codat.io/sync-for-expenses-api#/schemas/ExpenseTransaction) represent transactions made with a company debit or credit card. 

        **Integration-specific behaviour**

        Each accounting software supports different file formats and sizes.

        | Integration | File Size | File Extension                                                                                                      |  
        |-------------|-------------|--------------------------------------------------------------------------------------------------------------|
        | Xero | 4MB  | 7Z, BMP, CSV, DOC, DOCX, EML, GIF, JPEG, JPG, KEYNOTE, MSG, NUMBERS, ODF, ODS, ODT, PAGES, PDF, PNG, PPT, PPTX, RAR, RTF, TIF, TIFF, TXT, XLS, XLSX, ZIP |
        | QuickBooks Online | 100MB | AI, CSV, DOC, DOCX, EPS, GIF, JPEG, JPG, ODS, PAGES, PDF, PNG, RTF, TIF, TXT, XLS, XLSX, XML  |
        | NetSuite | 100MB | BMP, CSV, XLS, XLSX, JSON, PDF, PJPG, PJPEG, PNG, TXT, SVG, TIF, TIFF, DOC, DOCX, ZIP |
        | Dynamics 365 Business Central | 350 MB | Dynamics do not explicitly outline which file types are supported but they do state <a className=\"external\" href=\"https://learn.microsoft.com/en-gb/dynamics365/business-central/ui-how-add-link-to-record#to-attach-a-file-to-a-purchase-invoice\" target=\"_blank\">here</a> that \"You can attach any type of file, such as text, image, or video files\". |
        """
        hook_ctx = HookContext(operation_id='upload-expense-attachment', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UploadExpenseAttachmentRequest, base_url, '/companies/{companyId}/sync/expenses/syncs/{syncId}/transactions/{transactionId}/attachments', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        req_content_type, data, form = utils.serialize_request_body(request, operations.UploadExpenseAttachmentRequest, "attachment_upload", False, True, 'multipart')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['400','401','402','403','404','429','4XX','500','503','5XX'], http_res.status_code):
                http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
                if e:
                    raise e
            else:
                result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
                if isinstance(result, Exception):
                    raise result
                http_res = result

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        
        
        res = operations.UploadExpenseAttachmentResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[shared.Attachment])
                res.attachment = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.ErrorMessage)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    