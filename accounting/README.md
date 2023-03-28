# codatio-accounting

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install codat-accounting
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAccountTransactionRequest(
    account_transaction_id="unde",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)
    
res = s.account_transactions.get_account_transaction(req)

if res.source_modified_date is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations


### account_transactions

* `get_account_transaction` - Get account transaction
* `list_account_transactions` - List account transactions

### accounts

* `create_account` - Create account
* `get_account` - Get account
* `get_accounts` - List accounts
* `get_create_chart_of_accounts_model` - Get create account model

### bank_account_transactions

* `get_bank_account_push_options` - List push options for bank account bank transactions
* `list_bank_account_transactions` - List bank transactions for bank account
* `list_bank_transactions` - List all bank transactions
* `post_bank_transactions` - Create bank transactions

### bank_accounts

* `create_bank_account` - Create bank account
* `get_all_bank_account` - Get bank account
* `get_bank_account` - Get bank account
* `get_create_update_bank_accounts_model` - Get create/update bank account model
* `list_bank_accounts` - List bank accounts
* `put_bank_account` - Update bank account

### bill_credit_notes

* `create_bill_credit_note` - Create bill credit note
* `get_bill_credit_note` - Get bill credit note
* `get_create_update_bill_credit_notes_model` - Get create/update bill credit note model
* `list_bill_credit_notes` - List bill credit notes
* `update_bill_credit_note` - Update bill credit note

### bill_payments

* `create_bill_payment` - Create bill payments
* `delete_companies_company_id_connections_connection_id_push_bill_payments_bill_payment_id` - Delete bill payment
* `get_bill_payments` - Get bill payment
* `get_create_bill_payments_model` - Get create bill payment model
* `list_bill_payments` - List bill payments

### bills

* `create_bill` - Create bill
* `create_bill_attachments` - Create bill attachments
* `delete_companies_company_id_connections_connection_id_push_bills_bill_id` - Delete bill
* `download_bill_attachment` - Download bill attachment
* `get_bill` - Get bill
* `get_bill_attachment` - Get bill attachment
* `get_bill_attachments` - List bill attachments
* `get_create_update_bills_model` - Get create/update bill model
* `list_bills` - List bills
* `update_bill` - Update bill

### company_info

* `get_company_info` - Get company info
* `post_sync_info` - Refresh company info

### credit_notes

* `create_credit_note` - Update creditNote
* `get_create_update_credit_notes_model` - Get create/update credit note model
* `get_credit_note` - Get credit note
* `list_credit_notes` - List credit notes
* `push_credit_note` - Create credit note

### customers

* `create_customer` - Create customer
* `download_customer_attachment` - Download customer attachment
* `get_create_update_customers_model` - Get create/update customer model
* `get_customer` - Get customer
* `get_customer_attachment` - Get customer attachment
* `get_customer_attachments` - List customer attachments
* `get_customers` - List customers
* `update_customer` - Update customer

### direct_costs

* `create_direct_cost` - Create direct cost
* `download_direct_cost_attachment` - Download direct cost attachment
* `get_create_direct_costs_model` - Get create direct cost model
* `get_direct_cost` - Get direct cost
* `get_direct_cost_attachment` - Get direct cost attachment
* `get_direct_costs` - List direct costs
* `list_direct_cost_attachments` - List direct cost attachments
* `post_direct_cost_attachment` - Create direct cost attachment

### direct_incomes

* `create_direct_income` - Create direct income
* `download_direct_income_attachment` - Download direct income attachment
* `get_create_direct_incomes_model` - Get create direct income model
* `get_direct_income` - Get direct income
* `get_direct_income_attachment` - Get direct income attachment
* `get_direct_incomes` - Get direct incomes
* `list_direct_income_attachments` - List direct income attachments
* `post_direct_income_attachment` - Create direct income attachment

### financials

* `get_balance_sheet` - Get balance sheet
* `get_cash_flow_statement` - Get cash flow statement
* `get_profit_and_loss` - Get profit and loss

### invoices

* `create_invoice` - Create invoice
* `donwload_invoice_attachment` - Download invoice attachment
* `get_create_update_invoices_model` - Get create/update invoice model
* `get_invoice` - Get invoice
* `get_invoice_attachment` - Get invoice attachment
* `get_invoice_attachments` - Get invoice attachments
* `get_invoice_pdf` - Get invoice as PDF
* `list_invoices` - List invoices
* `push_invoice_attachment` - Push invoice attachment
* `update_invoice` - Update invoice

### items

* `create_item` - Create item
* `get_create_items_model` - Get create item model
* `get_item` - Get item
* `list_items` - List items

### journal_entries

* `create_journal_entry` - Create journal entry
* `get_create_journal_entries_model` - Get create journal entry model
* `get_journal_entry` - Get journal entry
* `list_journal_entries` - List journal entries

### journals

* `get_create_journals_model` - Get create journal model
* `get_journal` - Get journal
* `list_journals` - List journals
* `push_journal` - Create journal

### payment_methods

* `get_payment_method` - Get payment method
* `list_payment_methods` - List all payment methods

### payments

* `create_payment` - Create payment
* `get_create_payments_model` - Get create payment model
* `get_payment` - Get payment
* `list_payments` - List payments

### purchase_orders

* `create_purchase_order` - Create purchase order
* `get_create_update_purchase_orders_model` - Get create/update purchase order model
* `get_purchase_order` - Get purchase order
* `list_purchase_orders` - List purchase orders
* `update_purchase_order` - Update purchase order

### reports

* `get_aged_creditors_report` - Aged creditors report
* `get_aged_debtors_report` - Aged debtors report
* `is_aged_creditors_report_available` - Aged creditors report available
* `is_aged_debtor_report_available` - Aged debtors report available

### sales_orders

* `get_sales_order` - Get sales order
* `list_sales_orders` - List sales orders

### suppliers

* `create_suppliers` - Create suppliers
* `download_supplier_attachment` - Download supplier attachment
* `get_create_update_suppliers_model` - Get create/update supplier model
* `get_supplier` - Get supplier
* `get_supplier_attachment` - Get supplier attachment
* `list_supplier_attachments` - List supplier attachments
* `list_suppliers` - List suppliers
* `put_supplier` - Update supplier

### tax_rates

* `get_tax_rate` - Get tax rate
* `list_tax_rates` - List all tax rates

### tracking_categories

* `get_tracking_category` - Get tracking categories
* `list_tracking_categories` - List tracking categories

### transfers

* `create_transfer` - Create transfer
* `get_create_transfers_model` - Get create transfer model
* `get_transfer` - Get transfer
* `list_transfers` - List transfers
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
