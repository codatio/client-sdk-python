import requests
from . import utils
from codat.models import operations
from typing import Optional

class Financials:
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

    
    def get_balance_sheet(self, request: operations.GetBalanceSheetRequest) -> operations.GetBalanceSheetResponse:
        r"""Get balance sheet
        Gets the latest balance sheet for a company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/financials/balanceSheet", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetBalanceSheetResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetBalanceSheet200ApplicationJSON])
                res.get_balance_sheet_200_application_json_object = out

        return res

    
    def get_cash_flow_statement(self, request: operations.GetCashFlowStatementRequest) -> operations.GetCashFlowStatementResponse:
        r"""Get cash flow statement
        Gets the latest cash flow statement for a company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/financials/cashFlowStatement", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCashFlowStatementResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCashFlowStatement200ApplicationJSON])
                res.get_cash_flow_statement_200_application_json_object = out

        return res

    
    def get_profit_and_loss(self, request: operations.GetProfitAndLossRequest) -> operations.GetProfitAndLossResponse:
        r"""Get profit and loss
        Gets the latest profit and loss for a company.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/data/financials/profitAndLoss", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetProfitAndLossResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetProfitAndLoss200ApplicationJSON])
                res.get_profit_and_loss_200_application_json_object = out

        return res

    