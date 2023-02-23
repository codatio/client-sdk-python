import requests
from . import utils
from sdk.models import operations
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

    
    def get_companies_company_id_reports_enhanced_balanace_sheet_accounts(self, request: operations.GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsRequest) -> operations.GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsResponse:
        r"""Enhanced Balance Sheet Accounts
        Gets a list of accounts with account categories per statement period, specific to balance sheet
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/reports/enhancedBalanceSheet/accounts", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompaniesCompanyIDReportsEnhancedBalanaceSheetAccountsEnhancedReport])
                res.enhanced_report = out

        return res

    
    def get_companies_company_id_reports_enhanced_cash_flow_transactions(self, request: operations.GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsRequest) -> operations.GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsResponse:
        r"""Get enhanced cash flow report
        Gets a list of banking transactions and their categories.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/reports/enhancedCashFlow/transactions", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompaniesCompanyIDReportsEnhancedCashFlowTransactionsEnhancedCashFlowTransactions])
                res.enhanced_cash_flow_transactions = out

        return res

    
    def get_companies_company_id_reports_enhanced_profit_and_loss_accounts(self, request: operations.GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsRequest) -> operations.GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsResponse:
        r"""Enhanced Profit and Loss Accounts
        Gets a list of accounts with account categories per statement period, specific to profit and loss
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/reports/enhancedProfitAndLoss/accounts", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompaniesCompanyIDReportsEnhancedProfitAndLossAccountsEnhancedReport])
                res.enhanced_report = out

        return res

    
    def get_data_companies_company_id_connections_connection_id_assess_commerce_metrics_customer_retention(self, request: operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetentionRequest) -> operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetentionResponse:
        r"""Get the customer retention metrics for a specific company.
        Gets the customer retention metrics for a specific company connection, over one or more periods of time.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/customerRetention", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetentionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsCustomerRetention200ApplicationJSON])
                res.get_data_companies_company_id_connections_connection_id_assess_commerce_metrics_customer_retention_200_application_json_object = out

        return res

    
    def get_data_companies_company_id_connections_connection_id_assess_commerce_metrics_lifetime_value(self, request: operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsLifetimeValueRequest) -> operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsLifetimeValueResponse:
        r"""Get the lifetime value metric for a specific company.
        Gets the lifetime value metric for a specific company connection, over one or more periods of time.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/lifetimeValue", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsLifetimeValueResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsLifetimeValue200ApplicationJSON])
                res.get_data_companies_company_id_connections_connection_id_assess_commerce_metrics_lifetime_value_200_application_json_object = out

        return res

    
    def get_data_companies_company_id_connections_connection_id_assess_commerce_metrics_orders(self, request: operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsOrdersRequest) -> operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsOrdersResponse:
        r"""Get order information for a specific company
        Gets the order information for a specific company connection, over one or more periods of time.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/orders", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsOrdersResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsOrders200ApplicationJSON])
                res.get_data_companies_company_id_connections_connection_id_assess_commerce_metrics_orders_200_application_json_object = out

        return res

    
    def get_data_companies_company_id_connections_connection_id_assess_commerce_metrics_refunds(self, request: operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsRefundsRequest) -> operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsRefundsResponse:
        r"""Get the refunds information for a specific company
        Gets the refunds information for a specific company connection, over one or more periods of time.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/refunds", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsRefundsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsRefunds200ApplicationJSON])
                res.get_data_companies_company_id_connections_connection_id_assess_commerce_metrics_refunds_200_application_json_object = out

        return res

    
    def get_data_companies_company_id_connections_connection_id_assess_commerce_metrics_revenue(self, request: operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsRevenueRequest) -> operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsRevenueResponse:
        r"""Commerce Revenue Metrics
        Get the revenue and revenue growth for a specific company connection, over one or more periods of time.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/revenue", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsRevenueResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessCommerceMetricsRevenue200ApplicationJSON])
                res.get_data_companies_company_id_connections_connection_id_assess_commerce_metrics_revenue_200_application_json_object = out

        return res

    
    def get_data_companies_company_id_connections_connection_id_assess_enhanced_balance_sheet(self, request: operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheetRequest) -> operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheetResponse:
        r"""Enhanced Balance Sheet
        Gets a fully categorized balance sheet statement for a given company, over one or more period(s).
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/enhancedBalanceSheet", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheetResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedBalanceSheet200ApplicationJSON])
                res.get_data_companies_company_id_connections_connection_id_assess_enhanced_balance_sheet_200_application_json_object = out

        return res

    
    def get_data_companies_company_id_connections_connection_id_assess_enhanced_profit_and_loss(self, request: operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLossRequest) -> operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLossResponse:
        r"""Enhanced Profit and Loss
        Gets a fully categorized profit and loss statement for a given company, over one or more period(s).
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/enhancedProfitAndLoss", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLossResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessEnhancedProfitAndLoss200ApplicationJSON])
                res.get_data_companies_company_id_connections_connection_id_assess_enhanced_profit_and_loss_200_application_json_object = out

        return res

    
    def get_data_companies_company_id_connections_connection_id_assess_financial_metrics(self, request: operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetricsRequest) -> operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetricsResponse:
        r"""List finanicial metrics
        Gets all the available financial metrics for a given company, over one or more periods.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/financialMetrics", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetricsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessFinancialMetrics200ApplicationJSON])
                res.get_data_companies_company_id_connections_connection_id_assess_financial_metrics_200_application_json_object = out

        return res

    
    def get_data_companies_company_id_connections_connection_id_assess_subscriptions_mrr(self, request: operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessSubscriptionsMrrRequest) -> operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessSubscriptionsMrrResponse:
        r"""Get key metrics for subscription revenue
        Gets key metrics for subscription revenue.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/subscriptions/mrr", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessSubscriptionsMrrResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessSubscriptionsMrr200ApplicationJSON])
                res.get_data_companies_company_id_connections_connection_id_assess_subscriptions_mrr_200_application_json_object = out

        return res

    
    def get_data_companies_company_id_connections_connection_id_assess_subscriptions_process(self, request: operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessSubscriptionsProcessRequest) -> operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessSubscriptionsProcessResponse:
        r"""Request production of key subscription revenue metrics
        Request production of key subscription revenue metrics.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/subscriptions/process", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessSubscriptionsProcessResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessSubscriptionsProcess200ApplicationJSON])
                res.get_data_companies_company_id_connections_connection_id_assess_subscriptions_process_200_application_json_object = out

        return res

    