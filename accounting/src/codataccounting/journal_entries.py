"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from codataccounting.models import operations, shared
from typing import Optional

class JournalEntries:
    r"""Journal entries"""
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
        
    def create_journal_entry(self, request: operations.CreateJournalEntryRequest) -> operations.CreateJournalEntryResponse:
        r"""Create journal entry
        Posts a new journalEntry to the accounting package for a given company.
        
        Required data may vary by integration. To see what data to post, first call [Get create journal entry model](https://docs.codat.io/accounting-api#/operations/get-create-journalEntries-model).
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) for integrations that support creating journal entries.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateJournalEntryRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/journalEntries', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "journal_entry", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateJournalEntryRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateJournalEntryResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateJournalEntryResponse])
                res.create_journal_entry_response = out

        return res

    def delete_journal_entry(self, request: operations.DeleteJournalEntryRequest) -> operations.DeleteJournalEntryResponse:
        r"""Delete journal entry
        Deletes a journal entry from the accounting package for a given company.
        
        > **Supported Integrations**
        > 
        > This functionality is currently only supported for our QuickBooks Online integration. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteJournalEntryRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/journalEntries/{journalEntryId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteJournalEntryResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PushOperationSummary])
                res.push_operation_summary = out

        return res

    def get_create_journal_entries_model(self, request: operations.GetCreateJournalEntriesModelRequest) -> operations.GetCreateJournalEntriesModelResponse:
        r"""Get create journal entry model
        Get create journal entry model. Returns the expected data for the request payload.
        
        See the examples for integration-specific indicative models.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) for integrations that support creating journal entries.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCreateJournalEntriesModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/journalEntries', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCreateJournalEntriesModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PushOption])
                res.push_option = out

        return res

    def get_journal_entry(self, request: operations.GetJournalEntryRequest) -> operations.GetJournalEntryResponse:
        r"""Get journal entry
        Gets a single JournalEntry corresponding to the given ID.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetJournalEntryRequest, base_url, '/companies/{companyId}/data/journalEntries/{journalEntryId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetJournalEntryResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.JournalEntry])
                res.journal_entry = out

        return res

    def list_journal_entries(self, request: operations.ListJournalEntriesRequest) -> operations.ListJournalEntriesResponse:
        r"""List journal entries
        Gets the latest journal entries for a company, with pagination
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListJournalEntriesRequest, base_url, '/companies/{companyId}/data/journalEntries', request)
        
        query_params = utils.get_query_params(operations.ListJournalEntriesRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListJournalEntriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.JournalEntries])
                res.journal_entries = out

        return res

    