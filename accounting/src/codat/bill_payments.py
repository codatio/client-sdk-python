import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class BillPayments:
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
        
    def create_bill_payment(self, request: operations.CreateBillPaymentRequest) -> operations.CreateBillPaymentResponse:
        r"""Create bill payments
        Posts a new bill payment to the accounting package for a given company.
        
        Required data may vary by integration. To see what data to post, first call [Get create bill payment model](https://docs.codat.io/accounting-api#/operations/get-create-billPayments-model).
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating bill payments.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateBillPaymentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/billPayments', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateBillPaymentRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateBillPaymentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateBillPayment200ApplicationJSON])
                res.create_bill_payment_200_application_json_object = out

        return res

    def delete_companies_company_id_connections_connection_id_push_bill_payments_bill_payment_id(self, request: operations.DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentIDRequest) -> operations.DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentIDResponse:
        r"""Delete bill payment
        Deletes a bill payment from the accounting package for a given company.
        
        > **Supported Integrations**
        > 
        > This functionality is currently only supported for our Oracle NetSuite integration. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentIDRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/billPayments/{billPaymentId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSON])
                res.delete_companies_company_id_connections_connection_id_push_bill_payments_bill_payment_id_200_application_json_object = out

        return res

    def get_bill_payments(self, request: operations.GetBillPaymentsRequest) -> operations.GetBillPaymentsResponse:
        r"""Get bill payment
        Get a bill payment
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetBillPaymentsRequest, base_url, '/companies/{companyId}/data/billPayments/{billPaymentId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBillPaymentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetBillPaymentsSourceModifiedDate])
                res.source_modified_date = out

        return res

    def get_create_bill_payments_model(self, request: operations.GetCreateBillPaymentsModelRequest) -> operations.GetCreateBillPaymentsModelResponse:
        r"""Get create bill payment model
        Get create bill payment model.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating and deleting bill payments.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCreateBillPaymentsModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/billPayments', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCreateBillPaymentsModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCreateBillPaymentsModelPushOption])
                res.push_option = out

        return res

    def list_bill_payments(self, request: operations.ListBillPaymentsRequest) -> operations.ListBillPaymentsResponse:
        r"""List bill payments
        Gets the latest billPayments for a company, with pagination
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListBillPaymentsRequest, base_url, '/companies/{companyId}/data/billPayments', request)
        
        query_params = utils.get_query_params(operations.ListBillPaymentsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListBillPaymentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListBillPaymentsLinks])
                res.links = out

        return res

    