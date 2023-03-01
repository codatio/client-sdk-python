import requests
from . import utils
from codat.models import operations
from typing import Optional

class Connections:
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

    
    def create_data_connection(self, request: operations.CreateDataConnectionRequest) -> operations.CreateDataConnectionResponse:
        r"""Create a data connection
        Create a data connection for a company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("POST", url)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateDataConnectionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreateDataConnectionConnection])
                res.connection = out

        return res

    
    def delete_company_connection(self, request: operations.DeleteCompanyConnectionRequest) -> operations.DeleteCompanyConnectionResponse:
        r"""Delete connection
        Revoke and remove a connection from a company.
        This operation is not reversible - the end user would need to reauthorize a new data connection if you wish to view new data for this company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteCompanyConnectionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.DeleteCompanyConnection401ApplicationJSON])
                res.delete_company_connection_401_application_json_object = out
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.DeleteCompanyConnection404ApplicationJSON])
                res.delete_company_connection_404_application_json_object = out

        return res

    
    def get_companies_company_id_connections_connection_id_authorization(self, request: operations.GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationRequest) -> operations.GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationResponse:
        r"""Update authorization
        Update data connection's authorization.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/authorization", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompaniesCompanyIDConnectionsConnectionIDAuthorizationConnection])
                res.connection = out

        return res

    
    def get_company_connection(self, request: operations.GetCompanyConnectionRequest) -> operations.GetCompanyConnectionResponse:
        r"""Get connection
        Get a single connection for a company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCompanyConnectionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompanyConnectionConnection])
                res.connection = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompanyConnection401ApplicationJSON])
                res.get_company_connection_401_application_json_object = out
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompanyConnection404ApplicationJSON])
                res.get_company_connection_404_application_json_object = out

        return res

    
    def list_company_connections(self, request: operations.ListCompanyConnectionsRequest) -> operations.ListCompanyConnectionsResponse:
        r"""List connections
        List the connections for a company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListCompanyConnectionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListCompanyConnectionsLinks])
                res.links = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListCompanyConnections400ApplicationJSON])
                res.list_company_connections_400_application_json_object = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListCompanyConnections401ApplicationJSON])
                res.list_company_connections_401_application_json_object = out

        return res

    
    def patch_company_connection(self, request: operations.PatchCompanyConnectionRequest) -> operations.PatchCompanyConnectionResponse:
        r"""Unlink connection
        This allows you to deauthorize a connection, without deleting it from Codat. This means you can still view any data that has previously been pulled into Codat, and also lets you re-authorize in future if your customer wishes to resume sharing their data.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PatchCompanyConnectionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PatchCompanyConnectionConnection])
                res.connection = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PatchCompanyConnection401ApplicationJSON])
                res.patch_company_connection_401_application_json_object = out
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PatchCompanyConnection404ApplicationJSON])
                res.patch_company_connection_404_application_json_object = out

        return res

    