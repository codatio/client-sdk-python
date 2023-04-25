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

* [get_account_transaction](docs/accounttransactions/getaccounttransaction.md) - Get account transaction
* [list_account_transactions](docs/accounttransactions/listaccounttransactions.md) - List account transactions

### [accounts](docs/accounts/README.md)

* [create_account](docs/accounts/createaccount.md) - Create account
* [get_account](docs/accounts/getaccount.md) - Get account
* [get_create_chart_of_accounts_model](docs/accounts/getcreatechartofaccountsmodel.md) - Get create account model
* [list_accounts](docs/accounts/listaccounts.md) - List accounts

### [bank_account_transactions](docs/bankaccounttransactions/README.md)

* [create_bank_transactions](docs/bankaccounttransactions/createbanktransactions.md) - Create bank transactions
* [get_create_bank_account_model](docs/bankaccounttransactions/getcreatebankaccountmodel.md) - List push options for bank account bank transactions
* [list_bank_account_transactions](docs/bankaccounttransactions/listbankaccounttransactions.md) - List bank transactions for bank account
* [list_bank_transactions](docs/bankaccounttransactions/listbanktransactions.md) - List all bank transactions

### [bank_accounts](docs/bankaccounts/README.md)

* [create_bank_account](docs/bankaccounts/createbankaccount.md) - Create bank account
* [get_all_bank_account](docs/bankaccounts/getallbankaccount.md) - Get bank account
* [get_bank_account](docs/bankaccounts/getbankaccount.md) - Get bank account
* [get_create_update_bank_accounts_model](docs/bankaccounts/getcreateupdatebankaccountsmodel.md) - Get create/update bank account model
* [list_bank_accounts](docs/bankaccounts/listbankaccounts.md) - List bank accounts
* [update_bank_account](docs/bankaccounts/updatebankaccount.md) - Update bank account

### [bill_credit_notes](docs/billcreditnotes/README.md)

* [create_bill_credit_note](docs/billcreditnotes/createbillcreditnote.md) - Create bill credit note
* [get_bill_credit_note](docs/billcreditnotes/getbillcreditnote.md) - Get bill credit note
* [get_create_update_bill_credit_notes_model](docs/billcreditnotes/getcreateupdatebillcreditnotesmodel.md) - Get create/update bill credit note model
* [list_bill_credit_notes](docs/billcreditnotes/listbillcreditnotes.md) - List bill credit notes
* [update_bill_credit_note](docs/billcreditnotes/updatebillcreditnote.md) - Update bill credit note

### [bill_payments](docs/billpayments/README.md)

* [create_bill_payment](docs/billpayments/createbillpayment.md) - Create bill payments
* [delete_bill_payment](docs/billpayments/deletebillpayment.md) - Delete bill payment
* [get_bill_payments](docs/billpayments/getbillpayments.md) - Get bill payment
* [get_create_bill_payments_model](docs/billpayments/getcreatebillpaymentsmodel.md) - Get create bill payment model
* [list_bill_payments](docs/billpayments/listbillpayments.md) - List bill payments

### [bills](docs/bills/README.md)

* [create_bill](docs/bills/createbill.md) - Create bill
* [delete_bill](docs/bills/deletebill.md) - Delete bill
* [download_bill_attachment](docs/bills/downloadbillattachment.md) - Download bill attachment
* [get_bill](docs/bills/getbill.md) - Get bill
* [get_bill_attachment](docs/bills/getbillattachment.md) - Get bill attachment
* [get_bill_attachments](docs/bills/getbillattachments.md) - List bill attachments
* [get_create_update_bills_model](docs/bills/getcreateupdatebillsmodel.md) - Get create/update bill model
* [list_bills](docs/bills/listbills.md) - List bills
* [update_bill](docs/bills/updatebill.md) - Update bill
* [upload_bill_attachments](docs/bills/uploadbillattachments.md) - Upload bill attachments

### [company_info](docs/companyinfo/README.md)

* [get_company_info](docs/companyinfo/getcompanyinfo.md) - Get company info
* [post_sync_info](docs/companyinfo/postsyncinfo.md) - Refresh company info

### [credit_notes](docs/creditnotes/README.md)

* [create_credit_note](docs/creditnotes/createcreditnote.md) - Create credit note
* [get_create_update_credit_notes_model](docs/creditnotes/getcreateupdatecreditnotesmodel.md) - Get create/update credit note model
* [get_credit_note](docs/creditnotes/getcreditnote.md) - Get credit note
* [list_credit_notes](docs/creditnotes/listcreditnotes.md) - List credit notes
* [update_credit_note](docs/creditnotes/updatecreditnote.md) - Update creditNote

### [customers](docs/customers/README.md)

* [create_customer](docs/customers/createcustomer.md) - Create customer
* [download_customer_attachment](docs/customers/downloadcustomerattachment.md) - Download customer attachment
* [get_create_update_customers_model](docs/customers/getcreateupdatecustomersmodel.md) - Get create/update customer model
* [get_customer](docs/customers/getcustomer.md) - Get customer
* [get_customer_attachment](docs/customers/getcustomerattachment.md) - Get customer attachment
* [get_customer_attachments](docs/customers/getcustomerattachments.md) - List customer attachments
* [get_customers](docs/customers/getcustomers.md) - List customers
* [update_customer](docs/customers/updatecustomer.md) - Update customer

### [direct_costs](docs/directcosts/README.md)

* [create_direct_cost](docs/directcosts/createdirectcost.md) - Create direct cost
* [download_direct_cost_attachment](docs/directcosts/downloaddirectcostattachment.md) - Download direct cost attachment
* [get_create_direct_costs_model](docs/directcosts/getcreatedirectcostsmodel.md) - Get create direct cost model
* [get_direct_cost](docs/directcosts/getdirectcost.md) - Get direct cost
* [get_direct_cost_attachment](docs/directcosts/getdirectcostattachment.md) - Get direct cost attachment
* [get_direct_costs](docs/directcosts/getdirectcosts.md) - List direct costs
* [list_direct_cost_attachments](docs/directcosts/listdirectcostattachments.md) - List direct cost attachments
* [upload_direct_cost_attachment](docs/directcosts/uploaddirectcostattachment.md) - Upload direct cost attachment

### [direct_incomes](docs/directincomes/README.md)

* [create_direct_income](docs/directincomes/createdirectincome.md) - Create direct income
* [download_direct_income_attachment](docs/directincomes/downloaddirectincomeattachment.md) - Download direct income attachment
* [get_create_direct_incomes_model](docs/directincomes/getcreatedirectincomesmodel.md) - Get create direct income model
* [get_direct_income](docs/directincomes/getdirectincome.md) - Get direct income
* [get_direct_income_attachment](docs/directincomes/getdirectincomeattachment.md) - Get direct income attachment
* [get_direct_incomes](docs/directincomes/getdirectincomes.md) - Get direct incomes
* [list_direct_income_attachments](docs/directincomes/listdirectincomeattachments.md) - List direct income attachments
* [upload_direct_income_attachment](docs/directincomes/uploaddirectincomeattachment.md) - Create direct income attachment

### [financials](docs/financials/README.md)

* [get_balance_sheet](docs/financials/getbalancesheet.md) - Get balance sheet
* [get_cash_flow_statement](docs/financials/getcashflowstatement.md) - Get cash flow statement
* [get_profit_and_loss](docs/financials/getprofitandloss.md) - Get profit and loss

### [invoices](docs/invoices/README.md)

* [download_invoice_pdf](docs/invoices/downloadinvoicepdf.md) - Get invoice as PDF
* [create_invoice](docs/invoices/createinvoice.md) - Create invoice
* [delete_invoice](docs/invoices/deleteinvoice.md) - Delete invoice
* [download_invoice_attachment](docs/invoices/downloadinvoiceattachment.md) - Download invoice attachment
* [get_create_update_invoices_model](docs/invoices/getcreateupdateinvoicesmodel.md) - Get create/update invoice model
* [get_invoice](docs/invoices/getinvoice.md) - Get invoice
* [get_invoice_attachment](docs/invoices/getinvoiceattachment.md) - Get invoice attachment
* [get_invoice_attachments](docs/invoices/getinvoiceattachments.md) - Get invoice attachments
* [list_invoices](docs/invoices/listinvoices.md) - List invoices
* [update_invoice](docs/invoices/updateinvoice.md) - Update invoice
* [upload_invoice_attachment](docs/invoices/uploadinvoiceattachment.md) - Push invoice attachment

### [items](docs/items/README.md)

* [create_item](docs/items/createitem.md) - Create item
* [get_create_items_model](docs/items/getcreateitemsmodel.md) - Get create item model
* [get_item](docs/items/getitem.md) - Get item
* [list_items](docs/items/listitems.md) - List items

### [journal_entries](docs/journalentries/README.md)

* [create_journal_entry](docs/journalentries/createjournalentry.md) - Create journal entry
* [delete_journal_entry](docs/journalentries/deletejournalentry.md) - Delete journal entry
* [get_create_journal_entries_model](docs/journalentries/getcreatejournalentriesmodel.md) - Get create journal entry model
* [get_journal_entry](docs/journalentries/getjournalentry.md) - Get journal entry
* [list_journal_entries](docs/journalentries/listjournalentries.md) - List journal entries

### [journals](docs/journals/README.md)

* [get_create_journals_model](docs/journals/getcreatejournalsmodel.md) - Get create journal model
* [get_journal](docs/journals/getjournal.md) - Get journal
* [list_journals](docs/journals/listjournals.md) - List journals
* [push_journal](docs/journals/pushjournal.md) - Create journal

### [payment_methods](docs/paymentmethods/README.md)

* [get_payment_method](docs/paymentmethods/getpaymentmethod.md) - Get payment method
* [list_payment_methods](docs/paymentmethods/listpaymentmethods.md) - List all payment methods

### [payments](docs/payments/README.md)

* [create_payment](docs/payments/createpayment.md) - Create payment
* [get_create_payments_model](docs/payments/getcreatepaymentsmodel.md) - Get create payment model
* [get_payment](docs/payments/getpayment.md) - Get payment
* [list_payments](docs/payments/listpayments.md) - List payments

### [purchase_orders](docs/purchaseorders/README.md)

* [create_purchase_order](docs/purchaseorders/createpurchaseorder.md) - Create purchase order
* [get_create_update_purchase_orders_model](docs/purchaseorders/getcreateupdatepurchaseordersmodel.md) - Get create/update purchase order model
* [get_purchase_order](docs/purchaseorders/getpurchaseorder.md) - Get purchase order
* [list_purchase_orders](docs/purchaseorders/listpurchaseorders.md) - List purchase orders
* [update_purchase_order](docs/purchaseorders/updatepurchaseorder.md) - Update purchase order

### [reports](docs/reports/README.md)

* [get_aged_creditors_report](docs/reports/getagedcreditorsreport.md) - Aged creditors report
* [get_aged_debtors_report](docs/reports/getageddebtorsreport.md) - Aged debtors report
* [is_aged_creditors_report_available](docs/reports/isagedcreditorsreportavailable.md) - Aged creditors report available
* [is_aged_debtor_report_available](docs/reports/isageddebtorreportavailable.md) - Aged debtors report available

### [sales_orders](docs/salesorders/README.md)

* [get_sales_order](docs/salesorders/getsalesorder.md) - Get sales order
* [list_sales_orders](docs/salesorders/listsalesorders.md) - List sales orders

### [suppliers](docs/suppliers/README.md)

* [create_supplier](docs/suppliers/createsupplier.md) - Create suppliers
* [download_supplier_attachment](docs/suppliers/downloadsupplierattachment.md) - Download supplier attachment
* [get_create_update_suppliers_model](docs/suppliers/getcreateupdatesuppliersmodel.md) - Get create/update supplier model
* [get_supplier](docs/suppliers/getsupplier.md) - Get supplier
* [get_supplier_attachment](docs/suppliers/getsupplierattachment.md) - Get supplier attachment
* [list_supplier_attachments](docs/suppliers/listsupplierattachments.md) - List supplier attachments
* [list_suppliers](docs/suppliers/listsuppliers.md) - List suppliers
* [put_supplier](docs/suppliers/putsupplier.md) - Update supplier

### [tax_rates](docs/taxrates/README.md)

* [get_tax_rate](docs/taxrates/gettaxrate.md) - Get tax rate
* [list_tax_rates](docs/taxrates/listtaxrates.md) - List all tax rates

### [tracking_categories](docs/trackingcategories/README.md)

* [get_tracking_category](docs/trackingcategories/gettrackingcategory.md) - Get tracking categories
* [list_tracking_categories](docs/trackingcategories/listtrackingcategories.md) - List tracking categories

### [transfers](docs/transfers/README.md)

* [create_transfer](docs/transfers/createtransfer.md) - Create transfer
* [get_create_transfers_model](docs/transfers/getcreatetransfersmodel.md) - Get create transfer model
* [get_transfer](docs/transfers/gettransfer.md) - Get transfer
* [list_transfers](docs/transfers/listtransfers.md) - List transfers
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
