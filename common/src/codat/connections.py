import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Connections:
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
        
    def create_data_connection(self, request: operations.CreateDataConnectionRequest) -> operations.CreateDataConnectionResponse:
        r"""Create a data connection
        Create a data connection for a company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateDataConnectionRequest, base_url, '/companies/{companyId}/connections', request)
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateDataConnectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateDataConnectionConnection])
                res.connection = out

        return res

    def delete_company_connection(self, request: operations.DeleteCompanyConnectionRequest) -> operations.DeleteCompanyConnectionResponse:
        r"""Delete connection
        Revoke and remove a connection from a company.
        This operation is not reversible - the end user would need to reauthorize a new data connection if you wish to view new data for this company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteCompanyConnectionRequest, base_url, '/companies/{companyId}/connections/{connectionId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteCompanyConnectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteCompanyConnection401ApplicationJSON])
                res.delete_company_connection_401_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteCompanyConnection404ApplicationJSON])
                res.delete_company_connection_404_application_json_object = out

        return res

    def get_company_authorization(self, request: operations.GetCompanyAuthorizationRequest) -> operations.GetCompanyAuthorizationResponse:
        r"""Update authorization
        Update data connection's authorization.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCompanyAuthorizationRequest, base_url, '/companies/{companyId}/connections/{connectionId}/authorization', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCompanyAuthorizationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCompanyAuthorizationConnection])
                res.connection = out

        return res

    def get_company_connection(self, request: operations.GetCompanyConnectionRequest) -> operations.GetCompanyConnectionResponse:
        r"""Get connection
        Get a single connection for a company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCompanyConnectionRequest, base_url, '/companies/{companyId}/connections/{connectionId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCompanyConnectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCompanyConnectionConnection])
                res.connection = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCompanyConnection401ApplicationJSON])
                res.get_company_connection_401_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCompanyConnection404ApplicationJSON])
                res.get_company_connection_404_application_json_object = out

        return res

    def list_company_connections(self, request: operations.ListCompanyConnectionsRequest) -> operations.ListCompanyConnectionsResponse:
        r"""List connections
        List the connections for a company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListCompanyConnectionsRequest, base_url, '/companies/{companyId}/connections', request)
        
        query_params = utils.get_query_params(operations.ListCompanyConnectionsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListCompanyConnectionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListCompanyConnectionsLinks])
                res.links = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListCompanyConnections400ApplicationJSON])
                res.list_company_connections_400_application_json_object = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListCompanyConnections401ApplicationJSON])
                res.list_company_connections_401_application_json_object = out

        return res

    def unlink_company_connection(self, request: operations.UnlinkCompanyConnectionRequest) -> operations.UnlinkCompanyConnectionResponse:
        r"""Unlink connection
        This allows you to deauthorize a connection, without deleting it from Codat. This means you can still view any data that has previously been pulled into Codat, and also lets you re-authorize in future if your customer wishes to resume sharing their data.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.UnlinkCompanyConnectionRequest, base_url, '/companies/{companyId}/connections/{connectionId}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UnlinkCompanyConnectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UnlinkCompanyConnectionConnection])
                res.connection = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UnlinkCompanyConnection401ApplicationJSON])
                res.unlink_company_connection_401_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UnlinkCompanyConnection404ApplicationJSON])
                res.unlink_company_connection_404_application_json_object = out

        return res

    