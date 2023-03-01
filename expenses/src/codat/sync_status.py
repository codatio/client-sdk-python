import requests
from . import utils
from codat.models import operations
from typing import Optional

class SyncStatus:
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

    
    def get_last_successful_sync(self, request: operations.GetLastSuccessfulSyncRequest) -> operations.GetLastSuccessfulSyncResponse:
        r"""Last successful sync
        Gets the status of the last successfull sync
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/syncs/lastSuccessful/status", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetLastSuccessfulSyncResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetLastSuccessfulSync200ApplicationJSON])
                res.get_last_successful_sync_200_application_json_object = out

        return res

    
    def get_latest_sync(self, request: operations.GetLatestSyncRequest) -> operations.GetLatestSyncResponse:
        r"""Latest sync status
        Gets the latest sync status
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/syncs/latest/status", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetLatestSyncResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetLatestSync200ApplicationJSON])
                res.get_latest_sync_200_application_json_object = out

        return res

    
    def get_sync_by_id(self, request: operations.GetSyncByIDRequest) -> operations.GetSyncByIDResponse:
        r"""Get Sync status
        Get the sync status for a specified sync
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/syncs/{syncId}/status", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSyncByIDResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetSyncByID200ApplicationJSON])
                res.get_sync_by_id_200_application_json_object = out

        return res

    
    def list_syncs(self, request: operations.ListSyncsRequest) -> operations.ListSyncsResponse:
        r"""List sync statuses
        Gets a list of sync statuses
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/syncs/list/status", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListSyncsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[operations.ListSyncs200ApplicationJSON]])
                res.list_syncs_200_application_json_objects = out

        return res

    