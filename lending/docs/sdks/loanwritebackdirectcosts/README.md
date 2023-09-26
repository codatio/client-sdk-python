# LoanWriteback.DirectCosts

### Available Operations

* [create](#create) - Create direct cost
* [get_create_model](#get_create_model) - Get create direct cost model

## create

The *Create direct cost* endpoint creates a new [direct cost](https://docs.codat.io/lending-api#/schemas/DirectCost) for a given company's connection.

[Direct costs](https://docs.codat.io/lending-api#/schemas/DirectCost) are the expenses associated with a business' operations. For example, purchases of raw materials that are paid off at the point of the purchase and service fees are considered direct costs.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create direct cost model](https://docs.codat.io/lending-api#/operations/get-create-directCosts-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support creating an account.


### Example Usage

```python
import codatlending
from codatlending.models import operations, shared
from decimal import Decimal

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateDirectCostRequest(
    accounting_direct_cost=shared.AccountingDirectCost(
        contact_ref=shared.ContactRef(
            data_type=shared.DataType.INVOICES,
            id='02d502a9-4bb4-4f63-8969-e9a3efa77dfb',
        ),
        currency='GBP',
        currency_rate=Decimal('2974.37'),
        id='cd66ae39-5efb-49ba-88f3-a66997074ba4',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='69b6e214-1959-4890-afa5-63e2516fe4c8',
                    name='Dr. Arnold Bradtke',
                ),
                description='expedita',
                discount_amount=Decimal('4692.49'),
                discount_percentage=Decimal('9988.48'),
                item_ref=shared.ItemRef(
                    id='d2ed0289-21cd-4dc6-9260-1fb576b0d5f0',
                    name='Vincent Anderson',
                ),
                quantity=Decimal('9441.24'),
                sub_total=Decimal('7299.91'),
                tax_amount=Decimal('7499.99'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('1716.29'),
                    id='58705320-2c73-4d5f-a9b9-0c28909b3fe4',
                    name='Omar Leuschke',
                ),
                total_amount=Decimal('7508.44'),
                tracking=shared.Tracking(
                    invoice_to=shared.RecordRef(
                        data_type='accountTransaction',
                        id='f4863332-3f9b-477f-ba41-00674ebf6928',
                    ),
                    record_refs=[
                        shared.RecordRef(
                            data_type='journalEntry',
                            id='d1ba77a8-9ebf-4737-ae42-03ce5e6a95d8',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='a0d446ce-2af7-4a73-8f3b-e453f870b326',
                        name='Glen Oberbrunner',
                    ),
                ],
                unit_amount=Decimal('2776.28'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='cupiditate',
        payment_allocations=[
            shared.AccountingPaymentAllocation(
                allocation=shared.AccountingPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=Decimal('7470.8'),
                    total_amount=Decimal('1175.31'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='a8422bb6-79d2-4322-b15b-f0cbb1e31b8b',
                        name='Kevin Willms',
                    ),
                    currency='GBP',
                    currency_rate=Decimal('2408.29'),
                    id='a1108e0a-dcf4-4b92-9879-fce953f73ef7',
                    note='hic',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='quod',
                    total_amount=Decimal('4861.6'),
                ),
            ),
        ],
        reference='similique',
        source_modified_date='2022-10-23T00:00:00.000Z',
        sub_total=Decimal('8742.88'),
        supplemental_data=shared.SupplementalData(
            content={
                "ducimus": {
                    "dolore": 'quibusdam',
                },
            },
        ),
        tax_amount=Decimal('8489.44'),
        total_amount=Decimal('1943.42'),
    ),
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=617877,
)

res = s.loan_writeback.direct_costs.create(req)

if res.accounting_create_direct_cost_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateDirectCostRequest](../../models/operations/createdirectcostrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.CreateDirectCostResponse](../../models/operations/createdirectcostresponse.md)**


## get_create_model

The *Get create direct cost model* endpoint returns the expected data for the request payload when creating a [direct cost](https://docs.codat.io/lending-api#/schemas/DirectCost) for a given company and integration.

[Direct costs](https://docs.codat.io/lending-api#/schemas/DirectCost) are purchases of items that are paid off at the point of the purchase.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support creating a direct cost.


### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateDirectCostsModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.loan_writeback.direct_costs.get_create_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCreateDirectCostsModelRequest](../../models/operations/getcreatedirectcostsmodelrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.GetCreateDirectCostsModelResponse](../../models/operations/getcreatedirectcostsmodelresponse.md)**

