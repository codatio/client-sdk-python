import requests
from . import utils
from codat.models import operations
from typing import Optional

class Companies:
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
        
    def create_company(self, request: operations.CreateCompanyRequest) -> operations.CreateCompanyResponse:
        r"""Create company
        Create a new company
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/companies'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateCompanyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateCompany200ApplicationJSON])
                res.create_company_200_application_json_object = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateCompany401ApplicationJSON])
                res.create_company_401_application_json_object = out

        return res

    def delete_company(self, request: operations.DeleteCompanyRequest) -> operations.DeleteCompanyResponse:
        r"""Delete a company
        Delete the given company from Codat.
        This operation is not reversible.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteCompanyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteCompany401ApplicationJSON])
                res.delete_company_401_application_json_object = out

        return res

    def get_company(self, request: operations.GetCompanyRequest) -> operations.GetCompanyResponse:
        r"""Get company
        Get metadata for a single company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCompanyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCompanyCompany])
                res.company = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCompany401ApplicationJSON])
                res.get_company_401_application_json_object = out

        return res

    def list_companies(self, request: operations.ListCompaniesRequest) -> operations.ListCompaniesResponse:
        r"""List companies
        List all companies that you have created in Codat.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/companies'
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListCompaniesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListCompaniesLinks])
                res.links = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListCompanies400ApplicationJSON])
                res.list_companies_400_application_json_object = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListCompanies401ApplicationJSON])
                res.list_companies_401_application_json_object = out

        return res

    def update_company(self, request: operations.UpdateCompanyRequest) -> operations.UpdateCompanyResponse:
        r"""Update company
        Updates the given company with a new name and description
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateCompanyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateCompanyCompany])
                res.company = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateCompany401ApplicationJSON])
                res.update_company_401_application_json_object = out

        return res

    