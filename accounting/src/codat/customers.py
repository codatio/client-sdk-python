import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Customers:
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
        
    def download_customer_attachment(self, request: operations.DownloadCustomerAttachmentRequest) -> operations.DownloadCustomerAttachmentResponse:
        r"""Download customer attachment
        Download customer attachment
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments/{attachmentId}/download', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DownloadCustomerAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def get_customer(self, request: operations.GetCustomerRequest) -> operations.GetCustomerResponse:
        r"""Get customer
        Gets a single customer corresponding to the supplied Id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/data/customers/{customerId}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCustomerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCustomerSourceModifiedDate])
                res.source_modified_date = out

        return res

    def get_customer_attachment(self, request: operations.GetCustomerAttachmentRequest) -> operations.GetCustomerAttachmentResponse:
        r"""Get customer attachment
        Get  customer attachment
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments/{attachmentId}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCustomerAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCustomerAttachmentAttachment])
                res.attachment = out

        return res

    def get_customer_attachments(self, request: operations.GetCustomerAttachmentsRequest) -> operations.GetCustomerAttachmentsResponse:
        r"""List customer attachments
        Get customer attachments
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCustomerAttachmentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCustomerAttachmentsAttachments])
                res.attachments = out

        return res

    def get_customers(self, request: operations.GetCustomersRequest) -> operations.GetCustomersResponse:
        r"""List customers
        Gets the latest customers for a company, with pagination
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/data/customers', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCustomersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCustomersLinks])
                res.links = out

        return res

    def post_customer(self, request: operations.PostCustomerRequest) -> operations.PostCustomerResponse:
        r"""Create customer
        Posts an individual customer for a given company.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support POST methods.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/connections/{connectionId}/push/customers', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostCustomerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostCustomer200ApplicationJSON])
                res.post_customer_200_application_json_object = out

        return res

    def update_customer(self, request: operations.UpdateCustomerRequest) -> operations.UpdateCustomerResponse:
        r"""Update customer
        Posts an updated customer for a given company.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support PUT methods.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/connections/{connectionId}/push/customers/{customerId}', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateCustomerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateCustomer200ApplicationJSON])
                res.update_customer_200_application_json_object = out

        return res

    