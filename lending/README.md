# Lending

<!-- Start Codat Library Description -->
Lending helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from the operating systems they are already using. You can use that data for automating decisioning and surfacing new insights on the customer, all via one API.
<!-- End Codat Library Description -->

<!-- Start Summary [summary] -->
## Summary

Lending API: Our Lending API helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from accounting, banking, and commerce software they are already using. It also includes features to help providers verify the accuracy of data and process it more efficiently.

The Lending API is built on top of the latest accounting, commerce, and banking data, providing you with the most important data points you need to get a full picture of SMB creditworthiness and make a comprehensive assessment of your customers.

[Explore product](https://docs.codat.io/lending/overview) | [See OpenAPI spec](https://github.com/codatio/oas)

<!-- Start Codat Tags Table -->
## Endpoints

| Endpoints | Description |
| :- |:- |
| Companies | Create and manage your SMB users' companies. |
| Connections | Create new and manage existing data connections for a company. |
| Bank statements | Retrieve banking data from linked bank accounts. |
| Sales | Retrieve standardized sales data from a linked commerce software. |
| Financial statements | Financial data and reports from a linked accounting software. |
| Liabilities | Debt and other liabilities. |
| Accounts payable | Data from a linked accounting software representing money the business owes money to its suppliers. |
| Accounts receivable | Data from a linked accounting software representing money owed to the business for sold goods or services. |
| Transactions | Data from a linked accounting software representing transactions. |
| Company info | View company information fetched from the source platform. |
| Data integrity | Match mutable accounting data with immutable banking data to increase confidence in financial data. |
| Excel reports | Download reports in Excel format. |
| Manage data | Control how data is retrieved from an integration. |
| File upload | Endpoints to manage uploaded files. |
| Loan writeback | Implement the [loan writeback](https://docs.codat.io/lending/guides/loan-writeback/introduction) procedure in your lending process to maintain an accurate position of a loan during the entire lending cycle. |
<!-- End Codat Tags Table -->
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Lending](#lending)
  * [Endpoints](#endpoints)
  * [SDK Installation](#sdk-installation)
  * [Example Usage](#example-usage)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
  * [IDE Support](#ide-support)
  * [File uploads](#file-uploads)
  * [Debugging](#debugging)
  * [Support](#support)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install codat-lending
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add codat-lending
```
<!-- End SDK Installation [installation] -->

## Example Usage
<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from codat_lending import CodatLending

with CodatLending() as codat_lending:

    codat_lending.account_categories_updated(request={
        "alert_id": "a9367074-b5c3-42c4-9be4-be129f43577e",
        "client_id": "bae71d36-ff47-420a-b4a6-f8c9ddf41140",
        "client_name": "Bank of Dave",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "data": {
            "modified_date": "2022-10-23",
        },
        "data_connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "message": "Account categories updated for company f1c35bdc-1546-41b9-baf4-3f31135af968.",
        "rule_id": "70af3071-65d9-4ec3-b3cb-5283e8d55dac",
        "rule_type": "Account Categories Updated",
    })

    # Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from codat_lending import CodatLending

async def main():
    async with CodatLending() as codat_lending:

        await codat_lending.account_categories_updated_async(request={
            "alert_id": "a9367074-b5c3-42c4-9be4-be129f43577e",
            "client_id": "bae71d36-ff47-420a-b4a6-f8c9ddf41140",
            "client_name": "Bank of Dave",
            "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
            "data": {
                "modified_date": "2022-10-23",
            },
            "data_connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
            "message": "Account categories updated for company f1c35bdc-1546-41b9-baf4-3f31135af968.",
            "rule_id": "70af3071-65d9-4ec3-b3cb-5283e8d55dac",
            "rule_type": "Account Categories Updated",
        })

        # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [accounting_bank_data](docs/sdks/codatlendingaccountingbankdata/README.md)

* [list_transactions](docs/sdks/codatlendingaccountingbankdata/README.md#list_transactions) - List bank account transactions

#### [accounting_bank_data.accounts](docs/sdks/accounts/README.md)

* [get](docs/sdks/accounts/README.md#get) - Get bank account
* [list](docs/sdks/accounts/README.md#list) - List bank accounts

### [accounts_payable](docs/sdks/accountspayable/README.md)


#### [accounts_payable.bill_credit_notes](docs/sdks/billcreditnotes/README.md)

* [get](docs/sdks/billcreditnotes/README.md#get) - Get bill credit note
* [list](docs/sdks/billcreditnotes/README.md#list) - List bill credit notes

#### [accounts_payable.bill_payments](docs/sdks/billpayments/README.md)

* [get](docs/sdks/billpayments/README.md#get) - Get bill payment
* [list](docs/sdks/billpayments/README.md#list) - List bill payments

#### [accounts_payable.bills](docs/sdks/bills/README.md)

* [download_attachment](docs/sdks/bills/README.md#download_attachment) - Download bill attachment
* [get](docs/sdks/bills/README.md#get) - Get bill
* [get_attachment](docs/sdks/bills/README.md#get_attachment) - Get bill attachment
* [list](docs/sdks/bills/README.md#list) - List bills
* [list_attachments](docs/sdks/bills/README.md#list_attachments) - List bill attachments

#### [accounts_payable.suppliers](docs/sdks/suppliers/README.md)

* [download_attachment](docs/sdks/suppliers/README.md#download_attachment) - Download supplier attachment
* [get](docs/sdks/suppliers/README.md#get) - Get supplier
* [get_attachment](docs/sdks/suppliers/README.md#get_attachment) - Get supplier attachment
* [list](docs/sdks/suppliers/README.md#list) - List suppliers
* [list_attachments](docs/sdks/suppliers/README.md#list_attachments) - List supplier attachments

### [accounts_receivable](docs/sdks/accountsreceivable/README.md)


#### [accounts_receivable.credit_notes](docs/sdks/creditnotes/README.md)

* [get](docs/sdks/creditnotes/README.md#get) - Get credit note
* [list](docs/sdks/creditnotes/README.md#list) - List credit notes

#### [accounts_receivable.customers](docs/sdks/customers/README.md)

* [download_attachment](docs/sdks/customers/README.md#download_attachment) - Download customer attachment
* [get](docs/sdks/customers/README.md#get) - Get customer
* [get_attachment](docs/sdks/customers/README.md#get_attachment) - Get customer attachment
* [list](docs/sdks/customers/README.md#list) - List customers
* [list_attachments](docs/sdks/customers/README.md#list_attachments) - List customer attachments

#### [accounts_receivable.direct_incomes](docs/sdks/directincomes/README.md)

* [download_attachment](docs/sdks/directincomes/README.md#download_attachment) - Download direct income attachment
* [get](docs/sdks/directincomes/README.md#get) - Get direct income
* [get_attachment](docs/sdks/directincomes/README.md#get_attachment) - Get direct income attachment
* [list](docs/sdks/directincomes/README.md#list) - List direct incomes
* [list_attachments](docs/sdks/directincomes/README.md#list_attachments) - List direct income attachments

#### [accounts_receivable.invoices](docs/sdks/invoices/README.md)

* [download_attachment](docs/sdks/invoices/README.md#download_attachment) - Download invoice attachment
* [download_pdf](docs/sdks/invoices/README.md#download_pdf) - Get invoice as PDF
* [get](docs/sdks/invoices/README.md#get) - Get invoice
* [get_attachment](docs/sdks/invoices/README.md#get_attachment) - Get invoice attachment
* [list](docs/sdks/invoices/README.md#list) - List invoices
* [list_attachments](docs/sdks/invoices/README.md#list_attachments) - List invoice attachments
* [list_reconciled](docs/sdks/invoices/README.md#list_reconciled) - List reconciled invoices

#### [accounts_receivable.payments](docs/sdks/payments/README.md)

* [get](docs/sdks/payments/README.md#get) - Get payment
* [list](docs/sdks/payments/README.md#list) - List payments

#### [accounts_receivable.reports](docs/sdks/reports/README.md)

* [get_aged_creditors](docs/sdks/reports/README.md#get_aged_creditors) - Aged creditors report
* [get_aged_debtors](docs/sdks/reports/README.md#get_aged_debtors) - Aged debtors report
* [is_aged_creditors_available](docs/sdks/reports/README.md#is_aged_creditors_available) - Aged creditors report available
* [is_aged_debtors_available](docs/sdks/reports/README.md#is_aged_debtors_available) - Aged debtors report available

### [bank_statements](docs/sdks/bankstatements/README.md)

* [end_upload_session](docs/sdks/bankstatements/README.md#end_upload_session) - End upload session
* [get_upload_configuration](docs/sdks/bankstatements/README.md#get_upload_configuration) - Get upload configuration
* [set_upload_configuration](docs/sdks/bankstatements/README.md#set_upload_configuration) - Set upload configuration
* [start_upload_session](docs/sdks/bankstatements/README.md#start_upload_session) - Start upload session
* [upload_bank_statement_data](docs/sdks/bankstatements/README.md#upload_bank_statement_data) - Upload data

### [banking](docs/sdks/banking/README.md)


#### [banking.account_balances](docs/sdks/accountbalances/README.md)

* [list](docs/sdks/accountbalances/README.md#list) - List account balances

#### [banking.accounts](docs/sdks/codatlendingaccounts/README.md)

* [get](docs/sdks/codatlendingaccounts/README.md#get) - Get account
* [list](docs/sdks/codatlendingaccounts/README.md#list) - List accounts

#### [banking.categorized_statement](docs/sdks/categorizedstatement/README.md)

* [get](docs/sdks/categorizedstatement/README.md#get) - Get categorized bank statement

#### [banking.transaction_categories](docs/sdks/transactioncategories/README.md)

* [get](docs/sdks/transactioncategories/README.md#get) - Get transaction category
* [list](docs/sdks/transactioncategories/README.md#list) - List transaction categories

#### [banking.transactions](docs/sdks/codatlendingbankingtransactions/README.md)

* [get](docs/sdks/codatlendingbankingtransactions/README.md#get) - Get bank transaction
* [list](docs/sdks/codatlendingbankingtransactions/README.md#list) - List transactions


### [companies](docs/sdks/companies/README.md)

* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [list](docs/sdks/companies/README.md#list) - List companies
* [update](docs/sdks/companies/README.md#update) - Update company

### [company_info](docs/sdks/companyinfo/README.md)

* [get_accounting_profile](docs/sdks/companyinfo/README.md#get_accounting_profile) - Get company accounting profile
* [get_commerce_profile](docs/sdks/companyinfo/README.md#get_commerce_profile) - Get company commerce profile

### [connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [list](docs/sdks/connections/README.md#list) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [data_integrity](docs/sdks/dataintegrity/README.md)

* [details](docs/sdks/dataintegrity/README.md#details) - List data integrity details
* [status](docs/sdks/dataintegrity/README.md#status) - Get data integrity status
* [summaries](docs/sdks/dataintegrity/README.md#summaries) - Get data integrity summaries

### [excel_reports](docs/sdks/excelreports/README.md)

* [download](docs/sdks/excelreports/README.md#download) - Download Excel report
* [generate](docs/sdks/excelreports/README.md#generate) - Generate Excel report
* [get_status](docs/sdks/excelreports/README.md#get_status) - Get Excel report status

### [file_upload](docs/sdks/fileupload/README.md)

* [download](docs/sdks/fileupload/README.md#download) - Download all files for a company
* [list_uploaded](docs/sdks/fileupload/README.md#list_uploaded) - List all files uploaded by a company
* [upload](docs/sdks/fileupload/README.md#upload) - Upload files for a company

### [financial_statements](docs/sdks/financialstatements/README.md)


#### [financial_statements.accounts](docs/sdks/codatlendingfinancialstatementsaccounts/README.md)

* [get](docs/sdks/codatlendingfinancialstatementsaccounts/README.md#get) - Get account
* [list](docs/sdks/codatlendingfinancialstatementsaccounts/README.md#list) - List accounts

#### [financial_statements.balance_sheet](docs/sdks/balancesheet/README.md)

* [get](docs/sdks/balancesheet/README.md#get) - Get balance sheet
* [get_categorized_accounts](docs/sdks/balancesheet/README.md#get_categorized_accounts) - Get categorized balance sheet statement

#### [financial_statements.cash_flow](docs/sdks/cashflow/README.md)

* [get](docs/sdks/cashflow/README.md#get) - Get cash flow statement

#### [financial_statements.profit_and_loss](docs/sdks/profitandloss/README.md)

* [get](docs/sdks/profitandloss/README.md#get) - Get profit and loss
* [get_categorized_accounts](docs/sdks/profitandloss/README.md#get_categorized_accounts) - Get categorized profit and loss statement

### [liabilities](docs/sdks/liabilities/README.md)

* [generate_loan_summary](docs/sdks/liabilities/README.md#generate_loan_summary) - Generate loan summaries report
* [generate_loan_transactions](docs/sdks/liabilities/README.md#generate_loan_transactions) - Generate loan transactions report
* [get_loan_summary](docs/sdks/liabilities/README.md#get_loan_summary) - Get loan summaries
* [list_loan_transactions](docs/sdks/liabilities/README.md#list_loan_transactions) - List loan transactions

### [loan_writeback](docs/sdks/loanwriteback/README.md)


#### [loan_writeback.accounts](docs/sdks/codatlendingloanwritebackaccounts/README.md)

* [create](docs/sdks/codatlendingloanwritebackaccounts/README.md#create) - Create account
* [get_create_model](docs/sdks/codatlendingloanwritebackaccounts/README.md#get_create_model) - Get create account model

#### [loan_writeback.bank_accounts](docs/sdks/bankaccounts/README.md)

* [create](docs/sdks/bankaccounts/README.md#create) - Create bank account
* [get_create_update_model](docs/sdks/bankaccounts/README.md#get_create_update_model) - Get create/update bank account model

#### [loan_writeback.bank_transactions](docs/sdks/banktransactions/README.md)

* [create](docs/sdks/banktransactions/README.md#create) - Create bank account transactions
* [get_create_model](docs/sdks/banktransactions/README.md#get_create_model) - Get create bank account transactions model

#### [loan_writeback.create_operations](docs/sdks/createoperations/README.md)

* [get](docs/sdks/createoperations/README.md#get) - Get create operation
* [list](docs/sdks/createoperations/README.md#list) - List create operations

#### [loan_writeback.direct_costs](docs/sdks/directcosts/README.md)

* [create](docs/sdks/directcosts/README.md#create) - Create direct cost
* [get_create_model](docs/sdks/directcosts/README.md#get_create_model) - Get create direct cost model

#### [loan_writeback.payments](docs/sdks/codatlendingpayments/README.md)

* [create](docs/sdks/codatlendingpayments/README.md#create) - Create payment
* [get_create_model](docs/sdks/codatlendingpayments/README.md#get_create_model) - Get create payment model

#### [loan_writeback.source_accounts](docs/sdks/sourceaccounts/README.md)

* [create](docs/sdks/sourceaccounts/README.md#create) - Create source account
* [create_mapping](docs/sdks/sourceaccounts/README.md#create_mapping) - Create bank feed account mapping
* [list_mappings](docs/sdks/sourceaccounts/README.md#list_mappings) - List bank feed account mappings

#### [loan_writeback.suppliers](docs/sdks/codatlendingsuppliers/README.md)

* [create](docs/sdks/codatlendingsuppliers/README.md#create) - Create supplier
* [get_create_update_model](docs/sdks/codatlendingsuppliers/README.md#get_create_update_model) - Get create/update supplier model

#### [loan_writeback.transfers](docs/sdks/transfers/README.md)

* [create](docs/sdks/transfers/README.md#create) - Create transfer
* [get_create_model](docs/sdks/transfers/README.md#get_create_model) - Get create transfer model

### [manage_data](docs/sdks/managedata/README.md)

* [get_status](docs/sdks/managedata/README.md#get_status) - Get data status

#### [manage_data.pull_operations](docs/sdks/pulloperations/README.md)

* [get](docs/sdks/pulloperations/README.md#get) - Get pull operation
* [list](docs/sdks/pulloperations/README.md#list) - List pull operations

#### [manage_data.refresh](docs/sdks/refresh/README.md)

* [all_data_types](docs/sdks/refresh/README.md#all_data_types) - Refresh all data
* [data_type](docs/sdks/refresh/README.md#data_type) - Refresh data type

### [manage_reports](docs/sdks/managereports/README.md)

* [generate_report](docs/sdks/managereports/README.md#generate_report) - Generate report
* [list_reports](docs/sdks/managereports/README.md#list_reports) - List reports

### [sales](docs/sdks/sales/README.md)


#### [sales.customers](docs/sdks/codatlendingcustomers/README.md)

* [get](docs/sdks/codatlendingcustomers/README.md#get) - Get customer
* [list](docs/sdks/codatlendingcustomers/README.md#list) - List customers

#### [sales.disputes](docs/sdks/disputes/README.md)

* [get](docs/sdks/disputes/README.md#get) - Get dispute
* [list](docs/sdks/disputes/README.md#list) - List disputes

#### [sales.locations](docs/sdks/locations/README.md)

* [get](docs/sdks/locations/README.md#get) - Get location
* [list](docs/sdks/locations/README.md#list) - List locations

#### [sales.metrics](docs/sdks/metrics/README.md)

* [get_customer_retention](docs/sdks/metrics/README.md#get_customer_retention) - Get customer retention metrics
* [get_lifetime_value](docs/sdks/metrics/README.md#get_lifetime_value) - Get lifetime value metrics
* [get_revenue](docs/sdks/metrics/README.md#get_revenue) - Get commerce revenue metrics

#### [sales.orders](docs/sdks/orders/README.md)

* [get](docs/sdks/orders/README.md#get) - Get order
* [list](docs/sdks/orders/README.md#list) - List orders

#### [sales.payment_methods](docs/sdks/paymentmethods/README.md)

* [get](docs/sdks/paymentmethods/README.md#get) - Get payment method
* [list](docs/sdks/paymentmethods/README.md#list) - List payment methods

#### [sales.payments](docs/sdks/codatlendingsalespayments/README.md)

* [get](docs/sdks/codatlendingsalespayments/README.md#get) - Get payment
* [list](docs/sdks/codatlendingsalespayments/README.md#list) - List payments

#### [sales.product_categories](docs/sdks/productcategories/README.md)

* [get](docs/sdks/productcategories/README.md#get) - Get product category
* [list](docs/sdks/productcategories/README.md#list) - List product categories

#### [sales.products](docs/sdks/products/README.md)

* [get](docs/sdks/products/README.md#get) - Get product
* [list](docs/sdks/products/README.md#list) - List products

#### [sales.reports](docs/sdks/codatlendingreports/README.md)

* [get_orders](docs/sdks/codatlendingreports/README.md#get_orders) - Get orders report
* [get_refunds](docs/sdks/codatlendingreports/README.md#get_refunds) - Get refunds report

#### [sales.transactions](docs/sdks/codatlendingtransactions/README.md)

* [get](docs/sdks/codatlendingtransactions/README.md#get) - Get transaction
* [list](docs/sdks/codatlendingtransactions/README.md#list) - List transactions

### [transactions](docs/sdks/transactions/README.md)


#### [transactions.account_transactions](docs/sdks/accounttransactions/README.md)

* [get](docs/sdks/accounttransactions/README.md#get) - Get account transaction
* [list](docs/sdks/accounttransactions/README.md#list) - List account transactions

#### [transactions.direct_costs](docs/sdks/codatlendingdirectcosts/README.md)

* [download_attachment](docs/sdks/codatlendingdirectcosts/README.md#download_attachment) - Download direct cost attachment
* [get](docs/sdks/codatlendingdirectcosts/README.md#get) - Get direct cost
* [get_attachment](docs/sdks/codatlendingdirectcosts/README.md#get_attachment) - Get direct cost attachment
* [list](docs/sdks/codatlendingdirectcosts/README.md#list) - List direct costs
* [list_attachments](docs/sdks/codatlendingdirectcosts/README.md#list_attachments) - List direct cost attachments

#### [transactions.journal_entries](docs/sdks/journalentries/README.md)

* [get](docs/sdks/journalentries/README.md#get) - Get journal entry
* [list](docs/sdks/journalentries/README.md#list) - List journal entries

#### [transactions.journals](docs/sdks/journals/README.md)

* [get](docs/sdks/journals/README.md#get) - Get journal
* [list](docs/sdks/journals/README.md#list) - List journals

#### [transactions.transfers](docs/sdks/codatlendingtransfers/README.md)

* [get](docs/sdks/codatlendingtransfers/README.md#get) - Get transfer
* [list](docs/sdks/codatlendingtransfers/README.md#list) - List transfers

</details>
<!-- End Available Resources and Operations [operations] -->



<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from codat_lending import CodatLending
from codat_lending.models import shared
from codat_lending.utils import BackoffStrategy, RetryConfig

with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_lending:

    res = codat_lending.companies.create(request={
        "name": "Technicalium",
        "description": "Requested early access to the new financing scheme.",
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res is not None

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from codat_lending import CodatLending
from codat_lending.models import shared
from codat_lending.utils import BackoffStrategy, RetryConfig

with CodatLending(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_lending:

    res = codat_lending.companies.create(request={
        "name": "Technicalium",
        "description": "Requested early access to the new financing scheme.",
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_async` method may raise the following exceptions:

| Error Type          | Status Code                       | Content Type     |
| ------------------- | --------------------------------- | ---------------- |
| errors.ErrorMessage | 400, 401, 402, 403, 429, 500, 503 | application/json |
| errors.SDKError     | 4XX, 5XX                          | \*/\*            |

### Example

```python
from codat_lending import CodatLending
from codat_lending.models import errors, shared

with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_lending:
    res = None
    try:

        res = codat_lending.companies.create(request={
            "name": "Technicalium",
            "description": "Requested early access to the new financing scheme.",
        })

        assert res is not None

        # Handle response
        print(res)

    except errors.ErrorMessage as e:
        # handle e.data: errors.ErrorMessageData
        raise(e)
    except errors.SDKError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from codat_lending import CodatLending
from codat_lending.models import shared

with CodatLending(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_lending:

    res = codat_lending.companies.create(request={
        "name": "Technicalium",
        "description": "Requested early access to the new financing scheme.",
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from codat_lending import CodatLending
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatLending(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from codat_lending import CodatLending
from codat_lending.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = CodatLending(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type   | Scheme  |
| ------------- | ------ | ------- |
| `auth_header` | apiKey | API key |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
from codat_lending import CodatLending
from codat_lending.models import shared

with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_lending:

    res = codat_lending.companies.create(request={
        "name": "Technicalium",
        "description": "Requested early access to the new financing scheme.",
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from codat_lending import CodatLending
from codat_lending.models import shared

with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_lending:

    codat_lending.file_upload.upload(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Use the SDK ...

```
<!-- End File uploads [file-upload] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from codat_lending import CodatLending
import logging

logging.basicConfig(level=logging.DEBUG)
s = CodatLending(debug_logger=logging.getLogger("codat_lending"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

<!-- Start Codat Support Notes -->
## Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance. 
You can raise any issues by contacting your dedicated Codat representative or reaching out to our [support team](mailto:support@codat.io).
We're here to help ensure a smooth experience for you.
<!-- End Codat Support Notes -->

<!-- Start Codat Generated By -->
### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
<!-- End Codat Generated By -->