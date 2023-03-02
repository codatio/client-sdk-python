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
        r"""Create a company
        Create a new company
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/companies"
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateCompanyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreateCompany200ApplicationJSON])
                res.create_company_200_application_json_object = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreateCompany401ApplicationJSON])
                res.create_company_401_application_json_object = out

        return res

    
    def delete_companies_company_id(self, request: operations.DeleteCompaniesCompanyIDRequest) -> operations.DeleteCompaniesCompanyIDResponse:
        r"""Delete a company
        Delete the given company from Codat.
        This operation is not reversible.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteCompaniesCompanyIDResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.DeleteCompaniesCompanyID401ApplicationJSON])
                res.delete_companies_company_id_401_application_json_object = out

        return res

    
    def get_companies_company_id(self, request: operations.GetCompaniesCompanyIDRequest) -> operations.GetCompaniesCompanyIDResponse:
        r"""Get company
        Get metadata for a single company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCompaniesCompanyIDResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompaniesCompanyIDCompany])
                res.company = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompaniesCompanyID401ApplicationJSON])
                res.get_companies_company_id_401_application_json_object = out

        return res

    
    def list_companies(self, request: operations.ListCompaniesRequest) -> operations.ListCompaniesResponse:
        r"""List companies
        List all companies that you have created in Codat.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/companies"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListCompaniesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListCompaniesLinks])
                res.links = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListCompanies400ApplicationJSON])
                res.list_companies_400_application_json_object = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListCompanies401ApplicationJSON])
                res.list_companies_401_application_json_object = out

        return res

    
    def put_companies_company_id(self, request: operations.PutCompaniesCompanyIDRequest) -> operations.PutCompaniesCompanyIDResponse:
        r"""Update a company
        Updates the given company with a new name and description
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PutCompaniesCompanyIDResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PutCompaniesCompanyIDCompany])
                res.company = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PutCompaniesCompanyID401ApplicationJSON])
                res.put_companies_company_id_401_application_json_object = out

        return res

    