# AccountingCreditNotes
(*accounting_credit_notes*)

## Overview

Credit notes

### Available Operations

* [create_accounting_credit_note](#create_accounting_credit_note) - Create credit note

## create_accounting_credit_note

The *Create credit note* endpoint creates a new [credit note](https://docs.codat.io/accounting-api#/schemas/CreditNote) for a given company's connection.

[Credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) are issued to a customer to indicate debt, typically with reference to a previously issued invoice and/or purchase.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-creditNotes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support creating an account.


### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared
from decimal import Decimal

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountingCreditNoteRequest(
    accounting_credit_note=shared.AccountingCreditNote(
        allocated_on_date='2022-10-23T00:00:00.000Z',
        currency='GBP',
        customer_ref=shared.AccountingCustomerRef(
            id='<ID>',
        ),
        discount_percentage=Decimal('3961.39'),
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(),
                item_ref=shared.ItemRef(
                    id='<ID>',
                ),
                quantity=Decimal('1740.95'),
                tax_rate_ref=shared.TaxRateRef(),
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRefItems(
                            id='<ID>',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        id='<ID>',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.CreditNoteLineItemAccountingProjectReference(
                        id='<ID>',
                    ),
                    record_ref=shared.RecordRef(
                        data_type='accountTransaction',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRefItems(
                        id='<ID>',
                    ),
                ],
                unit_amount=Decimal('6472.07'),
            ),
        ],
        metadata=shared.Metadata(),
        modified_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.PaymentAllocationItems(
                allocation=shared.Allocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(),
                    currency='USD',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                ),
            ),
        ],
        remaining_credit=Decimal('3693.65'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.VOID,
        sub_total=Decimal('1915.04'),
        supplemental_data=shared.SupplementalData(
            content={
                'key': {
                    'key': 'string',
                },
            },
        ),
        total_amount=Decimal('5893.9'),
        total_discount=Decimal('579.23'),
        total_tax_amount=Decimal('3881.42'),
        withholding_tax=[
            shared.WithholdingTaxItems(
                amount=Decimal('7369.44'),
                name='string',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.accounting_credit_notes.create_accounting_credit_note(req)

if res.accounting_create_credit_note_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreateAccountingCreditNoteRequest](../../models/operations/createaccountingcreditnoterequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |


### Response

**[operations.CreateAccountingCreditNoteResponse](../../models/operations/createaccountingcreditnoteresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 400-600                         | */*                             |
