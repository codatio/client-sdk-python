# AccountingDirectIncomes
(*accounting_direct_incomes*)

## Overview

Direct incomes

### Available Operations

* [create_accounting_direct_income](#create_accounting_direct_income) - Create direct income

## create_accounting_direct_income

The *Create direct income* endpoint creates a new [direct income](https://docs.codat.io/accounting-api#/schemas/DirectIncome) for a given company's connection.

[Direct incomes](https://docs.codat.io/accounting-api#/schemas/DirectIncome) are sales of items directly to a customer where payment is received at the point of the sale. For example, cash sales of items to a customer, referral commissions, and service fee refunds are considered direct incomes.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create direct income model](https://docs.codat.io/accounting-api#/operations/get-create-directIncomes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating an account.


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

req = operations.CreateAccountingDirectIncomeRequest(
    accounting_direct_income=shared.AccountingDirectIncome(
        contact_ref=shared.AccountingDirectIncomeContactRef(
            data_type=shared.DataType.INVOICES,
            id='<ID>',
        ),
        currency='GBP',
        currency_rate=Decimal('6548.38'),
        id='<ID>',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='<ID>',
                    name='Meitnerium watt Assistant',
                ),
                description='Organized directional moratorium',
                discount_amount=Decimal('6259.31'),
                discount_percentage=Decimal('3251.14'),
                item_ref=shared.DirectIncomeLineItemItemReference(
                    id='<ID>',
                    name='Supervisor virtual sadly',
                ),
                quantity=Decimal('7605.88'),
                sub_total=Decimal('2695.32'),
                tax_amount=Decimal('3396.83'),
                tax_rate_ref=shared.DirectIncomeLineItemTaxRateReference(
                    effective_tax_rate=Decimal('2606.73'),
                    id='<ID>',
                    name='Pensacola Som Northwest',
                ),
                total_amount=Decimal('6880.22'),
                tracking_category_refs=[
                    shared.DirectIncomeLineItemTrackingCategoryRefs(
                        id='<ID>',
                        name='Pickup',
                    ),
                ],
                unit_amount=Decimal('8819.46'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='magni',
        payment_allocations=[
            shared.PaymentAllocationsitems(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=Decimal('2449.75'),
                    total_amount=Decimal('6540.35'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='<ID>',
                        name='Officer mobile Infrastructure',
                    ),
                    currency='EUR',
                    currency_rate=Decimal('4022.79'),
                    id='<ID>',
                    note='Tools Dynamic Industrial',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='parallelism',
                    total_amount=Decimal('9002.17'),
                ),
            ),
        ],
        reference='Man Cotton virtual',
        source_modified_date='2022-10-23T00:00:00.000Z',
        sub_total=Decimal('4300.87'),
        supplemental_data=shared.SupplementalData(
            content={
                "eos": {
                    "facere": 'TLS',
                },
            },
        ),
        tax_amount=Decimal('356.06'),
        total_amount=Decimal('9132.9'),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=156594,
)

res = s.accounting_direct_incomes.create_accounting_direct_income(req)

if res.accounting_create_direct_income_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.CreateAccountingDirectIncomeRequest](../../models/operations/createaccountingdirectincomerequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |


### Response

**[operations.CreateAccountingDirectIncomeResponse](../../models/operations/createaccountingdirectincomeresponse.md)**

