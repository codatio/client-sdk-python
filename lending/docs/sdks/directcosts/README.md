# LoanWriteback.DirectCosts

## Overview

### Available Operations

* [create](#create) - Create direct cost
* [get_create_model](#get_create_model) - Get create direct cost model

## create

The *Create direct cost* endpoint creates a new [direct cost](https://docs.codat.io/lending-api#/schemas/DirectCost) for a given company's connection.

[Direct costs](https://docs.codat.io/lending-api#/schemas/DirectCost) are business expenses that don't impact Accounts Payable.

**Integration-specific behavior**

Required data may vary by integration. To see what data to post, first call [Get create direct cost model](https://docs.codat.io/lending-api#/operations/get-create-directCosts-model).

### Example Usage

<!-- UsageSnippet language="python" operationID="create-direct-cost" method="post" path="/companies/{companyId}/connections/{connectionId}/push/directCosts" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared
from decimal import Decimal


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.direct_costs.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "direct_cost_prototype": {
            "contact_ref": {
                "data_type": shared.ContactRefDataType.SUPPLIERS,
                "id": "80000001-1671793885",
            },
            "currency": "USD",
            "issue_date": "2023-03-21T10:19:52.223Z",
            "line_items": [
                {
                    "account_ref": {
                        "id": "8000000D-1671793811",
                        "name": "Purchases - Hardware for Resale",
                    },
                    "description": "test description line 1",
                    "discount_amount": Decimal("0"),
                    "discount_percentage": Decimal("0"),
                    "item_ref": {
                        "id": "80000001-1674566705",
                        "name": "item test",
                    },
                    "quantity": Decimal("1"),
                    "sub_total": Decimal("99"),
                    "tax_amount": Decimal("360"),
                    "total_amount": Decimal("70"),
                    "tracking_category_refs": [
                        {
                            "id": "80000001-1674553252",
                            "name": "Class 1",
                        },
                    ],
                    "unit_amount": Decimal("7"),
                },
            ],
            "note": "directCost 21/03 09.20",
            "payment_allocations": [
                {
                    "allocation": {
                        "allocated_on_date": "2023-01-29T10:19:52.223Z",
                        "currency_rate": Decimal("0"),
                        "total_amount": Decimal("88"),
                    },
                    "payment": {
                        "account_ref": {
                            "id": "80000028-1671794219",
                            "name": "Bank Account 1",
                        },
                        "note": "payment allocations note",
                        "paid_on_date": "2023-01-28T10:19:52.223Z",
                        "reference": "payment allocations reference",
                        "total_amount": Decimal("54"),
                    },
                },
            ],
            "reference": "test ref",
            "sub_total": Decimal("362"),
            "tax_amount": Decimal("4"),
            "total_amount": Decimal("366"),
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateDirectCostRequest](../../models/operations/createdirectcostrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[shared.AccountingCreateDirectCostResponse](../../models/shared/accountingcreatedirectcostresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_create_model

The *Get create direct cost model* endpoint returns the expected data for the request payload when creating a [direct cost](https://docs.codat.io/lending-api#/schemas/DirectCost) for a given company and integration.

[Direct costs](https://docs.codat.io/lending-api#/schemas/DirectCost) are business expenses that don't impact Accounts Payable.

**Integration-specific behavior**

See the *response examples* for integration-specific indicative models.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-create-directCosts-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/directCosts" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.direct_costs.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCreateDirectCostsModelRequest](../../models/operations/getcreatedirectcostsmodelrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[shared.PushOption](../../models/shared/pushoption.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |