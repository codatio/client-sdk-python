import requests
from . import utils
from codat.models import operations
from typing import Optional

class Settings:
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

    
    def get_profile_sync_settings(self) -> operations.GetProfileSyncSettingsResponse:
        r"""Get sync settings
        Retrieve the sync settings for your client. This includes how often data types should be queued to be updated, and how much history should be fetched.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/profile/syncSettings"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetProfileSyncSettingsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetProfileSyncSettings200ApplicationJSON])
                res.get_profile_sync_settings_200_application_json_object = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetProfileSyncSettings401ApplicationJSON])
                res.get_profile_sync_settings_401_application_json_object = out

        return res

    
    def get_settings_profile(self) -> operations.GetSettingsProfileResponse:
        r"""Get profile
        Fetch your Codat profile.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/profile"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSettingsProfileResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetSettingsProfileProfile])
                res.profile = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetSettingsProfile401ApplicationJSON])
                res.get_settings_profile_401_application_json_object = out

        return res

    
    def post_profile_sync_settings(self, request: operations.PostProfileSyncSettingsRequest) -> operations.PostProfileSyncSettingsResponse:
        r"""Update all sync settings
        Update sync settings for all data types.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/profile/syncSettings"
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostProfileSyncSettingsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PostProfileSyncSettings401ApplicationJSON])
                res.post_profile_sync_settings_401_application_json_object = out

        return res

    
    def put_profile(self, request: operations.PutProfileRequest) -> operations.PutProfileResponse:
        r"""Update profile
        Update your Codat profile
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/profile"
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PutProfileResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PutProfileProfile])
                res.profile = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PutProfile401ApplicationJSON])
                res.put_profile_401_application_json_object = out

        return res

    