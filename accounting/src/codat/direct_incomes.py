import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class DirectIncomes:
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
        
    def create_direct_income(self, request: operations.CreateDirectIncomeRequest) -> operations.CreateDirectIncomeResponse:
        r"""Create direct income
        Posts a new direct income to the accounting package for a given company.
        
        Required data may vary by integration. To see what data to post, first call [Get create direct income model](https://docs.codat.io/accounting-api#/operations/get-create-directIncomes-model).
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating direct incomes.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateDirectIncomeRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/directIncomes', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateDirectIncomeRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateDirectIncomeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateDirectIncome200ApplicationJSON])
                res.create_direct_income_200_application_json_object = out

        return res

    def download_direct_income_attachment(self, request: operations.DownloadDirectIncomeAttachmentRequest) -> operations.DownloadDirectIncomeAttachmentResponse:
        r"""Download direct income attachment
        Downloads an attachment for the specified direct income for a given company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DownloadDirectIncomeAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}/attachments/{attachmentId}/download', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DownloadDirectIncomeAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def get_create_direct_incomes_model(self, request: operations.GetCreateDirectIncomesModelRequest) -> operations.GetCreateDirectIncomesModelResponse:
        r"""Get create direct income model
        Get create direct income model. Returns the expected data for the request payload.
        
        See the examples for integration-specific indicative models.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating direct incomes.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCreateDirectIncomesModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/directIncomes', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCreateDirectIncomesModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCreateDirectIncomesModelPushOption])
                res.push_option = out

        return res

    def get_direct_income(self, request: operations.GetDirectIncomeRequest) -> operations.GetDirectIncomeResponse:
        r"""Get direct income
        Gets the specified direct income for a given company and connection.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetDirectIncomeRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDirectIncomeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetDirectIncomeSourceModifiedDate])
                res.source_modified_date = out

        return res

    def get_direct_income_attachment(self, request: operations.GetDirectIncomeAttachmentRequest) -> operations.GetDirectIncomeAttachmentResponse:
        r"""Get direct income attachment
        Gets the specified direct income attachment for a given company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetDirectIncomeAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}/attachments/{attachmentId}', request)
        
        query_params = utils.get_query_params(operations.GetDirectIncomeAttachmentRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDirectIncomeAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetDirectIncomeAttachmentAttachment])
                res.attachment = out

        return res

    def get_direct_incomes(self, request: operations.GetDirectIncomesRequest) -> operations.GetDirectIncomesResponse:
        r"""Get direct incomes
        Gets the direct incomes for a given company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetDirectIncomesRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/directIncomes', request)
        
        query_params = utils.get_query_params(operations.GetDirectIncomesRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDirectIncomesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetDirectIncomesLinks])
                res.links = out

        return res

    def list_direct_income_attachments(self, request: operations.ListDirectIncomeAttachmentsRequest) -> operations.ListDirectIncomeAttachmentsResponse:
        r"""List direct income attachments
        Gets all attachments for the specified direct income for a given company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListDirectIncomeAttachmentsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}/attachments', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListDirectIncomeAttachmentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListDirectIncomeAttachmentsAttachments])
                res.attachments = out

        return res

    def post_direct_income_attachment(self, request: operations.PostDirectIncomeAttachmentRequest) -> operations.PostDirectIncomeAttachmentResponse:
        r"""Create direct income attachment
        Posts a new direct income attachment for a given company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostDirectIncomeAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/directIncomes/{directIncomeId}/attachment', request)
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostDirectIncomeAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    