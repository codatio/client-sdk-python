# LoanWriteback.DirectCosts

### Available Operations

* [create](#create) - Create direct cost
* [get_create_model](#get_create_model) - Get create direct cost model

## create

The *Create direct cost* endpoint creates a new [direct cost](https://docs.codat.io/accounting-api#/schemas/DirectCost) for a given company's connection.

[Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) are the expenses associated with a business' operations. For example, purchases of raw materials that are paid off at the point of the purchase and service fees are considered direct costs.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create direct cost model](https://docs.codat.io/accounting-api#/operations/get-create-directCosts-model).

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
            data_type='magni',
            id='d502a94b-b4f6-43c9-a9e9-a3efa77dfb14',
        ),
        currency='EUR',
        currency_rate=Decimal('8137.98'),
        id='66ae395e-fb9b-4a88-b3a6-6997074ba446',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='b6e21419-5989-40af-a563-e2516fe4c8b7',
                    name='Diane VonRueden',
                ),
                description='nihil',
                discount_amount=Decimal('9988.48'),
                discount_percentage=Decimal('8411.4'),
                item_ref=shared.ItemRef(
                    id='2ed02892-1cdd-4c69-a601-fb576b0d5f0d',
                    name='Jennifer Runolfsdottir',
                ),
                quantity=Decimal('7299.91'),
                sub_total=Decimal('7499.99'),
                tax_amount=Decimal('1716.29'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('3394.04'),
                    id='87053202-c73d-45fe-9b90-c28909b3fe49',
                    name='Casey Stracke',
                ),
                total_amount=Decimal('7301.22'),
                tracking=shared.Tracking(
                    invoice_to=shared.RecordRef(
                        data_type='transfer',
                        id='48633323-f9b7-47f3-a410-0674ebf69280',
                    ),
                    record_refs=[
                        shared.RecordRef(
                            data_type='transfer',
                            id='1ba77a89-ebf7-437a-a420-3ce5e6a95d8a',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='0d446ce2-af7a-473c-b3be-453f870b326b',
                        name='Joanna Kohler',
                    ),
                ],
                unit_amount=Decimal('1864.58'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='maxime',
        payment_allocations=[
            shared.AccountingPaymentAllocation(
                allocation=shared.AccountingPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=Decimal('1175.31'),
                    total_amount=Decimal('6748.48'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='8422bb67-9d23-4227-95bf-0cbb1e31b8b9',
                        name='Dixie Durgan',
                    ),
                    currency='GBP',
                    currency_rate=Decimal('6772.63'),
                    id='1108e0ad-cf4b-4921-879f-ce953f73ef7f',
                    note='distinctio',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='odio',
                    total_amount=Decimal('6304.48'),
                ),
            ),
        ],
        reference='facilis',
        source_modified_date='2022-10-23T00:00:00.000Z',
        sub_total=Decimal('4981.4'),
        supplemental_data=shared.SupplementalData(
            content={
                "dolore": {
                    "quibusdam": 'illum',
                },
            },
        ),
        tax_amount=Decimal('1943.42'),
        total_amount=Decimal('6178.77'),
    ),
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=773326,
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

The *Get create direct cost model* endpoint returns the expected data for the request payload when creating a [direct cost](https://docs.codat.io/accounting-api#/schemas/DirectCost) for a given company and integration.

[Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) are purchases of items that are paid off at the point of the purchase.

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

