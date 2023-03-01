import requests
from . import utils
from codat.models import operations
from typing import Optional

class CompanyManagement:
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

    
    def add_data_connection(self, request: operations.AddDataConnectionRequest) -> operations.AddDataConnectionResponse:
        r"""Create data connection
        Create a data connection.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/meta/companies/{companyId}/connections", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.AddDataConnectionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.AddDataConnection200ApplicationJSON])
                res.add_data_connection_200_application_json_object = out

        return res

    
    def companies(self, request: operations.CompaniesRequest) -> operations.CompaniesResponse:
        r"""List companies
        Retrieve a list of all companies the client has created.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/meta/companies"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.CompaniesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.Companies200ApplicationJSON])
                res.companies_200_application_json_object = out

        return res

    
    def get_dataconnections(self, request: operations.GetDataconnectionsRequest) -> operations.GetDataconnectionsResponse:
        r"""List connections
        Retrieve previously created data connections.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/meta/companies/{companyId}/connections", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataconnectionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataconnections200ApplicationJSON])
                res.get_dataconnections_200_application_json_object = out

        return res

    
    def post_companies(self, request: operations.PostCompaniesRequest) -> operations.PostCompaniesResponse:
        r"""Create a Sync for commerce company
        Creates a Codat company with a commerce partner data connection.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/meta/companies/sync"
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostCompaniesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PostCompanies200ApplicationJSON])
                res.post_companies_200_application_json_object = out

        return res

    
    def update_data_connection(self, request: operations.UpdateDataConnectionRequest) -> operations.UpdateDataConnectionResponse:
        r"""Update data connection
        Update a data connection
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/meta/companies/{companyId}/connections/{connectionId}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateDataConnectionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.UpdateDataConnection200ApplicationJSON])
                res.update_data_connection_200_application_json_object = out

        return res

    