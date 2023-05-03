# reports

## Overview

Data integrity is important

### Available Operations

* [get_accounts_for_enhanced_balance_sheet](#get_accounts_for_enhanced_balance_sheet) - Enhanced Balance Sheet Accounts
* [get_accounts_for_enhanced_profit_and_loss](#get_accounts_for_enhanced_profit_and_loss) - Enhanced Profit and Loss Accounts
* [get_commerce_customer_retention_metrics](#get_commerce_customer_retention_metrics) - Get the customer retention metrics for a specific company.
* [get_commerce_lifetime_value_metrics](#get_commerce_lifetime_value_metrics) - Get the lifetime value metric for a specific company.
* [get_commerce_orders_metrics](#get_commerce_orders_metrics) - Get order information for a specific company
* [get_commerce_refunds_metrics](#get_commerce_refunds_metrics) - Get the refunds information for a specific company
* [get_commerce_revenue_metrics](#get_commerce_revenue_metrics) - Commerce Revenue Metrics
* [get_enhanced_balance_sheet](#get_enhanced_balance_sheet) - Enhanced Balance Sheet
* [get_enhanced_cash_flow_transactions](#get_enhanced_cash_flow_transactions) - Get enhanced cash flow report
* [get_enhanced_financial_metrics](#get_enhanced_financial_metrics) - List financial metrics
* [get_enhanced_invoices_report](#get_enhanced_invoices_report) - Enhanced Invoices Report
* [get_enhanced_profit_and_loss](#get_enhanced_profit_and_loss) - Enhanced Profit and Loss
* [get_recurring_revenue_metrics](#get_recurring_revenue_metrics) - Get key metrics for subscription revenue
* [request_recurring_revenue_metrics](#request_recurring_revenue_metrics) - Request production of key subscription revenue metrics

## get_accounts_for_enhanced_balance_sheet

The Enhanced Balance Sheet Accounts endpoint returns a list of categorized accounts that appear on a company’s Balance Sheet along with a balance per financial statement date.

Codat suggests a category for each account automatically, but you can [change it](/docs/assess-categorizing-accounts-ecommerce-lending) to a more suitable one.

### Example Usage

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAccountsForEnhancedBalanceSheetRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    number_of_periods=979587,
    report_date='29-09-2020',
)

res = s.reports.get_accounts_for_enhanced_balance_sheet(req)

if res.enhanced_report is not None:
    # handle response
```

## get_accounts_for_enhanced_profit_and_loss

The Enhanced Profit and Loss Accounts endpoint returns a list of categorized accounts that appear on a company’s Profit and Loss. It also includes a balance per the financial statement date.

Codat suggests a category for each account automatically, but you can [change it](/docs/assess-categorizing-accounts-ecommerce-lending) to a more suitable one.

### Example Usage

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAccountsForEnhancedProfitAndLossRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    number_of_periods=120196,
    report_date='29-09-2020',
)

res = s.reports.get_accounts_for_enhanced_profit_and_loss(req)

if res.enhanced_report is not None:
    # handle response
```

## get_commerce_customer_retention_metrics

Gets the customer retention metrics for a specific company connection, over one or more periods of time.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCommerceCustomerRetentionMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=359444,
    period_length=296140,
    period_unit=shared.PeriodUnitEnum.WEEK,
    report_date='29-09-2020',
)

res = s.reports.get_commerce_customer_retention_metrics(req)

if res.report is not None:
    # handle response
```

## get_commerce_lifetime_value_metrics

Gets the lifetime value metric for a specific company connection, over one or more periods of time.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCommerceLifetimeValueMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=118727,
    period_length=688661,
    period_unit=shared.PeriodUnitEnum.WEEK,
    report_date='29-09-2020',
)

res = s.reports.get_commerce_lifetime_value_metrics(req)

if res.report is not None:
    # handle response
```

## get_commerce_orders_metrics

Gets the order information for a specific company connection, over one or more periods of time.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCommerceOrdersMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=880476,
    period_length=414263,
    period_unit=shared.PeriodUnitEnum.YEAR,
    report_date='29-09-2020',
)

res = s.reports.get_commerce_orders_metrics(req)

if res.report is not None:
    # handle response
```

## get_commerce_refunds_metrics

Gets the refunds information for a specific company connection, over one or more periods of time.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCommerceRefundsMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=64147,
    period_length=216822,
    period_unit=shared.PeriodUnitEnum.MONTH,
    report_date='29-09-2020',
)

res = s.reports.get_commerce_refunds_metrics(req)

if res.report is not None:
    # handle response
```

## get_commerce_revenue_metrics

Get the revenue and revenue growth for a specific company connection, over one or more periods of time.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCommerceRevenueMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=565189,
    period_length=566602,
    period_unit=shared.PeriodUnitEnum.YEAR,
    report_date='29-09-2020',
)

res = s.reports.get_commerce_revenue_metrics(req)

if res.report is not None:
    # handle response
```

## get_enhanced_balance_sheet

Gets a fully categorized balance sheet statement for a given company, over one or more period(s).

### Example Usage

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetEnhancedBalanceSheetRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=265389,
    period_length=508969,
    report_date='29-09-2020',
)

res = s.reports.get_enhanced_balance_sheet(req)

if res.report is not None:
    # handle response
```

## get_enhanced_cash_flow_transactions

The Enhanced Cash Flow Transactions endpoint provides a fully categorized list of banking transactions for a company. Accounts and transaction data are obtained from the company's banking data sources.

### Example Usage

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetEnhancedCashFlowTransactionsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    page=1,
    page_size=100,
    query='rem',
)

res = s.reports.get_enhanced_cash_flow_transactions(req)

if res.enhanced_cash_flow_transactions is not None:
    # handle response
```

## get_enhanced_financial_metrics

Gets all the available financial metrics for a given company, over one or more periods.

### Example Usage

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetEnhancedFinancialMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    number_of_periods=916723,
    period_length=93940,
    report_date='29-09-2020',
    show_metric_inputs=False,
)

res = s.reports.get_enhanced_financial_metrics(req)

if res.financial_metrics is not None:
    # handle response
```

## get_enhanced_invoices_report

Gets a list of invoices linked to the corresponding banking transaction

### Example Usage

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetEnhancedInvoicesReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    page=1,
    page_size=100,
    query='repudiandae',
)

res = s.reports.get_enhanced_invoices_report(req)

if res.enhanced_invoices_report is not None:
    # handle response
```

## get_enhanced_profit_and_loss

Gets a fully categorized profit and loss statement for a given company, over one or more period(s).

### Example Usage

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetEnhancedProfitAndLossRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=575947,
    period_length=83112,
    report_date='29-09-2020',
)

res = s.reports.get_enhanced_profit_and_loss(req)

if res.report is not None:
    # handle response
```

## get_recurring_revenue_metrics

Gets key metrics for subscription revenue.

### Example Usage

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetRecurringRevenueMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.reports.get_recurring_revenue_metrics(req)

if res.report is not None:
    # handle response
```

## request_recurring_revenue_metrics

Request production of key subscription revenue metrics.

### Example Usage

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.RequestRecurringRevenueMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.reports.request_recurring_revenue_metrics(req)

if res.report is not None:
    # handle response
```
