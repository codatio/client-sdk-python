"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from codatplatform import utils
from codatplatform._hooks import HookContext
from codatplatform.models import errors, operations, shared
from typing import Dict, Optional

class RefreshData:
    r"""Asynchronously retrieve data from an integration to refresh data in Codat."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def all(self, request: operations.RefreshCompanyDataRequest, retries: Optional[utils.RetryConfig] = None) -> operations.RefreshCompanyDataResponse:
        r"""Refresh all data
        Refreshes all data types with `fetch on first link` set to `true` for a given company.

        This is an asynchronous operation, and will bring updated data into Codat from the linked integration for you to view.

        [Read more](https://docs.codat.io/core-concepts/data-type-settings) about data type settings and `fetch on first link`.
        """
        hook_ctx = HookContext(operation_id='refresh-company-data', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.RefreshCompanyDataRequest, base_url, '/companies/{companyId}/data/all', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('POST', url, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['401','402','403','404','429','4XX','500','503','5XX'], http_res.status_code):
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
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.RefreshCompanyDataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.ErrorMessage)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def by_data_type(self, request: operations.RefreshDataTypeRequest, retries: Optional[utils.RetryConfig] = None) -> operations.RefreshDataTypeResponse:
        r"""Refresh data type
        Refreshes a given data type for a given company.

        This is an asynchronous operation, and will bring updated data into Codat from the linked integration for you to view.
        """
        hook_ctx = HookContext(operation_id='refresh-data-type', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.RefreshDataTypeRequest, base_url, '/companies/{companyId}/data/queue/{dataType}', request)
        headers = {}
        query_params = utils.get_query_params(operations.RefreshDataTypeRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('POST', url, params=query_params, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['401','402','403','404','429','4XX','500','503','5XX'], http_res.status_code):
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
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.RefreshDataTypeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PullOperation])
                res.pull_operation = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.ErrorMessage)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get(self, request: operations.GetCompanyDataStatusRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetCompanyDataStatusResponse:
        r"""Get data status
        Get the state of each data type for a company
        """
        hook_ctx = HookContext(operation_id='get-company-data-status', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetCompanyDataStatusRequest, base_url, '/companies/{companyId}/dataStatus', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('GET', url, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['401','402','403','404','429','4XX','500','503','5XX'], http_res.status_code):
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
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetCompanyDataStatusResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Dict[str, shared.DataStatus]])
                res.data_statuses = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.ErrorMessage)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_pull_operation(self, request: operations.GetPullOperationRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetPullOperationResponse:
        r"""Get pull operation
        Retrieve information about a single dataset or pull operation.
        """
        hook_ctx = HookContext(operation_id='get-pull-operation', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetPullOperationRequest, base_url, '/companies/{companyId}/data/history/{datasetId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('GET', url, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['401','402','403','404','429','4XX','500','503','5XX'], http_res.status_code):
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
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetPullOperationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PullOperation])
                res.pull_operation = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.ErrorMessage)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def list_pull_operations(self, request: operations.ListPullOperationsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListPullOperationsResponse:
        r"""List pull operations
        Gets the pull operation history (datasets) for a given company.
        """
        hook_ctx = HookContext(operation_id='list-pull-operations', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListPullOperationsRequest, base_url, '/companies/{companyId}/data/history', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListPullOperationsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('GET', url, params=query_params, headers=headers).prepare(),
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
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.ListPullOperationsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PullOperations])
                res.pull_operations = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.ErrorMessage)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    