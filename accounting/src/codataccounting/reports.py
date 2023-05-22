"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from codataccounting.models import operations, shared
from typing import Optional

class Reports:
    r"""Reports"""
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
        
    
    def get_aged_creditors_report(self, request: operations.GetAgedCreditorsReportRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetAgedCreditorsReportResponse:
        r"""Aged creditors report
        Returns aged creditors report for company that shows the total balance owed by a business to its suppliers over time.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetAgedCreditorsReportRequest, base_url, '/companies/{companyId}/reports/agedCreditor', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetAgedCreditorsReportRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url, params=query_params, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAgedCreditorsReportResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AgedCreditorReport])
                res.aged_creditor_report = out

        return res

    
    def get_aged_debtors_report(self, request: operations.GetAgedDebtorsReportRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetAgedDebtorsReportResponse:
        r"""Aged debtors report
        Returns aged debtors report for company that shows the total outstanding balance due from customers to the business over time.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetAgedDebtorsReportRequest, base_url, '/companies/{companyId}/reports/agedDebtor', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetAgedDebtorsReportRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url, params=query_params, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAgedDebtorsReportResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AgedDebtorReport])
                res.aged_debtor_report = out

        return res

    
    def get_balance_sheet(self, request: operations.GetBalanceSheetRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetBalanceSheetResponse:
        r"""Get balance sheet
        Gets the latest balance sheet for a company.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetBalanceSheetRequest, base_url, '/companies/{companyId}/data/financials/balanceSheet', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetBalanceSheetRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url, params=query_params, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBalanceSheetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BalanceSheet1])
                res.balance_sheet = out

        return res

    
    def get_cash_flow_statement(self, request: operations.GetCashFlowStatementRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetCashFlowStatementResponse:
        r"""Get cash flow statement
        Gets the latest cash flow statement for a company.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCashFlowStatementRequest, base_url, '/companies/{companyId}/data/financials/cashFlowStatement', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetCashFlowStatementRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url, params=query_params, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCashFlowStatementResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CashFlowStatement1])
                res.cash_flow_statement = out

        return res

    
    def get_profit_and_loss(self, request: operations.GetProfitAndLossRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetProfitAndLossResponse:
        r"""Get profit and loss
        Gets the latest profit and loss for a company.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetProfitAndLossRequest, base_url, '/companies/{companyId}/data/financials/profitAndLoss', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetProfitAndLossRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url, params=query_params, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetProfitAndLossResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ProfitAndLossReport1])
                res.profit_and_loss_report = out

        return res

    
    def is_aged_creditors_report_available(self, request: operations.IsAgedCreditorsReportAvailableRequest, retries: Optional[utils.RetryConfig] = None) -> operations.IsAgedCreditorsReportAvailableResponse:
        r"""Aged creditors report available
        Indicates whether the aged creditor report is available for the company.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.IsAgedCreditorsReportAvailableRequest, base_url, '/companies/{companyId}/reports/agedCreditor/available', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.IsAgedCreditorsReportAvailableResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[bool])
                res.is_aged_creditors_report_available_200_application_json_boolean = out

        return res

    
    def is_aged_debtor_report_available(self, request: operations.IsAgedDebtorReportAvailableRequest, retries: Optional[utils.RetryConfig] = None) -> operations.IsAgedDebtorReportAvailableResponse:
        r"""Aged debtors report available
        Indicates whether the aged debtor report is available for the company.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.IsAgedDebtorReportAvailableRequest, base_url, '/companies/{companyId}/reports/agedDebtor/available', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.IsAgedDebtorReportAvailableResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[bool])
                res.is_aged_debtor_report_available_200_application_json_boolean = out

        return res

    