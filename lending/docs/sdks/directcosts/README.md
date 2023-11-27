# DirectCosts
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
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_prototype=shared.DirectCostPrototype(
        contact_ref=shared.DirectCostPrototypeContactRef(
            data_type=shared.DataType.INVOICES,
            id='<ID>',
        ),
        currency='USD',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(),
                item_ref=shared.PropertieItemRef(
                    id='<ID>',
                ),
                quantity=Decimal('6384.24'),
                tax_rate_ref=shared.TaxRateRef(),
                tracking=shared.Tracking(
                    invoice_to=shared.RecordRef(
                        data_type='transfer',
                    ),
                    record_refs=[
                        shared.RecordRef(
                            data_type='invoice',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='<ID>',
                    ),
                ],
                unit_amount=Decimal('2884.08'),
            ),
        ],
        payment_allocations=[
            shared.AccountingPaymentAllocation(
                allocation=shared.Allocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(),
                    currency='GBP',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                ),
            ),
        ],
        sub_total=Decimal('7964.74'),
        supplemental_data=shared.SupplementalData(
            content={
                "key": {
                    "key": 'string',
                },
            },
        ),
        tax_amount=Decimal('3768.44'),
        total_amount=Decimal('9510.62'),
    ),
)

res = s.loan_writeback.direct_costs.create(req)

if res.accounting_create_direct_cost_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateDirectCostRequest](../../models/operations/createdirectcostrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.CreateDirectCostResponse](../../models/operations/createdirectcostresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 400-600                         | */*                             |

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
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCreateDirectCostsModelRequest](../../models/operations/getcreatedirectcostsmodelrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.GetCreateDirectCostsModelResponse](../../models/operations/getcreatedirectcostsmodelresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 400-600                     | */*                         |
