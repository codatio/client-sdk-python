import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Integrations:
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
        
    def get_integration_branding(self, request: operations.GetIntegrationBrandingRequest) -> operations.GetIntegrationBrandingResponse:
        r"""Get branding for an integration
        Retrieve Integration branding assets.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/config/integrations/{platformKey}/branding', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetIntegrationBrandingResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def get_integrations(self, request: operations.GetIntegrationsRequest) -> operations.GetIntegrationsResponse:
        r"""List Codat's integrations
        Retrieve a list of available integrations.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/config/integrations'
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetIntegrationsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetIntegrations200ApplicationJSON])
                res.get_integrations_200_application_json_object = out

        return res

    