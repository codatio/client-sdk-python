# reports

## Overview

Data integrity is important

### Available Operations

* [get_accounts_for_enhanced_balance_sheet](#get_accounts_for_enhanced_balance_sheet) - Get enhanced balance sheet accounts
* [get_accounts_for_enhanced_profit_and_loss](#get_accounts_for_enhanced_profit_and_loss) - Get enhanced profit and loss accounts
* [get_commerce_customer_retention_metrics](#get_commerce_customer_retention_metrics) - Get customer retention metrics
* [get_commerce_lifetime_value_metrics](#get_commerce_lifetime_value_metrics) - Get lifetime value metric
* [get_commerce_orders_metrics](#get_commerce_orders_metrics) - Get orders report
* [get_commerce_refunds_metrics](#get_commerce_refunds_metrics) - Get refunds report
* [get_commerce_revenue_metrics](#get_commerce_revenue_metrics) - Get commerce revenue metrics
* [get_enhanced_cash_flow_transactions](#get_enhanced_cash_flow_transactions) - Get enhanced cash flow report
* [get_enhanced_invoices_report](#get_enhanced_invoices_report) - Get enhanced invoices report
* [get_loan_summary](#get_loan_summary) - Get enhanced loan summaries
* [get_recurring_revenue_metrics](#get_recurring_revenue_metrics) - Get key subscription revenue metrics
* [list_loan_transactions](#list_loan_transactions) - List enhanced loan transactions
* [request_recurring_revenue_metrics](#request_recurring_revenue_metrics) - Generate key subscription revenue metrics

## get_accounts_for_enhanced_balance_sheet

The Enhanced Balance Sheet Accounts endpoint returns a list of categorized accounts that appear on a company’s Balance Sheet along with a balance per financial statement date.

Codat suggests a category for each account automatically, but you can [change it](/docs/assess-categorizing-accounts-ecommerce-lending) to a more suitable one.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountsForEnhancedBalanceSheetRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    number_of_periods=623564,
    report_date='29-09-2020',
)

res = s.reports.get_accounts_for_enhanced_balance_sheet(req)

if res.enhanced_report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetAccountsForEnhancedBalanceSheetRequest](../../models/operations/getaccountsforenhancedbalancesheetrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |


### Response

**[operations.GetAccountsForEnhancedBalanceSheetResponse](../../models/operations/getaccountsforenhancedbalancesheetresponse.md)**


## get_accounts_for_enhanced_profit_and_loss

The Enhanced Profit and Loss Accounts endpoint returns a list of categorized accounts that appear on a company’s Profit and Loss. It also includes a balance per the financial statement date.

Codat suggests a category for each account automatically, but you can [change it](/docs/assess-categorizing-accounts-ecommerce-lending) to a more suitable one.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountsForEnhancedProfitAndLossRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    number_of_periods=645894,
    report_date='29-09-2020',
)

res = s.reports.get_accounts_for_enhanced_profit_and_loss(req)

if res.enhanced_report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetAccountsForEnhancedProfitAndLossRequest](../../models/operations/getaccountsforenhancedprofitandlossrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |


### Response

**[operations.GetAccountsForEnhancedProfitAndLossResponse](../../models/operations/getaccountsforenhancedprofitandlossresponse.md)**


## get_commerce_customer_retention_metrics

Gets the customer retention metrics for a specific company connection, over one or more periods of time.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCommerceCustomerRetentionMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=384382,
    period_length=437587,
    period_unit=shared.PeriodUnit.WEEK,
    report_date='29-09-2020',
)

res = s.reports.get_commerce_customer_retention_metrics(req)

if res.report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetCommerceCustomerRetentionMetricsRequest](../../models/operations/getcommercecustomerretentionmetricsrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |


### Response

**[operations.GetCommerceCustomerRetentionMetricsResponse](../../models/operations/getcommercecustomerretentionmetricsresponse.md)**


## get_commerce_lifetime_value_metrics

Gets the lifetime value metric for a specific company connection, over one or more periods of time.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCommerceLifetimeValueMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=891773,
    period_length=56713,
    period_unit=shared.PeriodUnit.YEAR,
    report_date='29-09-2020',
)

res = s.reports.get_commerce_lifetime_value_metrics(req)

if res.report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetCommerceLifetimeValueMetricsRequest](../../models/operations/getcommercelifetimevaluemetricsrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |


### Response

**[operations.GetCommerceLifetimeValueMetricsResponse](../../models/operations/getcommercelifetimevaluemetricsresponse.md)**


## get_commerce_orders_metrics

Gets the order information for a specific company connection, over one or more periods of time.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCommerceOrdersMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=272656,
    period_length=383441,
    period_unit=shared.PeriodUnit.WEEK,
    report_date='29-09-2020',
)

res = s.reports.get_commerce_orders_metrics(req)

if res.report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetCommerceOrdersMetricsRequest](../../models/operations/getcommerceordersmetricsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |


### Response

**[operations.GetCommerceOrdersMetricsResponse](../../models/operations/getcommerceordersmetricsresponse.md)**


## get_commerce_refunds_metrics

Gets the refunds information for a specific company connection, over one or more periods of time.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCommerceRefundsMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=791725,
    period_length=812169,
    period_unit=shared.PeriodUnit.MONTH,
    report_date='29-09-2020',
)

res = s.reports.get_commerce_refunds_metrics(req)

if res.report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCommerceRefundsMetricsRequest](../../models/operations/getcommercerefundsmetricsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.GetCommerceRefundsMetricsResponse](../../models/operations/getcommercerefundsmetricsresponse.md)**


## get_commerce_revenue_metrics

Get the revenue and revenue growth for a specific company connection, over one or more periods of time.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCommerceRevenueMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=479977,
    period_length=568045,
    period_unit=shared.PeriodUnit.WEEK,
    report_date='29-09-2020',
)

res = s.reports.get_commerce_revenue_metrics(req)

if res.report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCommerceRevenueMetricsRequest](../../models/operations/getcommercerevenuemetricsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.GetCommerceRevenueMetricsResponse](../../models/operations/getcommercerevenuemetricsresponse.md)**


## get_enhanced_cash_flow_transactions

> **Categorization engine**
> 
> The categorization engine uses machine learning and has been fully trained against Plaid and TrueLayer banking data sources. It is not fully trained against the Basiq banking data source.

The Enhanced Cash Flow Transactions endpoint provides a fully categorized list of banking transactions for a company. Accounts and transaction data are obtained from the company's banking data sources.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetEnhancedCashFlowTransactionsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    page=1,
    page_size=100,
    query='recusandae',
)

res = s.reports.get_enhanced_cash_flow_transactions(req)

if res.enhanced_cash_flow_transactions is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetEnhancedCashFlowTransactionsRequest](../../models/operations/getenhancedcashflowtransactionsrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |


### Response

**[operations.GetEnhancedCashFlowTransactionsResponse](../../models/operations/getenhancedcashflowtransactionsresponse.md)**


## get_enhanced_invoices_report

Gets a list of invoices linked to the corresponding banking transaction

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetEnhancedInvoicesReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    page=1,
    page_size=100,
    query='temporibus',
)

res = s.reports.get_enhanced_invoices_report(req)

if res.enhanced_invoices_report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetEnhancedInvoicesReportRequest](../../models/operations/getenhancedinvoicesreportrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.GetEnhancedInvoicesReportResponse](../../models/operations/getenhancedinvoicesreportresponse.md)**


## get_loan_summary

Get enhanced loan summaries

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetLoanSummaryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.reports.get_loan_summary(req)

if res.loan_summary is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetLoanSummaryRequest](../../models/operations/getloansummaryrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.GetLoanSummaryResponse](../../models/operations/getloansummaryresponse.md)**


## get_recurring_revenue_metrics

Gets key metrics for subscription revenue.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
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

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetRecurringRevenueMetricsRequest](../../models/operations/getrecurringrevenuemetricsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |


### Response

**[operations.GetRecurringRevenueMetricsResponse](../../models/operations/getrecurringrevenuemetricsresponse.md)**


## list_loan_transactions

List enhanced loan transactions

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListLoanTransactionsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    source_type=operations.ListLoanTransactionsSourceType.BANKING,
)

res = s.reports.list_loan_transactions(req)

if res.loan_transactions is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListLoanTransactionsRequest](../../models/operations/listloantransactionsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.ListLoanTransactionsResponse](../../models/operations/listloantransactionsresponse.md)**


## request_recurring_revenue_metrics

Requests production of key subscription revenue metrics.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
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

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.RequestRecurringRevenueMetricsRequest](../../models/operations/requestrecurringrevenuemetricsrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |


### Response

**[operations.RequestRecurringRevenueMetricsResponse](../../models/operations/requestrecurringrevenuemetricsresponse.md)**

