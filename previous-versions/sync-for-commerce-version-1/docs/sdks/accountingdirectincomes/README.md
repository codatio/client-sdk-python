# accounting_direct_incomes

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

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountingDirectIncomeRequest(
    accounting_direct_income=shared.AccountingDirectIncome(
        contact_ref=shared.AccountingDirectIncomeContactRef(
            data_type='nisi',
            id='f48b656b-cdb3-45ff-ae4b-27537a8cd9e7',
        ),
        currency='GBP',
        currency_rate=1180.41,
        id='9c177d52-5f77-4b11-8eeb-52ff785fc378',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='d4c98e0c-2bb8-49eb-b5da-d636c600503d',
                    name='Willis Rippin Sr.',
                ),
                description='laudantium',
                discount_amount=407.1,
                discount_percentage=9384.12,
                item_ref=shared.DirectIncomeLineItemItemReference(
                    id='739ae9e0-57eb-4809-a281-0331f3981d4c',
                    name='Donna Aufderhar',
                ),
                quantity=467.91,
                sub_total=4894.59,
                tax_amount=9980.26,
                tax_rate_ref=shared.DirectIncomeLineItemTaxRateReference(
                    effective_tax_rate=2436.78,
                    id='c93c73b9-da3f-42ce-9a7e-23f2257411fa',
                    name='Kyle Reichel',
                ),
                total_amount=2883,
                tracking_category_refs=[
                    shared.DirectIncomeLineItemTrackingCategoryRefs(
                        id='e472e802-857a-45b4-8463-a7d575f1400e',
                        name='Gertrude Gerhold',
                    ),
                    shared.DirectIncomeLineItemTrackingCategoryRefs(
                        id='7334ec1b-781b-436a-8808-8d100efada20',
                        name='Mrs. Olive Weissnat',
                    ),
                ],
                unit_amount=1858.97,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='eb2164cf-9ab8-4366-8723-ffda9e06bee4',
                    name='Howard Hermann DVM',
                ),
                description='eligendi',
                discount_amount=620.35,
                discount_percentage=8850.22,
                item_ref=shared.DirectIncomeLineItemItemReference(
                    id='115c80bf-f918-4544-ac42-defcce8f1977',
                    name='Lydia Douglas',
                ),
                quantity=2086.83,
                sub_total=3577.58,
                tax_amount=3753.5,
                tax_rate_ref=shared.DirectIncomeLineItemTaxRateReference(
                    effective_tax_rate=1636.84,
                    id='a7b408f0-5e3d-448f-9af3-13a1f5fd9425',
                    name='Lucas Abbott',
                ),
                total_amount=4124.33,
                tracking_category_refs=[
                    shared.DirectIncomeLineItemTrackingCategoryRefs(
                        id='25ea944f-3b75-46c1-9f6c-37a512624383',
                        name='Kristy Quigley II',
                    ),
                    shared.DirectIncomeLineItemTrackingCategoryRefs(
                        id='a23a45ce-fc5f-4de1-8a0c-e2169e510019',
                        name='Elmer Spinka',
                    ),
                    shared.DirectIncomeLineItemTrackingCategoryRefs(
                        id='e3476279-9bfb-4be6-949f-b2bb4ecae6c3',
                        name='Maurice Stanton',
                    ),
                    shared.DirectIncomeLineItemTrackingCategoryRefs(
                        id='adebd5da-ea4c-4506-a8aa-94c02644cf5e',
                        name='Drew Mraz',
                    ),
                ],
                unit_amount=3442.89,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='corrupti',
        payment_allocations=[
            shared.PaymentAllocationsitems(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=986.1,
                    total_amount=6472.18,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='c600dec0-01ac-4802-a2ec-09ff8f0f816f',
                        name='Lee Gibson',
                    ),
                    currency='EUR',
                    currency_rate=946.97,
                    id='3e902c14-125b-4096-8a66-8151a472af92',
                    note='nesciunt',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='quis',
                    total_amount=5861.08,
                ),
            ),
            shared.PaymentAllocationsitems(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=9804.1,
                    total_amount=5120.81,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='3f350cf8-76ff-4b90-9c6e-cbb4e243cf78',
                        name='Jerald Wilkinson',
                    ),
                    currency='EUR',
                    currency_rate=8615.91,
                    id='a53e5ae6-e0ac-4184-82b9-c247c88373a4',
                    note='perferendis',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='architecto',
                    total_amount=5646.27,
                ),
            ),
            shared.PaymentAllocationsitems(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=9829.91,
                    total_amount=2050.11,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='2e550557-56f5-4d56-90bd-0af2dfe13db4',
                        name='Elmer Champlin',
                    ),
                    currency='EUR',
                    currency_rate=2425.31,
                    id='f8941aeb-c0b8-40a6-924d-3b2ecfcc8f89',
                    note='corporis',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='illo',
                    total_amount=142.51,
                ),
            ),
        ],
        reference='doloribus',
        source_modified_date='2022-10-23T00:00:00.000Z',
        sub_total=8698.48,
        supplemental_data=shared.SupplementalData(
            content={
                "neque": {
                    "vel": 'sapiente',
                    "mollitia": 'quae',
                    "quos": 'aperiam',
                    "non": 'voluptates',
                },
                "ad": {
                    "quisquam": 'quas',
                    "consequuntur": 'maiores',
                },
                "inventore": {
                    "laudantium": 'est',
                    "dolor": 'aliquid',
                },
                "consectetur": {
                    "rem": 'voluptatum',
                    "ducimus": 'adipisci',
                    "recusandae": 'tempora',
                    "blanditiis": 'numquam',
                },
            },
        ),
        tax_amount=1963.74,
        total_amount=5323.2,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=27078,
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

