import requests
from . import utils
from codat.models import operations
from typing import Optional

class Expenses:
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

    
    def create_expense_dataset(self, request: operations.CreateExpenseDatasetRequest) -> operations.CreateExpenseDatasetResponse:
        r"""Create expense-transactions
        Create an expense transaction
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/expense-transactions", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateExpenseDatasetResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreateExpenseDataset200ApplicationJSON])
                res.create_expense_dataset_200_application_json_object = out

        return res

    
    def upload_attachment(self, request: operations.UploadAttachmentRequest) -> operations.UploadAttachmentResponse:
        r"""Upload attachment
        Creates an attachment in the accounting software against the given transactionId
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/syncs/{syncId}/transactions/{transactionId}/attachments", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("POST", url)
        content_type = r.headers.get("Content-Type")

        res = operations.UploadAttachmentResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.UploadAttachment200ApplicationJSON])
                res.upload_attachment_200_application_json_object = out

        return res

    