import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Reports:
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
        
    def get_accounts_for_enhanced_balance_sheet(self, request: operations.GetAccountsForEnhancedBalanceSheetRequest) -> operations.GetAccountsForEnhancedBalanceSheetResponse:
        r"""Enhanced Balance Sheet Accounts
        Gets a list of accounts with account categories per statement period, specific to balance sheet
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/reports/enhancedBalanceSheet/accounts', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAccountsForEnhancedBalanceSheetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAccountsForEnhancedBalanceSheetEnhancedReport])
                res.enhanced_report = out

        return res

    def get_accounts_for_enhanced_profit_and_loss(self, request: operations.GetAccountsForEnhancedProfitAndLossRequest) -> operations.GetAccountsForEnhancedProfitAndLossResponse:
        r"""Enhanced Profit and Loss Accounts
        Gets a list of accounts with account categories per statement period, specific to profit and loss
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/reports/enhancedProfitAndLoss/accounts', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAccountsForEnhancedProfitAndLossResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAccountsForEnhancedProfitAndLossEnhancedReport])
                res.enhanced_report = out

        return res

    def get_commerce_customer_retention_metrics(self, request: operations.GetCommerceCustomerRetentionMetricsRequest) -> operations.GetCommerceCustomerRetentionMetricsResponse:
        r"""Get the customer retention metrics for a specific company.
        Gets the customer retention metrics for a specific company connection, over one or more periods of time.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/customerRetention', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCommerceCustomerRetentionMetricsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCommerceCustomerRetentionMetrics200ApplicationJSON])
                res.get_commerce_customer_retention_metrics_200_application_json_object = out

        return res

    def get_commerce_lifetime_value_metrics(self, request: operations.GetCommerceLifetimeValueMetricsRequest) -> operations.GetCommerceLifetimeValueMetricsResponse:
        r"""Get the lifetime value metric for a specific company.
        Gets the lifetime value metric for a specific company connection, over one or more periods of time.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/lifetimeValue', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCommerceLifetimeValueMetricsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCommerceLifetimeValueMetrics200ApplicationJSON])
                res.get_commerce_lifetime_value_metrics_200_application_json_object = out

        return res

    def get_commerce_orders_metrics(self, request: operations.GetCommerceOrdersMetricsRequest) -> operations.GetCommerceOrdersMetricsResponse:
        r"""Get order information for a specific company
        Gets the order information for a specific company connection, over one or more periods of time.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/orders', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCommerceOrdersMetricsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCommerceOrdersMetrics200ApplicationJSON])
                res.get_commerce_orders_metrics_200_application_json_object = out

        return res

    def get_commerce_refunds_metrics(self, request: operations.GetCommerceRefundsMetricsRequest) -> operations.GetCommerceRefundsMetricsResponse:
        r"""Get the refunds information for a specific company
        Gets the refunds information for a specific company connection, over one or more periods of time.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/refunds', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCommerceRefundsMetricsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCommerceRefundsMetrics200ApplicationJSON])
                res.get_commerce_refunds_metrics_200_application_json_object = out

        return res

    def get_commerce_revenue_metrics(self, request: operations.GetCommerceRevenueMetricsRequest) -> operations.GetCommerceRevenueMetricsResponse:
        r"""Commerce Revenue Metrics
        Get the revenue and revenue growth for a specific company connection, over one or more periods of time.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/revenue', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCommerceRevenueMetricsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCommerceRevenueMetrics200ApplicationJSON])
                res.get_commerce_revenue_metrics_200_application_json_object = out

        return res

    def get_enhanced_balance_sheet(self, request: operations.GetEnhancedBalanceSheetRequest) -> operations.GetEnhancedBalanceSheetResponse:
        r"""Enhanced Balance Sheet
        Gets a fully categorized balance sheet statement for a given company, over one or more period(s).
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/enhancedBalanceSheet', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEnhancedBalanceSheetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEnhancedBalanceSheet200ApplicationJSON])
                res.get_enhanced_balance_sheet_200_application_json_object = out

        return res

    def get_enhanced_cash_flow_transactions(self, request: operations.GetEnhancedCashFlowTransactionsRequest) -> operations.GetEnhancedCashFlowTransactionsResponse:
        r"""Get enhanced cash flow report
        Gets a list of banking transactions and their categories.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/companies/{companyId}/reports/enhancedCashFlow/transactions', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEnhancedCashFlowTransactionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEnhancedCashFlowTransactionsEnhancedCashFlowTransactions])
                res.enhanced_cash_flow_transactions = out

        return res

    def get_enhanced_financial_metrics(self, request: operations.GetEnhancedFinancialMetricsRequest) -> operations.GetEnhancedFinancialMetricsResponse:
        r"""List finanicial metrics
        Gets all the available financial metrics for a given company, over one or more periods.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/financialMetrics', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEnhancedFinancialMetricsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEnhancedFinancialMetrics200ApplicationJSON])
                res.get_enhanced_financial_metrics_200_application_json_object = out

        return res

    def get_enhanced_profit_and_loss(self, request: operations.GetEnhancedProfitAndLossRequest) -> operations.GetEnhancedProfitAndLossResponse:
        r"""Enhanced Profit and Loss
        Gets a fully categorized profit and loss statement for a given company, over one or more period(s).
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/enhancedProfitAndLoss', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEnhancedProfitAndLossResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEnhancedProfitAndLoss200ApplicationJSON])
                res.get_enhanced_profit_and_loss_200_application_json_object = out

        return res

    def get_recurring_revenue_metrics(self, request: operations.GetRecurringRevenueMetricsRequest) -> operations.GetRecurringRevenueMetricsResponse:
        r"""Get key metrics for subscription revenue
        Gets key metrics for subscription revenue.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/subscriptions/mrr', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRecurringRevenueMetricsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetRecurringRevenueMetrics200ApplicationJSON])
                res.get_recurring_revenue_metrics_200_application_json_object = out

        return res

    def request_recurring_revenue_metrics(self, request: operations.RequestRecurringRevenueMetricsRequest) -> operations.RequestRecurringRevenueMetricsResponse:
        r"""Request production of key subscription revenue metrics
        Request production of key subscription revenue metrics.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/subscriptions/process', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RequestRecurringRevenueMetricsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.RequestRecurringRevenueMetrics200ApplicationJSON])
                res.request_recurring_revenue_metrics_200_application_json_object = out

        return res

    