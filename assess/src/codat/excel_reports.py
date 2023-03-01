import requests
from . import utils
from codat.models import operations
from typing import Optional

class ExcelReports:
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

    
    def get_accounting_marketing_metrics(self, request: operations.GetAccountingMarketingMetricsRequest) -> operations.GetAccountingMarketingMetricsResponse:
        r"""Get the marketing metrics from an accounting source for a given company.
        Request an Excel report for download.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/accountingMetrics/marketing", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAccountingMarketingMetricsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAccountingMarketingMetrics200ApplicationJSON])
                res.get_accounting_marketing_metrics_200_application_json_object = out

        return res

    
    def get_excel_report(self, request: operations.GetExcelReportRequest) -> operations.GetExcelReportResponse:
        r"""Download generated excel report
        Download the Excel report to a local drive.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/assess/excel/download", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("POST", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetExcelReportResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/octet-stream"):
                res.body = r.content

        return res

    
    def make_request_to_download_excel_report(self, request: operations.MakeRequestToDownloadExcelReportRequest) -> operations.MakeRequestToDownloadExcelReportResponse:
        r"""Request an Excel report for download
        Returns the status of the latest report requested.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/assess/excel", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.MakeRequestToDownloadExcelReportResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.MakeRequestToDownloadExcelReport200ApplicationJSON])
                res.make_request_to_download_excel_report_200_application_json_object = out

        return res

    
    def request_excel_report_for_download(self, request: operations.RequestExcelReportForDownloadRequest) -> operations.RequestExcelReportForDownloadResponse:
        r"""Request an Excel report for download
        Request an Excel report for download.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/assess/excel", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("POST", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.RequestExcelReportForDownloadResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.RequestExcelReportForDownload200ApplicationJSON])
                res.request_excel_report_for_download_200_application_json_object = out

        return res

    