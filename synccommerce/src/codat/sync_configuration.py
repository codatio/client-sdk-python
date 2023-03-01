import requests
from . import utils
from codat.models import operations
from typing import Optional

class SyncConfiguration:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
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
        
        url = utils.generate_url(base_url, "/config/companies/{companyId}/sync/commerce", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ConfigureSyncResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ConfigureSync200ApplicationJSON])
                res.configure_sync_200_application_json_object = out

        return res

    
    def get_company_commerce_sync_status(self, request: operations.GetCompanyCommerceSyncStatusRequest) -> operations.GetCompanyCommerceSyncStatusResponse:
        r"""Get Sync for Commerce status
        Check the sync history and status for a company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/meta/companies/{companyId}/sync/commerce/status", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCompanyCommerceSyncStatusResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def get_sync_flow_url(self, request: operations.GetSyncFlowURLRequest) -> operations.GetSyncFlowURLResponse:
        r"""Get Sync Flow Url
        To get a URL for Sync Flow including a one time passcode.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/config/sync/commerce/{commerceKey}/{accountingKey}/start", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSyncFlowURLResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def get_sync_options(self, request: operations.GetSyncOptionsRequest) -> operations.GetSyncOptionsResponse:
        r"""List options for Sync for Commerce settings
        Retrieve sync options and current sync configuration for a Company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/config/companies/{companyId}/sync/commerce", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSyncOptionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetSyncOptions200ApplicationJSON])
                res.get_sync_options_200_application_json_object = out

        return res

    