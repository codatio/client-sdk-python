import requests
from . import utils
from codat.models import operations
from typing import Optional

class Configuration:
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

    
    def get_company_configuration(self, request: operations.GetCompanyConfigurationRequest) -> operations.GetCompanyConfigurationResponse:
        r"""Get Company configuration
        Gets a companies expense sync configuration
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/config", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCompanyConfigurationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompanyConfiguration200ApplicationJSON])
                res.get_company_configuration_200_application_json_object = out

        return res

    
    def save_company_configuration(self, request: operations.SaveCompanyConfigurationRequest) -> operations.SaveCompanyConfigurationResponse:
        r"""Set Company configuration
        Sets a companies expense sync configuration
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/config", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.SaveCompanyConfigurationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.SaveCompanyConfiguration200ApplicationJSON])
                res.save_company_configuration_200_application_json_object = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.SaveCompanyConfiguration400ApplicationJSON])
                res.save_company_configuration_400_application_json_object = out

        return res

    