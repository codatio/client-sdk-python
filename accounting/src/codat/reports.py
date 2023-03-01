import requests
from . import utils
from codat.models import operations
from typing import Optional

class Reports:
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

    
    def get_aged_creditors_report(self, request: operations.GetAgedCreditorsReportRequest) -> operations.GetAgedCreditorsReportResponse:
        r"""Aged creditors report
        Returns aged creditors report for company that shows the total balance owed by a business to its suppliers over time.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/reports/agedCreditor", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAgedCreditorsReportResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAgedCreditorsReportAgedCreditorsReport])
                res.aged_creditors_report = out

        return res

    
    def get_aged_debtors_report(self, request: operations.GetAgedDebtorsReportRequest) -> operations.GetAgedDebtorsReportResponse:
        r"""Aged debtors report
        Returns aged debtors report for company that shows the total outstanding balance due from customers to the business over time.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/reports/agedDebtor", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAgedDebtorsReportResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAgedDebtorsReportAgedDebtorsReport])
                res.aged_debtors_report = out

        return res

    
    def is_aged_creditors_report_available(self, request: operations.IsAgedCreditorsReportAvailableRequest) -> operations.IsAgedCreditorsReportAvailableResponse:
        r"""Aged creditors report available
        Indicates whether the aged creditor report is available for the company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/reports/agedCreditor/available", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.IsAgedCreditorsReportAvailableResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[bool])
                res.is_aged_creditors_report_available_200_application_json_boolean = out

        return res

    
    def is_aged_debtor_report_available(self, request: operations.IsAgedDebtorReportAvailableRequest) -> operations.IsAgedDebtorReportAvailableResponse:
        r"""Aged debtors report available
        Indicates whether the aged debtor report is available for the company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/reports/agedDebtor/available", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.IsAgedDebtorReportAvailableResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[bool])
                res.is_aged_debtor_report_available_200_application_json_boolean = out

        return res

    