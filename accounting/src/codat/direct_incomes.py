import requests
from . import utils
from codat.models import operations
from typing import Optional

class DirectIncomes:
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

    
    def download_direct_income_attachment(self, request: operations.DownloadDirectIncomeAttachmentRequest) -> operations.DownloadDirectIncomeAttachmentResponse:
        r"""Download direct income attachment
        Downloads an attachment for the specified direct income for a given company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}/attachments/{attachmentId}/download", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DownloadDirectIncomeAttachmentResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def get_direct_income(self, request: operations.GetDirectIncomeRequest) -> operations.GetDirectIncomeResponse:
        r"""Get direct income
        Gets the specified direct income for a given company and connection.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDirectIncomeResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDirectIncomeSourceModifiedDate])
                res.source_modified_date = out

        return res

    
    def get_direct_income_attachment(self, request: operations.GetDirectIncomeAttachmentRequest) -> operations.GetDirectIncomeAttachmentResponse:
        r"""Get direct income attachment
        Gets the specified direct income attachment for a given company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}/attachments/{attachmentId}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDirectIncomeAttachmentResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDirectIncomeAttachmentAttachment])
                res.attachment = out

        return res

    
    def get_direct_incomes(self, request: operations.GetDirectIncomesRequest) -> operations.GetDirectIncomesResponse:
        r"""Get direct incomes
        Gets the direct incomes for a given company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/data/directIncomes", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDirectIncomesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDirectIncomesLinks])
                res.links = out

        return res

    
    def list_direct_income_attachments(self, request: operations.ListDirectIncomeAttachmentsRequest) -> operations.ListDirectIncomeAttachmentsResponse:
        r"""List direct income attachments
        Gets all attachments for the specified direct income for a given company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}/attachments", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListDirectIncomeAttachmentsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListDirectIncomeAttachmentsAttachments])
                res.attachments = out

        return res

    
    def post_direct_income(self, request: operations.PostDirectIncomeRequest) -> operations.PostDirectIncomeResponse:
        r"""Create direct income
        Posts a new direct income to the accounting package for a given company.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support POST methods.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/push/directIncomes", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostDirectIncomeResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PostDirectIncome200ApplicationJSON])
                res.post_direct_income_200_application_json_object = out

        return res

    
    def post_direct_income_attachment(self, request: operations.PostDirectIncomeAttachmentRequest) -> operations.PostDirectIncomeAttachmentResponse:
        r"""Create direct income attachment
        Posts a new direct income attachment for a given company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/push/directIncomes/{directIncomeId}/attachment", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PostDirectIncomeAttachmentResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    