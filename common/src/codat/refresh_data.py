import requests
from . import utils
from codat.models import operations
from typing import Optional

class RefreshData:
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

    
    def create_many_pull_operations(self, request: operations.CreateManyPullOperationsRequest) -> operations.CreateManyPullOperationsResponse:
        r"""Queue pull operations
        Refreshes all data types marked Fetch on first link.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/all", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("POST", url)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateManyPullOperationsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreateManyPullOperations401ApplicationJSON])
                res.create_many_pull_operations_401_application_json_object = out
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreateManyPullOperations404ApplicationJSON])
                res.create_many_pull_operations_404_application_json_object = out

        return res

    
    def create_pull_operation(self, request: operations.CreatePullOperationRequest) -> operations.CreatePullOperationResponse:
        r"""Queue pull operation
        Queue a single pull operation for the given company and data type.
        
        This will bring updated data into Codat from the linked integration for you to view.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/queue/{dataType}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("POST", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.CreatePullOperationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreatePullOperationPullOperation])
                res.pull_operation = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreatePullOperation401ApplicationJSON])
                res.create_pull_operation_401_application_json_object = out
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreatePullOperation404ApplicationJSON])
                res.create_pull_operation_404_application_json_object = out

        return res

    