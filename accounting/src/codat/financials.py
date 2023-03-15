import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Financials:
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
        
    def get_balance_sheet(self, request: operations.GetBalanceSheetRequest) -> operations.GetBalanceSheetResponse:
        r"""Get balance sheet
        Gets the latest balance sheet for a company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetBalanceSheetRequest, base_url, '/companies/{companyId}/data/financials/balanceSheet', request)
        
        query_params = utils.get_query_params(operations.GetBalanceSheetRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBalanceSheetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetBalanceSheet200ApplicationJSON])
                res.get_balance_sheet_200_application_json_object = out

        return res

    def get_cash_flow_statement(self, request: operations.GetCashFlowStatementRequest) -> operations.GetCashFlowStatementResponse:
        r"""Get cash flow statement
        Gets the latest cash flow statement for a company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCashFlowStatementRequest, base_url, '/companies/{companyId}/data/financials/cashFlowStatement', request)
        
        query_params = utils.get_query_params(operations.GetCashFlowStatementRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCashFlowStatementResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCashFlowStatement200ApplicationJSON])
                res.get_cash_flow_statement_200_application_json_object = out

        return res

    def get_profit_and_loss(self, request: operations.GetProfitAndLossRequest) -> operations.GetProfitAndLossResponse:
        r"""Get profit and loss
        Gets the latest profit and loss for a company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetProfitAndLossRequest, base_url, '/companies/{companyId}/data/financials/profitAndLoss', request)
        
        query_params = utils.get_query_params(operations.GetProfitAndLossRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetProfitAndLossResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetProfitAndLoss200ApplicationJSON])
                res.get_profit_and_loss_200_application_json_object = out

        return res

    