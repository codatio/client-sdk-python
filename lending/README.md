# Lending
    
Lending helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from the operating systems they are already using. You can use that data for automating decisioning and surfacing new insights on the customer, all via one API.

## SDK Installation

```bash
pip install codat-lending
```## SDK Installation

```bash
pip install codat-lending
```## SDK Installation

```bash
pip install codat-lending
```## SDK Installation

```bash
pip install codat-lending
```<!-- Start SDK Installation -->

<!-- End SDK Installation -->

## Example Usage


```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountingBankAccountRequest(
    account_id='corrupti',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.accounting_bank_data.get_account(req)

if res.accounting_bank_account is not None:
    # handle response
```

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountingBankAccountRequest(
    account_id='corrupti',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.accounting_bank_data.get_account(req)

if res.accounting_bank_account is not None:
    # handle response
```

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountingProfileRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.get_accounting_profile(req)

if res.accounting_company_info is not None:
    # handle response
```

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListAccountingBankAccountTransactionsRequest(
    account_id='corrupti',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='provident',
)

res = s.accounting_bank_data.list_transactions(req)

if res.accounting_bank_transactions is not None:
    # handle response
```<!-- Start SDK Example Usage -->

<!-- End SDK Example Usage -->

## Available Resources and Operations


### [accounting_bank_data](docs/sdks/accountingbankdata/README.md)

* [get_account](docs/sdks/accountingbankdata/README.md#get_account) - Get bank account
* [list_accounts](docs/sdks/accountingbankdata/README.md#list_accounts) - List bank accounts
* [list_transactions](docs/sdks/accountingbankdata/README.md#list_transactions) - List bank account transactions

### [accounts_payable](docs/sdks/accountspayable/README.md)

* [download_bill_attachment](docs/sdks/accountspayable/README.md#download_bill_attachment) - Download bill attachment
* [download_supplier_attachment](docs/sdks/accountspayable/README.md#download_supplier_attachment) - Download supplier attachment
* [get_aged_creditors_report](docs/sdks/accountspayable/README.md#get_aged_creditors_report) - Aged creditors report
* [get_bill](docs/sdks/accountspayable/README.md#get_bill) - Get bill
* [get_bill_attachment](docs/sdks/accountspayable/README.md#get_bill_attachment) - Get bill attachment
* [get_bill_credit_note](docs/sdks/accountspayable/README.md#get_bill_credit_note) - Get bill credit note
* [get_bill_payment](docs/sdks/accountspayable/README.md#get_bill_payment) - Get bill payment
* [get_supplier](docs/sdks/accountspayable/README.md#get_supplier) - Get supplier
* [get_supplier_attachment](docs/sdks/accountspayable/README.md#get_supplier_attachment) - Get supplier attachment
* [is_aged_creditors_report_available](docs/sdks/accountspayable/README.md#is_aged_creditors_report_available) - Aged creditors report available
* [list_bill_attachments](docs/sdks/accountspayable/README.md#list_bill_attachments) - List bill attachments
* [list_bill_credit_notes](docs/sdks/accountspayable/README.md#list_bill_credit_notes) - List bill credit notes
* [list_bill_payments](docs/sdks/accountspayable/README.md#list_bill_payments) - List bill payments
* [list_bills](docs/sdks/accountspayable/README.md#list_bills) - List bills
* [list_supplier_attachments](docs/sdks/accountspayable/README.md#list_supplier_attachments) - List supplier attachments
* [list_suppliers](docs/sdks/accountspayable/README.md#list_suppliers) - List suppliers

### [accounts_receivable](docs/sdks/accountsreceivable/README.md)

* [download_customer_attachment](docs/sdks/accountsreceivable/README.md#download_customer_attachment) - Download customer attachment
* [download_direct_income_attachment](docs/sdks/accountsreceivable/README.md#download_direct_income_attachment) - Download direct income attachment
* [download_invoice_attachment](docs/sdks/accountsreceivable/README.md#download_invoice_attachment) - Download invoice attachment
* [download_invoice_pdf](docs/sdks/accountsreceivable/README.md#download_invoice_pdf) - Get invoice as PDF
* [get_aged_debtors_report](docs/sdks/accountsreceivable/README.md#get_aged_debtors_report) - Aged debtors report
* [get_credit_note](docs/sdks/accountsreceivable/README.md#get_credit_note) - Get credit note
* [get_customer](docs/sdks/accountsreceivable/README.md#get_customer) - Get customer
* [get_customer_attachment](docs/sdks/accountsreceivable/README.md#get_customer_attachment) - Get customer attachment
* [get_direct_income](docs/sdks/accountsreceivable/README.md#get_direct_income) - Get direct income
* [get_direct_income_attachment](docs/sdks/accountsreceivable/README.md#get_direct_income_attachment) - Get direct income attachment
* [get_invoice](docs/sdks/accountsreceivable/README.md#get_invoice) - Get invoice
* [get_invoice_attachment](docs/sdks/accountsreceivable/README.md#get_invoice_attachment) - Get invoice attachment
* [get_payment](docs/sdks/accountsreceivable/README.md#get_payment) - Get payment
* [get_reconciled_invoices](docs/sdks/accountsreceivable/README.md#get_reconciled_invoices) - Get reconciled invoices
* [is_aged_debtor_report_available](docs/sdks/accountsreceivable/README.md#is_aged_debtor_report_available) - Aged debtors report available
* [list_credit_notes](docs/sdks/accountsreceivable/README.md#list_credit_notes) - List credit notes
* [list_customer_attachments](docs/sdks/accountsreceivable/README.md#list_customer_attachments) - List customer attachments
* [list_customers](docs/sdks/accountsreceivable/README.md#list_customers) - List customers
* [list_direct_income_attachments](docs/sdks/accountsreceivable/README.md#list_direct_income_attachments) - List direct income attachments
* [list_direct_incomes](docs/sdks/accountsreceivable/README.md#list_direct_incomes) - List direct incomes
* [list_invoice_attachments](docs/sdks/accountsreceivable/README.md#list_invoice_attachments) - List invoice attachments
* [list_invoices](docs/sdks/accountsreceivable/README.md#list_invoices) - List invoices
* [list_payments](docs/sdks/accountsreceivable/README.md#list_payments) - List payments

### [banking](docs/sdks/banking/README.md)

* [get_bank_account](docs/sdks/banking/README.md#get_bank_account) - Get account
* [get_bank_transaction](docs/sdks/banking/README.md#get_bank_transaction) - Get bank transaction
* [get_bank_transaction_category](docs/sdks/banking/README.md#get_bank_transaction_category) - Get transaction category
* [get_categorized_bank_statement](docs/sdks/banking/README.md#get_categorized_bank_statement) - Get categorized bank statement
* [list_bank_account_balances](docs/sdks/banking/README.md#list_bank_account_balances) - List account balances
* [list_bank_accounts](docs/sdks/banking/README.md#list_bank_accounts) - List accounts
* [list_bank_transaction_categories](docs/sdks/banking/README.md#list_bank_transaction_categories) - List transaction categories
* [list_bank_transactions](docs/sdks/banking/README.md#list_bank_transactions) - List transactions

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

* [get_account](docs/sdks/financialstatements/README.md#get_account) - Get account
* [get_balance_sheet](docs/sdks/financialstatements/README.md#get_balance_sheet) - Get balance sheet
* [get_cash_flow_statement](docs/sdks/financialstatements/README.md#get_cash_flow_statement) - Get cash flow statement
* [get_categorized_balance_sheet](docs/sdks/financialstatements/README.md#get_categorized_balance_sheet) - Get categorized balance sheet statement
* [get_categorized_profit_and_loss](docs/sdks/financialstatements/README.md#get_categorized_profit_and_loss) - Get categorized profit and loss statement
* [get_profit_and_loss](docs/sdks/financialstatements/README.md#get_profit_and_loss) - Get profit and loss
* [list_accounts](docs/sdks/financialstatements/README.md#list_accounts) - List accounts

### [liabilities](docs/sdks/liabilities/README.md)

* [get_loan_summary](docs/sdks/liabilities/README.md#get_loan_summary) - Get loan summaries
* [list_loan_transactions](docs/sdks/liabilities/README.md#list_loan_transactions) - List loan transactions

### [manage_data](docs/sdks/managedata/README.md)

* [get](docs/sdks/managedata/README.md#get) - Get data status
* [get_pull_operation](docs/sdks/managedata/README.md#get_pull_operation) - Get pull operation
* [list_pull_operations](docs/sdks/managedata/README.md#list_pull_operations) - List pull operations
* [refresh_all_data_types](docs/sdks/managedata/README.md#refresh_all_data_types) - Refresh all data
* [refresh_data_type](docs/sdks/managedata/README.md#refresh_data_type) - Refresh data type

### [sales](docs/sdks/sales/README.md)

* [get_customer](docs/sdks/sales/README.md#get_customer) - Get customer
* [get_customer_retention_metrics](docs/sdks/sales/README.md#get_customer_retention_metrics) - Get customer retention metrics
* [get_dispute](docs/sdks/sales/README.md#get_dispute) - Get dispute
* [get_lifetime_value_metrics](docs/sdks/sales/README.md#get_lifetime_value_metrics) - Get lifetime value metrics
* [get_location](docs/sdks/sales/README.md#get_location) - Get location
* [get_order](docs/sdks/sales/README.md#get_order) - Get order
* [get_orders_report](docs/sdks/sales/README.md#get_orders_report) - Get orders report
* [get_payment](docs/sdks/sales/README.md#get_payment) - Get payment
* [get_payment_method](docs/sdks/sales/README.md#get_payment_method) - Get payment method
* [get_product](docs/sdks/sales/README.md#get_product) - Get product
* [get_product_category](docs/sdks/sales/README.md#get_product_category) - Get product category
* [get_refunds_report](docs/sdks/sales/README.md#get_refunds_report) - Get refunds report
* [get_revenue_metrics](docs/sdks/sales/README.md#get_revenue_metrics) - Get commerce revenue metrics
* [get_transaction](docs/sdks/sales/README.md#get_transaction) - Get transaction
* [list_customers](docs/sdks/sales/README.md#list_customers) - List customers
* [list_disputes](docs/sdks/sales/README.md#list_disputes) - List disputes
* [list_locations](docs/sdks/sales/README.md#list_locations) - List locations
* [list_orders](docs/sdks/sales/README.md#list_orders) - List orders
* [list_payment_methods](docs/sdks/sales/README.md#list_payment_methods) - List payment methods
* [list_payments](docs/sdks/sales/README.md#list_payments) - List payments
* [list_product_categories](docs/sdks/sales/README.md#list_product_categories) - List product categories
* [list_products](docs/sdks/sales/README.md#list_products) - List products
* [list_transactions](docs/sdks/sales/README.md#list_transactions) - List transactions

### [transactions](docs/sdks/transactions/README.md)

* [download_direct_cost_attachment](docs/sdks/transactions/README.md#download_direct_cost_attachment) - Download direct cost attachment
* [get_account_transaction](docs/sdks/transactions/README.md#get_account_transaction) - Get account transaction
* [get_direct_cost](docs/sdks/transactions/README.md#get_direct_cost) - Get direct cost
* [get_direct_cost_attachment](docs/sdks/transactions/README.md#get_direct_cost_attachment) - Get direct cost attachment
* [get_journal](docs/sdks/transactions/README.md#get_journal) - Get journal
* [get_journal_entry](docs/sdks/transactions/README.md#get_journal_entry) - Get journal entry
* [get_transfer](docs/sdks/transactions/README.md#get_transfer) - Get transfer
* [list_account_transactions](docs/sdks/transactions/README.md#list_account_transactions) - List account transactions
* [list_direct_cost_attachments](docs/sdks/transactions/README.md#list_direct_cost_attachments) - List direct cost attachments
* [list_direct_costs](docs/sdks/transactions/README.md#list_direct_costs) - List direct costs
* [list_journal_entries](docs/sdks/transactions/README.md#list_journal_entries) - List journal entries
* [list_journals](docs/sdks/transactions/README.md#list_journals) - List journals
* [list_transfers](docs/sdks/transactions/README.md#list_transfers) - List transfers## Available Resources and Operations


### [accounting_bank_data](docs/sdks/accountingbankdata/README.md)

* [get_account](docs/sdks/accountingbankdata/README.md#get_account) - Get bank account
* [list_accounts](docs/sdks/accountingbankdata/README.md#list_accounts) - List bank accounts
* [list_transactions](docs/sdks/accountingbankdata/README.md#list_transactions) - List bank account transactions

### [accounts_payable](docs/sdks/accountspayable/README.md)

* [download_bill_attachment](docs/sdks/accountspayable/README.md#download_bill_attachment) - Download bill attachment
* [download_supplier_attachment](docs/sdks/accountspayable/README.md#download_supplier_attachment) - Download supplier attachment
* [get_aged_creditors_report](docs/sdks/accountspayable/README.md#get_aged_creditors_report) - Aged creditors report
* [get_bill](docs/sdks/accountspayable/README.md#get_bill) - Get bill
* [get_bill_attachment](docs/sdks/accountspayable/README.md#get_bill_attachment) - Get bill attachment
* [get_bill_credit_note](docs/sdks/accountspayable/README.md#get_bill_credit_note) - Get bill credit note
* [get_bill_payment](docs/sdks/accountspayable/README.md#get_bill_payment) - Get bill payment
* [get_supplier](docs/sdks/accountspayable/README.md#get_supplier) - Get supplier
* [get_supplier_attachment](docs/sdks/accountspayable/README.md#get_supplier_attachment) - Get supplier attachment
* [is_aged_creditors_report_available](docs/sdks/accountspayable/README.md#is_aged_creditors_report_available) - Aged creditors report available
* [list_bill_attachments](docs/sdks/accountspayable/README.md#list_bill_attachments) - List bill attachments
* [list_bill_credit_notes](docs/sdks/accountspayable/README.md#list_bill_credit_notes) - List bill credit notes
* [list_bill_payments](docs/sdks/accountspayable/README.md#list_bill_payments) - List bill payments
* [list_bills](docs/sdks/accountspayable/README.md#list_bills) - List bills
* [list_supplier_attachments](docs/sdks/accountspayable/README.md#list_supplier_attachments) - List supplier attachments
* [list_suppliers](docs/sdks/accountspayable/README.md#list_suppliers) - List suppliers

### [accounts_receivable](docs/sdks/accountsreceivable/README.md)

* [download_customer_attachment](docs/sdks/accountsreceivable/README.md#download_customer_attachment) - Download customer attachment
* [download_direct_income_attachment](docs/sdks/accountsreceivable/README.md#download_direct_income_attachment) - Download direct income attachment
* [download_invoice_attachment](docs/sdks/accountsreceivable/README.md#download_invoice_attachment) - Download invoice attachment
* [download_invoice_pdf](docs/sdks/accountsreceivable/README.md#download_invoice_pdf) - Get invoice as PDF
* [get_aged_debtors_report](docs/sdks/accountsreceivable/README.md#get_aged_debtors_report) - Aged debtors report
* [get_credit_note](docs/sdks/accountsreceivable/README.md#get_credit_note) - Get credit note
* [get_customer](docs/sdks/accountsreceivable/README.md#get_customer) - Get customer
* [get_customer_attachment](docs/sdks/accountsreceivable/README.md#get_customer_attachment) - Get customer attachment
* [get_direct_income](docs/sdks/accountsreceivable/README.md#get_direct_income) - Get direct income
* [get_direct_income_attachment](docs/sdks/accountsreceivable/README.md#get_direct_income_attachment) - Get direct income attachment
* [get_invoice](docs/sdks/accountsreceivable/README.md#get_invoice) - Get invoice
* [get_invoice_attachment](docs/sdks/accountsreceivable/README.md#get_invoice_attachment) - Get invoice attachment
* [get_payment](docs/sdks/accountsreceivable/README.md#get_payment) - Get payment
* [get_reconciled_invoices](docs/sdks/accountsreceivable/README.md#get_reconciled_invoices) - Get reconciled invoices
* [is_aged_debtor_report_available](docs/sdks/accountsreceivable/README.md#is_aged_debtor_report_available) - Aged debtors report available
* [list_credit_notes](docs/sdks/accountsreceivable/README.md#list_credit_notes) - List credit notes
* [list_customer_attachments](docs/sdks/accountsreceivable/README.md#list_customer_attachments) - List customer attachments
* [list_customers](docs/sdks/accountsreceivable/README.md#list_customers) - List customers
* [list_direct_income_attachments](docs/sdks/accountsreceivable/README.md#list_direct_income_attachments) - List direct income attachments
* [list_direct_incomes](docs/sdks/accountsreceivable/README.md#list_direct_incomes) - List direct incomes
* [list_invoice_attachments](docs/sdks/accountsreceivable/README.md#list_invoice_attachments) - List invoice attachments
* [list_invoices](docs/sdks/accountsreceivable/README.md#list_invoices) - List invoices
* [list_payments](docs/sdks/accountsreceivable/README.md#list_payments) - List payments

### [banking](docs/sdks/banking/README.md)

* [get_bank_account](docs/sdks/banking/README.md#get_bank_account) - Get account
* [get_bank_transaction](docs/sdks/banking/README.md#get_bank_transaction) - Get bank transaction
* [get_bank_transaction_category](docs/sdks/banking/README.md#get_bank_transaction_category) - Get transaction category
* [get_categorized_bank_statement](docs/sdks/banking/README.md#get_categorized_bank_statement) - Get categorized bank statement
* [list_bank_account_balances](docs/sdks/banking/README.md#list_bank_account_balances) - List account balances
* [list_bank_accounts](docs/sdks/banking/README.md#list_bank_accounts) - List accounts
* [list_bank_transaction_categories](docs/sdks/banking/README.md#list_bank_transaction_categories) - List transaction categories
* [list_bank_transactions](docs/sdks/banking/README.md#list_bank_transactions) - List transactions

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

* [get_account](docs/sdks/financialstatements/README.md#get_account) - Get account
* [get_balance_sheet](docs/sdks/financialstatements/README.md#get_balance_sheet) - Get balance sheet
* [get_cash_flow_statement](docs/sdks/financialstatements/README.md#get_cash_flow_statement) - Get cash flow statement
* [get_categorized_balance_sheet](docs/sdks/financialstatements/README.md#get_categorized_balance_sheet) - Get categorized balance sheet statement
* [get_categorized_profit_and_loss](docs/sdks/financialstatements/README.md#get_categorized_profit_and_loss) - Get categorized profit and loss statement
* [get_profit_and_loss](docs/sdks/financialstatements/README.md#get_profit_and_loss) - Get profit and loss
* [list_accounts](docs/sdks/financialstatements/README.md#list_accounts) - List accounts

### [liabilities](docs/sdks/liabilities/README.md)

* [get_loan_summary](docs/sdks/liabilities/README.md#get_loan_summary) - Get loan summaries
* [list_loan_transactions](docs/sdks/liabilities/README.md#list_loan_transactions) - List loan transactions

### [manage_data](docs/sdks/managedata/README.md)

* [get](docs/sdks/managedata/README.md#get) - Get data status
* [get_pull_operation](docs/sdks/managedata/README.md#get_pull_operation) - Get pull operation
* [list_pull_operations](docs/sdks/managedata/README.md#list_pull_operations) - List pull operations
* [refresh_all_data_types](docs/sdks/managedata/README.md#refresh_all_data_types) - Refresh all data
* [refresh_data_type](docs/sdks/managedata/README.md#refresh_data_type) - Refresh data type

### [sales](docs/sdks/sales/README.md)

* [get_customer](docs/sdks/sales/README.md#get_customer) - Get customer
* [get_customer_retention_metrics](docs/sdks/sales/README.md#get_customer_retention_metrics) - Get customer retention metrics
* [get_dispute](docs/sdks/sales/README.md#get_dispute) - Get dispute
* [get_lifetime_value_metrics](docs/sdks/sales/README.md#get_lifetime_value_metrics) - Get lifetime value metrics
* [get_location](docs/sdks/sales/README.md#get_location) - Get location
* [get_order](docs/sdks/sales/README.md#get_order) - Get order
* [get_orders_report](docs/sdks/sales/README.md#get_orders_report) - Get orders report
* [get_payment](docs/sdks/sales/README.md#get_payment) - Get payment
* [get_payment_method](docs/sdks/sales/README.md#get_payment_method) - Get payment method
* [get_product](docs/sdks/sales/README.md#get_product) - Get product
* [get_product_category](docs/sdks/sales/README.md#get_product_category) - Get product category
* [get_refunds_report](docs/sdks/sales/README.md#get_refunds_report) - Get refunds report
* [get_revenue_metrics](docs/sdks/sales/README.md#get_revenue_metrics) - Get commerce revenue metrics
* [get_transaction](docs/sdks/sales/README.md#get_transaction) - Get transaction
* [list_customers](docs/sdks/sales/README.md#list_customers) - List customers
* [list_disputes](docs/sdks/sales/README.md#list_disputes) - List disputes
* [list_locations](docs/sdks/sales/README.md#list_locations) - List locations
* [list_orders](docs/sdks/sales/README.md#list_orders) - List orders
* [list_payment_methods](docs/sdks/sales/README.md#list_payment_methods) - List payment methods
* [list_payments](docs/sdks/sales/README.md#list_payments) - List payments
* [list_product_categories](docs/sdks/sales/README.md#list_product_categories) - List product categories
* [list_products](docs/sdks/sales/README.md#list_products) - List products
* [list_transactions](docs/sdks/sales/README.md#list_transactions) - List transactions

### [transactions](docs/sdks/transactions/README.md)

* [download_direct_cost_attachment](docs/sdks/transactions/README.md#download_direct_cost_attachment) - Download direct cost attachment
* [get_account_transaction](docs/sdks/transactions/README.md#get_account_transaction) - Get account transaction
* [get_direct_cost](docs/sdks/transactions/README.md#get_direct_cost) - Get direct cost
* [get_direct_cost_attachment](docs/sdks/transactions/README.md#get_direct_cost_attachment) - Get direct cost attachment
* [get_journal](docs/sdks/transactions/README.md#get_journal) - Get journal
* [get_journal_entry](docs/sdks/transactions/README.md#get_journal_entry) - Get journal entry
* [get_transfer](docs/sdks/transactions/README.md#get_transfer) - Get transfer
* [list_account_transactions](docs/sdks/transactions/README.md#list_account_transactions) - List account transactions
* [list_direct_cost_attachments](docs/sdks/transactions/README.md#list_direct_cost_attachments) - List direct cost attachments
* [list_direct_costs](docs/sdks/transactions/README.md#list_direct_costs) - List direct costs
* [list_journal_entries](docs/sdks/transactions/README.md#list_journal_entries) - List journal entries
* [list_journals](docs/sdks/transactions/README.md#list_journals) - List journals
* [list_transfers](docs/sdks/transactions/README.md#list_transfers) - List transfers## Available Resources and Operations

### [CodatLending SDK](docs/sdks/codatlending/README.md)

* [get_accounting_profile](docs/sdks/codatlending/README.md#get_accounting_profile) - Get company accounting profile

### [accounting_bank_data](docs/sdks/accountingbankdata/README.md)

* [get_account](docs/sdks/accountingbankdata/README.md#get_account) - Get bank account
* [list_accounts](docs/sdks/accountingbankdata/README.md#list_accounts) - List bank accounts
* [list_transactions](docs/sdks/accountingbankdata/README.md#list_transactions) - List bank account transactions

### [accounts_payable](docs/sdks/accountspayable/README.md)

* [download_bill_attachment](docs/sdks/accountspayable/README.md#download_bill_attachment) - Download bill attachment
* [download_supplier_attachment](docs/sdks/accountspayable/README.md#download_supplier_attachment) - Download supplier attachment
* [get_aged_creditors_report](docs/sdks/accountspayable/README.md#get_aged_creditors_report) - Aged creditors report
* [get_bill](docs/sdks/accountspayable/README.md#get_bill) - Get bill
* [get_bill_attachment](docs/sdks/accountspayable/README.md#get_bill_attachment) - Get bill attachment
* [get_bill_credit_note](docs/sdks/accountspayable/README.md#get_bill_credit_note) - Get bill credit note
* [get_bill_payment](docs/sdks/accountspayable/README.md#get_bill_payment) - Get bill payment
* [get_supplier](docs/sdks/accountspayable/README.md#get_supplier) - Get supplier
* [get_supplier_attachment](docs/sdks/accountspayable/README.md#get_supplier_attachment) - Get supplier attachment
* [is_aged_creditors_report_available](docs/sdks/accountspayable/README.md#is_aged_creditors_report_available) - Aged creditors report available
* [list_bill_attachments](docs/sdks/accountspayable/README.md#list_bill_attachments) - List bill attachments
* [list_bill_credit_notes](docs/sdks/accountspayable/README.md#list_bill_credit_notes) - List bill credit notes
* [list_bill_payments](docs/sdks/accountspayable/README.md#list_bill_payments) - List bill payments
* [list_bills](docs/sdks/accountspayable/README.md#list_bills) - List bills
* [list_supplier_attachments](docs/sdks/accountspayable/README.md#list_supplier_attachments) - List supplier attachments
* [list_suppliers](docs/sdks/accountspayable/README.md#list_suppliers) - List suppliers

### [accounts_receivable](docs/sdks/accountsreceivable/README.md)

* [download_customer_attachment](docs/sdks/accountsreceivable/README.md#download_customer_attachment) - Download customer attachment
* [download_direct_income_attachment](docs/sdks/accountsreceivable/README.md#download_direct_income_attachment) - Download direct income attachment
* [download_invoice_attachment](docs/sdks/accountsreceivable/README.md#download_invoice_attachment) - Download invoice attachment
* [download_invoice_pdf](docs/sdks/accountsreceivable/README.md#download_invoice_pdf) - Get invoice as PDF
* [get_aged_debtors_report](docs/sdks/accountsreceivable/README.md#get_aged_debtors_report) - Aged debtors report
* [get_credit_note](docs/sdks/accountsreceivable/README.md#get_credit_note) - Get credit note
* [get_customer](docs/sdks/accountsreceivable/README.md#get_customer) - Get customer
* [get_customer_attachment](docs/sdks/accountsreceivable/README.md#get_customer_attachment) - Get customer attachment
* [get_direct_income](docs/sdks/accountsreceivable/README.md#get_direct_income) - Get direct income
* [get_direct_income_attachment](docs/sdks/accountsreceivable/README.md#get_direct_income_attachment) - Get direct income attachment
* [get_invoice](docs/sdks/accountsreceivable/README.md#get_invoice) - Get invoice
* [get_invoice_attachment](docs/sdks/accountsreceivable/README.md#get_invoice_attachment) - Get invoice attachment
* [get_payment](docs/sdks/accountsreceivable/README.md#get_payment) - Get payment
* [get_reconciled_invoices](docs/sdks/accountsreceivable/README.md#get_reconciled_invoices) - Get reconciled invoices
* [is_aged_debtor_report_available](docs/sdks/accountsreceivable/README.md#is_aged_debtor_report_available) - Aged debtors report available
* [list_credit_notes](docs/sdks/accountsreceivable/README.md#list_credit_notes) - List credit notes
* [list_customer_attachments](docs/sdks/accountsreceivable/README.md#list_customer_attachments) - List customer attachments
* [list_customers](docs/sdks/accountsreceivable/README.md#list_customers) - List customers
* [list_direct_income_attachments](docs/sdks/accountsreceivable/README.md#list_direct_income_attachments) - List direct income attachments
* [list_direct_incomes](docs/sdks/accountsreceivable/README.md#list_direct_incomes) - List direct incomes
* [list_invoice_attachments](docs/sdks/accountsreceivable/README.md#list_invoice_attachments) - List invoice attachments
* [list_invoices](docs/sdks/accountsreceivable/README.md#list_invoices) - List invoices
* [list_payments](docs/sdks/accountsreceivable/README.md#list_payments) - List payments

### [bank_statements](docs/sdks/bankstatements/README.md)

* [get_bank_account](docs/sdks/bankstatements/README.md#get_bank_account) - Get account
* [get_bank_transaction](docs/sdks/bankstatements/README.md#get_bank_transaction) - Get bank transaction
* [get_bank_transaction_category](docs/sdks/bankstatements/README.md#get_bank_transaction_category) - Get transaction category
* [get_categorized_bank_statement](docs/sdks/bankstatements/README.md#get_categorized_bank_statement) - Get categorized bank statement
* [list_bank_account_balances](docs/sdks/bankstatements/README.md#list_bank_account_balances) - List account balances
* [list_bank_accounts](docs/sdks/bankstatements/README.md#list_bank_accounts) - List accounts
* [list_bank_transaction_categories](docs/sdks/bankstatements/README.md#list_bank_transaction_categories) - List transaction categories
* [list_bank_transactions](docs/sdks/bankstatements/README.md#list_bank_transactions) - List transactions

### [companies](docs/sdks/companies/README.md)

* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [list](docs/sdks/companies/README.md#list) - List companies
* [update](docs/sdks/companies/README.md#update) - Update company

### [company_info](docs/sdks/companyinfo/README.md)

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

* [get_account](docs/sdks/financialstatements/README.md#get_account) - Get account
* [get_balance_sheet](docs/sdks/financialstatements/README.md#get_balance_sheet) - Get balance sheet
* [get_cash_flow_statement](docs/sdks/financialstatements/README.md#get_cash_flow_statement) - Get cash flow statement
* [get_categorized_balance_sheet](docs/sdks/financialstatements/README.md#get_categorized_balance_sheet) - Get categorized balance sheet statement
* [get_categorized_profit_and_loss](docs/sdks/financialstatements/README.md#get_categorized_profit_and_loss) - Get categorized profit and loss statement
* [get_profit_and_loss](docs/sdks/financialstatements/README.md#get_profit_and_loss) - Get profit and loss
* [list_accounts](docs/sdks/financialstatements/README.md#list_accounts) - List accounts

### [liabilities](docs/sdks/liabilities/README.md)

* [get_loan_summary](docs/sdks/liabilities/README.md#get_loan_summary) - Get loan summaries
* [list_loan_transactions](docs/sdks/liabilities/README.md#list_loan_transactions) - List loan transactions

### [manage_data](docs/sdks/managedata/README.md)

* [get](docs/sdks/managedata/README.md#get) - Get data status
* [get_pull_operation](docs/sdks/managedata/README.md#get_pull_operation) - Get pull operation
* [list_pull_operations](docs/sdks/managedata/README.md#list_pull_operations) - List pull operations
* [refresh_all_data_types](docs/sdks/managedata/README.md#refresh_all_data_types) - Refresh all data
* [refresh_data_type](docs/sdks/managedata/README.md#refresh_data_type) - Refresh data type

### [sales](docs/sdks/sales/README.md)

* [get_customer](docs/sdks/sales/README.md#get_customer) - Get customer
* [get_customer_retention_metrics](docs/sdks/sales/README.md#get_customer_retention_metrics) - Get customer retention metrics
* [get_dispute](docs/sdks/sales/README.md#get_dispute) - Get dispute
* [get_lifetime_value_metrics](docs/sdks/sales/README.md#get_lifetime_value_metrics) - Get lifetime value metrics
* [get_location](docs/sdks/sales/README.md#get_location) - Get location
* [get_order](docs/sdks/sales/README.md#get_order) - Get order
* [get_orders_report](docs/sdks/sales/README.md#get_orders_report) - Get orders report
* [get_payment](docs/sdks/sales/README.md#get_payment) - Get payment
* [get_payment_method](docs/sdks/sales/README.md#get_payment_method) - Get payment method
* [get_product](docs/sdks/sales/README.md#get_product) - Get product
* [get_product_category](docs/sdks/sales/README.md#get_product_category) - Get product category
* [get_refunds_report](docs/sdks/sales/README.md#get_refunds_report) - Get refunds report
* [get_revenue_metrics](docs/sdks/sales/README.md#get_revenue_metrics) - Get commerce revenue metrics
* [get_transaction](docs/sdks/sales/README.md#get_transaction) - Get transaction
* [list_customers](docs/sdks/sales/README.md#list_customers) - List customers
* [list_disputes](docs/sdks/sales/README.md#list_disputes) - List disputes
* [list_locations](docs/sdks/sales/README.md#list_locations) - List locations
* [list_orders](docs/sdks/sales/README.md#list_orders) - List orders
* [list_payment_methods](docs/sdks/sales/README.md#list_payment_methods) - List payment methods
* [list_payments](docs/sdks/sales/README.md#list_payments) - List payments
* [list_product_categories](docs/sdks/sales/README.md#list_product_categories) - List product categories
* [list_products](docs/sdks/sales/README.md#list_products) - List products
* [list_transactions](docs/sdks/sales/README.md#list_transactions) - List transactions

### [transactions](docs/sdks/transactions/README.md)

* [download_direct_cost_attachment](docs/sdks/transactions/README.md#download_direct_cost_attachment) - Download direct cost attachment
* [get_account_transaction](docs/sdks/transactions/README.md#get_account_transaction) - Get account transaction
* [get_direct_cost](docs/sdks/transactions/README.md#get_direct_cost) - Get direct cost
* [get_direct_cost_attachment](docs/sdks/transactions/README.md#get_direct_cost_attachment) - Get direct cost attachment
* [get_journal](docs/sdks/transactions/README.md#get_journal) - Get journal
* [get_journal_entry](docs/sdks/transactions/README.md#get_journal_entry) - Get journal entry
* [get_transfer](docs/sdks/transactions/README.md#get_transfer) - Get transfer
* [list_account_transactions](docs/sdks/transactions/README.md#list_account_transactions) - List account transactions
* [list_direct_cost_attachments](docs/sdks/transactions/README.md#list_direct_cost_attachments) - List direct cost attachments
* [list_direct_costs](docs/sdks/transactions/README.md#list_direct_costs) - List direct costs
* [list_journal_entries](docs/sdks/transactions/README.md#list_journal_entries) - List journal entries
* [list_journals](docs/sdks/transactions/README.md#list_journals) - List journals
* [list_transfers](docs/sdks/transactions/README.md#list_transfers) - List transfers## Available Resources and Operations


### [accounting_bank_data](docs/sdks/accountingbankdata/README.md)

* [list_transactions](docs/sdks/accountingbankdata/README.md#list_transactions) - List bank account transactions

### [accounts_payable](docs/sdks/accountspayable/README.md)

* [download_bill_attachment](docs/sdks/accountspayable/README.md#download_bill_attachment) - Download bill attachment
* [get_bill_attachment](docs/sdks/accountspayable/README.md#get_bill_attachment) - Get bill attachment

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

### [liabilities](docs/sdks/liabilities/README.md)

* [get_loan_summary](docs/sdks/liabilities/README.md#get_loan_summary) - Get loan summaries
* [list_loan_transactions](docs/sdks/liabilities/README.md#list_loan_transactions) - List loan transactions


### [accounting_bank_data_accounts](docs/sdks/accountingbankdataaccounts/README.md)

* [get](docs/sdks/accountingbankdataaccounts/README.md#get) - Get bank account
* [list](docs/sdks/accountingbankdataaccounts/README.md#list) - List bank accounts


### [accounts_payable_bill_credit_notes](docs/sdks/accountspayablebillcreditnotes/README.md)

* [get](docs/sdks/accountspayablebillcreditnotes/README.md#get) - Get bill credit note
* [list](docs/sdks/accountspayablebillcreditnotes/README.md#list) - List bill credit notes

### [accounts_payable_bill_payments](docs/sdks/accountspayablebillpayments/README.md)

* [get](docs/sdks/accountspayablebillpayments/README.md#get) - Get bill payment
* [list](docs/sdks/accountspayablebillpayments/README.md#list) - List bill payments

### [accounts_payable_bills](docs/sdks/accountspayablebills/README.md)

* [get](docs/sdks/accountspayablebills/README.md#get) - Get bill
* [list](docs/sdks/accountspayablebills/README.md#list) - List bills
* [list_attachments](docs/sdks/accountspayablebills/README.md#list_attachments) - List bill attachments

### [accounts_payable_suppliers](docs/sdks/accountspayablesuppliers/README.md)

* [download_attachment](docs/sdks/accountspayablesuppliers/README.md#download_attachment) - Download supplier attachment
* [get](docs/sdks/accountspayablesuppliers/README.md#get) - Get supplier
* [get_attachment](docs/sdks/accountspayablesuppliers/README.md#get_attachment) - Get supplier attachment
* [list](docs/sdks/accountspayablesuppliers/README.md#list) - List suppliers
* [list_attachments](docs/sdks/accountspayablesuppliers/README.md#list_attachments) - List supplier attachments


### [accounts_receivable_credit_notes](docs/sdks/accountsreceivablecreditnotes/README.md)

* [get](docs/sdks/accountsreceivablecreditnotes/README.md#get) - Get credit note
* [list](docs/sdks/accountsreceivablecreditnotes/README.md#list) - List credit notes

### [accounts_receivable_customers](docs/sdks/accountsreceivablecustomers/README.md)

* [download_attachment](docs/sdks/accountsreceivablecustomers/README.md#download_attachment) - Download customer attachment
* [get](docs/sdks/accountsreceivablecustomers/README.md#get) - Get customer
* [get_attachment](docs/sdks/accountsreceivablecustomers/README.md#get_attachment) - Get customer attachment
* [list](docs/sdks/accountsreceivablecustomers/README.md#list) - List customers
* [list_attachments](docs/sdks/accountsreceivablecustomers/README.md#list_attachments) - List customer attachments

### [accounts_receivable_direct_incomes](docs/sdks/accountsreceivabledirectincomes/README.md)

* [download_attachment](docs/sdks/accountsreceivabledirectincomes/README.md#download_attachment) - Download direct income attachment
* [get](docs/sdks/accountsreceivabledirectincomes/README.md#get) - Get direct income
* [get_attachment](docs/sdks/accountsreceivabledirectincomes/README.md#get_attachment) - Get direct income attachment
* [list](docs/sdks/accountsreceivabledirectincomes/README.md#list) - List direct incomes
* [list_attachments](docs/sdks/accountsreceivabledirectincomes/README.md#list_attachments) - List direct income attachments

### [accounts_receivable_invoices](docs/sdks/accountsreceivableinvoices/README.md)

* [download_attachment](docs/sdks/accountsreceivableinvoices/README.md#download_attachment) - Download invoice attachment
* [download_pdf](docs/sdks/accountsreceivableinvoices/README.md#download_pdf) - Get invoice as PDF
* [get](docs/sdks/accountsreceivableinvoices/README.md#get) - Get invoice
* [get_attachment](docs/sdks/accountsreceivableinvoices/README.md#get_attachment) - Get invoice attachment
* [list](docs/sdks/accountsreceivableinvoices/README.md#list) - List invoices
* [list_attachments](docs/sdks/accountsreceivableinvoices/README.md#list_attachments) - List invoice attachments
* [list_reconciled](docs/sdks/accountsreceivableinvoices/README.md#list_reconciled) - List reconciled invoices

### [accounts_receivable_payments](docs/sdks/accountsreceivablepayments/README.md)

* [get](docs/sdks/accountsreceivablepayments/README.md#get) - Get payment
* [list](docs/sdks/accountsreceivablepayments/README.md#list) - List payments

### [accounts_receivable_reports](docs/sdks/accountsreceivablereports/README.md)

* [get_aged_creditors](docs/sdks/accountsreceivablereports/README.md#get_aged_creditors) - Aged creditors report
* [get_aged_debtors](docs/sdks/accountsreceivablereports/README.md#get_aged_debtors) - Aged debtors report
* [is_aged_creditors_available](docs/sdks/accountsreceivablereports/README.md#is_aged_creditors_available) - Aged creditors report available
* [is_aged_debtors_available](docs/sdks/accountsreceivablereports/README.md#is_aged_debtors_available) - Aged debtors report available


### [banking_account_balances](docs/sdks/bankingaccountbalances/README.md)

* [list](docs/sdks/bankingaccountbalances/README.md#list) - List account balances

### [Banking.Accounts](docs/sdks/bankingaccounts/README.md)

* [get](docs/sdks/bankingaccounts/README.md#get) - Get account
* [list](docs/sdks/bankingaccounts/README.md#list) - List accounts

### [banking_categorized_statement](docs/sdks/bankingcategorizedstatement/README.md)

* [get](docs/sdks/bankingcategorizedstatement/README.md#get) - Get categorized bank statement

### [banking_transaction_categories](docs/sdks/bankingtransactioncategories/README.md)

* [get](docs/sdks/bankingtransactioncategories/README.md#get) - Get transaction category
* [list](docs/sdks/bankingtransactioncategories/README.md#list) - List transaction categories

### [Banking.Transactions](docs/sdks/bankingtransactions/README.md)

* [get](docs/sdks/bankingtransactions/README.md#get) - Get bank transaction
* [list](docs/sdks/bankingtransactions/README.md#list) - List transactions


### [financial_statements_accounts](docs/sdks/financialstatementsaccounts/README.md)

* [get](docs/sdks/financialstatementsaccounts/README.md#get) - Get account
* [list](docs/sdks/financialstatementsaccounts/README.md#list) - List accounts

### [financial_statements_balance_sheet](docs/sdks/financialstatementsbalancesheet/README.md)

* [get](docs/sdks/financialstatementsbalancesheet/README.md#get) - Get balance sheet
* [get_categorized_accounts](docs/sdks/financialstatementsbalancesheet/README.md#get_categorized_accounts) - Get categorized balance sheet statement

### [financial_statements_cash_flow](docs/sdks/financialstatementscashflow/README.md)

* [get](docs/sdks/financialstatementscashflow/README.md#get) - Get cash flow statement

### [financial_statements_profit_and_loss](docs/sdks/financialstatementsprofitandloss/README.md)

* [get](docs/sdks/financialstatementsprofitandloss/README.md#get) - Get profit and loss
* [get_categorized_accounts](docs/sdks/financialstatementsprofitandloss/README.md#get_categorized_accounts) - Get categorized profit and loss statement

### [manage_data](docs/sdks/managedata/README.md)

* [get_status](docs/sdks/managedata/README.md#get_status) - Get data status

### [manage_data_pull_operations](docs/sdks/managedatapulloperations/README.md)

* [get](docs/sdks/managedatapulloperations/README.md#get) - Get pull operation
* [list](docs/sdks/managedatapulloperations/README.md#list) - List pull operations

### [manage_data_refresh](docs/sdks/managedatarefresh/README.md)

* [all_data_types](docs/sdks/managedatarefresh/README.md#all_data_types) - Refresh all data
* [data_type](docs/sdks/managedatarefresh/README.md#data_type) - Refresh data type


### [Sales.Customers](docs/sdks/salescustomers/README.md)

* [get](docs/sdks/salescustomers/README.md#get) - Get customer
* [list](docs/sdks/salescustomers/README.md#list) - List customers

### [Sales.Disputes](docs/sdks/salesdisputes/README.md)

* [get](docs/sdks/salesdisputes/README.md#get) - Get dispute
* [list](docs/sdks/salesdisputes/README.md#list) - List disputes

### [Sales.Locations](docs/sdks/saleslocations/README.md)

* [get](docs/sdks/saleslocations/README.md#get) - Get location
* [list](docs/sdks/saleslocations/README.md#list) - List locations

### [Sales.Metrics](docs/sdks/salesmetrics/README.md)

* [get_customer_retention](docs/sdks/salesmetrics/README.md#get_customer_retention) - Get customer retention metrics
* [get_lifetime_value](docs/sdks/salesmetrics/README.md#get_lifetime_value) - Get lifetime value metrics
* [get_revenue](docs/sdks/salesmetrics/README.md#get_revenue) - Get commerce revenue metrics

### [Sales.Orders](docs/sdks/salesorders/README.md)

* [get](docs/sdks/salesorders/README.md#get) - Get order
* [list](docs/sdks/salesorders/README.md#list) - List orders

### [sales_payment_methods](docs/sdks/salespaymentmethods/README.md)

* [get](docs/sdks/salespaymentmethods/README.md#get) - Get payment method
* [list](docs/sdks/salespaymentmethods/README.md#list) - List payment methods

### [Sales.Payments](docs/sdks/salespayments/README.md)

* [get](docs/sdks/salespayments/README.md#get) - Get payment
* [list](docs/sdks/salespayments/README.md#list) - List payments

### [sales_product_categories](docs/sdks/salesproductcategories/README.md)

* [get](docs/sdks/salesproductcategories/README.md#get) - Get product category
* [list](docs/sdks/salesproductcategories/README.md#list) - List product categories

### [Sales.Products](docs/sdks/salesproducts/README.md)

* [get](docs/sdks/salesproducts/README.md#get) - Get product
* [list](docs/sdks/salesproducts/README.md#list) - List products

### [Sales.Reports](docs/sdks/salesreports/README.md)

* [get_orders](docs/sdks/salesreports/README.md#get_orders) - Get orders report
* [get_refunds](docs/sdks/salesreports/README.md#get_refunds) - Get refunds report

### [Sales.Transactions](docs/sdks/salestransactions/README.md)

* [get](docs/sdks/salestransactions/README.md#get) - Get transaction
* [list](docs/sdks/salestransactions/README.md#list) - List transactions


### [transactions_account_transactions](docs/sdks/transactionsaccounttransactions/README.md)

* [get](docs/sdks/transactionsaccounttransactions/README.md#get) - Get account transaction
* [list](docs/sdks/transactionsaccounttransactions/README.md#list) - List account transactions

### [transactions_direct_costs](docs/sdks/transactionsdirectcosts/README.md)

* [download_attachment](docs/sdks/transactionsdirectcosts/README.md#download_attachment) - Download direct cost attachment
* [get](docs/sdks/transactionsdirectcosts/README.md#get) - Get direct cost
* [get_attachment](docs/sdks/transactionsdirectcosts/README.md#get_attachment) - Get direct cost attachment
* [list](docs/sdks/transactionsdirectcosts/README.md#list) - List direct costs
* [list_attachments](docs/sdks/transactionsdirectcosts/README.md#list_attachments) - List direct cost attachments

### [transactions_journal_entries](docs/sdks/transactionsjournalentries/README.md)

* [get](docs/sdks/transactionsjournalentries/README.md#get) - Get journal entry
* [list](docs/sdks/transactionsjournalentries/README.md#list) - List journal entries

### [Transactions.Journals](docs/sdks/transactionsjournals/README.md)

* [get](docs/sdks/transactionsjournals/README.md#get) - Get journal
* [list](docs/sdks/transactionsjournals/README.md#list) - List journals

### [Transactions.Transfers](docs/sdks/transactionstransfers/README.md)

* [get](docs/sdks/transactionstransfers/README.md#get) - Get transfer
* [list](docs/sdks/transactionstransfers/README.md#list) - List transfers<!-- Start SDK Available Operations -->

<!-- End SDK Available Operations -->
### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
