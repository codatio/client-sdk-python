import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Files:
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
        
    def download_files(self, request: operations.DownloadFilesRequest) -> operations.DownloadFilesResponse:
        r"""Download all files for a company
        You can specify a date to download specific files for.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DownloadFilesRequest, base_url, '/companies/{companyId}/files/download', request)
        
        query_params = utils.get_query_params(operations.DownloadFilesRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DownloadFilesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def list_files(self, request: operations.ListFilesRequest) -> operations.ListFilesResponse:
        r"""List all files uploaded by a company
        Returns an array of files that have been uploaded for a given company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListFilesRequest, base_url, '/companies/{companyId}/files', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListFilesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[operations.ListFilesFile]])
                res.files = out

        return res

    def upload_files(self, request: operations.UploadFilesRequest) -> operations.UploadFilesResponse:
        r"""Upload files for a company
        Upload files
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.UploadFilesRequest, base_url, '/companies/{companyId}/connections/{connectionId}/files', request)
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UploadFilesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    