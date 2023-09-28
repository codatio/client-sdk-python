# LoanWritebackDirectCosts
(*loan_writeback.direct_costs*)

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
            id='502a94bb-4f63-4c96-9e9a-3efa77dfb14c',
        ),
        currency='EUR',
        currency_rate=Decimal('4118.2'),
        id='6ae395ef-b9ba-488f-ba66-997074ba4469',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='6e214195-9890-4afa-963e-2516fe4c8b71',
                    name='Elvira Herman',
                ),
                description='repellat',
                discount_amount=Decimal('8411.4'),
                discount_percentage=Decimal('1494.48'),
                item_ref=shared.ItemRef(
                    id='ed028921-cddc-4692-a01f-b576b0d5f0d3',
                    name='Erma Hessel',
                ),
                quantity=Decimal('7499.99'),
                sub_total=Decimal('1716.29'),
                tax_amount=Decimal('3394.04'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('5210.37'),
                    id='7053202c-73d5-4fe9-b90c-28909b3fe49a',
                    name='Ervin McLaughlin',
                ),
                total_amount=Decimal('9644.9'),
                tracking=shared.Tracking(
                    invoice_to=shared.RecordRef(
                        data_type='invoice',
                        id='8633323f-9b77-4f3a-8100-674ebf69280d',
                    ),
                    record_refs=[
                        shared.RecordRef(
                            data_type='journalEntry',
                            id='ba77a89e-bf73-47ae-8203-ce5e6a95d8a0',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='d446ce2a-f7a7-43cf-bbe4-53f870b326b5',
                        name='Darryl Emard',
                    ),
                ],
                unit_amount=Decimal('5867.84'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='pariatur',
        payment_allocations=[
            shared.AccountingPaymentAllocation(
                allocation=shared.AccountingPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=Decimal('6748.48'),
                    total_amount=Decimal('5173.79'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='422bb679-d232-4271-9bf0-cbb1e31b8b90',
                        name='Mike Greenholt',
                    ),
                    currency='EUR',
                    currency_rate=Decimal('1002.94'),
                    id='108e0adc-f4b9-4218-b9fc-e953f73ef7fb',
                    note='quod',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='similique',
                    total_amount=Decimal('7085.48'),
                ),
            ),
        ],
        reference='vero',
        source_modified_date='2022-10-23T00:00:00.000Z',
        sub_total=Decimal('2930.2'),
        supplemental_data=shared.SupplementalData(
            content={
                "quibusdam": {
                    "illum": 'sequi',
                },
            },
        ),
        tax_amount=Decimal('6178.77'),
        total_amount=Decimal('7733.26'),
    ),
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=13236,
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

