import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Configuration:
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
        
    def get_company_configuration(self, request: operations.GetCompanyConfigurationRequest) -> operations.GetCompanyConfigurationResponse:
        r"""Get company configuration
        Gets a companies expense sync configuration
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCompanyConfigurationRequest, base_url, '/companies/{companyId}/sync/expenses/config', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCompanyConfigurationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCompanyConfiguration200ApplicationJSON])
                res.get_company_configuration_200_application_json_object = out

        return res

    def save_company_configuration(self, request: operations.SaveCompanyConfigurationRequest) -> operations.SaveCompanyConfigurationResponse:
        r"""Set company configuration
        Sets a companies expense sync configuration
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.SaveCompanyConfigurationRequest, base_url, '/companies/{companyId}/sync/expenses/config', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SaveCompanyConfigurationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SaveCompanyConfiguration200ApplicationJSON])
                res.save_company_configuration_200_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SaveCompanyConfiguration400ApplicationJSON])
                res.save_company_configuration_400_application_json_object = out

        return res

    