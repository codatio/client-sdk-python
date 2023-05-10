# Assess

Assess helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from the operating systems they are already using.
You can use that data for automating decisioning and surfacing new insights on the customer, all via one API.

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install codat-assess
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetAccountCategoryRequest(
    account_id='corrupti',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.categories.get_account_category(req)

if res.categorised_account is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [categories](docs/categories/README.md)

* [~~get_account_category~~](docs/categories/README.md#get_account_category) - Get suggested and/or confirmed category for a specific account :warning: **Deprecated**
* [~~list_accounts_categories~~](docs/categories/README.md#list_accounts_categories) - List suggested and confirmed account categories :warning: **Deprecated**
* [~~list_available_account_categories~~](docs/categories/README.md#list_available_account_categories) - List account categories :warning: **Deprecated**
* [~~update_account_category~~](docs/categories/README.md#update_account_category) - Patch account categories :warning: **Deprecated**
* [~~update_accounts_categories~~](docs/categories/README.md#update_accounts_categories) - Confirm categories for accounts :warning: **Deprecated**

### [data_integrity](docs/dataintegrity/README.md)

* [get_data_integrity_details](docs/dataintegrity/README.md#get_data_integrity_details) - Lists data integrity details for date type
* [get_data_integrity_status](docs/dataintegrity/README.md#get_data_integrity_status) - Get data integrity status
* [get_data_integrity_summaries](docs/dataintegrity/README.md#get_data_integrity_summaries) - Get data integrity summary

### [excel_reports](docs/excelreports/README.md)

* [~~download_excel_report~~](docs/excelreports/README.md#download_excel_report) - Download generated excel report :warning: **Deprecated**
* [generate_excel_report](docs/excelreports/README.md#generate_excel_report) - Generate an Excel report
* [get_accounting_marketing_metrics](docs/excelreports/README.md#get_accounting_marketing_metrics) - Get the marketing metrics from an accounting source for a given company.
* [get_excel_report](docs/excelreports/README.md#get_excel_report) - Download generated excel report
* [get_excel_report_generation_status](docs/excelreports/README.md#get_excel_report_generation_status) - Get status of Excel report

### [reports](docs/reports/README.md)

* [get_accounts_for_enhanced_balance_sheet](docs/reports/README.md#get_accounts_for_enhanced_balance_sheet) - Enhanced Balance Sheet Accounts
* [get_accounts_for_enhanced_profit_and_loss](docs/reports/README.md#get_accounts_for_enhanced_profit_and_loss) - Enhanced Profit and Loss Accounts
* [get_commerce_customer_retention_metrics](docs/reports/README.md#get_commerce_customer_retention_metrics) - Get the customer retention metrics for a specific company.
* [get_commerce_lifetime_value_metrics](docs/reports/README.md#get_commerce_lifetime_value_metrics) - Get the lifetime value metric for a specific company.
* [get_commerce_orders_metrics](docs/reports/README.md#get_commerce_orders_metrics) - Get order information for a specific company
* [get_commerce_refunds_metrics](docs/reports/README.md#get_commerce_refunds_metrics) - Get the refunds information for a specific company
* [get_commerce_revenue_metrics](docs/reports/README.md#get_commerce_revenue_metrics) - Commerce Revenue Metrics
* [~~get_enhanced_balance_sheet~~](docs/reports/README.md#get_enhanced_balance_sheet) - Enhanced Balance Sheet :warning: **Deprecated**
* [get_enhanced_cash_flow_transactions](docs/reports/README.md#get_enhanced_cash_flow_transactions) - Get enhanced cash flow report
* [~~get_enhanced_financial_metrics~~](docs/reports/README.md#get_enhanced_financial_metrics) - List financial metrics :warning: **Deprecated**
* [get_enhanced_invoices_report](docs/reports/README.md#get_enhanced_invoices_report) - Enhanced Invoices Report
* [~~get_enhanced_profit_and_loss~~](docs/reports/README.md#get_enhanced_profit_and_loss) - Enhanced Profit and Loss :warning: **Deprecated**
* [get_recurring_revenue_metrics](docs/reports/README.md#get_recurring_revenue_metrics) - Get key metrics for subscription revenue
* [request_recurring_revenue_metrics](docs/reports/README.md#request_recurring_revenue_metrics) - Request production of key subscription revenue metrics
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
