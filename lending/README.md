# Lending

Lending helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from the operating systems they are already using. You can use that data for automating decisioning and surfacing new insights on the customer, all via one API.

## Summary

Lending: Our Lending solution helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from accounting, banking, and commerce software they are already using. It also includes features to help providers verify the accuracy of data and process it more efficiently.

The Lending solution is built on top of the latest accounting, commerce, and banking data, providing you with the most important data points you need to get a full picture of SMB creditworthiness and make a comprehensive assessment of your customers.

[Explore solution](https://docs.codat.io/lending/overview) | [See OpenAPI spec](https://github.com/codatio/oas)

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

## Table of Contents

* [Summary](#summary)
* [Endpoints](#endpoints)
* [SDK Installation](#sdk-installation)
* [IDE Support](#ide-support)
* [SDK Example Usage](#sdk-example-usage)
* [Available Resources and Operations](#available-resources-and-operations)
* [File uploads](#file-uploads)
* [Retries](#retries)
* [Error Handling](#error-handling)
* [Server Selection](#server-selection)
* [Custom HTTP Client](#custom-http-client)
* [Authentication](#authentication)
* [Resource Management](#resource-management)
* [Support](#support)

## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add codat-lending
```

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

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from codat-lending python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "codat-lending",
# ]
# ///

from codat_lending import CodatLending

sdk = CodatLending(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.

## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)

## SDK Example Usage

### Example

```python
# Synchronous Example
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from codat_lending import CodatLending
from codat_lending.models import shared

async def main():

    async with CodatLending(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as cl_client:

        res = await cl_client.companies.list_async(request={
            "order_by": "-modifiedDate",
            "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
            "tags": "region=uk && team=invoice-finance",
        })

        # Handle response
        print(res)

asyncio.run(main())
```

## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [AccountingBankData](docs/sdks/codatlendingaccountingbankdata/README.md)

* [list_transactions](docs/sdks/codatlendingaccountingbankdata/README.md#list_transactions) - List bank account transactions

#### [AccountingBankData.Accounts](docs/sdks/accounts/README.md)

* [get](docs/sdks/accounts/README.md#get) - Get bank account
* [list](docs/sdks/accounts/README.md#list) - List bank accounts

### [AccountsPayable.BillCreditNotes](docs/sdks/billcreditnotes/README.md)

* [get](docs/sdks/billcreditnotes/README.md#get) - Get bill credit note
* [list](docs/sdks/billcreditnotes/README.md#list) - List bill credit notes

### [AccountsPayable.BillPayments](docs/sdks/billpayments/README.md)

* [get](docs/sdks/billpayments/README.md#get) - Get bill payment
* [list](docs/sdks/billpayments/README.md#list) - List bill payments

### [AccountsPayable.Bills](docs/sdks/bills/README.md)

* [download_attachment](docs/sdks/bills/README.md#download_attachment) - Download bill attachment
* [get](docs/sdks/bills/README.md#get) - Get bill
* [get_attachment](docs/sdks/bills/README.md#get_attachment) - Get bill attachment
* [list](docs/sdks/bills/README.md#list) - List bills
* [list_attachments](docs/sdks/bills/README.md#list_attachments) - List bill attachments

### [AccountsPayable.Suppliers](docs/sdks/suppliers/README.md)

* [download_attachment](docs/sdks/suppliers/README.md#download_attachment) - Download supplier attachment
* [get](docs/sdks/suppliers/README.md#get) - Get supplier
* [get_attachment](docs/sdks/suppliers/README.md#get_attachment) - Get supplier attachment
* [list](docs/sdks/suppliers/README.md#list) - List suppliers
* [list_attachments](docs/sdks/suppliers/README.md#list_attachments) - List supplier attachments

### [AccountsReceivable.CreditNotes](docs/sdks/creditnotes/README.md)

* [get](docs/sdks/creditnotes/README.md#get) - Get credit note
* [list](docs/sdks/creditnotes/README.md#list) - List credit notes

### [AccountsReceivable.Customers](docs/sdks/customers/README.md)

* [download_attachment](docs/sdks/customers/README.md#download_attachment) - Download customer attachment
* [get](docs/sdks/customers/README.md#get) - Get customer
* [get_attachment](docs/sdks/customers/README.md#get_attachment) - Get customer attachment
* [list](docs/sdks/customers/README.md#list) - List customers
* [list_attachments](docs/sdks/customers/README.md#list_attachments) - List customer attachments

### [AccountsReceivable.DirectIncomes](docs/sdks/directincomes/README.md)

* [download_attachment](docs/sdks/directincomes/README.md#download_attachment) - Download direct income attachment
* [get](docs/sdks/directincomes/README.md#get) - Get direct income
* [get_attachment](docs/sdks/directincomes/README.md#get_attachment) - Get direct income attachment
* [list](docs/sdks/directincomes/README.md#list) - List direct incomes
* [list_attachments](docs/sdks/directincomes/README.md#list_attachments) - List direct income attachments

### [AccountsReceivable.Invoices](docs/sdks/invoices/README.md)

* [download_attachment](docs/sdks/invoices/README.md#download_attachment) - Download invoice attachment
* [download_pdf](docs/sdks/invoices/README.md#download_pdf) - Get invoice as PDF
* [get](docs/sdks/invoices/README.md#get) - Get invoice
* [get_attachment](docs/sdks/invoices/README.md#get_attachment) - Get invoice attachment
* [list](docs/sdks/invoices/README.md#list) - List invoices
* [list_attachments](docs/sdks/invoices/README.md#list_attachments) - List invoice attachments
* [list_reconciled](docs/sdks/invoices/README.md#list_reconciled) - List reconciled invoices

### [AccountsReceivable.Payments](docs/sdks/payments/README.md)

* [get](docs/sdks/payments/README.md#get) - Get payment
* [list](docs/sdks/payments/README.md#list) - List payments

### [AccountsReceivable.Reports](docs/sdks/reports/README.md)

* [get_aged_creditors](docs/sdks/reports/README.md#get_aged_creditors) - Aged creditors report
* [get_aged_debtors](docs/sdks/reports/README.md#get_aged_debtors) - Aged debtors report
* [is_aged_creditors_available](docs/sdks/reports/README.md#is_aged_creditors_available) - Aged creditors report available
* [is_aged_debtors_available](docs/sdks/reports/README.md#is_aged_debtors_available) - Aged debtors report available

### [Banking.AccountBalances](docs/sdks/accountbalances/README.md)

* [list](docs/sdks/accountbalances/README.md#list) - List account balances

### [Banking.Accounts](docs/sdks/codatlendingaccounts/README.md)

* [get](docs/sdks/codatlendingaccounts/README.md#get) - Get account
* [list](docs/sdks/codatlendingaccounts/README.md#list) - List accounts

### [Banking.CategorizedStatement](docs/sdks/categorizedstatement/README.md)

* [get](docs/sdks/categorizedstatement/README.md#get) - Get categorized bank statement

### [Banking.TransactionCategories](docs/sdks/transactioncategories/README.md)

* [get](docs/sdks/transactioncategories/README.md#get) - Get transaction category
* [list](docs/sdks/transactioncategories/README.md#list) - List transaction categories

### [Banking.Transactions](docs/sdks/codatlendingbankingtransactions/README.md)

* [get](docs/sdks/codatlendingbankingtransactions/README.md#get) - Get bank transaction
* [list](docs/sdks/codatlendingbankingtransactions/README.md#list) - List transactions

### [BankStatements](docs/sdks/bankstatements/README.md)

* [download_categorized_bank_statement_excel](docs/sdks/bankstatements/README.md#download_categorized_bank_statement_excel) - Download categorized bank statement Excel
* [end_upload_session](docs/sdks/bankstatements/README.md#end_upload_session) - End upload session
* [get_categorized_bank_statement_transactions](docs/sdks/bankstatements/README.md#get_categorized_bank_statement_transactions) - Get categorized bank statement transactions
* [get_upload_configuration](docs/sdks/bankstatements/README.md#get_upload_configuration) - Get upload configuration
* [list_categorized_bank_statement_accounts](docs/sdks/bankstatements/README.md#list_categorized_bank_statement_accounts) - List categorized bank statement accounts
* [set_upload_configuration](docs/sdks/bankstatements/README.md#set_upload_configuration) - Set upload configuration
* [start_upload_session](docs/sdks/bankstatements/README.md#start_upload_session) - Start upload session
* [upload_bank_statement_data](docs/sdks/bankstatements/README.md#upload_bank_statement_data) - Upload data

### [Companies](docs/sdks/companies/README.md)

* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [list](docs/sdks/companies/README.md#list) - List companies
* [replace](docs/sdks/companies/README.md#replace) - Replace company
* [update](docs/sdks/companies/README.md#update) - Update company

### [CompanyInfo](docs/sdks/companyinfo/README.md)

* [get_accounting_profile](docs/sdks/companyinfo/README.md#get_accounting_profile) - Get company accounting profile
* [get_commerce_profile](docs/sdks/companyinfo/README.md#get_commerce_profile) - Get company commerce profile

### [Connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [list](docs/sdks/connections/README.md#list) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [DataIntegrity](docs/sdks/dataintegrity/README.md)

* [details](docs/sdks/dataintegrity/README.md#details) - List data integrity details
* [status](docs/sdks/dataintegrity/README.md#status) - Get data integrity status
* [summaries](docs/sdks/dataintegrity/README.md#summaries) - Get data integrity summaries

### [ExcelReports](docs/sdks/excelreports/README.md)

* [download](docs/sdks/excelreports/README.md#download) - Download Excel report
* [generate](docs/sdks/excelreports/README.md#generate) - Generate Excel report
* [get_status](docs/sdks/excelreports/README.md#get_status) - Get Excel report status

### [FileUpload](docs/sdks/fileupload/README.md)

* [download](docs/sdks/fileupload/README.md#download) - Download all files for a company
* [list_uploaded](docs/sdks/fileupload/README.md#list_uploaded) - List all files uploaded by a company
* [upload](docs/sdks/fileupload/README.md#upload) - Upload files for a company

### [FinancialStatements.Accounts](docs/sdks/codatlendingfinancialstatementsaccounts/README.md)

* [get](docs/sdks/codatlendingfinancialstatementsaccounts/README.md#get) - Get account
* [list](docs/sdks/codatlendingfinancialstatementsaccounts/README.md#list) - List accounts

### [FinancialStatements.BalanceSheet](docs/sdks/balancesheet/README.md)

* [get](docs/sdks/balancesheet/README.md#get) - Get balance sheet
* [get_categorized_accounts](docs/sdks/balancesheet/README.md#get_categorized_accounts) - Get categorized balance sheet statement

### [FinancialStatements.CashFlow](docs/sdks/cashflow/README.md)

* [get](docs/sdks/cashflow/README.md#get) - Get cash flow statement

### [FinancialStatements.ProfitAndLoss](docs/sdks/profitandloss/README.md)

* [get](docs/sdks/profitandloss/README.md#get) - Get profit and loss
* [get_categorized_accounts](docs/sdks/profitandloss/README.md#get_categorized_accounts) - Get categorized profit and loss statement

### [FinancialSummary](docs/sdks/financialsummary/README.md)

* [download_credit_model_excel](docs/sdks/financialsummary/README.md#download_credit_model_excel) - Download credit model Excel
* [get_financial_summary](docs/sdks/financialsummary/README.md#get_financial_summary) - Get financial summary insights

### [Liabilities](docs/sdks/liabilities/README.md)

* [generate_loan_summary](docs/sdks/liabilities/README.md#generate_loan_summary) - Generate loan summaries report
* [generate_loan_transactions](docs/sdks/liabilities/README.md#generate_loan_transactions) - Generate loan transactions report
* [get_loan_summary](docs/sdks/liabilities/README.md#get_loan_summary) - Get loan summaries
* [list_loan_transactions](docs/sdks/liabilities/README.md#list_loan_transactions) - List loan transactions

### [LoanWriteback.Accounts](docs/sdks/codatlendingloanwritebackaccounts/README.md)

* [create](docs/sdks/codatlendingloanwritebackaccounts/README.md#create) - Create account
* [get_create_model](docs/sdks/codatlendingloanwritebackaccounts/README.md#get_create_model) - Get create account model

### [LoanWriteback.BankAccounts](docs/sdks/bankaccounts/README.md)

* [create](docs/sdks/bankaccounts/README.md#create) - Create bank account
* [get_create_update_model](docs/sdks/bankaccounts/README.md#get_create_update_model) - Get create/update bank account model

### [LoanWriteback.BankTransactions](docs/sdks/banktransactions/README.md)

* [create](docs/sdks/banktransactions/README.md#create) - Create bank account transactions
* [get_create_model](docs/sdks/banktransactions/README.md#get_create_model) - Get create bank account transactions model

### [LoanWriteback.CreateOperations](docs/sdks/createoperations/README.md)

* [get](docs/sdks/createoperations/README.md#get) - Get create operation
* [list](docs/sdks/createoperations/README.md#list) - List create operations

### [LoanWriteback.DirectCosts](docs/sdks/directcosts/README.md)

* [create](docs/sdks/directcosts/README.md#create) - Create direct cost
* [get_create_model](docs/sdks/directcosts/README.md#get_create_model) - Get create direct cost model

### [LoanWriteback.Payments](docs/sdks/codatlendingpayments/README.md)

* [create](docs/sdks/codatlendingpayments/README.md#create) - Create payment
* [get_create_model](docs/sdks/codatlendingpayments/README.md#get_create_model) - Get create payment model

### [LoanWriteback.SourceAccounts](docs/sdks/sourceaccounts/README.md)

* [create](docs/sdks/sourceaccounts/README.md#create) - Create source account
* [create_mapping](docs/sdks/sourceaccounts/README.md#create_mapping) - Create bank feed account mapping
* [list_mappings](docs/sdks/sourceaccounts/README.md#list_mappings) - List bank feed account mappings

### [LoanWriteback.Suppliers](docs/sdks/codatlendingsuppliers/README.md)

* [create](docs/sdks/codatlendingsuppliers/README.md#create) - Create supplier
* [get_create_update_model](docs/sdks/codatlendingsuppliers/README.md#get_create_update_model) - Get create/update supplier model

### [LoanWriteback.Transfers](docs/sdks/transfers/README.md)

* [create](docs/sdks/transfers/README.md#create) - Create transfer
* [get_create_model](docs/sdks/transfers/README.md#get_create_model) - Get create transfer model

### [ManageData](docs/sdks/managedata/README.md)

* [get_status](docs/sdks/managedata/README.md#get_status) - Get data status

#### [ManageData.PullOperations](docs/sdks/pulloperations/README.md)

* [get](docs/sdks/pulloperations/README.md#get) - Get pull operation
* [list](docs/sdks/pulloperations/README.md#list) - List pull operations

#### [ManageData.Refresh](docs/sdks/refresh/README.md)

* [all_data_types](docs/sdks/refresh/README.md#all_data_types) - Refresh all data
* [data_type](docs/sdks/refresh/README.md#data_type) - Refresh data type

### [ManageReports](docs/sdks/managereports/README.md)

* [generate_report](docs/sdks/managereports/README.md#generate_report) - Generate report
* [get_report_status](docs/sdks/managereports/README.md#get_report_status) - Get report status
* [list_reports](docs/sdks/managereports/README.md#list_reports) - List reports

### [Sales.Customers](docs/sdks/codatlendingcustomers/README.md)

* [get](docs/sdks/codatlendingcustomers/README.md#get) - Get customer
* [list](docs/sdks/codatlendingcustomers/README.md#list) - List customers

### [Sales.Disputes](docs/sdks/disputes/README.md)

* [get](docs/sdks/disputes/README.md#get) - Get dispute
* [list](docs/sdks/disputes/README.md#list) - List disputes

### [Sales.Locations](docs/sdks/locations/README.md)

* [get](docs/sdks/locations/README.md#get) - Get location
* [list](docs/sdks/locations/README.md#list) - List locations

### [Sales.Metrics](docs/sdks/metrics/README.md)

* [get_customer_retention](docs/sdks/metrics/README.md#get_customer_retention) - Get customer retention metrics
* [get_lifetime_value](docs/sdks/metrics/README.md#get_lifetime_value) - Get lifetime value metrics
* [get_revenue](docs/sdks/metrics/README.md#get_revenue) - Get commerce revenue metrics

### [Sales.Orders](docs/sdks/orders/README.md)

* [get](docs/sdks/orders/README.md#get) - Get order
* [list](docs/sdks/orders/README.md#list) - List orders

### [Sales.PaymentMethods](docs/sdks/paymentmethods/README.md)

* [get](docs/sdks/paymentmethods/README.md#get) - Get payment method
* [list](docs/sdks/paymentmethods/README.md#list) - List payment methods

### [Sales.Payments](docs/sdks/codatlendingsalespayments/README.md)

* [get](docs/sdks/codatlendingsalespayments/README.md#get) - Get payment
* [list](docs/sdks/codatlendingsalespayments/README.md#list) - List payments

### [Sales.ProductCategories](docs/sdks/productcategories/README.md)

* [get](docs/sdks/productcategories/README.md#get) - Get product category
* [list](docs/sdks/productcategories/README.md#list) - List product categories

### [Sales.Products](docs/sdks/products/README.md)

* [get](docs/sdks/products/README.md#get) - Get product
* [list](docs/sdks/products/README.md#list) - List products

### [Sales.Reports](docs/sdks/codatlendingreports/README.md)

* [get_orders](docs/sdks/codatlendingreports/README.md#get_orders) - Get orders report
* [get_refunds](docs/sdks/codatlendingreports/README.md#get_refunds) - Get refunds report

### [Sales.Transactions](docs/sdks/codatlendingtransactions/README.md)

* [get](docs/sdks/codatlendingtransactions/README.md#get) - Get transaction
* [list](docs/sdks/codatlendingtransactions/README.md#list) - List transactions

### [Transactions.AccountTransactions](docs/sdks/accounttransactions/README.md)

* [get](docs/sdks/accounttransactions/README.md#get) - Get account transaction
* [list](docs/sdks/accounttransactions/README.md#list) - List account transactions

### [Transactions.DirectCosts](docs/sdks/codatlendingdirectcosts/README.md)

* [download_attachment](docs/sdks/codatlendingdirectcosts/README.md#download_attachment) - Download direct cost attachment
* [get](docs/sdks/codatlendingdirectcosts/README.md#get) - Get direct cost
* [get_attachment](docs/sdks/codatlendingdirectcosts/README.md#get_attachment) - Get direct cost attachment
* [list](docs/sdks/codatlendingdirectcosts/README.md#list) - List direct costs
* [list_attachments](docs/sdks/codatlendingdirectcosts/README.md#list_attachments) - List direct cost attachments

### [Transactions.JournalEntries](docs/sdks/journalentries/README.md)

* [get](docs/sdks/journalentries/README.md#get) - Get journal entry
* [list](docs/sdks/journalentries/README.md#list) - List journal entries

### [Transactions.Journals](docs/sdks/journals/README.md)

* [get](docs/sdks/journals/README.md#get) - Get journal
* [list](docs/sdks/journals/README.md#list) - List journals

### [Transactions.Transfers](docs/sdks/codatlendingtransfers/README.md)

* [get](docs/sdks/codatlendingtransfers/README.md#get) - Get transfer
* [list](docs/sdks/codatlendingtransfers/README.md#list) - List transfers

</details>

## File uploads

Certain SDK methods accept files as part of a multi-part request. Pass each file as its name and its contents in bytes. The following example demonstrates how to attach a file to a request.

```python
from pathlib import Path
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    cl_client.file_upload.upload(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "file_upload": {
            "file": {
                "file_name": "example.file",
                "content": Path("example.file").read_bytes(),
            },
        },
    })

    # Use the SDK ...
```

## Retries

Every operation in this SDK retries failed requests with a default backoff strategy. By default it retries connection errors and responses with status 408, 429 or 5XX, starting at 500 ms and backing off by a factor of 1.5 up to 60 s between attempts, for at most an hour. You can override the retry strategy for a single call, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from codat_lending import CodatLending
from codat_lending.models import shared
from codat_lending.utils import BackoffStrategy, RetryConfig


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    }, retries=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)
```

If you'd like to override the default retry strategy for all operations, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from codat_lending import CodatLending
from codat_lending.models import shared
from codat_lending.utils import BackoffStrategy, RetryConfig


with CodatLending(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    })

    # Handle response
    print(res)
```

## Error Handling

[`CodatLendingError`](./src/codat_lending/models/errors/codatlendingerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type                  | Description                                                                             |
| ------------------ | --------------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`                 | Error message                                                                           |
| `err.status_code`  | `int`                 | HTTP response status code eg `404`                                                      |
| `err.headers`      | `Mapping[str, str]`   | HTTP response headers, looked up case-insensitively                                     |
| `err.body`         | `str`                 | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `Any`                 | The SDK exception or response the error was built from; prefer the properties above     |
| `err.data`         |                       | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from codat_lending import CodatLending
from codat_lending.models import errors, shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:
    res = None
    try:

        res = cl_client.companies.list(request={
            "order_by": "-modifiedDate",
            "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
            "tags": "region=uk && team=invoice-finance",
        })

        # Handle response
        print(res)

    except errors.CodatLendingError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.ErrorMessage):
            print(e.data.can_be_retried)  # Optional[str]
            print(e.data.correlation_id)  # Optional[str]
            print(e.data.detailed_error_code)  # Optional[int]
            print(e.data.error)  # Optional[str]
            print(e.data.service)  # Optional[str]
```

### Error Classes
**Primary errors:**
* [`CodatLendingError`](./src/codat_lending/models/errors/codatlendingerror.py): The base class for HTTP error responses.
  * [`ErrorMessage`](./src/codat_lending/models/errors/errormessage.py): A Codat API error response. Its structured fields are on `err.data`.

<details><summary>Less common errors (2)</summary>

<br />

**Inherit from [`CodatLendingError`](./src/codat_lending/models/errors/codatlendingerror.py)**:
* [`SDKError`](./src/codat_lending/models/errors/sdkerror.py): The fallback error class if no more specific error class is matched.
* [`ResponseValidationError`](./src/codat_lending/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

Network failures, such as a refused connection or a timeout, are raised by the underlying HTTP library: `urllib3` by default, or `httpx` when you pass `client`.

## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    })

    # Handle response
    print(res)
```

## Custom HTTP Client

The Python SDK can make its API calls through an [httpx](https://www.python-httpx.org/) client you provide. This is a convenient way to configure cookies, proxies, custom headers, and other low-level settings. Pass an `httpx.Client` instance as the `client` parameter when initializing the SDK. It carries every request, including those made by the `_async` methods. The `async_client` parameter is accepted for compatibility with earlier SDK versions but is not used.

The SDK sets the timeout of every request itself, so a timeout configured on the `httpx.Client` is overridden. Use the `timeout_ms` parameter instead, when initializing the SDK or on a single call. The default is 5000 ms.

For example, you could specify a header for every request that this SDK makes as follows:
```python
from codat_lending import CodatLending
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatLending(client=http_client)
```

or you could subclass `httpx.Client` to wrap each request in your own custom logic:
```python
from codat_lending import CodatLending
import httpx


class CustomClient(httpx.Client):
    def send(self, request: httpx.Request, **kwargs) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"
        return super().send(request, **kwargs)


s = CodatLending(client=CustomClient())
```

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
) as cl_client:

    res = cl_client.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    })

    # Handle response
    print(res)
```

## Resource Management

The `CodatLending` class implements the context manager protocol, so existing code that uses it in a `with` or `async with` block keeps working. Leaving the context does not close any HTTP connections: if you pass your own `client`, close it yourself when you are done. In longer-lived programs, create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from codat_lending import CodatLending
from codat_lending.models import shared
def main():

    with CodatLending(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as cl_client:
        # Rest of application here...
        pass


# Or when using async:
async def amain():

    async with CodatLending(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as cl_client:
        # Rest of application here...
        pass
```

## Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance.
You can raise any issues by contacting your dedicated Codat representative or reaching out to our [support team](mailto:support@codat.io).
We're here to help ensure a smooth experience for you.
