# bills

## Overview

Bills

### Available Operations

* [create](#create) - Create bill
* [delete](#delete) - Delete bill
* [download_attachment](#download_attachment) - Download bill attachment
* [get](#get) - Get bill
* [get_attachment](#get_attachment) - Get bill attachment
* [get_create_update_model](#get_create_update_model) - Get create/update bill model
* [list](#list) - List bills
* [list_attachments](#list_attachments) - List bill attachments
* [update](#update) - Update bill
* [upload_attachment](#upload_attachment) - Upload bill attachment

## create

Posts a new bill to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/accounting-api#/operations/get-create-update-bills-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating a bill.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateBillRequest(
    bill=shared.Bill(
        amount_due=7068.72,
        currency="non",
        currency_rate=6495.34,
        due_date="assumenda",
        id="ebd5daea-4c50-46a8-aa94-c02644cf5e9d",
        issue_date="error",
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id="4578adc1-ac60-40de-8001-ac802e2ec09f",
                    name="Dr. Armando Wunsch",
                ),
                description="dicta",
                discount_amount=3805.95,
                discount_percentage=9382.57,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id="f3477c13-e902-4c14-925b-0960a668151a",
                    name="Constance Dach",
                ),
                quantity=6095.37,
                sub_total=1512.3,
                tax_amount=2009.5,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8054.63,
                    id="5949f83f-350c-4f87-affb-901c6ecbb4e2",
                    name="Lillian Rosenbaum",
                ),
                total_amount=5000.21,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="ffafeda5-3e5a-4e6e-8ac1-84c2b9c247c8",
                            name="Allen Kozey",
                        ),
                        shared.TrackingCategoryRef(
                            id="40e1942f-32e5-4505-9756-f5d56d0bd0af",
                            name="Elena Zieme I",
                        ),
                        shared.TrackingCategoryRef(
                            id="db4f62cb-a3f8-4941-aebc-0b80a6924d3b",
                            name="Eloise Rowe",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="quo",
                        id="8f895010-f5dd-43d6-ba18-04e54c82f168",
                    ),
                    is_billed_to="Customer",
                    is_rebilled_to="Unknown",
                    project_ref=shared.ProjectRef(
                        id="63c8873e-4843-480b-9f6b-8ca275a60a04",
                        name="Jay Morar",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="699171b5-1c1b-4db1-8f4b-888ebdfc4ccc",
                        name="Marshall McClure",
                    ),
                    shared.TrackingCategoryRef(
                        id="7fc0b2dc-e108-473e-82b0-06d678878ba8",
                        name="Kay Bradtke",
                    ),
                    shared.TrackingCategoryRef(
                        id="8208c54f-efa9-4c95-b2ea-c5565d307cfe",
                        name="Hugh Carroll III",
                    ),
                    shared.TrackingCategoryRef(
                        id="e2813fa4-a41c-4480-93f2-132af03102d5",
                        name="Danielle Willms",
                    ),
                ],
                unit_amount=7505.37,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id="6f18bf96-21a6-4a4f-b7a8-7ee3e4be752c",
                    name="Beatrice Purdy",
                ),
                description="quaerat",
                discount_amount=1039.88,
                discount_percentage=5069.66,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id="e3bb91c8-d975-4e0e-8419-d8f84f144f3e",
                    name="Joy Toy",
                ),
                quantity=7690.47,
                sub_total=3028.78,
                tax_amount=6778.95,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6448.27,
                    id="5f3cabd9-05a9-472e-8567-28227b2d3094",
                    name="Sharon Raynor",
                ),
                total_amount=6671.69,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="fa87cf53-5a6f-4ae5-8ebf-60c321f023b7",
                            name="Paulette Dibbert",
                        ),
                        shared.TrackingCategoryRef(
                            id="7fe1a0cc-8df7-49f0-a396-d90c364b7c15",
                            name="Emilio Rau",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="accusamus",
                        id="188b1c4e-e2c8-4c6c-a611-feeb1c7cbdb6",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="c74378ba-2531-4774-bdc9-15ad2caf5dd6",
                        name="Judith Feest",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="f5ae2f3a-6b70-4087-8756-143f5a6c98b5",
                        name="Holly Harber V",
                    ),
                ],
                unit_amount=408.74,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id="d40bcacc-6cbd-46b5-b3ec-909304f926ba",
                    name="Wayne Hintz",
                ),
                description="voluptatum",
                discount_amount=987.59,
                discount_percentage=6225.66,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id="b474b0ed-20e5-4624-8fff-639a910abdca",
                    name="Edgar Corkery",
                ),
                quantity=3931.22,
                sub_total=3971.6,
                tax_amount=5897.12,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3857.6,
                    id="e1ec0022-1b33-45d8-9acb-3ecfda8d0c54",
                    name="Mrs. Hugo Wehner Jr.",
                ),
                total_amount=2737.32,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="78a61fa1-cf20-4688-b77c-1ffc71dca163",
                            name="Aaron O'Kon",
                        ),
                        shared.TrackingCategoryRef(
                            id="80a97ff3-34cd-4df8-97a9-e61876c6ab21",
                            name="Victor Mosciski",
                        ),
                        shared.TrackingCategoryRef(
                            id="c94d6fec-d799-4390-866a-6d2d00035533",
                            name="Wilbert Walsh IV",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="iure",
                        id="fa21e915-2cb3-4119-967b-8e3c8db03408",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="d364ffd4-5590-46d1-a63d-48e935c2c9e8",
                        name="Miss Jeannie Emmerich",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="e43202d7-2165-4765-8664-1870d9d21f9a",
                        name="Miss Michael Ferry",
                    ),
                ],
                unit_amount=8907.65,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="cumque",
        note="maxime",
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date="beatae",
                    currency="id",
                    currency_rate=90.6,
                    total_amount=5515.76,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="36429068-b850-42a5-9e7f-73bc845e320a",
                        name="Christine Mueller",
                    ),
                    currency="rerum",
                    currency_rate=6786.95,
                    id="df947c9a-867b-4c42-8266-65816ddca8ef",
                    note="nemo",
                    paid_on_date="illo",
                    reference="doloribus",
                    total_amount=7666.7,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id="4c593ec1-2cda-4ad0-ac7a-fedbd80df448",
                purchase_order_number="similique",
            ),
            shared.PurchaseOrderRef(
                id="47f9390c-5888-4098-bdab-f9ef3ffdd9f7",
                purchase_order_number="voluptatibus",
            ),
            shared.PurchaseOrderRef(
                id="079af4d3-5724-4cdb-8f4d-281187d56844",
                purchase_order_number="accusamus",
            ),
        ],
        reference="nulla",
        source_modified_date="repudiandae",
        status="Draft",
        sub_total=5057.99,
        supplemental_data=shared.BillSupplementalData(
            content={
                "animi": {
                    "quae": "eum",
                    "nostrum": "eveniet",
                    "laboriosam": "ratione",
                },
                "blanditiis": {
                    "illum": "reiciendis",
                    "placeat": "dolores",
                    "consequatur": "nesciunt",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="2b6c8799-23b7-4e13-984f-7ae12c6891f8",
            supplier_name="aspernatur",
        ),
        tax_amount=7552.4,
        total_amount=9178.77,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=810.53,
                name="Heidi Bode",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=209602,
)

res = s.bills.create(req)

if res.create_bill_response is not None:
    # handle response
```

## delete

Deletes a bill from the accounting package for a given company.

> **Supported Integrations**
> 
> This functionality is currently only supported for our Oracle NetSuite and QuickBooks Online integrations. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteBillRequest(
    bill_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.bills.delete(req)

if res.push_operation_summary is not None:
    # handle response
```

## download_attachment

Download bill attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadBillAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    bill_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.bills.download_attachment(req)

if res.data is not None:
    # handle response
```

## get

Get bill

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetBillRequest(
    bill_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.bills.get(req)

if res.bill is not None:
    # handle response
```

## get_attachment

Get bill attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetBillAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    bill_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.bills.get_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_create_update_model

Get create/update bill model.

 > **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating and updating a bill.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateUpdateBillsModelRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.bills.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

## list

Gets the latest bills for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListBillsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="eaque",
)

res = s.bills.list(req)

if res.bills is not None:
    # handle response
```

## list_attachments

List bill attachments

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListBillAttachmentsRequest(
    bill_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.bills.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## update

Posts an updated bill to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/accounting-api#/operations/get-create-update-bills-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support updating a bill.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateBillRequest(
    bill=shared.Bill(
        amount_due=3474.6,
        currency="amet",
        currency_rate=4541.65,
        due_date="voluptate",
        id="dcfa89df-975e-4356-a860-92e9c3ddc5f1",
        issue_date="vitae",
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id="dea1026d-541a-44d1-90fe-b21780bccc0d",
                    name="Kelvin Shanahan",
                ),
                description="magnam",
                discount_amount=5123.49,
                discount_percentage=2726.35,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id="708fb4e3-91e6-4bc1-98c4-c4e54599ea34",
                    name="Dr. Rose Hoeger",
                ),
                quantity=7495.37,
                sub_total=1861.3,
                tax_amount=374.77,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=92.48,
                    id="ce78a1bd-8fb7-4a0a-916c-e723d4097fa3",
                    name="Alyssa Morar",
                ),
                total_amount=4974.8,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="5b291220-30d8-43f5-aeb7-799d22e8c1f8",
                            name="Erika Farrell III",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="delectus",
                        id="dc42c876-c2c2-4dfb-8cfc-1c76230f841f",
                    ),
                    is_billed_to="Customer",
                    is_rebilled_to="Unknown",
                    project_ref=shared.ProjectRef(
                        id="bd23fdb1-4db6-4be5-a685-998e22ae20da",
                        name="Lucy Wilkinson",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="271a289c-57e8-454e-9043-9d2224656946",
                        name="Juanita Batz IV",
                    ),
                    shared.TrackingCategoryRef(
                        id="4f7ab37c-ef02-4225-994d-b55410adc669",
                        name="Miss Cary McKenzie",
                    ),
                    shared.TrackingCategoryRef(
                        id="6c7cdc98-1f06-4898-9d6b-b33cfaa348c3",
                        name="Antoinette Wolf IV",
                    ),
                ],
                unit_amount=9334.56,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="necessitatibus",
        note="numquam",
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date="eligendi",
                    currency="sapiente",
                    currency_rate=0.73,
                    total_amount=7704.67,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="42b78f15-6263-498a-8dc7-66324ccb06c8",
                        name="Rex Bode",
                    ),
                    currency="sit",
                    currency_rate=1720.42,
                    id="529270b8-d572-42dd-895b-8bcf24db9596",
                    note="provident",
                    paid_on_date="amet",
                    reference="dolor",
                    total_amount=3440.1,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date="qui",
                    currency="tenetur",
                    currency_rate=4773.52,
                    total_amount=2925.71,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="533994d7-8de3-4b6e-9389-f5abb7f66255",
                        name="Monique Denesik",
                    ),
                    currency="totam",
                    currency_rate=1835.04,
                    id="ac483afd-2315-4bba-a501-64e06f5bf6ae",
                    note="nemo",
                    paid_on_date="molestias",
                    reference="architecto",
                    total_amount=7112.75,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date="quisquam",
                    currency="praesentium",
                    currency_rate=7080.75,
                    total_amount=8264.78,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="ef3612b6-3c20-45fd-a840-774a68a9a35d",
                        name="Leona Hodkiewicz",
                    ),
                    currency="maiores",
                    currency_rate=4120.24,
                    id="6fef020e-9f44-43b4-a57b-992c8dbda6a6",
                    note="dicta",
                    paid_on_date="recusandae",
                    reference="sapiente",
                    total_amount=6617.64,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date="odit",
                    currency="inventore",
                    currency_rate=6122.38,
                    total_amount=5421.87,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="258fd0a9-eba4-47f7-93ef-049640d6a183",
                        name="Rosalie Lindgren",
                    ),
                    currency="temporibus",
                    currency_rate=9559.13,
                    id="596fdf1a-d837-4ae8-8c1c-19c95ba99867",
                    note="voluptatum",
                    paid_on_date="sapiente",
                    reference="deserunt",
                    total_amount=2212.4,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id="696991af-388c-4e03-a144-48c7977a0ef2",
                purchase_order_number="delectus",
            ),
            shared.PurchaseOrderRef(
                id="536028ef-eef9-4341-92ed-7e253f4c157d",
                purchase_order_number="voluptates",
            ),
            shared.PurchaseOrderRef(
                id="aa7170f4-45ac-4cf6-a7aa-f9bbad185fe4",
                purchase_order_number="nesciunt",
            ),
            shared.PurchaseOrderRef(
                id="1d6bf5c8-38fb-4b8c-a0cb-67fc4b425e99",
                purchase_order_number="debitis",
            ),
        ],
        reference="laboriosam",
        source_modified_date="eos",
        status="Open",
        sub_total=2796.79,
        supplemental_data=shared.BillSupplementalData(
            content={
                "occaecati": {
                    "voluptate": "tempore",
                    "in": "omnis",
                    "possimus": "tenetur",
                    "recusandae": "expedita",
                },
                "iusto": {
                    "harum": "ad",
                    "quod": "ratione",
                },
                "totam": {
                    "dolore": "nam",
                    "officia": "maiores",
                    "cupiditate": "illo",
                    "saepe": "enim",
                },
                "eaque": {
                    "eveniet": "delectus",
                    "deleniti": "provident",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="0a54b475-f16f-456d-b85a-3c4ac631b99e",
            supplier_name="fugit",
        ),
        tax_amount=4188.92,
        total_amount=7637.09,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=8528.73,
                name="Tommie Mraz",
            ),
            shared.BillWithholdingTax(
                amount=7063.71,
                name="Dr. Marcus Bosco",
            ),
            shared.BillWithholdingTax(
                amount=2458.49,
                name="Rudolph Weimann IV",
            ),
            shared.BillWithholdingTax(
                amount=5422.42,
                name="Mr. Nellie Reichert",
            ),
        ],
    ),
    bill_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    timeout_in_minutes=990454,
)

res = s.bills.update(req)

if res.update_bill_response is not None:
    # handle response
```

## upload_attachment

Upload bill attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UploadBillAttachmentRequest(
    request_body=operations.UploadBillAttachmentRequestBody(
        content="at".encode(),
        request_body="quibusdam",
    ),
    bill_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.bills.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
