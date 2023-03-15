import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class SyncData:
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
        
    def check_data_status(self, request: operations.CheckDataStatusRequest) -> operations.CheckDataStatusResponse:
        r"""Get dataset status
        Check whether the dataset has been accepted and validated.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.CheckDataStatusRequest, base_url, '/meta/companies/{companyId}/pull/history/{datasetId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CheckDataStatusResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def send_orders_data(self, request: operations.SendOrdersDataRequest) -> operations.SendOrdersDataResponse:
        r"""Create orders dataset
        Create a dataset of the merchants sales
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.SendOrdersDataRequest, base_url, '/data/companies/{companyId}/sync/commerce-orders', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SendOrdersDataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SendOrdersData200ApplicationJSON])
                res.send_orders_data_200_application_json_object = out

        return res

    def send_payments_data(self, request: operations.SendPaymentsDataRequest) -> operations.SendPaymentsDataResponse:
        r"""Create payments dataset
        Create a dataset of the merchants payments.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.SendPaymentsDataRequest, base_url, '/data/companies/{companyId}/sync/commerce-payments', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SendPaymentsDataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SendPaymentsData200ApplicationJSON])
                res.send_payments_data_200_application_json_object = out

        return res

    def send_transactions_data(self, request: operations.SendTransactionsDataRequest) -> operations.SendTransactionsDataResponse:
        r"""Create transactions dataset
        Create a dataset of the merchants transactions
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.SendTransactionsDataRequest, base_url, '/data/companies/{companyId}/sync/commerce-transactions', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SendTransactionsDataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SendTransactionsData200ApplicationJSON])
                res.send_transactions_data_200_application_json_object = out

        return res

    