"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from codatsynccommerce import utils
from codatsynccommerce.models import operations
from typing import Optional

class SyncStatus:
    r"""Status of the sync between commerce company data into their respective accounting software."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def get_sync_status(self, request: operations.GetSyncStatusRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetSyncStatusResponse:
        r"""Get sync status
        Gets a list of sync statuses.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetSyncStatusRequest, base_url, '/meta/companies/{companyId}/sync/commerce/status', request)
        headers = {}
        headers['Accept'] = '*/*'
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

        res = operations.GetSyncStatusResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    