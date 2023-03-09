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
        
    def create_customer(self, request: operations.CreateCustomerRequest) -> operations.CreateCustomerResponse:
        r"""Create customer
        Posts an individual customer for a given company.
        
        Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating customers.
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

        res = operations.CreateCustomerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateCustomer200ApplicationJSON])
                res.create_customer_200_application_json_object = out

        return res

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

    def get_create_update_customers_model(self, request: operations.GetCreateUpdateCustomersModelRequest) -> operations.GetCreateUpdateCustomersModelResponse:
        r"""Get create/update customer model
        Get create/update customer model. Returns the expected data for the request payload.
        
        See the examples for integration-specific indicative models.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating and updating customers.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/connections/{connectionId}/options/customers', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCreateUpdateCustomersModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCreateUpdateCustomersModelPushOption])
                res.push_option = out

        return res

    def get_customer(self, request: operations.GetCustomerRequest) -> operations.GetCustomerResponse:
        r"""Get customer
        Gets a single customer corresponding to the given Id
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

    def update_customer(self, request: operations.UpdateCustomerRequest) -> operations.UpdateCustomerResponse:
        r"""Update customer
        Posts an updated customer for a given company.
        
        Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support updating customers.
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

    