import requests
from . import utils
from codat.models import operations
from typing import Optional

class DataStatus:
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

    
    def get_companies_company_id_data_status(self, request: operations.GetCompaniesCompanyIDDataStatusRequest) -> operations.GetCompaniesCompanyIDDataStatusResponse:
        r"""Get data status
        Get the state of each data type for a company
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/dataStatus", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCompaniesCompanyIDDataStatusResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompaniesCompanyIDDataStatus200ApplicationJSON])
                res.get_companies_company_id_data_status_200_application_json_object = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompaniesCompanyIDDataStatus401ApplicationJSON])
                res.get_companies_company_id_data_status_401_application_json_object = out
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompaniesCompanyIDDataStatus404ApplicationJSON])
                res.get_companies_company_id_data_status_404_application_json_object = out

        return res

    
    def get_company_data_history(self, request: operations.GetCompanyDataHistoryRequest) -> operations.GetCompanyDataHistoryResponse:
        r"""Get pull operations
        Gets the pull operation history (datasets) for a given company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/history", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCompanyDataHistoryResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompanyDataHistoryLinks])
                res.links = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompanyDataHistory400ApplicationJSON])
                res.get_company_data_history_400_application_json_object = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompanyDataHistory401ApplicationJSON])
                res.get_company_data_history_401_application_json_object = out
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompanyDataHistory404ApplicationJSON])
                res.get_company_data_history_404_application_json_object = out

        return res

    
    def get_pull_operation(self, request: operations.GetPullOperationRequest) -> operations.GetPullOperationResponse:
        r"""Get pull operation
        Retrieve information about a single dataset or pull operation.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/history/{datasetId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetPullOperationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetPullOperationPullOperation])
                res.pull_operation = out
        elif r.status_code == 401:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetPullOperation401ApplicationJSON])
                res.get_pull_operation_401_application_json_object = out
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetPullOperation404ApplicationJSON])
                res.get_pull_operation_404_application_json_object = out

        return res

    