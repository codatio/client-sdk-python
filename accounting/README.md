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

s = codat.Codat()
s.config_security(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    )
)
   
req = operations.GetAccountTransactionRequest(
    security=operations.GetAccountTransactionSecurity(
        api_key="YOUR_API_KEY_HERE",
    ),
    path_params=operations.GetAccountTransactionPathParams(
        account_transaction_id="unde",
        company_id="deserunt",
        connection_id="porro",
    ),
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

* `get_account` - Get account
* `get_accounts` - List accounts
* `post_account` - Create account

### bank_account_transactions

* `get_bank_account_push_options` - List push options for bank account bank transactions
* `list_all_bank_transactionscount` - List bank transactions for bank account
* `list_bank_transactions` - List all bank transactions
* `post_bank_transactions` - Create bank transactions

### bank_accounts

* `get_all_bank_account` - Get bank account
* `get_bank_account` - Get bank account
* `list_bank_accounts` - List bank accounts
* `post_bank_account` - Create bank account
* `put_bank_account` - Update bank account

### bill_credit_notes

* `get_bill_credit_note` - Get bill credit note
* `list_bill_credit_notes` - List bill credit notes
* `post_bill_credit_note` - Create bill credit note
* `update_bill_credit_note` - Update bill credit note

### bill_payments

* `get_bill_payments` - Get bill payment
* `list_bill_payments` - List bill payments
* `post_bill_payment` - Create bill payment

### bills

* `download_bill_attachment` - Download bill attachment
* `get_bill` - Get bill
* `get_bill_attachment` - Get bill attachment
* `get_bill_attachments` - List bill attachments
* `list_bills` - List bills
* `post_bill` - Create bill
* `post_bill_attachments` - Create bill attachments
* `update_bill` - Update bill

### credit_notes

* `get_credit_note` - Get credit note
* `list_credit_notes` - List credit notes
* `post_credit_note` - Update creditNote
* `push_credit_note` - Create credit note

### customers

* `download_customer_attachment` - Download customer attachment
* `get_customer` - Get customer
* `get_customer_attachment` - Get customer attachment
* `get_customer_attachments` - List customer attachments
* `get_customers` - List customers
* `post_customer` - Create customer
* `update_customer` - Update customer

### direct_costs

* `download_direct_cost_attachment` - Download direct cost attachment
* `get_direct_cost` - Get direct cost
* `get_direct_cost_attachment` - Get direct cost attachment
* `get_direct_costs` - List direct costs
* `list_direct_cost_attachments` - List direct cost attachments
* `post_direct_cost` - Create direct cost
* `post_direct_cost_attachment` - Create direct cost attachment

### direct_incomes

* `download_direct_income_attachment` - Download direct income attachment
* `get_direct_income` - Get direct income
* `get_direct_income_attachment` - Get direct income attachment
* `get_direct_incomes` - Get direct incomes
* `list_direct_income_attachments` - List direct income attachments
* `post_direct_income` - Create direct income
* `post_direct_income_attachment` - Create direct income attachment

### financials

* `get_balance_sheet` - Get balance sheet
* `get_cash_flow_statement` - Get cash flow statement
* `get_profit_and_loss` - Get profit and loss

### info

* `get_company_info` - Get company info
* `post_sync_info` - Refresh company info

### invoices

* `donwload_invoice_attachment` - Download invoice attachment
* `get_invoice` - Get invoice
* `get_invoice_attachment` - Get invoice attachment
* `get_invoice_attachments` - Get invoice attachments
* `get_invoice_pdf` - Get invoice as PDF
* `list_invoices` - List invoices
* `post_invoice` - Create invoice
* `push_invoice_attachment` - Push invoice attachment
* `update_invoice` - Update invoice

### items

* `get_item` - Get item
* `list_items` - List items
* `post_item` - Create item

### journal_entries

* `get_journal_entry` - Get journal entry
* `list_journal_entries` - List journal entries
* `post_journal_entry` - Create journal entry

### journals

* `get_journal` - Get journal
* `list_journals` - List journals
* `push_journal` - Create journal

### payment_methods

* `get_payment_method` - Get payment method
* `list_payment_methods` - List all payment methods

### payments

* `get_payment` - Get payment
* `list_payments` - List payments
* `post_payment` - Create payment

### purchase_orders

* `get_purchase_order` - Get purchase order
* `list_purchase_orders` - List purchase orders
* `post_purchase_order` - Create purchase order
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

* `download_supplier_attachment` - Download supplier attachment
* `get_supplier` - Get supplier
* `get_supplier_attachment` - Get supplier attachment
* `list_supplier_attachments` - List supplier attachments
* `list_suppliers` - List suppliers
* `post_suppliers` - Create suppliers
* `put_supplier` - Update supplier

### tax_rates

* `get_tax_rate` - Get tax rate
* `list_tax_rates` - List all tax rates

### tracking_categories

* `get_tracking_category` - Get tracking categories
* `list_tracking_categories` - List tracking categories

### transfers

* `get_transfer` - Get transfer
* `list_transfers` - List transfers
* `post_transfer` - Create transfer
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
