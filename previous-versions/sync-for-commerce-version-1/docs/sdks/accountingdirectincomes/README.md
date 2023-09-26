# AccountingDirectIncomes

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
            id='5fce6c55-6146-4c3e-a50f-b008c42e141a',
        ),
        currency='EUR',
        currency_rate=Decimal('8104.24'),
        id='366c8dd6-b144-4290-b474-778a7bd466d2',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='c10ab3cd-ca42-4519-84e5-23c7e0bc7178',
                    name='Tom Kuhn',
                ),
                description='sapiente',
                discount_amount=Decimal('1741.12'),
                discount_percentage=Decimal('6455.7'),
                item_ref=shared.DirectIncomeLineItemItemReference(
                    id='70c68828-2aa4-4825-a2f2-22e9817ee17c',
                    name='Dr. Ignacio Jacobi',
                ),
                quantity=Decimal('6900.25'),
                sub_total=Decimal('4732.21'),
                tax_amount=Decimal('6996.22'),
                tax_rate_ref=shared.DirectIncomeLineItemTaxRateReference(
                    effective_tax_rate=Decimal('5801.97'),
                    id='5bc0ab3c-20c4-4f37-89fd-871f99dd2efd',
                    name='Marilyn Botsford',
                ),
                total_amount=Decimal('3984.34'),
                tracking_category_refs=[
                    shared.DirectIncomeLineItemTrackingCategoryRefs(
                        id='f1e674bd-b04f-4157-9608-2d68ea19f1d1',
                        name='Mrs. Cynthia Hansen',
                    ),
                ],
                unit_amount=Decimal('6144.65'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='accusantium',
        payment_allocations=[
            shared.PaymentAllocationsitems(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=Decimal('5130.75'),
                    total_amount=Decimal('4287.96'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='a1840394-c260-471f-93f5-f0642dac7af5',
                        name='Darlene Sawayn',
                    ),
                    currency='GBP',
                    currency_rate=Decimal('2414.18'),
                    id='aa63aae8-d678-464d-bb67-5fd5e60b375e',
                    note='facere',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='doloribus',
                    total_amount=Decimal('3817.6'),
                ),
            ),
        ],
        reference='reiciendis',
        source_modified_date='2022-10-23T00:00:00.000Z',
        sub_total=Decimal('9049.49'),
        supplemental_data=shared.SupplementalData(
            content={
                "necessitatibus": {
                    "dolore": 'sunt',
                },
            },
        ),
        tax_amount=Decimal('9920.12'),
        total_amount=Decimal('2415.45'),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=249420,
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

