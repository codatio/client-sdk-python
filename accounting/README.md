# Accounting API

Codat's Accounting API is a flexible API for pulling and pushing up-to-date accounting data to your customer's accounting software.
It gives you a simple way to view, create, update adn delete data without having to worry about each platform's specific complexities.

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install codat-accounting
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAccountTransactionRequest(
    account_transaction_id="corrupti",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.account_transactions.get(req)

if res.account_transaction is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [account_transactions](docs/accounttransactions/README.md)

* [get](docs/accounttransactions/README.md#get) - Get account transaction
* [list](docs/accounttransactions/README.md#list) - List account transactions

### [accounts](docs/accounts/README.md)

* [create](docs/accounts/README.md#create) - Create account
* [get](docs/accounts/README.md#get) - Get account
* [get_create_model](docs/accounts/README.md#get_create_model) - Get create account model
* [list](docs/accounts/README.md#list) - List accounts

### [bank_account_transactions](docs/bankaccounttransactions/README.md)

* [create](docs/bankaccounttransactions/README.md#create) - Create bank transactions
* [get_create_model](docs/bankaccounttransactions/README.md#get_create_model) - List push options for bank account bank transactions
* [list](docs/bankaccounttransactions/README.md#list) - List bank transactions for bank account
* [list_transactions](docs/bankaccounttransactions/README.md#list_transactions) - List all bank transactions

### [bank_accounts](docs/bankaccounts/README.md)

* [create](docs/bankaccounts/README.md#create) - Create bank account
* [get](docs/bankaccounts/README.md#get) - Get bank account
* [get_create_update_model](docs/bankaccounts/README.md#get_create_update_model) - Get create/update bank account model
* [list](docs/bankaccounts/README.md#list) - List bank accounts
* [update](docs/bankaccounts/README.md#update) - Update bank account

### [bill_credit_notes](docs/billcreditnotes/README.md)

* [create](docs/billcreditnotes/README.md#create) - Create bill credit note
* [get](docs/billcreditnotes/README.md#get) - Get bill credit note
* [get_create_update_model](docs/billcreditnotes/README.md#get_create_update_model) - Get create/update bill credit note model
* [list](docs/billcreditnotes/README.md#list) - List bill credit notes
* [update](docs/billcreditnotes/README.md#update) - Update bill credit note

### [bill_payments](docs/billpayments/README.md)

* [create](docs/billpayments/README.md#create) - Create bill payments
* [delete](docs/billpayments/README.md#delete) - Delete bill payment
* [get](docs/billpayments/README.md#get) - Get bill payment
* [get_create_model](docs/billpayments/README.md#get_create_model) - Get create bill payment model
* [list](docs/billpayments/README.md#list) - List bill payments

### [bills](docs/bills/README.md)

* [create](docs/bills/README.md#create) - Create bill
* [delete](docs/bills/README.md#delete) - Delete bill
* [download_attachment](docs/bills/README.md#download_attachment) - Download bill attachment
* [get](docs/bills/README.md#get) - Get bill
* [get_attachment](docs/bills/README.md#get_attachment) - Get bill attachment
* [get_create_update_model](docs/bills/README.md#get_create_update_model) - Get create/update bill model
* [list](docs/bills/README.md#list) - List bills
* [list_attachments](docs/bills/README.md#list_attachments) - List bill attachments
* [update](docs/bills/README.md#update) - Update bill
* [upload_attachment](docs/bills/README.md#upload_attachment) - Upload bill attachment

### [company_info](docs/companyinfo/README.md)

* [get](docs/companyinfo/README.md#get) - Get company info
* [refresh](docs/companyinfo/README.md#refresh) - Refresh company info

### [credit_notes](docs/creditnotes/README.md)

* [create](docs/creditnotes/README.md#create) - Create credit note
* [get](docs/creditnotes/README.md#get) - Get credit note
* [get_create_update_model](docs/creditnotes/README.md#get_create_update_model) - Get create/update credit note model
* [list](docs/creditnotes/README.md#list) - List credit notes
* [update](docs/creditnotes/README.md#update) - Update creditNote

### [customers](docs/customers/README.md)

* [create](docs/customers/README.md#create) - Create customer
* [download_attachment](docs/customers/README.md#download_attachment) - Download customer attachment
* [get](docs/customers/README.md#get) - Get customer
* [get_attachment](docs/customers/README.md#get_attachment) - Get customer attachment
* [get_create_update_model](docs/customers/README.md#get_create_update_model) - Get create/update customer model
* [list](docs/customers/README.md#list) - List customers
* [list_attachments](docs/customers/README.md#list_attachments) - List customer attachments
* [update](docs/customers/README.md#update) - Update customer

### [direct_costs](docs/directcosts/README.md)

* [create](docs/directcosts/README.md#create) - Create direct cost
* [download_attachment](docs/directcosts/README.md#download_attachment) - Download direct cost attachment
* [get](docs/directcosts/README.md#get) - Get direct cost
* [get_attachment](docs/directcosts/README.md#get_attachment) - Get direct cost attachment
* [get_create_model](docs/directcosts/README.md#get_create_model) - Get create direct cost model
* [list](docs/directcosts/README.md#list) - List direct costs
* [list_attachments](docs/directcosts/README.md#list_attachments) - List direct cost attachments
* [upload_attachment](docs/directcosts/README.md#upload_attachment) - Upload direct cost attachment

### [direct_incomes](docs/directincomes/README.md)

* [create](docs/directincomes/README.md#create) - Create direct income
* [download_attachment](docs/directincomes/README.md#download_attachment) - Download direct income attachment
* [get](docs/directincomes/README.md#get) - Get direct income
* [get_attachment](docs/directincomes/README.md#get_attachment) - Get direct income attachment
* [get_create_model](docs/directincomes/README.md#get_create_model) - Get create direct income model
* [list](docs/directincomes/README.md#list) - List direct incomes
* [list_attachments](docs/directincomes/README.md#list_attachments) - List direct income attachments
* [upload_attachment](docs/directincomes/README.md#upload_attachment) - Create direct income attachment

### [financials](docs/financials/README.md)

* [get_balance_sheet](docs/financials/README.md#get_balance_sheet) - Get balance sheet
* [get_cash_flow_statement](docs/financials/README.md#get_cash_flow_statement) - Get cash flow statement
* [get_profit_and_loss](docs/financials/README.md#get_profit_and_loss) - Get profit and loss

### [invoices](docs/invoices/README.md)

* [create](docs/invoices/README.md#create) - Create invoice
* [delete](docs/invoices/README.md#delete) - Delete invoice
* [download_attachment](docs/invoices/README.md#download_attachment) - Download invoice attachment
* [download_pdf](docs/invoices/README.md#download_pdf) - Get invoice as PDF
* [get](docs/invoices/README.md#get) - Get invoice
* [get_attachment](docs/invoices/README.md#get_attachment) - Get invoice attachment
* [get_create_update_model](docs/invoices/README.md#get_create_update_model) - Get create/update invoice model
* [list](docs/invoices/README.md#list) - List invoices
* [list_attachments](docs/invoices/README.md#list_attachments) - List invoice attachments
* [update](docs/invoices/README.md#update) - Update invoice
* [upload_attachment](docs/invoices/README.md#upload_attachment) - Push invoice attachment

### [items](docs/items/README.md)

* [create](docs/items/README.md#create) - Create item
* [get](docs/items/README.md#get) - Get item
* [get_create_model](docs/items/README.md#get_create_model) - Get create item model
* [list](docs/items/README.md#list) - List items

### [journal_entries](docs/journalentries/README.md)

* [create](docs/journalentries/README.md#create) - Create journal entry
* [delete](docs/journalentries/README.md#delete) - Delete journal entry
* [get](docs/journalentries/README.md#get) - Get journal entry
* [get_create_model](docs/journalentries/README.md#get_create_model) - Get create journal entry model
* [list](docs/journalentries/README.md#list) - List journal entries

### [journals](docs/journals/README.md)

* [create](docs/journals/README.md#create) - Create journal
* [get](docs/journals/README.md#get) - Get journal
* [get_create_model](docs/journals/README.md#get_create_model) - Get create journal model
* [list](docs/journals/README.md#list) - List journals

### [payment_methods](docs/paymentmethods/README.md)

* [get](docs/paymentmethods/README.md#get) - Get payment method
* [list](docs/paymentmethods/README.md#list) - List all payment methods

### [payments](docs/payments/README.md)

* [create](docs/payments/README.md#create) - Create payment
* [get](docs/payments/README.md#get) - Get payment
* [get_create_model](docs/payments/README.md#get_create_model) - Get create payment model
* [list](docs/payments/README.md#list) - List payments

### [purchase_orders](docs/purchaseorders/README.md)

* [create](docs/purchaseorders/README.md#create) - Create purchase order
* [get](docs/purchaseorders/README.md#get) - Get purchase order
* [get_create_update_model](docs/purchaseorders/README.md#get_create_update_model) - Get create/update purchase order model
* [list](docs/purchaseorders/README.md#list) - List purchase orders
* [update](docs/purchaseorders/README.md#update) - Update purchase order

### [reports](docs/reports/README.md)

* [get_aged_creditors_report](docs/reports/README.md#get_aged_creditors_report) - Aged creditors report
* [get_aged_debtors_report](docs/reports/README.md#get_aged_debtors_report) - Aged debtors report
* [is_aged_creditors_report_available](docs/reports/README.md#is_aged_creditors_report_available) - Aged creditors report available
* [is_aged_debtor_report_available](docs/reports/README.md#is_aged_debtor_report_available) - Aged debtors report available

### [sales_orders](docs/salesorders/README.md)

* [get](docs/salesorders/README.md#get) - Get sales order
* [list](docs/salesorders/README.md#list) - List sales orders

### [suppliers](docs/suppliers/README.md)

* [create](docs/suppliers/README.md#create) - Create supplier
* [download_attachment](docs/suppliers/README.md#download_attachment) - Download supplier attachment
* [get](docs/suppliers/README.md#get) - Get supplier
* [get_attachment](docs/suppliers/README.md#get_attachment) - Get supplier attachment
* [get_create_update_model](docs/suppliers/README.md#get_create_update_model) - Get create/update supplier model
* [list](docs/suppliers/README.md#list) - List suppliers
* [list_attachments](docs/suppliers/README.md#list_attachments) - List supplier attachments
* [update](docs/suppliers/README.md#update) - Update supplier

### [tax_rates](docs/taxrates/README.md)

* [get](docs/taxrates/README.md#get) - Get tax rate
* [list](docs/taxrates/README.md#list) - List all tax rates

### [tracking_categories](docs/trackingcategories/README.md)

* [get](docs/trackingcategories/README.md#get) - Get tracking categories
* [list](docs/trackingcategories/README.md#list) - List tracking categories

### [transfers](docs/transfers/README.md)

* [create](docs/transfers/README.md#create) - Create transfer
* [get](docs/transfers/README.md#get) - Get transfer
* [get_create_model](docs/transfers/README.md#get_create_model) - Get create transfer model
* [list](docs/transfers/README.md#list) - List transfers
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
