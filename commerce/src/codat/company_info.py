import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class CompanyInfo:
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
        
    def get_commerce_info(self, request: operations.GetCommerceInfoRequest) -> operations.GetCommerceInfoResponse:
        r"""Get company info
        Retrieve information about the company, as seen in the commerce platform.
        
        This may include information like addresses, tax registration details and social media or website information.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCommerceInfoRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/commerce-info', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCommerceInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCommerceInfoSourceModifiedDate])
                res.source_modified_date = out

        return res

    