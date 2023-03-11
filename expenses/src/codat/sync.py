import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Sync:
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
        
    def intiate_sync(self, request: operations.IntiateSyncRequest) -> operations.IntiateSyncResponse:
        r"""Initiate sync
        Initiate sync of pending transactions.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/sync/expenses/syncs', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.IntiateSyncResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 202:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.IntiateSync202ApplicationJSON])
                res.intiate_sync_202_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.IntiateSync400ApplicationJSON])
                res.intiate_sync_400_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.IntiateSync404ApplicationJSON])
                res.intiate_sync_404_application_json_object = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.IntiateSync422ApplicationJSON])
                res.intiate_sync_422_application_json_object = out

        return res

    