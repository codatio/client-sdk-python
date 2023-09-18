# Lending
    
Lending helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from the operating systems they are already using. You can use that data for automating decisioning and surfacing new insights on the customer, all via one API.

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install codat-lending
```
<!-- End SDK Installation -->

## Example Usage
<!-- Start SDK Example Usage -->


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
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [AccountingBankData](docs/sdks/accountingbankdata/README.md)

* [list_transactions](docs/sdks/accountingbankdata/README.md#list_transactions) - List bank account transactions

### [AccountingBankData.Accounts](docs/sdks/accountingbankdataaccounts/README.md)

* [get](docs/sdks/accountingbankdataaccounts/README.md#get) - Get bank account
* [list](docs/sdks/accountingbankdataaccounts/README.md#list) - List bank accounts

### [Companies](docs/sdks/companies/README.md)

* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [list](docs/sdks/companies/README.md#list) - List companies
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

### [Liabilities](docs/sdks/liabilities/README.md)

* [get_loan_summary](docs/sdks/liabilities/README.md#get_loan_summary) - Get loan summaries
* [list_loan_transactions](docs/sdks/liabilities/README.md#list_loan_transactions) - List loan transactions


### [AccountsPayable.BillCreditNotes](docs/sdks/accountspayablebillcreditnotes/README.md)

* [get](docs/sdks/accountspayablebillcreditnotes/README.md#get) - Get bill credit note
* [list](docs/sdks/accountspayablebillcreditnotes/README.md#list) - List bill credit notes

### [AccountsPayable.BillPayments](docs/sdks/accountspayablebillpayments/README.md)

* [get](docs/sdks/accountspayablebillpayments/README.md#get) - Get bill payment
* [list](docs/sdks/accountspayablebillpayments/README.md#list) - List bill payments

### [AccountsPayable.Bills](docs/sdks/accountspayablebills/README.md)

* [download_attachment](docs/sdks/accountspayablebills/README.md#download_attachment) - Download bill attachment
* [get](docs/sdks/accountspayablebills/README.md#get) - Get bill
* [get_attachment](docs/sdks/accountspayablebills/README.md#get_attachment) - Get bill attachment
* [list](docs/sdks/accountspayablebills/README.md#list) - List bills
* [list_attachments](docs/sdks/accountspayablebills/README.md#list_attachments) - List bill attachments

### [AccountsPayable.Suppliers](docs/sdks/accountspayablesuppliers/README.md)

* [download_attachment](docs/sdks/accountspayablesuppliers/README.md#download_attachment) - Download supplier attachment
* [get](docs/sdks/accountspayablesuppliers/README.md#get) - Get supplier
* [get_attachment](docs/sdks/accountspayablesuppliers/README.md#get_attachment) - Get supplier attachment
* [list](docs/sdks/accountspayablesuppliers/README.md#list) - List suppliers
* [list_attachments](docs/sdks/accountspayablesuppliers/README.md#list_attachments) - List supplier attachments


### [AccountsReceivable.CreditNotes](docs/sdks/accountsreceivablecreditnotes/README.md)

* [get](docs/sdks/accountsreceivablecreditnotes/README.md#get) - Get credit note
* [list](docs/sdks/accountsreceivablecreditnotes/README.md#list) - List credit notes

### [AccountsReceivable.Customers](docs/sdks/accountsreceivablecustomers/README.md)

* [download_attachment](docs/sdks/accountsreceivablecustomers/README.md#download_attachment) - Download customer attachment
* [get](docs/sdks/accountsreceivablecustomers/README.md#get) - Get customer
* [get_attachment](docs/sdks/accountsreceivablecustomers/README.md#get_attachment) - Get customer attachment
* [list](docs/sdks/accountsreceivablecustomers/README.md#list) - List customers
* [list_attachments](docs/sdks/accountsreceivablecustomers/README.md#list_attachments) - List customer attachments

### [AccountsReceivable.DirectIncomes](docs/sdks/accountsreceivabledirectincomes/README.md)

* [download_attachment](docs/sdks/accountsreceivabledirectincomes/README.md#download_attachment) - Download direct income attachment
* [get](docs/sdks/accountsreceivabledirectincomes/README.md#get) - Get direct income
* [get_attachment](docs/sdks/accountsreceivabledirectincomes/README.md#get_attachment) - Get direct income attachment
* [list](docs/sdks/accountsreceivabledirectincomes/README.md#list) - List direct incomes
* [list_attachments](docs/sdks/accountsreceivabledirectincomes/README.md#list_attachments) - List direct income attachments

### [AccountsReceivable.Invoices](docs/sdks/accountsreceivableinvoices/README.md)

* [download_attachment](docs/sdks/accountsreceivableinvoices/README.md#download_attachment) - Download invoice attachment
* [download_pdf](docs/sdks/accountsreceivableinvoices/README.md#download_pdf) - Get invoice as PDF
* [get](docs/sdks/accountsreceivableinvoices/README.md#get) - Get invoice
* [get_attachment](docs/sdks/accountsreceivableinvoices/README.md#get_attachment) - Get invoice attachment
* [list](docs/sdks/accountsreceivableinvoices/README.md#list) - List invoices
* [list_attachments](docs/sdks/accountsreceivableinvoices/README.md#list_attachments) - List invoice attachments
* [list_reconciled](docs/sdks/accountsreceivableinvoices/README.md#list_reconciled) - List reconciled invoices

### [AccountsReceivable.Payments](docs/sdks/accountsreceivablepayments/README.md)

* [get](docs/sdks/accountsreceivablepayments/README.md#get) - Get payment
* [list](docs/sdks/accountsreceivablepayments/README.md#list) - List payments

### [AccountsReceivable.Reports](docs/sdks/accountsreceivablereports/README.md)

* [get_aged_creditors](docs/sdks/accountsreceivablereports/README.md#get_aged_creditors) - Aged creditors report
* [get_aged_debtors](docs/sdks/accountsreceivablereports/README.md#get_aged_debtors) - Aged debtors report
* [is_aged_creditors_available](docs/sdks/accountsreceivablereports/README.md#is_aged_creditors_available) - Aged creditors report available
* [is_aged_debtors_available](docs/sdks/accountsreceivablereports/README.md#is_aged_debtors_available) - Aged debtors report available


### [Banking.AccountBalances](docs/sdks/bankingaccountbalances/README.md)

* [list](docs/sdks/bankingaccountbalances/README.md#list) - List account balances

### [Banking.Accounts](docs/sdks/bankingaccounts/README.md)

* [get](docs/sdks/bankingaccounts/README.md#get) - Get account
* [list](docs/sdks/bankingaccounts/README.md#list) - List accounts

### [Banking.CategorizedStatement](docs/sdks/bankingcategorizedstatement/README.md)

* [get](docs/sdks/bankingcategorizedstatement/README.md#get) - Get categorized bank statement

### [Banking.TransactionCategories](docs/sdks/bankingtransactioncategories/README.md)

* [get](docs/sdks/bankingtransactioncategories/README.md#get) - Get transaction category
* [list](docs/sdks/bankingtransactioncategories/README.md#list) - List transaction categories

### [Banking.Transactions](docs/sdks/bankingtransactions/README.md)

* [get](docs/sdks/bankingtransactions/README.md#get) - Get bank transaction
* [list](docs/sdks/bankingtransactions/README.md#list) - List transactions


### [FinancialStatements.Accounts](docs/sdks/financialstatementsaccounts/README.md)

* [get](docs/sdks/financialstatementsaccounts/README.md#get) - Get account
* [list](docs/sdks/financialstatementsaccounts/README.md#list) - List accounts

### [FinancialStatements.BalanceSheet](docs/sdks/financialstatementsbalancesheet/README.md)

* [get](docs/sdks/financialstatementsbalancesheet/README.md#get) - Get balance sheet
* [get_categorized_accounts](docs/sdks/financialstatementsbalancesheet/README.md#get_categorized_accounts) - Get categorized balance sheet statement

### [FinancialStatements.CashFlow](docs/sdks/financialstatementscashflow/README.md)

* [get](docs/sdks/financialstatementscashflow/README.md#get) - Get cash flow statement

### [FinancialStatements.ProfitAndLoss](docs/sdks/financialstatementsprofitandloss/README.md)

* [get](docs/sdks/financialstatementsprofitandloss/README.md#get) - Get profit and loss
* [get_categorized_accounts](docs/sdks/financialstatementsprofitandloss/README.md#get_categorized_accounts) - Get categorized profit and loss statement

### [ManageData](docs/sdks/managedata/README.md)

* [get_status](docs/sdks/managedata/README.md#get_status) - Get data status

### [ManageData.PullOperations](docs/sdks/managedatapulloperations/README.md)

* [get](docs/sdks/managedatapulloperations/README.md#get) - Get pull operation
* [list](docs/sdks/managedatapulloperations/README.md#list) - List pull operations

### [ManageData.Refresh](docs/sdks/managedatarefresh/README.md)

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

### [Sales.PaymentMethods](docs/sdks/salespaymentmethods/README.md)

* [get](docs/sdks/salespaymentmethods/README.md#get) - Get payment method
* [list](docs/sdks/salespaymentmethods/README.md#list) - List payment methods

### [Sales.Payments](docs/sdks/salespayments/README.md)

* [get](docs/sdks/salespayments/README.md#get) - Get payment
* [list](docs/sdks/salespayments/README.md#list) - List payments

### [Sales.ProductCategories](docs/sdks/salesproductcategories/README.md)

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


### [Transactions.AccountTransactions](docs/sdks/transactionsaccounttransactions/README.md)

* [get](docs/sdks/transactionsaccounttransactions/README.md#get) - Get account transaction
* [list](docs/sdks/transactionsaccounttransactions/README.md#list) - List account transactions

### [Transactions.DirectCosts](docs/sdks/transactionsdirectcosts/README.md)

* [download_attachment](docs/sdks/transactionsdirectcosts/README.md#download_attachment) - Download direct cost attachment
* [get](docs/sdks/transactionsdirectcosts/README.md#get) - Get direct cost
* [get_attachment](docs/sdks/transactionsdirectcosts/README.md#get_attachment) - Get direct cost attachment
* [list](docs/sdks/transactionsdirectcosts/README.md#list) - List direct costs
* [list_attachments](docs/sdks/transactionsdirectcosts/README.md#list_attachments) - List direct cost attachments

### [Transactions.JournalEntries](docs/sdks/transactionsjournalentries/README.md)

* [get](docs/sdks/transactionsjournalentries/README.md#get) - Get journal entry
* [list](docs/sdks/transactionsjournalentries/README.md#list) - List journal entries

### [Transactions.Journals](docs/sdks/transactionsjournals/README.md)

* [get](docs/sdks/transactionsjournals/README.md#get) - Get journal
* [list](docs/sdks/transactionsjournals/README.md#list) - List journals

### [Transactions.Transfers](docs/sdks/transactionstransfers/README.md)

* [get](docs/sdks/transactionstransfers/README.md#get) - Get transfer
* [list](docs/sdks/transactionstransfers/README.md#list) - List transfers
<!-- End SDK Available Operations -->
### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
