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
            data_type='tempora',
            id='5626d436-813f-416d-9f5f-ce6c556146c3',
        ),
        currency='EUR',
        currency_rate=1324.87,
        id='50fb008c-42e1-441a-ac36-6c8dd6b14429',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='7474778a-7bd4-466d-a8c1-0ab3cdca4251',
                    name='William Goodwin',
                ),
                description='aspernatur',
                discount_amount=1970.54,
                discount_percentage=7791.92,
                item_ref=shared.DirectIncomeLineItemItemReference(
                    id='7e0bc717-8e47-496f-aa70-c688282aa482',
                    name='Sue Corkery',
                ),
                quantity=1871.31,
                sub_total=1294.12,
                tax_amount=9039.84,
                tax_rate_ref=shared.DirectIncomeLineItemTaxRateReference(
                    effective_tax_rate=5789.22,
                    id='817ee17c-be61-4e6b-bb95-bc0ab3c20c4f',
                    name='Joy Labadie',
                ),
                total_amount=8577.23,
                tracking_category_refs=[
                    shared.DirectIncomeLineItemTrackingCategoryRefs(
                        id='871f99dd-2efd-4121-aa6f-1e674bdb04f1',
                        name='Delores Hermiston IV',
                    ),
                ],
                unit_amount=1852.32,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='ex',
        payment_allocations=[
            shared.PaymentAllocationsitems(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=6802.7,
                    total_amount=996.15,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='9f1d1705-1339-4d08-886a-1840394c2607',
                        name='Elisa Mosciski',
                    ),
                    currency='USD',
                    currency_rate=9903.45,
                    id='0642dac7-af51-45cc-813a-a63aae8d6786',
                    note='labore',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='facilis',
                    total_amount=7382.27,
                ),
            ),
        ],
        reference='commodi',
        source_modified_date='2022-10-23T00:00:00.000Z',
        sub_total=3605.45,
        supplemental_data=shared.SupplementalData(
            content={
                "reiciendis": {
                    "assumenda": 'nemo',
                },
            },
        ),
        tax_amount=9249.67,
        total_amount=3975.33,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=46007,
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

