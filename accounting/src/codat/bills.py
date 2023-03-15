import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Bills:
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
        
    def create_bill(self, request: operations.CreateBillRequest) -> operations.CreateBillResponse:
        r"""Create bill
        Posts a new bill to the accounting package for a given company.
        
        Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/accounting-api#/operations/get-create-update-bills-model).
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating a bill.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateBillRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/bills', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateBillRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateBillResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateBill200ApplicationJSON])
                res.create_bill_200_application_json_object = out

        return res

    def create_bill_attachments(self, request: operations.CreateBillAttachmentsRequest) -> operations.CreateBillAttachmentsResponse:
        r"""Create bill attachments
        Post bill attachments
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateBillAttachmentsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/bills/{billId}/attachments', request)
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateBillAttachmentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def delete_companies_company_id_connections_connection_id_push_bills_bill_id(self, request: operations.DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillsBillIDRequest) -> operations.DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillsBillIDResponse:
        r"""Delete bill
        Deletes a bill from the accounting package for a given company.
        
        > **Supported Integrations**
        > 
        > This functionality is currently only supported for our Oracle NetSuite integration. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillsBillIDRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/bills/{billId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillsBillIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillsBillID200ApplicationJSON])
                res.delete_companies_company_id_connections_connection_id_push_bills_bill_id_200_application_json_object = out
            if utils.match_content_type(content_type, 'application/xml'):
                res.body = http_res.content
            if utils.match_content_type(content_type, 'multipart/form-data'):
                res.body = http_res.content

        return res

    def download_bill_attachment(self, request: operations.DownloadBillAttachmentRequest) -> operations.DownloadBillAttachmentResponse:
        r"""Download bill attachment
        Download bill attachment
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DownloadBillAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments/{attachmentId}/download', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DownloadBillAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def get_bill(self, request: operations.GetBillRequest) -> operations.GetBillResponse:
        r"""Get bill
        Get bill
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetBillRequest, base_url, '/companies/{companyId}/data/bills/{billId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBillResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetBillSourceModifiedDate])
                res.source_modified_date = out

        return res

    def get_bill_attachment(self, request: operations.GetBillAttachmentRequest) -> operations.GetBillAttachmentResponse:
        r"""Get bill attachment
        Get bill attachment
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetBillAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments/{attachmentId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBillAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetBillAttachmentAttachment])
                res.attachment = out

        return res

    def get_bill_attachments(self, request: operations.GetBillAttachmentsRequest) -> operations.GetBillAttachmentsResponse:
        r"""List bill attachments
        Get bill attachments
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetBillAttachmentsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBillAttachmentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetBillAttachmentsAttachments])
                res.attachments = out

        return res

    def get_create_update_bills_model(self, request: operations.GetCreateUpdateBillsModelRequest) -> operations.GetCreateUpdateBillsModelResponse:
        r"""Get create/update bill model
        Get create/update bill model.
        
         > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating and updating a bill.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCreateUpdateBillsModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/bills', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCreateUpdateBillsModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCreateUpdateBillsModelPushOption])
                res.push_option = out

        return res

    def list_bills(self, request: operations.ListBillsRequest) -> operations.ListBillsResponse:
        r"""List bills
        Gets the latest bills for a company, with pagination
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListBillsRequest, base_url, '/companies/{companyId}/data/bills', request)
        
        query_params = utils.get_query_params(operations.ListBillsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListBillsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListBillsLinks])
                res.links = out

        return res

    def update_bill(self, request: operations.UpdateBillRequest) -> operations.UpdateBillResponse:
        r"""Update bill
        Posts an updated bill to the accounting package for a given company.
        
        Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/accounting-api#/operations/get-create-update-bills-model).
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support updating a bill.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateBillRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/bills/{billId}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.UpdateBillRequest, request)
        
        client = self._security_client
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateBillResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateBill200ApplicationJSON])
                res.update_bill_200_application_json_object = out

        return res

    