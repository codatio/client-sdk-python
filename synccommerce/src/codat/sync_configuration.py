import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class SyncConfiguration:
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
        
    def configure_sync(self, request: operations.ConfigureSyncRequest) -> operations.ConfigureSyncResponse:
        r"""Update Sync for Commerce settings
        Configure Sync for Commerce for a Company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ConfigureSyncRequest, base_url, '/config/companies/{companyId}/sync/commerce', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ConfigureSyncResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ConfigureSync200ApplicationJSON])
                res.configure_sync_200_application_json_object = out

        return res

    def get_company_commerce_sync_status(self, request: operations.GetCompanyCommerceSyncStatusRequest) -> operations.GetCompanyCommerceSyncStatusResponse:
        r"""Get Sync for Commerce status
        Check the sync history and status for a company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCompanyCommerceSyncStatusRequest, base_url, '/meta/companies/{companyId}/sync/commerce/status', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCompanyCommerceSyncStatusResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def get_sync_flow_url(self, request: operations.GetSyncFlowURLRequest) -> operations.GetSyncFlowURLResponse:
        r"""Get Sync Flow Url
        To get a URL for Sync Flow including a one time passcode.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetSyncFlowURLRequest, base_url, '/config/sync/commerce/{commerceKey}/{accountingKey}/start', request)
        
        query_params = utils.get_query_params(operations.GetSyncFlowURLRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSyncFlowURLResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def get_sync_options(self, request: operations.GetSyncOptionsRequest) -> operations.GetSyncOptionsResponse:
        r"""List options for Sync for Commerce settings
        Retrieve sync options and current sync configuration for a Company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetSyncOptionsRequest, base_url, '/config/companies/{companyId}/sync/commerce', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSyncOptionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetSyncOptions200ApplicationJSON])
                res.get_sync_options_200_application_json_object = out

        return res

    