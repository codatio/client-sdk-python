import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class CompanyManagement:
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
        
    def add_data_connection(self, request: operations.AddDataConnectionRequest) -> operations.AddDataConnectionResponse:
        r"""Create data connection
        Create a data connection.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.AddDataConnectionRequest, base_url, '/meta/companies/{companyId}/connections', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'string')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AddDataConnectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.AddDataConnection200ApplicationJSON])
                res.add_data_connection_200_application_json_object = out

        return res

    def companies(self, request: operations.CompaniesRequest) -> operations.CompaniesResponse:
        r"""List companies
        Retrieve a list of all companies the client has created.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/meta/companies'
        
        query_params = utils.get_query_params(operations.CompaniesRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CompaniesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.Companies200ApplicationJSON])
                res.companies_200_application_json_object = out

        return res

    def get_dataconnections(self, request: operations.GetDataconnectionsRequest) -> operations.GetDataconnectionsResponse:
        r"""List connections
        Retrieve previously created data connections.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetDataconnectionsRequest, base_url, '/meta/companies/{companyId}/connections', request)
        
        query_params = utils.get_query_params(operations.GetDataconnectionsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDataconnectionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetDataconnections200ApplicationJSON])
                res.get_dataconnections_200_application_json_object = out

        return res

    def post_companies(self, request: operations.PostCompaniesRequestBody) -> operations.PostCompaniesResponse:
        r"""Create a Sync for Commerce company
        Creates a Codat company with a commerce partner data connection.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/meta/companies/sync'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostCompaniesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostCompanies200ApplicationJSON])
                res.post_companies_200_application_json_object = out

        return res

    def update_data_connection(self, request: operations.UpdateDataConnectionRequest) -> operations.UpdateDataConnectionResponse:
        r"""Update data connection
        Update a data connection
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateDataConnectionRequest, base_url, '/meta/companies/{companyId}/connections/{connectionId}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateDataConnectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateDataConnection200ApplicationJSON])
                res.update_data_connection_200_application_json_object = out

        return res

    