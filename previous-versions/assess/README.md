# Assess
    
﻿Assess helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from the operating systems they are already using.
You can use that data for automating decisioning and surfacing new insights on the customer, all via one API.

## SDK Installation

```bash
pip install codat-assess
```## SDK Installation

```bash
pip install codat-assess
```<!-- Start SDK Installation -->

<!-- End SDK Installation -->

## Example Usage


```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDataTypeDataIntegrityDetailsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    data_type=shared.DataIntegrityDataType.BANKING_ACCOUNTS,
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='corrupti',
)

res = s.data_integrity.details(req)

if res.details is not None:
    # handle response
```

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDataTypeDataIntegrityDetailsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    data_type=shared.DataIntegrityDataType.BANKING_ACCOUNTS,
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='corrupti',
)

res = s.data_integrity.details(req)

if res.details is not None:
    # handle response
```<!-- Start SDK Example Usage -->

<!-- End SDK Example Usage -->

## Available Resources and Operations


### [data_integrity](docs/sdks/dataintegrity/README.md)

* [details](docs/sdks/dataintegrity/README.md#details) - List data type data integrity
* [status](docs/sdks/dataintegrity/README.md#status) - Get data integrity status
* [summary](docs/sdks/dataintegrity/README.md#summary) - Get data integrity summary

### [excel_reports](docs/sdks/excelreports/README.md)

* [generate_excel_report](docs/sdks/excelreports/README.md#generate_excel_report) - Generate Excel report
* [get_accounting_marketing_metrics](docs/sdks/excelreports/README.md#get_accounting_marketing_metrics) - Get marketing metrics report
* [get_excel_report](docs/sdks/excelreports/README.md#get_excel_report) - Download Excel report
* [get_excel_report_generation_status](docs/sdks/excelreports/README.md#get_excel_report_generation_status) - Get Excel report status

### [reports](docs/sdks/reports/README.md)

* [get_accounts_for_enhanced_balance_sheet](docs/sdks/reports/README.md#get_accounts_for_enhanced_balance_sheet) - Get enhanced balance sheet accounts
* [get_accounts_for_enhanced_profit_and_loss](docs/sdks/reports/README.md#get_accounts_for_enhanced_profit_and_loss) - Get enhanced profit and loss accounts
* [get_commerce_customer_retention_metrics](docs/sdks/reports/README.md#get_commerce_customer_retention_metrics) - Get customer retention metrics
* [get_commerce_lifetime_value_metrics](docs/sdks/reports/README.md#get_commerce_lifetime_value_metrics) - Get lifetime value metric
* [get_commerce_orders_metrics](docs/sdks/reports/README.md#get_commerce_orders_metrics) - Get orders report
* [get_commerce_refunds_metrics](docs/sdks/reports/README.md#get_commerce_refunds_metrics) - Get refunds report
* [get_commerce_revenue_metrics](docs/sdks/reports/README.md#get_commerce_revenue_metrics) - Get commerce revenue metrics
* [get_enhanced_cash_flow_transactions](docs/sdks/reports/README.md#get_enhanced_cash_flow_transactions) - Get enhanced cash flow report
* [get_enhanced_invoices_report](docs/sdks/reports/README.md#get_enhanced_invoices_report) - Get enhanced invoices report
* [get_loan_summary](docs/sdks/reports/README.md#get_loan_summary) - Get enhanced loan summaries
* [get_recurring_revenue_metrics](docs/sdks/reports/README.md#get_recurring_revenue_metrics) - Get key subscription revenue metrics
* [list_loan_transactions](docs/sdks/reports/README.md#list_loan_transactions) - List enhanced loan transactions
* [request_recurring_revenue_metrics](docs/sdks/reports/README.md#request_recurring_revenue_metrics) - Generate key subscription revenue metrics## Available Resources and Operations


### [data_integrity](docs/sdks/dataintegrity/README.md)

* [details](docs/sdks/dataintegrity/README.md#details) - List data type data integrity
* [status](docs/sdks/dataintegrity/README.md#status) - Get data integrity status
* [summary](docs/sdks/dataintegrity/README.md#summary) - Get data integrity summary

### [excel_reports](docs/sdks/excelreports/README.md)

* [generate_excel_report](docs/sdks/excelreports/README.md#generate_excel_report) - Generate Excel report
* [get_accounting_marketing_metrics](docs/sdks/excelreports/README.md#get_accounting_marketing_metrics) - Get marketing metrics report
* [get_excel_report](docs/sdks/excelreports/README.md#get_excel_report) - Download Excel report
* [get_excel_report_generation_status](docs/sdks/excelreports/README.md#get_excel_report_generation_status) - Get Excel report status

### [reports](docs/sdks/reports/README.md)

* [get_accounts_for_enhanced_balance_sheet](docs/sdks/reports/README.md#get_accounts_for_enhanced_balance_sheet) - Get enhanced balance sheet accounts
* [get_accounts_for_enhanced_profit_and_loss](docs/sdks/reports/README.md#get_accounts_for_enhanced_profit_and_loss) - Get enhanced profit and loss accounts
* [get_commerce_customer_retention_metrics](docs/sdks/reports/README.md#get_commerce_customer_retention_metrics) - Get customer retention metrics
* [get_commerce_lifetime_value_metrics](docs/sdks/reports/README.md#get_commerce_lifetime_value_metrics) - Get lifetime value metric
* [get_commerce_orders_metrics](docs/sdks/reports/README.md#get_commerce_orders_metrics) - Get orders report
* [get_commerce_refunds_metrics](docs/sdks/reports/README.md#get_commerce_refunds_metrics) - Get refunds report
* [get_commerce_revenue_metrics](docs/sdks/reports/README.md#get_commerce_revenue_metrics) - Get commerce revenue metrics
* [get_enhanced_cash_flow_transactions](docs/sdks/reports/README.md#get_enhanced_cash_flow_transactions) - Get enhanced cash flow report
* [get_enhanced_invoices_report](docs/sdks/reports/README.md#get_enhanced_invoices_report) - Get enhanced invoices report
* [get_loan_summary](docs/sdks/reports/README.md#get_loan_summary) - Get enhanced loan summaries
* [get_recurring_revenue_metrics](docs/sdks/reports/README.md#get_recurring_revenue_metrics) - Get key subscription revenue metrics
* [list_loan_transactions](docs/sdks/reports/README.md#list_loan_transactions) - List enhanced loan transactions
* [request_recurring_revenue_metrics](docs/sdks/reports/README.md#request_recurring_revenue_metrics) - Generate key subscription revenue metrics<!-- Start SDK Available Operations -->

<!-- End SDK Available Operations -->
### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
