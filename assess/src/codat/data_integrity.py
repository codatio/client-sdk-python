import requests
from . import utils
from codat.models import operations
from typing import Optional

class DataIntegrity:
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

    
    def get_data_integrity_details(self, request: operations.GetDataIntegrityDetailsRequest) -> operations.GetDataIntegrityDetailsResponse:
        r"""Lists data integrity details for date type
        Gets record-by-record match results for a given company and datatype, optionally restricted by a Codat query string.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/assess/dataTypes/{dataType}/dataIntegrity/details", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataIntegrityDetailsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataIntegrityDetailsLinks])
                res.links = out

        return res

    
    def get_data_integrity_status(self, request: operations.GetDataIntegrityStatusRequest) -> operations.GetDataIntegrityStatusResponse:
        r"""Get data integrity status
        Gets match status for a given company and datatype.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/assess/dataTypes/{dataType}/dataIntegrity/status", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataIntegrityStatusResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataIntegrityStatus200ApplicationJSON])
                res.get_data_integrity_status_200_application_json_object = out

        return res

    
    def get_data_integrity_summaries(self, request: operations.GetDataIntegritySummariesRequest) -> operations.GetDataIntegritySummariesResponse:
        r"""Get data integrity summary
        Gets match summary for a given company and datatype, optionally restricted by a Codat query string.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/assess/dataTypes/{dataType}/dataIntegrity/summaries", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataIntegritySummariesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataIntegritySummaries200ApplicationJSON])
                res.get_data_integrity_summaries_200_application_json_object = out

        return res

    