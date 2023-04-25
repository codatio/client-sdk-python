# direct_costs

## Overview

Direct costs

### Available Operations

* [create_direct_cost](#create_direct_cost) - Create direct cost
* [download_direct_cost_attachment](#download_direct_cost_attachment) - Download direct cost attachment
* [get_create_direct_costs_model](#get_create_direct_costs_model) - Get create direct cost model
* [get_direct_cost](#get_direct_cost) - Get direct cost
* [get_direct_cost_attachment](#get_direct_cost_attachment) - Get direct cost attachment
* [get_direct_costs](#get_direct_costs) - List direct costs
* [list_direct_cost_attachments](#list_direct_cost_attachments) - List direct cost attachments
* [upload_direct_cost_attachment](#upload_direct_cost_attachment) - Upload direct cost attachment

## create_direct_cost

Posts a new direct cost to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create direct cost model](https://docs.codat.io/accounting-api#/operations/get-create-directCosts-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support creating direct costs.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateDirectCostRequest(
    direct_cost=shared.DirectCost(
        contact_ref=shared.ContactRef(
            data_type="sed",
            id="de35f8e0-1bf3-43ea-ab45-402ac1704bf1",
        ),
        currency="maxime",
        currency_rate=8111.67,
        id="9fc61aae-5eb5-4f0c-892b-5744d08a2267",
        issue_date="est",
        line_items=[
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id="ee79e3c7-1ad3-41be-8b83-d2378ae3bfc2",
                    name="Christie Marquardt",
                ),
                description="aperiam",
                discount_amount=6589.17,
                discount_percentage=6038.63,
                item_ref=shared.ItemRef(
                    id="86a495ba-c707-4f06-b28e-cc86492386f6",
                    name="Lynne Miller",
                ),
                quantity=7548.72,
                sub_total=2765.07,
                tax_amount=7900.8,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7977.92,
                    id="6b78890a-3fd3-4c81-9a10-f8c23df931da",
                    name="Henrietta Schuppe",
                ),
                total_amount=1152.02,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingInvoiceTo(
                        data_type="repellat",
                        id="ad94acc9-4351-4377-a6d1-5321b832a56d",
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type="sint",
                            id="180ff60e-b9a6-4658-a69a-4b843d382dbe",
                        ),
                        shared.InvoiceTo(
                            data_type="porro",
                            id="75c68c60-6594-468c-a304-d8849bf8214c",
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="37f96bb0-c69e-4372-9b13-44ba9f78a5c0",
                        name="Bryant Kiehn",
                    ),
                ],
                unit_amount=7429.37,
            ),
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id="62e97261-fb0c-458d-a7b5-1996b5b4b50e",
                    name="Mr. Darrin Kub",
                ),
                description="ducimus",
                discount_amount=6577.63,
                discount_percentage=4967.86,
                item_ref=shared.ItemRef(
                    id="ab0344b1-7106-488d-aebe-f897f3dd0ccd",
                    name="Mr. Cindy White",
                ),
                quantity=2054.73,
                sub_total=9131.52,
                tax_amount=3033.65,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9165.77,
                    id="080aa104-186e-4c75-9e02-f3702c5c8e2d",
                    name="Barbara Von",
                ),
                total_amount=2133.99,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingInvoiceTo(
                        data_type="sunt",
                        id="04fa4470-7bf3-475b-8428-2821fdb2f69e",
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type="unde",
                            id="267c71cc-8d3c-4d42-98d0-358a82c808fe",
                        ),
                        shared.InvoiceTo(
                            data_type="odit",
                            id="751a2047-c044-49e1-83f9-619bb7d40d5a",
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="1fa436e6-2592-433f-95c9-d237397c785b",
                        name="Betsy Reynolds",
                    ),
                ],
                unit_amount=3401.67,
            ),
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id="00183feb-df67-46b7-a06d-ab750052a564",
                    name="Gretchen Steuber",
                ),
                description="sequi",
                discount_amount=6159.32,
                discount_percentage=9053.57,
                item_ref=shared.ItemRef(
                    id="d8c4320f-4124-40d4-887a-c693b94c3b9d",
                    name="Esther Lind",
                ),
                quantity=4884.37,
                sub_total=6008.1,
                tax_amount=3215.82,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6383.23,
                    id="a42fc405-669f-469a-806d-21249450819d",
                    name="Krista Emard MD",
                ),
                total_amount=3003.75,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingInvoiceTo(
                        data_type="illo",
                        id="844060e0-0310-4d02-bdc9-01f5afd2a6c4",
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type="praesentium",
                            id="46ae9d89-253c-4896-af48-96bf51e4652d",
                        ),
                        shared.InvoiceTo(
                            data_type="dolorem",
                            id="c343d617-78af-4491-a477-25e621909e91",
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="44a5de59-ac77-4066-b0cf-1cf593260525",
                        name="Elvira Jacobson",
                    ),
                ],
                unit_amount=7414,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="non",
        note="quia",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="deleniti",
                    currency="molestias",
                    currency_rate=4937.34,
                    total_amount=8134.63,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="99a2d335-670e-493e-a6cf-59f358aaeaca",
                        name="Philip Crooks",
                    ),
                    currency="adipisci",
                    currency_rate=799.07,
                    id="bf7ba1cc-9771-46c8-82cc-9e0c7d9d323f",
                    note="quae",
                    paid_on_date="animi",
                    reference="est",
                    total_amount=4209.27,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="sequi",
                    currency="officiis",
                    currency_rate=8610.9,
                    total_amount=5823.51,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="cf1c856b-cba5-41ef-a454-a47facf116cd",
                        name="Jorge Grady",
                    ),
                    currency="officia",
                    currency_rate=4413.58,
                    id="562873c7-dd9e-4faf-83dc-623620f3138f",
                    note="nesciunt",
                    paid_on_date="doloremque",
                    reference="at",
                    total_amount=9458.52,
                ),
            ),
        ],
        reference="sequi",
        source_modified_date="temporibus",
        sub_total=7364.8,
        supplemental_data=shared.SupplementalData(
            content={
                "magni": {
                    "earum": "similique",
                },
            },
        ),
        tax_amount=6633.25,
        total_amount=3507.98,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=415121,
)

res = s.direct_costs.create_direct_cost(req)

if res.create_direct_cost_response is not None:
    # handle response
```

## download_direct_cost_attachment

Downloads an attachment for the specified direct cost for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadDirectCostAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    direct_cost_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.direct_costs.download_direct_cost_attachment(req)

if res.data is not None:
    # handle response
```

## get_create_direct_costs_model

Get create direct cost model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support creating direct costs.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateDirectCostsModelRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.direct_costs.get_create_direct_costs_model(req)

if res.push_option is not None:
    # handle response
```

## get_direct_cost

Gets the specified direct cost for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDirectCostRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    direct_cost_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.direct_costs.get_direct_cost(req)

if res.direct_cost is not None:
    # handle response
```

## get_direct_cost_attachment

Gets the specified direct cost attachment for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDirectCostAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    direct_cost_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.direct_costs.get_direct_cost_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_direct_costs

Gets the direct costs for the company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDirectCostsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="nostrum",
)

res = s.direct_costs.get_direct_costs(req)

if res.direct_costs is not None:
    # handle response
```

## list_direct_cost_attachments

Gets all attachments for the specified direct cost for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListDirectCostAttachmentsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    direct_cost_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.direct_costs.list_direct_cost_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## upload_direct_cost_attachment

Posts a new direct cost attachment for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UploadDirectCostAttachmentRequest(
    request_body=operations.UploadDirectCostAttachmentRequestBody(
        content="delectus".encode(),
        request_body="quidem",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    direct_cost_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.direct_costs.upload_direct_cost_attachment(req)

if res.status_code == 200:
    # handle response
```
