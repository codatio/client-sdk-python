# Lending

<!-- Start Codat Library Description -->
Lending helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from the operating systems they are already using. You can use that data for automating decisioning and surfacing new insights on the customer, all via one API.
<!-- End Codat Library Description -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install codat-lending
```
<!-- End SDK Installation [installation] -->

## Example Usage
<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import codatlending
from codatlending.models import shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [companies](docs/sdks/companies/README.md)

* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [list](docs/sdks/companies/README.md#list) - List companies
* [update](docs/sdks/companies/README.md#update) - Update company

### [connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [list](docs/sdks/connections/README.md#list) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection


### [transactions.account_transactions](docs/sdks/accounttransactions/README.md)

* [get](docs/sdks/accounttransactions/README.md#get) - Get account transaction
* [list](docs/sdks/accounttransactions/README.md#list) - List account transactions

### [transactions.direct_costs](docs/sdks/codatlendingdirectcosts/README.md)

* [download_attachment](docs/sdks/codatlendingdirectcosts/README.md#download_attachment) - Download direct cost attachment
* [get](docs/sdks/codatlendingdirectcosts/README.md#get) - Get direct cost
* [get_attachment](docs/sdks/codatlendingdirectcosts/README.md#get_attachment) - Get direct cost attachment
* [list](docs/sdks/codatlendingdirectcosts/README.md#list) - List direct costs
* [list_attachments](docs/sdks/codatlendingdirectcosts/README.md#list_attachments) - List direct cost attachments

### [transactions.transfers](docs/sdks/codatlendingtransfers/README.md)

* [get](docs/sdks/codatlendingtransfers/README.md#get) - Get transfer
* [list](docs/sdks/codatlendingtransfers/README.md#list) - List transfers

### [transactions.journal_entries](docs/sdks/journalentries/README.md)

* [get](docs/sdks/journalentries/README.md#get) - Get journal entry
* [list](docs/sdks/journalentries/README.md#list) - List journal entries

### [transactions.journals](docs/sdks/journals/README.md)

* [get](docs/sdks/journals/README.md#get) - Get journal
* [list](docs/sdks/journals/README.md#list) - List journals

### [accounting_bank_data](docs/sdks/codatlendingaccountingbankdata/README.md)

* [list_transactions](docs/sdks/codatlendingaccountingbankdata/README.md#list_transactions) - List bank account transactions

### [accounting_bank_data.accounts](docs/sdks/accounts/README.md)

* [get](docs/sdks/accounts/README.md#get) - Get bank account
* [list](docs/sdks/accounts/README.md#list) - List bank accounts


### [banking.account_balances](docs/sdks/accountbalances/README.md)

* [list](docs/sdks/accountbalances/README.md#list) - List account balances

### [banking.accounts](docs/sdks/codatlendingaccounts/README.md)

* [get](docs/sdks/codatlendingaccounts/README.md#get) - Get account
* [list](docs/sdks/codatlendingaccounts/README.md#list) - List accounts

### [banking.transaction_categories](docs/sdks/transactioncategories/README.md)

* [get](docs/sdks/transactioncategories/README.md#get) - Get transaction category
* [list](docs/sdks/transactioncategories/README.md#list) - List transaction categories

### [banking.transactions](docs/sdks/codatlendingbankingtransactions/README.md)

* [get](docs/sdks/codatlendingbankingtransactions/README.md#get) - Get bank transaction
* [list](docs/sdks/codatlendingbankingtransactions/README.md#list) - List transactions

### [banking.categorized_statement](docs/sdks/categorizedstatement/README.md)

* [get](docs/sdks/categorizedstatement/README.md#get) - Get categorized bank statement


### [accounts_payable.bills](docs/sdks/bills/README.md)

* [download_attachment](docs/sdks/bills/README.md#download_attachment) - Download bill attachment
* [get](docs/sdks/bills/README.md#get) - Get bill
* [get_attachment](docs/sdks/bills/README.md#get_attachment) - Get bill attachment
* [list](docs/sdks/bills/README.md#list) - List bills
* [list_attachments](docs/sdks/bills/README.md#list_attachments) - List bill attachments

### [accounts_payable.suppliers](docs/sdks/suppliers/README.md)

* [download_attachment](docs/sdks/suppliers/README.md#download_attachment) - Download supplier attachment
* [get](docs/sdks/suppliers/README.md#get) - Get supplier
* [get_attachment](docs/sdks/suppliers/README.md#get_attachment) - Get supplier attachment
* [list](docs/sdks/suppliers/README.md#list) - List suppliers
* [list_attachments](docs/sdks/suppliers/README.md#list_attachments) - List supplier attachments

### [accounts_payable.bill_credit_notes](docs/sdks/billcreditnotes/README.md)

* [get](docs/sdks/billcreditnotes/README.md#get) - Get bill credit note
* [list](docs/sdks/billcreditnotes/README.md#list) - List bill credit notes

### [accounts_payable.bill_payments](docs/sdks/billpayments/README.md)

* [get](docs/sdks/billpayments/README.md#get) - Get bill payment
* [list](docs/sdks/billpayments/README.md#list) - List bill payments


### [sales.customers](docs/sdks/codatlendingcustomers/README.md)

* [get](docs/sdks/codatlendingcustomers/README.md#get) - Get customer
* [list](docs/sdks/codatlendingcustomers/README.md#list) - List customers

### [sales.disputes](docs/sdks/disputes/README.md)

* [get](docs/sdks/disputes/README.md#get) - Get dispute
* [list](docs/sdks/disputes/README.md#list) - List disputes

### [sales.locations](docs/sdks/locations/README.md)

* [get](docs/sdks/locations/README.md#get) - Get location
* [list](docs/sdks/locations/README.md#list) - List locations

### [sales.orders](docs/sdks/orders/README.md)

* [get](docs/sdks/orders/README.md#get) - Get order
* [list](docs/sdks/orders/README.md#list) - List orders

### [sales.payment_methods](docs/sdks/paymentmethods/README.md)

* [get](docs/sdks/paymentmethods/README.md#get) - Get payment method
* [list](docs/sdks/paymentmethods/README.md#list) - List payment methods

### [sales.payments](docs/sdks/codatlendingsalespayments/README.md)

* [get](docs/sdks/codatlendingsalespayments/README.md#get) - Get payment
* [list](docs/sdks/codatlendingsalespayments/README.md#list) - List payments

### [sales.product_categories](docs/sdks/productcategories/README.md)

* [get](docs/sdks/productcategories/README.md#get) - Get product category
* [list](docs/sdks/productcategories/README.md#list) - List product categories

### [sales.products](docs/sdks/products/README.md)

* [get](docs/sdks/products/README.md#get) - Get product
* [list](docs/sdks/products/README.md#list) - List products

### [sales.transactions](docs/sdks/codatlendingtransactions/README.md)

* [get](docs/sdks/codatlendingtransactions/README.md#get) - Get transaction
* [list](docs/sdks/codatlendingtransactions/README.md#list) - List transactions

### [sales.metrics](docs/sdks/metrics/README.md)

* [get_customer_retention](docs/sdks/metrics/README.md#get_customer_retention) - Get customer retention metrics
* [get_lifetime_value](docs/sdks/metrics/README.md#get_lifetime_value) - Get lifetime value metrics
* [get_revenue](docs/sdks/metrics/README.md#get_revenue) - Get commerce revenue metrics

### [sales.reports](docs/sdks/codatlendingreports/README.md)

* [get_orders](docs/sdks/codatlendingreports/README.md#get_orders) - Get orders report
* [get_refunds](docs/sdks/codatlendingreports/README.md#get_refunds) - Get refunds report

### [company_info](docs/sdks/companyinfo/README.md)

* [get_accounting_profile](docs/sdks/companyinfo/README.md#get_accounting_profile) - Get company accounting profile
* [get_commerce_profile](docs/sdks/companyinfo/README.md#get_commerce_profile) - Get company commerce profile


### [accounts_receivable.customers](docs/sdks/customers/README.md)

* [download_attachment](docs/sdks/customers/README.md#download_attachment) - Download customer attachment
* [get](docs/sdks/customers/README.md#get) - Get customer
* [get_attachment](docs/sdks/customers/README.md#get_attachment) - Get customer attachment
* [list](docs/sdks/customers/README.md#list) - List customers
* [list_attachments](docs/sdks/customers/README.md#list_attachments) - List customer attachments

### [accounts_receivable.direct_incomes](docs/sdks/directincomes/README.md)

* [download_attachment](docs/sdks/directincomes/README.md#download_attachment) - Download direct income attachment
* [get](docs/sdks/directincomes/README.md#get) - Get direct income
* [get_attachment](docs/sdks/directincomes/README.md#get_attachment) - Get direct income attachment
* [list](docs/sdks/directincomes/README.md#list) - List direct incomes
* [list_attachments](docs/sdks/directincomes/README.md#list_attachments) - List direct income attachments

### [accounts_receivable.invoices](docs/sdks/invoices/README.md)

* [download_attachment](docs/sdks/invoices/README.md#download_attachment) - Download invoice attachment
* [download_pdf](docs/sdks/invoices/README.md#download_pdf) - Get invoice as PDF
* [get](docs/sdks/invoices/README.md#get) - Get invoice
* [get_attachment](docs/sdks/invoices/README.md#get_attachment) - Get invoice attachment
* [list](docs/sdks/invoices/README.md#list) - List invoices
* [list_attachments](docs/sdks/invoices/README.md#list_attachments) - List invoice attachments
* [list_reconciled](docs/sdks/invoices/README.md#list_reconciled) - List reconciled invoices

### [accounts_receivable.credit_notes](docs/sdks/creditnotes/README.md)

* [get](docs/sdks/creditnotes/README.md#get) - Get credit note
* [list](docs/sdks/creditnotes/README.md#list) - List credit notes

### [accounts_receivable.payments](docs/sdks/payments/README.md)

* [get](docs/sdks/payments/README.md#get) - Get payment
* [list](docs/sdks/payments/README.md#list) - List payments

### [accounts_receivable.reports](docs/sdks/reports/README.md)

* [get_aged_creditors](docs/sdks/reports/README.md#get_aged_creditors) - Aged creditors report
* [get_aged_debtors](docs/sdks/reports/README.md#get_aged_debtors) - Aged debtors report
* [is_aged_creditors_available](docs/sdks/reports/README.md#is_aged_creditors_available) - Aged creditors report available
* [is_aged_debtors_available](docs/sdks/reports/README.md#is_aged_debtors_available) - Aged debtors report available

### [file_upload](docs/sdks/fileupload/README.md)

* [download](docs/sdks/fileupload/README.md#download) - Download all files for a company
* [list_uploaded](docs/sdks/fileupload/README.md#list_uploaded) - List all files uploaded by a company
* [upload](docs/sdks/fileupload/README.md#upload) - Upload files for a company


### [loan_writeback.bank_accounts](docs/sdks/bankaccounts/README.md)

* [create](docs/sdks/bankaccounts/README.md#create) - Create bank account
* [get_create_update_model](docs/sdks/bankaccounts/README.md#get_create_update_model) - Get create/update bank account model

### [loan_writeback.bank_transactions](docs/sdks/banktransactions/README.md)

* [create](docs/sdks/banktransactions/README.md#create) - Create bank account transactions
* [get_create_model](docs/sdks/banktransactions/README.md#get_create_model) - Get create bank account transactions model

### [loan_writeback.accounts](docs/sdks/codatlendingloanwritebackaccounts/README.md)

* [create](docs/sdks/codatlendingloanwritebackaccounts/README.md#create) - Create account
* [get_create_model](docs/sdks/codatlendingloanwritebackaccounts/README.md#get_create_model) - Get create account model

### [loan_writeback.direct_costs](docs/sdks/directcosts/README.md)

* [create](docs/sdks/directcosts/README.md#create) - Create direct cost
* [get_create_model](docs/sdks/directcosts/README.md#get_create_model) - Get create direct cost model

### [loan_writeback.payments](docs/sdks/codatlendingpayments/README.md)

* [create](docs/sdks/codatlendingpayments/README.md#create) - Create payment
* [get_create_model](docs/sdks/codatlendingpayments/README.md#get_create_model) - Get create payment model

### [loan_writeback.suppliers](docs/sdks/codatlendingsuppliers/README.md)

* [create](docs/sdks/codatlendingsuppliers/README.md#create) - Create supplier
* [get_create_update_model](docs/sdks/codatlendingsuppliers/README.md#get_create_update_model) - Get create/update supplier model

### [loan_writeback.transfers](docs/sdks/transfers/README.md)

* [create](docs/sdks/transfers/README.md#create) - Create transfer
* [get_create_model](docs/sdks/transfers/README.md#get_create_model) - Get create transfer model

### [loan_writeback.create_operations](docs/sdks/createoperations/README.md)

* [get](docs/sdks/createoperations/README.md#get) - Get create operation
* [list](docs/sdks/createoperations/README.md#list) - List create operations


### [financial_statements.accounts](docs/sdks/codatlendingfinancialstatementsaccounts/README.md)

* [get](docs/sdks/codatlendingfinancialstatementsaccounts/README.md#get) - Get account
* [list](docs/sdks/codatlendingfinancialstatementsaccounts/README.md#list) - List accounts

### [financial_statements.balance_sheet](docs/sdks/balancesheet/README.md)

* [get](docs/sdks/balancesheet/README.md#get) - Get balance sheet
* [get_categorized_accounts](docs/sdks/balancesheet/README.md#get_categorized_accounts) - Get categorized balance sheet statement

### [financial_statements.cash_flow](docs/sdks/cashflow/README.md)

* [get](docs/sdks/cashflow/README.md#get) - Get cash flow statement

### [financial_statements.profit_and_loss](docs/sdks/profitandloss/README.md)

* [get](docs/sdks/profitandloss/README.md#get) - Get profit and loss
* [get_categorized_accounts](docs/sdks/profitandloss/README.md#get_categorized_accounts) - Get categorized profit and loss statement

### [manage_data](docs/sdks/managedata/README.md)

* [get_status](docs/sdks/managedata/README.md#get_status) - Get data status

### [manage_data.refresh](docs/sdks/refresh/README.md)

* [all_data_types](docs/sdks/refresh/README.md#all_data_types) - Refresh all data
* [data_type](docs/sdks/refresh/README.md#data_type) - Refresh data type

### [manage_data.pull_operations](docs/sdks/pulloperations/README.md)

* [get](docs/sdks/pulloperations/README.md#get) - Get pull operation
* [list](docs/sdks/pulloperations/README.md#list) - List pull operations

### [liabilities](docs/sdks/liabilities/README.md)

* [generate_loan_summary](docs/sdks/liabilities/README.md#generate_loan_summary) - Generate loan summaries report
* [generate_loan_transactions](docs/sdks/liabilities/README.md#generate_loan_transactions) - Generate loan transactions report
* [get_loan_summary](docs/sdks/liabilities/README.md#get_loan_summary) - Get loan summaries
* [list_loan_transactions](docs/sdks/liabilities/README.md#list_loan_transactions) - List loan transactions

### [data_integrity](docs/sdks/dataintegrity/README.md)

* [details](docs/sdks/dataintegrity/README.md#details) - List data integrity details
* [status](docs/sdks/dataintegrity/README.md#status) - Get data integrity status
* [summaries](docs/sdks/dataintegrity/README.md#summaries) - Get data integrity summaries

### [excel_reports](docs/sdks/excelreports/README.md)

* [download](docs/sdks/excelreports/README.md#download) - Download Excel report
* [generate](docs/sdks/excelreports/README.md#generate) - Generate Excel report
* [get_status](docs/sdks/excelreports/README.md#get_status) - Get Excel report status
<!-- End Available Resources and Operations [operations] -->



<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import codatlending
from codatlending.models import shared
from codatlending.utils import BackoffStrategy, RetryConfig

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create(req,
    RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False))

if res.company is not None:
    # handle response
    pass
```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import codatlending
from codatlending.models import shared
from codatlending.utils import BackoffStrategy, RetryConfig

s = codatlending.CodatLending(
    retry_config=RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False)
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
    pass
```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 400,401,402,403,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

### Example

```python
import codatlending
from codatlending.models import errors, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = None
try:
    res = s.companies.create(req)
except errors.ErrorMessage as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.company is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.codat.io` | None |

#### Example

```python
import codatlending
from codatlending.models import shared

s = codatlending.CodatLending(
    server_idx=0,
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import codatlending
from codatlending.models import shared

s = codatlending.CodatLending(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import codatlending
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = codatlending.CodatLending(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `auth_header` | apiKey        | API key       |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
import codatlending
from codatlending.models import shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

<!-- Start Codat Support Notes -->
### Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance. 
You can raise any issues by contacting your dedicated Codat representative or reaching out to our [support team](mailto:support@codat.io).
We're here to help ensure a smooth experience for you.
<!-- End Codat Support Notes -->

<!-- Start Codat Generated By -->
### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
<!-- End Codat Generated By -->