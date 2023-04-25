# direct_incomes

## Overview

Direct incomes

### Available Operations

* [create_direct_income](#create_direct_income) - Create direct income
* [download_direct_income_attachment](#download_direct_income_attachment) - Download direct income attachment
* [get_create_direct_incomes_model](#get_create_direct_incomes_model) - Get create direct income model
* [get_direct_income](#get_direct_income) - Get direct income
* [get_direct_income_attachment](#get_direct_income_attachment) - Get direct income attachment
* [get_direct_incomes](#get_direct_incomes) - Get direct incomes
* [list_direct_income_attachments](#list_direct_income_attachments) - List direct income attachments
* [upload_direct_income_attachment](#upload_direct_income_attachment) - Create direct income attachment

## create_direct_income

Posts a new direct income to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create direct income model](https://docs.codat.io/accounting-api#/operations/get-create-directIncomes-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating direct incomes.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateDirectIncomeRequest(
    direct_income=shared.DirectIncome(
        contact_ref=shared.ContactRef(
            data_type="rem",
            id="f652ebb9-d383-4838-b902-43b293dab30e",
        ),
        currency="excepturi",
        currency_rate=1194.72,
        id="7f50fda0-4c8b-41bb-95a2-92b0bc3bb744",
        issue_date="laboriosam",
        line_items=[
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id="4eb1d033-88b0-4d1b-b17a-fee74b6feb94",
                    name="Colleen Schmidt",
                ),
                description="illum",
                discount_amount=6734.93,
                discount_percentage=9682.72,
                item_ref=shared.ItemRef(
                    id="39d16fbf-76fd-4162-b303-e3023b93e343",
                    name="Jeanne Schowalter",
                ),
                quantity=3667.8,
                sub_total=7436.12,
                tax_amount=2976.24,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1923.84,
                    id="13553ccf-1c20-44c4-adcc-9904c5195b86",
                    name="Irma Rowe",
                ),
                total_amount=6497.91,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="8f1e2d3b-901e-4095-abbb-4cbb19f713d9",
                        name="Mrs. Kristi Greenholt",
                    ),
                    shared.TrackingCategoryRef(
                        id="c1387271-e18e-4a9e-8511-8c2cc57fbd60",
                        name="Jack Paucek",
                    ),
                ],
                unit_amount=9102.97,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id="d29a9d4e-ea85-4658-82d4-f4c88be4f278",
                    name="Laurence Mitchell",
                ),
                description="molestiae",
                discount_amount=8828.26,
                discount_percentage=2892.08,
                item_ref=shared.ItemRef(
                    id="6c51d2ff-aa58-4dce-b234-c955b9bdf219",
                    name="Alberta Rogahn",
                ),
                quantity=7129.08,
                sub_total=6908.74,
                tax_amount=7889.95,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7535.25,
                    id="2725ec26-59ce-4028-8840-c69ef68e45c8",
                    name="Taylor Schuster",
                ),
                total_amount=7591.92,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="54500430-c663-42b4-b91f-df01c3e91e8f",
                        name="Jeannette Schmeler",
                    ),
                    shared.TrackingCategoryRef(
                        id="d460a77e-ceb2-46d1-8f1e-f2631c7c0f0f",
                        name="Allan Ebert",
                    ),
                ],
                unit_amount=8159.77,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="veniam",
        note="eligendi",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="nemo",
                    currency="doloribus",
                    currency_rate=8503.86,
                    total_amount=2499.41,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="e0b4a4a4-253c-4302-9711-f42c7e7dc548",
                        name="Bradford Balistreri",
                    ),
                    currency="numquam",
                    currency_rate=989.55,
                    id="a7a215ca-12a4-4ba9-9599-88192cfd0c77",
                    note="eligendi",
                    paid_on_date="ullam",
                    reference="dolorem",
                    total_amount=8782.82,
                ),
            ),
        ],
        reference="esse",
        source_modified_date="vero",
        sub_total=4930.61,
        supplemental_data=shared.SupplementalData(
            content={
                "eius": {
                    "vero": "nisi",
                    "recusandae": "deleniti",
                    "nobis": "excepturi",
                    "consequatur": "distinctio",
                },
                "similique": {
                    "consectetur": "molestias",
                    "modi": "saepe",
                    "qui": "dolor",
                    "sint": "ea",
                },
                "in": {
                    "sequi": "maiores",
                },
                "itaque": {
                    "adipisci": "sunt",
                    "quo": "veniam",
                    "sit": "deleniti",
                    "qui": "dolore",
                },
            },
        ),
        tax_amount=8188.66,
        total_amount=1179.02,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=536427,
)

res = s.direct_incomes.create_direct_income(req)

if res.create_direct_income_response is not None:
    # handle response
```

## download_direct_income_attachment

Downloads an attachment for the specified direct income for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadDirectIncomeAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    direct_income_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.direct_incomes.download_direct_income_attachment(req)

if res.data is not None:
    # handle response
```

## get_create_direct_incomes_model

Get create direct income model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating direct incomes.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateDirectIncomesModelRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.direct_incomes.get_create_direct_incomes_model(req)

if res.push_option is not None:
    # handle response
```

## get_direct_income

Gets the specified direct income for a given company and connection.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDirectIncomeRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    direct_income_id="perspiciatis",
)

res = s.direct_incomes.get_direct_income(req)

if res.direct_income is not None:
    # handle response
```

## get_direct_income_attachment

Gets the specified direct income attachment for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDirectIncomeAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    direct_income_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    timeout_in_minutes=646108,
)

res = s.direct_incomes.get_direct_income_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_direct_incomes

Gets the direct incomes for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDirectIncomesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="dolor",
)

res = s.direct_incomes.get_direct_incomes(req)

if res.direct_incomes is not None:
    # handle response
```

## list_direct_income_attachments

Gets all attachments for the specified direct income for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListDirectIncomeAttachmentsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    direct_income_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.direct_incomes.list_direct_income_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## upload_direct_income_attachment

Posts a new direct income attachment for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UploadDirectIncomeAttachmentRequest(
    request_body=operations.UploadDirectIncomeAttachmentRequestBody(
        content="eum".encode(),
        request_body="culpa",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    direct_income_id="iure",
)

res = s.direct_incomes.upload_direct_income_attachment(req)

if res.status_code == 200:
    # handle response
```
