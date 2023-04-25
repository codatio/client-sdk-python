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

res = s.account_transactions.get_account_transaction(req)

if res.account_transaction is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [account_transactions](docs/accounttransactions/README.md)

* [get_account_transaction](docs/accounttransactions/README.md#get_account_transaction) - Get account transaction
* [list_account_transactions](docs/accounttransactions/README.md#list_account_transactions) - List account transactions

### [accounts](docs/accounts/README.md)

* [create_account](docs/accounts/README.md#create_account) - Create account
* [get_account](docs/accounts/README.md#get_account) - Get account
* [get_create_chart_of_accounts_model](docs/accounts/README.md#get_create_chart_of_accounts_model) - Get create account model
* [list_accounts](docs/accounts/README.md#list_accounts) - List accounts

### [bank_account_transactions](docs/bankaccounttransactions/README.md)

* [create_bank_transactions](docs/bankaccounttransactions/README.md#create_bank_transactions) - Create bank transactions
* [get_create_bank_account_model](docs/bankaccounttransactions/README.md#get_create_bank_account_model) - List push options for bank account bank transactions
* [list_bank_account_transactions](docs/bankaccounttransactions/README.md#list_bank_account_transactions) - List bank transactions for bank account
* [list_bank_transactions](docs/bankaccounttransactions/README.md#list_bank_transactions) - List all bank transactions

### [bank_accounts](docs/bankaccounts/README.md)

* [create_bank_account](docs/bankaccounts/README.md#create_bank_account) - Create bank account
* [get_all_bank_account](docs/bankaccounts/README.md#get_all_bank_account) - Get bank account
* [get_bank_account](docs/bankaccounts/README.md#get_bank_account) - Get bank account
* [get_create_update_bank_accounts_model](docs/bankaccounts/README.md#get_create_update_bank_accounts_model) - Get create/update bank account model
* [list_bank_accounts](docs/bankaccounts/README.md#list_bank_accounts) - List bank accounts
* [update_bank_account](docs/bankaccounts/README.md#update_bank_account) - Update bank account

### [bill_credit_notes](docs/billcreditnotes/README.md)

* [create_bill_credit_note](docs/billcreditnotes/README.md#create_bill_credit_note) - Create bill credit note
* [get_bill_credit_note](docs/billcreditnotes/README.md#get_bill_credit_note) - Get bill credit note
* [get_create_update_bill_credit_notes_model](docs/billcreditnotes/README.md#get_create_update_bill_credit_notes_model) - Get create/update bill credit note model
* [list_bill_credit_notes](docs/billcreditnotes/README.md#list_bill_credit_notes) - List bill credit notes
* [update_bill_credit_note](docs/billcreditnotes/README.md#update_bill_credit_note) - Update bill credit note

### [bill_payments](docs/billpayments/README.md)

* [create_bill_payment](docs/billpayments/README.md#create_bill_payment) - Create bill payments
* [delete_bill_payment](docs/billpayments/README.md#delete_bill_payment) - Delete bill payment
* [get_bill_payments](docs/billpayments/README.md#get_bill_payments) - Get bill payment
* [get_create_bill_payments_model](docs/billpayments/README.md#get_create_bill_payments_model) - Get create bill payment model
* [list_bill_payments](docs/billpayments/README.md#list_bill_payments) - List bill payments

### [bills](docs/bills/README.md)

* [create_bill](docs/bills/README.md#create_bill) - Create bill
* [delete_bill](docs/bills/README.md#delete_bill) - Delete bill
* [download_bill_attachment](docs/bills/README.md#download_bill_attachment) - Download bill attachment
* [get_bill](docs/bills/README.md#get_bill) - Get bill
* [get_bill_attachment](docs/bills/README.md#get_bill_attachment) - Get bill attachment
* [get_bill_attachments](docs/bills/README.md#get_bill_attachments) - List bill attachments
* [get_create_update_bills_model](docs/bills/README.md#get_create_update_bills_model) - Get create/update bill model
* [list_bills](docs/bills/README.md#list_bills) - List bills
* [update_bill](docs/bills/README.md#update_bill) - Update bill
* [upload_bill_attachments](docs/bills/README.md#upload_bill_attachments) - Upload bill attachments

### [company_info](docs/companyinfo/README.md)

* [get_company_info](docs/companyinfo/README.md#get_company_info) - Get company info
* [post_sync_info](docs/companyinfo/README.md#post_sync_info) - Refresh company info

### [credit_notes](docs/creditnotes/README.md)

* [create_credit_note](docs/creditnotes/README.md#create_credit_note) - Create credit note
* [get_create_update_credit_notes_model](docs/creditnotes/README.md#get_create_update_credit_notes_model) - Get create/update credit note model
* [get_credit_note](docs/creditnotes/README.md#get_credit_note) - Get credit note
* [list_credit_notes](docs/creditnotes/README.md#list_credit_notes) - List credit notes
* [update_credit_note](docs/creditnotes/README.md#update_credit_note) - Update creditNote

### [customers](docs/customers/README.md)

* [create_customer](docs/customers/README.md#create_customer) - Create customer
* [download_customer_attachment](docs/customers/README.md#download_customer_attachment) - Download customer attachment
* [get_create_update_customers_model](docs/customers/README.md#get_create_update_customers_model) - Get create/update customer model
* [get_customer](docs/customers/README.md#get_customer) - Get customer
* [get_customer_attachment](docs/customers/README.md#get_customer_attachment) - Get customer attachment
* [get_customer_attachments](docs/customers/README.md#get_customer_attachments) - List customer attachments
* [get_customers](docs/customers/README.md#get_customers) - List customers
* [update_customer](docs/customers/README.md#update_customer) - Update customer

### [direct_costs](docs/directcosts/README.md)

* [create_direct_cost](docs/directcosts/README.md#create_direct_cost) - Create direct cost
* [download_direct_cost_attachment](docs/directcosts/README.md#download_direct_cost_attachment) - Download direct cost attachment
* [get_create_direct_costs_model](docs/directcosts/README.md#get_create_direct_costs_model) - Get create direct cost model
* [get_direct_cost](docs/directcosts/README.md#get_direct_cost) - Get direct cost
* [get_direct_cost_attachment](docs/directcosts/README.md#get_direct_cost_attachment) - Get direct cost attachment
* [get_direct_costs](docs/directcosts/README.md#get_direct_costs) - List direct costs
* [list_direct_cost_attachments](docs/directcosts/README.md#list_direct_cost_attachments) - List direct cost attachments
* [upload_direct_cost_attachment](docs/directcosts/README.md#upload_direct_cost_attachment) - Upload direct cost attachment

### [direct_incomes](docs/directincomes/README.md)

* [create_direct_income](docs/directincomes/README.md#create_direct_income) - Create direct income
* [download_direct_income_attachment](docs/directincomes/README.md#download_direct_income_attachment) - Download direct income attachment
* [get_create_direct_incomes_model](docs/directincomes/README.md#get_create_direct_incomes_model) - Get create direct income model
* [get_direct_income](docs/directincomes/README.md#get_direct_income) - Get direct income
* [get_direct_income_attachment](docs/directincomes/README.md#get_direct_income_attachment) - Get direct income attachment
* [get_direct_incomes](docs/directincomes/README.md#get_direct_incomes) - Get direct incomes
* [list_direct_income_attachments](docs/directincomes/README.md#list_direct_income_attachments) - List direct income attachments
* [upload_direct_income_attachment](docs/directincomes/README.md#upload_direct_income_attachment) - Create direct income attachment

### [financials](docs/financials/README.md)

* [get_balance_sheet](docs/financials/README.md#get_balance_sheet) - Get balance sheet
* [get_cash_flow_statement](docs/financials/README.md#get_cash_flow_statement) - Get cash flow statement
* [get_profit_and_loss](docs/financials/README.md#get_profit_and_loss) - Get profit and loss

### [invoices](docs/invoices/README.md)

* [download_invoice_pdf](docs/invoices/README.md#download_invoice_pdf) - Get invoice as PDF
* [create_invoice](docs/invoices/README.md#create_invoice) - Create invoice
* [delete_invoice](docs/invoices/README.md#delete_invoice) - Delete invoice
* [download_invoice_attachment](docs/invoices/README.md#download_invoice_attachment) - Download invoice attachment
* [get_create_update_invoices_model](docs/invoices/README.md#get_create_update_invoices_model) - Get create/update invoice model
* [get_invoice](docs/invoices/README.md#get_invoice) - Get invoice
* [get_invoice_attachment](docs/invoices/README.md#get_invoice_attachment) - Get invoice attachment
* [get_invoice_attachments](docs/invoices/README.md#get_invoice_attachments) - Get invoice attachments
* [list_invoices](docs/invoices/README.md#list_invoices) - List invoices
* [update_invoice](docs/invoices/README.md#update_invoice) - Update invoice
* [upload_invoice_attachment](docs/invoices/README.md#upload_invoice_attachment) - Push invoice attachment

### [items](docs/items/README.md)

* [create_item](docs/items/README.md#create_item) - Create item
* [get_create_items_model](docs/items/README.md#get_create_items_model) - Get create item model
* [get_item](docs/items/README.md#get_item) - Get item
* [list_items](docs/items/README.md#list_items) - List items

### [journal_entries](docs/journalentries/README.md)

* [create_journal_entry](docs/journalentries/README.md#create_journal_entry) - Create journal entry
* [delete_journal_entry](docs/journalentries/README.md#delete_journal_entry) - Delete journal entry
* [get_create_journal_entries_model](docs/journalentries/README.md#get_create_journal_entries_model) - Get create journal entry model
* [get_journal_entry](docs/journalentries/README.md#get_journal_entry) - Get journal entry
* [list_journal_entries](docs/journalentries/README.md#list_journal_entries) - List journal entries

### [journals](docs/journals/README.md)

* [get_create_journals_model](docs/journals/README.md#get_create_journals_model) - Get create journal model
* [get_journal](docs/journals/README.md#get_journal) - Get journal
* [list_journals](docs/journals/README.md#list_journals) - List journals
* [push_journal](docs/journals/README.md#push_journal) - Create journal

### [payment_methods](docs/paymentmethods/README.md)

* [get_payment_method](docs/paymentmethods/README.md#get_payment_method) - Get payment method
* [list_payment_methods](docs/paymentmethods/README.md#list_payment_methods) - List all payment methods

### [payments](docs/payments/README.md)

* [create_payment](docs/payments/README.md#create_payment) - Create payment
* [get_create_payments_model](docs/payments/README.md#get_create_payments_model) - Get create payment model
* [get_payment](docs/payments/README.md#get_payment) - Get payment
* [list_payments](docs/payments/README.md#list_payments) - List payments

### [purchase_orders](docs/purchaseorders/README.md)

* [create_purchase_order](docs/purchaseorders/README.md#create_purchase_order) - Create purchase order
* [get_create_update_purchase_orders_model](docs/purchaseorders/README.md#get_create_update_purchase_orders_model) - Get create/update purchase order model
* [get_purchase_order](docs/purchaseorders/README.md#get_purchase_order) - Get purchase order
* [list_purchase_orders](docs/purchaseorders/README.md#list_purchase_orders) - List purchase orders
* [update_purchase_order](docs/purchaseorders/README.md#update_purchase_order) - Update purchase order

### [reports](docs/reports/README.md)

* [get_aged_creditors_report](docs/reports/README.md#get_aged_creditors_report) - Aged creditors report
* [get_aged_debtors_report](docs/reports/README.md#get_aged_debtors_report) - Aged debtors report
* [is_aged_creditors_report_available](docs/reports/README.md#is_aged_creditors_report_available) - Aged creditors report available
* [is_aged_debtor_report_available](docs/reports/README.md#is_aged_debtor_report_available) - Aged debtors report available

### [sales_orders](docs/salesorders/README.md)

* [get_sales_order](docs/salesorders/README.md#get_sales_order) - Get sales order
* [list_sales_orders](docs/salesorders/README.md#list_sales_orders) - List sales orders

### [suppliers](docs/suppliers/README.md)

* [create_supplier](docs/suppliers/README.md#create_supplier) - Create suppliers
* [download_supplier_attachment](docs/suppliers/README.md#download_supplier_attachment) - Download supplier attachment
* [get_create_update_suppliers_model](docs/suppliers/README.md#get_create_update_suppliers_model) - Get create/update supplier model
* [get_supplier](docs/suppliers/README.md#get_supplier) - Get supplier
* [get_supplier_attachment](docs/suppliers/README.md#get_supplier_attachment) - Get supplier attachment
* [list_supplier_attachments](docs/suppliers/README.md#list_supplier_attachments) - List supplier attachments
* [list_suppliers](docs/suppliers/README.md#list_suppliers) - List suppliers
* [put_supplier](docs/suppliers/README.md#put_supplier) - Update supplier

### [tax_rates](docs/taxrates/README.md)

* [get_tax_rate](docs/taxrates/README.md#get_tax_rate) - Get tax rate
* [list_tax_rates](docs/taxrates/README.md#list_tax_rates) - List all tax rates

### [tracking_categories](docs/trackingcategories/README.md)

* [get_tracking_category](docs/trackingcategories/README.md#get_tracking_category) - Get tracking categories
* [list_tracking_categories](docs/trackingcategories/README.md#list_tracking_categories) - List tracking categories

### [transfers](docs/transfers/README.md)

* [create_transfer](docs/transfers/README.md#create_transfer) - Create transfer
* [get_create_transfers_model](docs/transfers/README.md#get_create_transfers_model) - Get create transfer model
* [get_transfer](docs/transfers/README.md#get_transfer) - Get transfer
* [list_transfers](docs/transfers/README.md#list_transfers) - List transfers
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
