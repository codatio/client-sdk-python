import requests
from . import utils
from codat.models import operations
from typing import Optional

class BillCreditNotes:
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

    
    def get_bill_credit_note(self, request: operations.GetBillCreditNoteRequest) -> operations.GetBillCreditNoteResponse:
        r"""Get bill credit note
        Gets a single billCreditNote corresponding to the supplied Id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetBillCreditNoteResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetBillCreditNoteSourceModifiedDate])
                res.source_modified_date = out

        return res

    
    def list_bill_credit_notes(self, request: operations.ListBillCreditNotesRequest) -> operations.ListBillCreditNotesResponse:
        r"""List bill credit notes
        Gets a list of all bill credit notes for a company, with pagination
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/billCreditNotes", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListBillCreditNotesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListBillCreditNotesLinks])
                res.links = out

        return res

    
    def post_bill_credit_note(self, request: operations.PostBillCreditNoteRequest) -> operations.PostBillCreditNoteResponse:
        r"""Create bill credit note
        Posts a new billCreditNote to the accounting package for a given company.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support POST methods.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/push/billCreditNotes", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostBillCreditNoteResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PostBillCreditNote200ApplicationJSON])
                res.post_bill_credit_note_200_application_json_object = out

        return res

    
    def update_bill_credit_note(self, request: operations.UpdateBillCreditNoteRequest) -> operations.UpdateBillCreditNoteResponse:
        r"""Update bill credit note
        Posts an updated billCreditNote to the accounting package for a given company.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support PUT methods.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/push/billCreditNotes/{billCreditNoteId}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PUT", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateBillCreditNoteResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.UpdateBillCreditNote200ApplicationJSON])
                res.update_bill_credit_note_200_application_json_object = out

        return res

    