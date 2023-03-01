import requests
from . import utils
from codat.models import operations
from typing import Optional

class Bills:
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

    
    def download_bill_attachment(self, request: operations.DownloadBillAttachmentRequest) -> operations.DownloadBillAttachmentResponse:
        r"""Download bill attachment
        Download bill attachment
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments/{attachmentId}/download", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DownloadBillAttachmentResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def get_bill(self, request: operations.GetBillRequest) -> operations.GetBillResponse:
        r"""Get bill
        Get bill
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/bills/{billId}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetBillResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetBillSourceModifiedDate])
                res.source_modified_date = out

        return res

    
    def get_bill_attachment(self, request: operations.GetBillAttachmentRequest) -> operations.GetBillAttachmentResponse:
        r"""Get bill attachment
        Get bill attachment
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments/{attachmentId}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetBillAttachmentResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetBillAttachmentAttachment])
                res.attachment = out

        return res

    
    def get_bill_attachments(self, request: operations.GetBillAttachmentsRequest) -> operations.GetBillAttachmentsResponse:
        r"""List bill attachments
        Get bill attachments
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetBillAttachmentsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetBillAttachmentsAttachments])
                res.attachments = out

        return res

    
    def list_bills(self, request: operations.ListBillsRequest) -> operations.ListBillsResponse:
        r"""List bills
        Gets the latest bills for a company, with pagination
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/bills", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListBillsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListBillsLinks])
                res.links = out

        return res

    
    def post_bill(self, request: operations.PostBillRequest) -> operations.PostBillResponse:
        r"""Create bill
        Posts a new bill to the accounting package for a given company.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support POST methods.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/push/bills", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostBillResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PostBill200ApplicationJSON])
                res.post_bill_200_application_json_object = out

        return res

    
    def post_bill_attachments(self, request: operations.PostBillAttachmentsRequest) -> operations.PostBillAttachmentsResponse:
        r"""Create bill attachments
        Post bill attachments
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/push/bills/{billId}/attachments", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PostBillAttachmentsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def update_bill(self, request: operations.UpdateBillRequest) -> operations.UpdateBillResponse:
        r"""Update bill
        Posts an updated bill to the accounting package for a given company.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support PUT methods.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/push/bills/{billId}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PUT", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateBillResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.UpdateBill200ApplicationJSON])
                res.update_bill_200_application_json_object = out

        return res

    