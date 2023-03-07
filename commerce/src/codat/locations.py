import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Locations:
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
        
    def list_commerce_locations(self, request: operations.ListCommerceLocationsRequest) -> operations.ListCommerceLocationsResponse:
        r"""List locations
        Retrieve a list of locations as seen in the commerce platform.
        
        A `location` is a geographic place at which stocks of products may be held, or from where orders were placed.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/connections/{connectionId}/data/commerce-locations', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListCommerceLocationsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListCommerceLocationsLinks])
                res.links = out

        return res

    