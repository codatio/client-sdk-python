# bills

## Overview

Bills

### Available Operations

* [create_bill](#create_bill) - Create bill
* [delete_bill](#delete_bill) - Delete bill
* [download_bill_attachment](#download_bill_attachment) - Download bill attachment
* [get_bill](#get_bill) - Get bill
* [get_bill_attachment](#get_bill_attachment) - Get bill attachment
* [get_bill_attachments](#get_bill_attachments) - List bill attachments
* [get_create_update_bills_model](#get_create_update_bills_model) - Get create/update bill model
* [list_bills](#list_bills) - List bills
* [update_bill](#update_bill) - Update bill
* [upload_bill_attachments](#upload_bill_attachments) - Upload bill attachments

## create_bill

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
        amount_due=941.22,
        currency="rem",
        currency_rate=4935.79,
        due_date="doloremque",
        id="d9d21f9a-d030-4c4e-8c11-a0836429068b",
        issue_date="laudantium",
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id="02a55e7f-73bc-4845-a320-a319f4badf94",
                    name="Pat Mueller",
                ),
                description="aliquid",
                discount_amount=4693.84,
                discount_percentage=7063.28,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id="c4242666-5816-4ddc-a8ef-51fcb4c593ec",
                    name="Beverly Satterfield",
                ),
                quantity=6615.78,
                sub_total=8409.92,
                tax_amount=590.23,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8792.08,
                    id="c7afedbd-80df-4448-a47f-9390c5888098",
                    name="Eula Paucek",
                ),
                total_amount=6229.68,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="f3ffdd9f-7f07-49af-8d35-724cdb0f4d28",
                            name="Alice Langosh",
                        ),
                        shared.TrackingCategoryRef(
                            id="56844ede-d85a-4906-9e62-8bdfc2032b6c",
                            name="Cody Mohr",
                        ),
                        shared.TrackingCategoryRef(
                            id="3b7e1358-4f7a-4e12-8689-1f82ce115717",
                            name="Dawn Bechtelar",
                        ),
                        shared.TrackingCategoryRef(
                            id="77dcfa89-df97-45e3-9668-6092e9c3ddc5",
                            name="Dr. Jack Buckridge",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="laborum",
                        id="1026d541-a4d1-490f-ab21-780bccc0dbbd",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="Customer",
                    project_ref=shared.ProjectRef(
                        id="484708fb-4e39-41e6-bc15-8c4c4e54599e",
                        name="Jeffery Glover",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="0e9b200c-e78a-41bd-8fb7-a0a116ce723d",
                        name="Susan Mraz",
                    ),
                    shared.TrackingCategoryRef(
                        id="a30e9af7-25b2-4912-a030-d83f5aeb7799",
                        name="Nicholas Conroy",
                    ),
                ],
                unit_amount=7607.93,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id="1f849382-5fdc-442c-876c-2c2dfb4cfc1c",
                    name="Sue Christiansen DVM",
                ),
                description="quos",
                discount_amount=2563.1,
                discount_percentage=1138.94,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id="fb1bd23f-db14-4db6-be5a-685998e22ae2",
                    name="Ms. Lora Olson",
                ),
                quantity=7912.82,
                sub_total=1489.58,
                tax_amount=7211.98,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1554.73,
                    id="71a289c5-7e85-44e9-8439-d22246569462",
                    name="Ms. Sharon Kuhlman",
                ),
                total_amount=9624.11,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="ab37cef0-2225-4194-9b55-410adc669af9",
                            name="Sandy Considine",
                        ),
                        shared.TrackingCategoryRef(
                            id="7cdc981f-0689-481d-abb3-3cfaa348c31b",
                            name="Oscar Beatty",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="necessitatibus",
                        id="4fcf0c42-b78f-4156-a639-8a0dc766324c",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="Customer",
                    project_ref=shared.ProjectRef(
                        id="06c8ca12-d025-4292-b0b8-d5722dd895b8",
                        name="Guadalupe Wisoky",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="b9596933-52f7-4453-b994-d78de3b6e938",
                        name="Courtney Hermann",
                    ),
                    shared.TrackingCategoryRef(
                        id="b7f66255-0a28-4382-ac48-3afd2315bba6",
                        name="Helen Blick",
                    ),
                    shared.TrackingCategoryRef(
                        id="e06f5bf6-ae59-41bc-8bde-f3612b63c205",
                        name="Bryant Ondricka",
                    ),
                    shared.TrackingCategoryRef(
                        id="0774a68a-9a35-4d08-ab6f-66fef020e9f4",
                        name="Ethel Robel",
                    ),
                ],
                unit_amount=3184.03,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="nihil",
        note="libero",
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date="excepturi",
                    currency="eos",
                    currency_rate=7890.36,
                    total_amount=5471.84,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="dbda6a61-efa2-4198-a58f-d0a9eba47f7d",
                        name="Mrs. Tasha Wilkinson",
                    ),
                    currency="aliquid",
                    currency_rate=2946.5,
                    id="0d6a1831-c87a-4df5-96fd-f1ad837ae80c",
                    note="vitae",
                    paid_on_date="cumque",
                    reference="architecto",
                    total_amount=5754.04,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date="eligendi",
                    currency="occaecati",
                    currency_rate=3396.51,
                    total_amount=7343.61,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="a998678f-a3f6-4969-91af-388ce0361444",
                        name="Sylvester Kling",
                    ),
                    currency="reprehenderit",
                    currency_rate=6541.99,
                    id="0ef2f536-028e-4fee-b934-152ed7e253f4",
                    note="quod",
                    paid_on_date="sunt",
                    reference="ullam",
                    total_amount=4630.44,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date="illum",
                    currency="voluptates",
                    currency_rate=6410.06,
                    total_amount=6687.83,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="7170f445-accf-4667-aaf9-bbad185fe431",
                        name="Rick Predovic",
                    ),
                    currency="cumque",
                    currency_rate=5291.74,
                    id="38fbb8c2-0cb6-47fc-8b42-5e99e6234c9f",
                    note="voluptate",
                    paid_on_date="tempore",
                    reference="in",
                    total_amount=6098.64,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id="feb77a5c-38d4-4baf-91e5-06ef890a54b4",
                purchase_order_number="odio",
            ),
            shared.PurchaseOrderRef(
                id="5f16f56d-385a-43c4-ac63-1b99e26ced8f",
                purchase_order_number="natus",
            ),
            shared.PurchaseOrderRef(
                id="fdb9410f-63bb-4f81-b837-b01afdd78862",
                purchase_order_number="labore",
            ),
            shared.PurchaseOrderRef(
                id="189eb448-73f5-4033-b19d-bf125ce4152e",
                purchase_order_number="error",
            ),
        ],
        reference="expedita",
        source_modified_date="error",
        status="Void",
        sub_total=8382.27,
        supplemental_data=shared.BillSupplementalData(
            content={
                "earum": {
                    "odit": "odit",
                    "eius": "error",
                },
                "vel": {
                    "alias": "itaque",
                    "ab": "sunt",
                    "amet": "cum",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="7847ec59-e1f6-47f3-84cc-e4b6d7696ff3",
            supplier_name="eligendi",
        ),
        tax_amount=3534.24,
        total_amount=4713.15,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=4895.97,
                name="Margaret Bradtke",
            ),
            shared.BillWithholdingTax(
                amount=4713.02,
                name="Micheal Gusikowski",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=115522,
)

res = s.bills.create_bill(req)

if res.create_bill_response is not None:
    # handle response
```

## delete_bill

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

res = s.bills.delete_bill(req)

if res.push_operation_summary is not None:
    # handle response
```

## download_bill_attachment

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

res = s.bills.download_bill_attachment(req)

if res.data is not None:
    # handle response
```

## get_bill

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

res = s.bills.get_bill(req)

if res.bill is not None:
    # handle response
```

## get_bill_attachment

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

res = s.bills.get_bill_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_bill_attachments

Get bill attachments

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetBillAttachmentsRequest(
    bill_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.bills.get_bill_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## get_create_update_bills_model

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

res = s.bills.get_create_update_bills_model(req)

if res.push_option is not None:
    # handle response
```

## list_bills

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
    query="hic",
)

res = s.bills.list_bills(req)

if res.bills is not None:
    # handle response
```

## update_bill

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
        amount_due=5055.58,
        currency="libero",
        currency_rate=99.12,
        due_date="totam",
        id="4c3197e1-93a2-4454-a7f9-4874c2d5cc49",
        issue_date="ducimus",
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id="233e66bd-8fe5-4d00-b979-ef2038732059",
                    name="Pat Schmitt Jr.",
                ),
                description="perspiciatis",
                discount_amount=4069.46,
                discount_percentage=2622.31,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id="00313b3e-5044-4f65-be72-dc4077d0cc3f",
                    name="Carol Lowe",
                ),
                quantity=7738.54,
                sub_total=1199.28,
                tax_amount=3588.61,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7720.62,
                    id="eb4d6e1e-ae0f-475a-adf2-acab58b991c9",
                    name="Jeanette Schultz",
                ),
                total_amount=3130.99,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="9461e742-1cbe-46d9-902f-0ea930b69f7a",
                            name="Carlos Wunsch DVM",
                        ),
                        shared.TrackingCategoryRef(
                            id="88500904-9116-4082-8788-8ec66183bfe9",
                            name="Marion Mills",
                        ),
                        shared.TrackingCategoryRef(
                            id="40ec16fa-f75b-40b5-b2a4-da37cbaaf445",
                            name="Bernadette Hahn",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="explicabo",
                        id="c9b2ad32-dafe-481a-88f4-444573fecd47",
                    ),
                    is_billed_to="Unknown",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="3f63c820-9379-4aa6-9cd5-fbcf79da18a7",
                        name="Martin Daugherty",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="5894e686-1adb-455f-9e5d-751c9fe8f750",
                        name="Susie Wolf",
                    ),
                    shared.TrackingCategoryRef(
                        id="3450841f-1764-4456-b79f-3fb27e21f862",
                        name="Ida Kihn",
                    ),
                    shared.TrackingCategoryRef(
                        id="6fc6b9f5-87ce-4525-8676-41a8312e5047",
                        name="Mario Runolfsson DDS",
                    ),
                ],
                unit_amount=7678.8,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="distinctio",
        note="numquam",
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date="amet",
                    currency="culpa",
                    currency_rate=7057.53,
                    total_amount=7925.55,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="dc91faab-dd88-4e71-b6c4-8252d7771e7f",
                        name="Thomas Kirlin Jr.",
                    ),
                    currency="iste",
                    currency_rate=8814.13,
                    id="f8d29de1-dd70-497b-9da0-8c57fa6c78a2",
                    note="architecto",
                    paid_on_date="ea",
                    reference="accusamus",
                    total_amount=768.73,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id="bafeca61-9149-4814-8b64-ff8ae170ef03",
                purchase_order_number="distinctio",
            ),
            shared.PurchaseOrderRef(
                id="5f37e4aa-8685-4559-a673-2aa5dcb6682c",
                purchase_order_number="expedita",
            ),
            shared.PurchaseOrderRef(
                id="70f8cfd5-fb6e-491b-9a9f-74846e2c3309",
                purchase_order_number="repellendus",
            ),
        ],
        reference="soluta",
        source_modified_date="aut",
        status="PartiallyPaid",
        sub_total=2271.85,
        supplemental_data=shared.BillSupplementalData(
            content={
                "quibusdam": {
                    "voluptates": "nihil",
                    "ad": "eligendi",
                    "fuga": "consequatur",
                },
                "sit": {
                    "earum": "quis",
                    "dolorem": "omnis",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="2c11a25a-8bf9-42f9-b428-ad9a9f8bf822",
            supplier_name="illo",
        ),
        tax_amount=1037.6,
        total_amount=1541.17,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=2449.9,
                name="Sherri Schuster",
            ),
            shared.BillWithholdingTax(
                amount=2326.02,
                name="Lance Zieme",
            ),
        ],
    ),
    bill_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    timeout_in_minutes=453111,
)

res = s.bills.update_bill(req)

if res.update_bill_response is not None:
    # handle response
```

## upload_bill_attachments

Upload bill attachments

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UploadBillAttachmentsRequest(
    request_body=operations.UploadBillAttachmentsRequestBody(
        content="cupiditate".encode(),
        request_body="maxime",
    ),
    bill_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.bills.upload_bill_attachments(req)

if res.status_code == 200:
    # handle response
```
