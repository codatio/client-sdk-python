import requests
from . import utils
from codat.models import operations
from typing import Optional

class Integrations:
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

    
    def get_integrations_platform_key(self, request: operations.GetIntegrationsPlatformKeyRequest) -> operations.GetIntegrationsPlatformKeyResponse:
        r"""Get integration
        Get single integration, by platformKey
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/integrations/{platformKey}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetIntegrationsPlatformKeyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetIntegrationsPlatformKeyIntegration])
                res.integration = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetIntegrationsPlatformKey401ApplicationJSON])
                res.get_integrations_platform_key_401_application_json_object = out
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetIntegrationsPlatformKey404ApplicationJSON])
                res.get_integrations_platform_key_404_application_json_object = out

        return res

    
    def get_integrations_platform_key_branding(self, request: operations.GetIntegrationsPlatformKeyBrandingRequest) -> operations.GetIntegrationsPlatformKeyBrandingResponse:
        r"""Get branding
        Get branding for platform.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/integrations/{platformKey}/branding", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetIntegrationsPlatformKeyBrandingResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetIntegrationsPlatformKeyBrandingBranding])
                res.branding = out

        return res

    
    def list_integrations(self, request: operations.ListIntegrationsRequest) -> operations.ListIntegrationsResponse:
        r"""List integrations
        List your available integrations
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/integrations"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListIntegrationsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListIntegrationsLinks])
                res.links = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListIntegrations400ApplicationJSON])
                res.list_integrations_400_application_json_object = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListIntegrations401ApplicationJSON])
                res.list_integrations_401_application_json_object = out

        return res

    