import requests
from . import utils
from codat.models import operations
from typing import Optional

class SyncData:
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

    
    def check_data_status(self, request: operations.CheckDataStatusRequest) -> operations.CheckDataStatusResponse:
        r"""Get dataset status
        Check whether the dataset has been accepted and validated.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/meta/companies/{companyId}/pull/history/{datasetId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.CheckDataStatusResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def send_orders_data(self, request: operations.SendOrdersDataRequest) -> operations.SendOrdersDataResponse:
        r"""Create orders dataset
        Create a dataset of the merchants sales
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/sync/commerce-orders", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.SendOrdersDataResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.SendOrdersData200ApplicationJSON])
                res.send_orders_data_200_application_json_object = out

        return res

    
    def send_payments_data(self, request: operations.SendPaymentsDataRequest) -> operations.SendPaymentsDataResponse:
        r"""Create payments dataset
        Create a dataset of the merchants payments.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/sync/commerce-payments", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.SendPaymentsDataResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.SendPaymentsData200ApplicationJSON])
                res.send_payments_data_200_application_json_object = out

        return res

    
    def send_transactions_data(self, request: operations.SendTransactionsDataRequest) -> operations.SendTransactionsDataResponse:
        r"""Create transactions dataset
        Create a dataset of the merchants transactions
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/sync/commerce-transactions", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.SendTransactionsDataResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.SendTransactionsData200ApplicationJSON])
                res.send_transactions_data_200_application_json_object = out

        return res

    