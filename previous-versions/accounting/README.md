# Accounting

<!-- Start Codat Library Description -->
﻿Codat's Accounting API is a flexible API for pulling and pushing up-to-date accounting data to your customer's accounting software.
It gives you a simple way to view, create, update adn delete data without having to worry about each platform's specific complexities.

<!-- End Codat Library Description -->


<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install codat-accounting
```
<!-- End SDK Installation -->

## Example Usage
<!-- Start SDK Example Usage -->
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountTransactionRequest(
    account_transaction_id='Northeast Hatchback Kia',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.account_transactions.get(req)

if res.account_transaction is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [account_transactions](docs/sdks/accounttransactions/README.md)

* [get](docs/sdks/accounttransactions/README.md#get) - Get account transaction
* [list](docs/sdks/accounttransactions/README.md#list) - List account transactions

### [accounts](docs/sdks/accounts/README.md)

* [create](docs/sdks/accounts/README.md#create) - Create account
* [get](docs/sdks/accounts/README.md#get) - Get account
* [get_create_model](docs/sdks/accounts/README.md#get_create_model) - Get create account model
* [list](docs/sdks/accounts/README.md#list) - List accounts

### [bank_account_transactions](docs/sdks/bankaccounttransactions/README.md)

* [create](docs/sdks/bankaccounttransactions/README.md#create) - Create bank account transactions
* [get_create_model](docs/sdks/bankaccounttransactions/README.md#get_create_model) - Get create bank account transactions model
* [list](docs/sdks/bankaccounttransactions/README.md#list) - List bank account transactions

### [bank_accounts](docs/sdks/bankaccounts/README.md)

* [create](docs/sdks/bankaccounts/README.md#create) - Create bank account
* [get](docs/sdks/bankaccounts/README.md#get) - Get bank account
* [get_create_update_model](docs/sdks/bankaccounts/README.md#get_create_update_model) - Get create/update bank account model
* [list](docs/sdks/bankaccounts/README.md#list) - List bank accounts
* [update](docs/sdks/bankaccounts/README.md#update) - Update bank account

### [bill_credit_notes](docs/sdks/billcreditnotes/README.md)

* [create](docs/sdks/billcreditnotes/README.md#create) - Create bill credit note
* [get](docs/sdks/billcreditnotes/README.md#get) - Get bill credit note
* [get_create_update_model](docs/sdks/billcreditnotes/README.md#get_create_update_model) - Get create/update bill credit note model
* [list](docs/sdks/billcreditnotes/README.md#list) - List bill credit notes
* [update](docs/sdks/billcreditnotes/README.md#update) - Update bill credit note
* [upload_attachment](docs/sdks/billcreditnotes/README.md#upload_attachment) - Upload bill credit note attachment

### [bill_payments](docs/sdks/billpayments/README.md)

* [create](docs/sdks/billpayments/README.md#create) - Create bill payments
* [delete](docs/sdks/billpayments/README.md#delete) - Delete bill payment
* [get](docs/sdks/billpayments/README.md#get) - Get bill payment
* [get_create_model](docs/sdks/billpayments/README.md#get_create_model) - Get create bill payment model
* [list](docs/sdks/billpayments/README.md#list) - List bill payments

### [bills](docs/sdks/bills/README.md)

* [create](docs/sdks/bills/README.md#create) - Create bill
* [delete](docs/sdks/bills/README.md#delete) - Delete bill
* [download_attachment](docs/sdks/bills/README.md#download_attachment) - Download bill attachment
* [get](docs/sdks/bills/README.md#get) - Get bill
* [get_attachment](docs/sdks/bills/README.md#get_attachment) - Get bill attachment
* [get_create_update_model](docs/sdks/bills/README.md#get_create_update_model) - Get create/update bill model
* [list](docs/sdks/bills/README.md#list) - List bills
* [list_attachments](docs/sdks/bills/README.md#list_attachments) - List bill attachments
* [update](docs/sdks/bills/README.md#update) - Update bill
* [upload_attachment](docs/sdks/bills/README.md#upload_attachment) - Upload bill attachment

### [company_info](docs/sdks/companyinfo/README.md)

* [get](docs/sdks/companyinfo/README.md#get) - Get company info
* [refresh](docs/sdks/companyinfo/README.md#refresh) - Refresh company info

### [credit_notes](docs/sdks/creditnotes/README.md)

* [create](docs/sdks/creditnotes/README.md#create) - Create credit note
* [get](docs/sdks/creditnotes/README.md#get) - Get credit note
* [get_create_update_model](docs/sdks/creditnotes/README.md#get_create_update_model) - Get create/update credit note model
* [list](docs/sdks/creditnotes/README.md#list) - List credit notes
* [update](docs/sdks/creditnotes/README.md#update) - Update credit note

### [customers](docs/sdks/customers/README.md)

* [create](docs/sdks/customers/README.md#create) - Create customer
* [download_attachment](docs/sdks/customers/README.md#download_attachment) - Download customer attachment
* [get](docs/sdks/customers/README.md#get) - Get customer
* [get_attachment](docs/sdks/customers/README.md#get_attachment) - Get customer attachment
* [get_create_update_model](docs/sdks/customers/README.md#get_create_update_model) - Get create/update customer model
* [list](docs/sdks/customers/README.md#list) - List customers
* [list_attachments](docs/sdks/customers/README.md#list_attachments) - List customer attachments
* [update](docs/sdks/customers/README.md#update) - Update customer

### [direct_costs](docs/sdks/directcosts/README.md)

* [create](docs/sdks/directcosts/README.md#create) - Create direct cost
* [download_attachment](docs/sdks/directcosts/README.md#download_attachment) - Download direct cost attachment
* [get](docs/sdks/directcosts/README.md#get) - Get direct cost
* [get_attachment](docs/sdks/directcosts/README.md#get_attachment) - Get direct cost attachment
* [get_create_model](docs/sdks/directcosts/README.md#get_create_model) - Get create direct cost model
* [list](docs/sdks/directcosts/README.md#list) - List direct costs
* [list_attachments](docs/sdks/directcosts/README.md#list_attachments) - List direct cost attachments
* [upload_attachment](docs/sdks/directcosts/README.md#upload_attachment) - Upload direct cost attachment

### [direct_incomes](docs/sdks/directincomes/README.md)

* [create](docs/sdks/directincomes/README.md#create) - Create direct income
* [download_attachment](docs/sdks/directincomes/README.md#download_attachment) - Download direct income attachment
* [get](docs/sdks/directincomes/README.md#get) - Get direct income
* [get_attachment](docs/sdks/directincomes/README.md#get_attachment) - Get direct income attachment
* [get_create_model](docs/sdks/directincomes/README.md#get_create_model) - Get create direct income model
* [list](docs/sdks/directincomes/README.md#list) - List direct incomes
* [list_attachments](docs/sdks/directincomes/README.md#list_attachments) - List direct income attachments
* [upload_attachment](docs/sdks/directincomes/README.md#upload_attachment) - Create direct income attachment

### [invoices](docs/sdks/invoices/README.md)

* [create](docs/sdks/invoices/README.md#create) - Create invoice
* [delete](docs/sdks/invoices/README.md#delete) - Delete invoice
* [download_attachment](docs/sdks/invoices/README.md#download_attachment) - Download invoice attachment
* [download_pdf](docs/sdks/invoices/README.md#download_pdf) - Get invoice as PDF
* [get](docs/sdks/invoices/README.md#get) - Get invoice
* [get_attachment](docs/sdks/invoices/README.md#get_attachment) - Get invoice attachment
* [get_create_update_model](docs/sdks/invoices/README.md#get_create_update_model) - Get create/update invoice model
* [list](docs/sdks/invoices/README.md#list) - List invoices
* [list_attachments](docs/sdks/invoices/README.md#list_attachments) - List invoice attachments
* [update](docs/sdks/invoices/README.md#update) - Update invoice
* [upload_attachment](docs/sdks/invoices/README.md#upload_attachment) - Push invoice attachment

### [items](docs/sdks/items/README.md)

* [create](docs/sdks/items/README.md#create) - Create item
* [get](docs/sdks/items/README.md#get) - Get item
* [get_create_model](docs/sdks/items/README.md#get_create_model) - Get create item model
* [list](docs/sdks/items/README.md#list) - List items

### [journal_entries](docs/sdks/journalentries/README.md)

* [create](docs/sdks/journalentries/README.md#create) - Create journal entry
* [delete](docs/sdks/journalentries/README.md#delete) - Delete journal entry
* [get](docs/sdks/journalentries/README.md#get) - Get journal entry
* [get_create_model](docs/sdks/journalentries/README.md#get_create_model) - Get create journal entry model
* [list](docs/sdks/journalentries/README.md#list) - List journal entries

### [journals](docs/sdks/journals/README.md)

* [create](docs/sdks/journals/README.md#create) - Create journal
* [get](docs/sdks/journals/README.md#get) - Get journal
* [get_create_model](docs/sdks/journals/README.md#get_create_model) - Get create journal model
* [list](docs/sdks/journals/README.md#list) - List journals

### [payment_methods](docs/sdks/paymentmethods/README.md)

* [get](docs/sdks/paymentmethods/README.md#get) - Get payment method
* [list](docs/sdks/paymentmethods/README.md#list) - List payment methods

### [payments](docs/sdks/payments/README.md)

* [create](docs/sdks/payments/README.md#create) - Create payment
* [get](docs/sdks/payments/README.md#get) - Get payment
* [get_create_model](docs/sdks/payments/README.md#get_create_model) - Get create payment model
* [list](docs/sdks/payments/README.md#list) - List payments

### [purchase_orders](docs/sdks/purchaseorders/README.md)

* [create](docs/sdks/purchaseorders/README.md#create) - Create purchase order
* [get](docs/sdks/purchaseorders/README.md#get) - Get purchase order
* [get_create_update_model](docs/sdks/purchaseorders/README.md#get_create_update_model) - Get create/update purchase order model
* [list](docs/sdks/purchaseorders/README.md#list) - List purchase orders
* [update](docs/sdks/purchaseorders/README.md#update) - Update purchase order

### [reports](docs/sdks/reports/README.md)

* [get_aged_creditors_report](docs/sdks/reports/README.md#get_aged_creditors_report) - Aged creditors report
* [get_aged_debtors_report](docs/sdks/reports/README.md#get_aged_debtors_report) - Aged debtors report
* [get_balance_sheet](docs/sdks/reports/README.md#get_balance_sheet) - Get balance sheet
* [get_cash_flow_statement](docs/sdks/reports/README.md#get_cash_flow_statement) - Get cash flow statement
* [get_profit_and_loss](docs/sdks/reports/README.md#get_profit_and_loss) - Get profit and loss
* [is_aged_creditors_report_available](docs/sdks/reports/README.md#is_aged_creditors_report_available) - Aged creditors report available
* [is_aged_debtor_report_available](docs/sdks/reports/README.md#is_aged_debtor_report_available) - Aged debtors report available

### [sales_orders](docs/sdks/salesorders/README.md)

* [get](docs/sdks/salesorders/README.md#get) - Get sales order
* [list](docs/sdks/salesorders/README.md#list) - List sales orders

### [suppliers](docs/sdks/suppliers/README.md)

* [create](docs/sdks/suppliers/README.md#create) - Create supplier
* [download_attachment](docs/sdks/suppliers/README.md#download_attachment) - Download supplier attachment
* [get](docs/sdks/suppliers/README.md#get) - Get supplier
* [get_attachment](docs/sdks/suppliers/README.md#get_attachment) - Get supplier attachment
* [get_create_update_model](docs/sdks/suppliers/README.md#get_create_update_model) - Get create/update supplier model
* [list](docs/sdks/suppliers/README.md#list) - List suppliers
* [list_attachments](docs/sdks/suppliers/README.md#list_attachments) - List supplier attachments
* [update](docs/sdks/suppliers/README.md#update) - Update supplier

### [tax_rates](docs/sdks/taxrates/README.md)

* [get](docs/sdks/taxrates/README.md#get) - Get tax rate
* [list](docs/sdks/taxrates/README.md#list) - List all tax rates

### [tracking_categories](docs/sdks/trackingcategories/README.md)

* [get](docs/sdks/trackingcategories/README.md#get) - Get tracking categories
* [list](docs/sdks/trackingcategories/README.md#list) - List tracking categories

### [transfers](docs/sdks/transfers/README.md)

* [create](docs/sdks/transfers/README.md#create) - Create transfer
* [get](docs/sdks/transfers/README.md#get) - Get transfer
* [get_create_model](docs/sdks/transfers/README.md#get_create_model) - Get create transfer model
* [list](docs/sdks/transfers/README.md#list) - List transfers
* [upload_attachment](docs/sdks/transfers/README.md#upload_attachment) - Push invoice attachment
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->



<!-- End Dev Containers -->

<!-- Placeholder for Future Speakeasy SDK Sections -->


### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)