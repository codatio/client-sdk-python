# invoices

## Overview

Invoices

### Available Operations

* [download_invoice_pdf](#download_invoice_pdf) - Get invoice as PDF
* [create_invoice](#create_invoice) - Create invoice
* [delete_invoice](#delete_invoice) - Delete invoice
* [download_invoice_attachment](#download_invoice_attachment) - Download invoice attachment
* [get_create_update_invoices_model](#get_create_update_invoices_model) - Get create/update invoice model
* [get_invoice](#get_invoice) - Get invoice
* [get_invoice_attachment](#get_invoice_attachment) - Get invoice attachment
* [get_invoice_attachments](#get_invoice_attachments) - Get invoice attachments
* [list_invoices](#list_invoices) - List invoices
* [update_invoice](#update_invoice) - Update invoice
* [upload_invoice_attachment](#upload_invoice_attachment) - Push invoice attachment

## download_invoice_pdf

Get invoice as PDF

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadInvoicePdfRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.invoices.download_invoice_pdf(req)

if res.data is not None:
    # handle response
```

## create_invoice

Posts a new invoice to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support creating invoices.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateInvoiceRequest(
    invoice=shared.Invoice(
        additional_tax_amount=4724.55,
        additional_tax_percentage=6309.47,
        amount_due=6663.31,
        currency="iure",
        currency_rate=141.26,
        customer_ref=shared.CustomerRef(
            company_name="placeat",
            id="8fe46e61-77db-49db-bb70-ffbb6970ee77",
        ),
        discount_percentage=580.86,
        due_date="eveniet",
        id="36097ef7-c206-4e61-b0d3-08714c20a3d9",
        invoice_number="corrupti",
        issue_date="ea",
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id="7ca85c3f-e655-474d-baf9-4a7c98f13af2",
                    name="Mack Rempel",
                ),
                description="sapiente",
                discount_amount=1646.09,
                discount_percentage=7103.52,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="f4f3ded3-56d7-4e14-b21c-d98196d55af6",
                    name="Hubert Casper",
                ),
                quantity=7070.73,
                sub_total=4962.61,
                tax_amount=6175.35,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6847.46,
                    id="e33681c2-3c39-4a7c-8e17-cb12c5ba825f",
                    name="Nicholas Dare",
                ),
                total_amount=3186.14,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="ba6fbfec-932a-4f68-93d6-5bfecec2dd69",
                            name="Eileen Ziemann",
                        ),
                        shared.TrackingCategoryRef(
                            id="c7dda70e-c60e-4607-9894-d61c14cd9022",
                            name="Sophie Doyle",
                        ),
                        shared.TrackingCategoryRef(
                            id="0d977f1a-5491-4abe-9751-b106d23e03e6",
                            name="Dwight Casper",
                        ),
                        shared.TrackingCategoryRef(
                            id="ae99fcde-9e72-49c9-94f2-d8a44640ca60",
                            name="Geoffrey Kovacek",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="consequuntur",
                        id="f93f467d-c0d8-4da5-a122-026ab8f27748",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="1976af98-0da7-4a08-9fc4-4db274530e5c",
                        name="Jared Schinner",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="cbcfdcd3-34b6-4f62-bbce-cab50aee5e0d",
                        name="Clifton Rippin",
                    ),
                ],
                unit_amount=9594.77,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="nisi",
        note="id",
        paid_on_date="nulla",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="ullam",
                    currency="incidunt",
                    currency_rate=5382.58,
                    total_amount=3905.07,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="e7b413cb-e2d1-476d-81c4-3d40f61d1711",
                        name="Joy Runolfsdottir",
                    ),
                    currency="enim",
                    currency_rate=9324.15,
                    id="e4f72118-4077-42f3-ae3b-49dbe0f23b7b",
                    note="suscipit",
                    paid_on_date="fugiat",
                    reference="perspiciatis",
                    total_amount=5855.5,
                ),
            ),
        ],
        sales_order_refs=[
            "quas",
            "assumenda",
        ],
        source_modified_date="aliquid",
        status="Void",
        sub_total=8165.56,
        supplemental_data=shared.SupplementalData(
            content={
                "fugiat": {
                    "voluptate": "odio",
                    "voluptas": "deleniti",
                },
                "eaque": {
                    "minus": "iure",
                    "laborum": "ab",
                    "iure": "deserunt",
                    "blanditiis": "dolores",
                },
                "necessitatibus": {
                    "vero": "totam",
                    "eos": "delectus",
                },
                "illum": {
                    "praesentium": "fugiat",
                },
            },
        ),
        total_amount=1061.18,
        total_discount=187.83,
        total_tax_amount=3114.84,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=6869.46,
                name="Mr. Henrietta Marquardt",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=185041,
)

res = s.invoices.create_invoice(req)

if res.create_invoice_response is not None:
    # handle response
```

## delete_invoice

Deletes an invoice from the accounting package for a given company.

> **Supported Integrations**
> 
> This functionality is currently only supported for our QuickBooks Online integration. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteInvoiceRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.invoices.delete_invoice(req)

if res.push_operation_summary is not None:
    # handle response
```

## download_invoice_attachment

Download invoice attachments

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadInvoiceAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.invoices.download_invoice_attachment(req)

if res.data is not None:
    # handle response
```

## get_create_update_invoices_model

Get create/update invoice model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support creating and updating invoices.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateUpdateInvoicesModelRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.invoices.get_create_update_invoices_model(req)

if res.push_option is not None:
    # handle response
```

## get_invoice

Get invoice

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetInvoiceRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.invoices.get_invoice(req)

if res.invoice is not None:
    # handle response
```

## get_invoice_attachment

Get invoice attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetInvoiceAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.invoices.get_invoice_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_invoice_attachments

Get invoice attachments

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetInvoiceAttachmentsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.invoices.get_invoice_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## list_invoices

Gets the latest invoices for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListInvoicesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="dolorum",
)

res = s.invoices.list_invoices(req)

if res.invoices is not None:
    # handle response
```

## update_invoice

Posts an updated invoice to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support updating invoices.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateInvoiceRequest(
    invoice=shared.Invoice(
        additional_tax_amount=7197.2,
        additional_tax_percentage=2761.77,
        amount_due=3084.29,
        currency="eligendi",
        currency_rate=7102.56,
        customer_ref=shared.CustomerRef(
            company_name="architecto",
            id="835008f4-61ce-453e-9144-98a9ba460add",
        ),
        discount_percentage=9692.94,
        due_date="temporibus",
        id="e410c37d-aa91-482a-89d9-625d3caffc19",
        invoice_number="blanditiis",
        issue_date="voluptates",
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id="a4452792-bcd4-440e-a98b-ecce0486de0d",
                    name="Jeanne Skiles",
                ),
                description="distinctio",
                discount_amount=121.81,
                discount_percentage=612.49,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="5503e8dc-626f-4f77-8656-75f5b70e3e4c",
                    name="Gregg Russel",
                ),
                quantity=5828.22,
                sub_total=696.5,
                tax_amount=8969.21,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8038.15,
                    id="52624d00-014e-4f45-8ea1-1ac53ebb6587",
                    name="Mrs. Jeffery Gerlach II",
                ),
                total_amount=8117.74,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="b9acee40-0ae9-4f92-8af1-b025f1d14718",
                            name="Charlie Wolf DVM",
                        ),
                        shared.TrackingCategoryRef(
                            id="ad0c06c5-d954-472c-9d14-fc43b70bca88",
                            name="Miss Ernesto Kulas",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="consectetur",
                        id="351c3dd1-eb8f-47f7-9f4f-23f1c0a586c3",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="7d7b67fe-ef5e-4142-995b-1dbeceff7c4b",
                        name="Dolores Jerde",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="78275eea-7681-4746-8063-f799b7956c0b",
                        name="Miss Mindy O'Keefe",
                    ),
                ],
                unit_amount=1799.04,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id="0a40e7c4-ae64-4064-a726-57b01a07c08f",
                    name="Jimmy Morar DDS",
                ),
                description="dolores",
                discount_amount=3486.63,
                discount_percentage=4420.79,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="930d6f09-3a3e-4fa4-ad36-6dfa1011a091",
                    name="Rodney Turcotte",
                ),
                quantity=7336.81,
                sub_total=3503.06,
                tax_amount=2447.13,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5203.56,
                    id="62de1a9d-14fe-472e-921f-90303dfc3383",
                    name="Javier Wisozk",
                ),
                total_amount=6258.87,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="d1d32090-fc15-47ac-9fe1-961ce9be41c8",
                            name="Belinda Stoltenberg",
                        ),
                        shared.TrackingCategoryRef(
                            id="d9719d07-b200-4a58-bfd2-967df8fd882a",
                            name="Miss Tomas Hodkiewicz",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="commodi",
                        id="20cd9c5a-fdd0-44c3-b525-12beae1d87ec",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="fdcea8e7-a883-4116-a2cd-a6d77c1d8606",
                        name="Kathy Douglas",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="227866db-8a74-49e3-9845-11cc75e4f0c0",
                        name="Ellen Rodriguez",
                    ),
                    shared.TrackingCategoryRef(
                        id="b758cc94-562f-4006-9685-fcd1a173d84b",
                        name="Elias Connelly",
                    ),
                ],
                unit_amount=1277.99,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id="9834afb0-735c-4b62-85d4-a29aaa1e1691",
                    name="Alma Ziemann",
                ),
                description="aspernatur",
                discount_amount=9264.79,
                discount_percentage=9197.03,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="209505bf-03a9-43e9-8480-ca37fb107890",
                    name="Theresa O'Connell",
                ),
                quantity=2286.72,
                sub_total=1995.11,
                tax_amount=933.23,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4630.78,
                    id="2e2dd79e-c74b-4a7e-88dd-b36fd1ccc341",
                    name="Willard Johnston",
                ),
                total_amount=2225.2,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="74f0a740-fb4a-4b44-9c3a-09e763995d80",
                            name="Garry Reichel",
                        ),
                        shared.TrackingCategoryRef(
                            id="94455ebc-550a-41c4-a6b5-9c8366fdcc13",
                            name="Ida Lemke",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="et",
                        id="b855e889-d9ef-4932-a900-0a13ad812420",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="fd234118-98e7-4387-9efb-e8baebabb794",
                        name="Rita Keeling",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="351bb976-3172-40b7-ba5a-5365a79f1527",
                        name="Miss Winifred Barton PhD",
                    ),
                ],
                unit_amount=2078.87,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id="61fed8dc-5eff-4b45-be90-89e871fdb4d6",
                    name="Fernando Rippin",
                ),
                description="perspiciatis",
                discount_amount=7911.41,
                discount_percentage=5639.57,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="85e43734-a5d7-42d9-add7-85be5e7afe55",
                    name="Kristina Kozey",
                ),
                quantity=3860.49,
                sub_total=1265.14,
                tax_amount=5110.98,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1221.01,
                    id="f44e3a23-394a-468c-880d-30ff72164d0a",
                    name="Keith Zulauf",
                ),
                total_amount=8512.2,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="6553b89e-0009-4c66-92de-7b3562201a6a",
                            name="Bennie Gislason",
                        ),
                        shared.TrackingCategoryRef(
                            id="7b1a5b90-8d4e-4304-91aa-35d4a839f03b",
                            name="Willis Krajcik",
                        ),
                        shared.TrackingCategoryRef(
                            id="918f0313-9845-407e-8e39-c7e23ecb0604",
                            name="Melanie Corkery",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="ipsum",
                        id="a3d6c657-e9de-48f7-b002-d1986aa99d3a",
                    ),
                    is_billed_to="Unknown",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="32329e45-837e-48f2-ad6b-b10e255fdc48",
                        name="Krystal Hoeger",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="08675cbf-1868-456a-be82-cdf9d0fc282c",
                        name="Eileen Kassulke",
                    ),
                ],
                unit_amount=1988.04,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="optio",
        note="ratione",
        paid_on_date="a",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="nostrum",
                    currency="totam",
                    currency_rate=5904.76,
                    total_amount=7165.27,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="ea5d264e-41e2-4ca8-8822-e513f6d9d2ad",
                        name="Nellie Schmeler V",
                    ),
                    currency="occaecati",
                    currency_rate=328.36,
                    id="77c10b68-7921-463e-a7d4-8860543c0a30",
                    note="labore",
                    paid_on_date="excepturi",
                    reference="quisquam",
                    total_amount=2173.4,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="quod",
                    currency="voluptatibus",
                    currency_rate=3769.3,
                    total_amount=7836.87,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="0276e7b2-1bad-490d-a743-fd6c2a10e6c2",
                        name="Erik Lindgren",
                    ),
                    currency="eos",
                    currency_rate=3181.5,
                    id="6a5b0922-7fcc-4479-96c9-77bbc57f3892",
                    note="quos",
                    paid_on_date="est",
                    reference="blanditiis",
                    total_amount=3890.14,
                ),
            ),
        ],
        sales_order_refs=[
            "eaque",
        ],
        source_modified_date="quo",
        status="Draft",
        sub_total=5387.08,
        supplemental_data=shared.SupplementalData(
            content={
                "eum": {
                    "facere": "ea",
                    "sequi": "voluptates",
                },
                "tempora": {
                    "officia": "exercitationem",
                    "laboriosam": "quos",
                    "aliquam": "vel",
                },
                "numquam": {
                    "odio": "omnis",
                    "quo": "maiores",
                },
                "maxime": {
                    "quisquam": "eaque",
                    "officiis": "corporis",
                },
            },
        ),
        total_amount=507.41,
        total_discount=2229.84,
        total_tax_amount=9822.17,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=4264.61,
                name="Johnny Bins PhD",
            ),
            shared.WithholdingTaxitems(
                amount=5621.97,
                name="Al Ledner",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    timeout_in_minutes=185898,
)

res = s.invoices.update_invoice(req)

if res.update_invoice_response is not None:
    # handle response
```

## upload_invoice_attachment

Push invoice attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UploadInvoiceAttachmentRequest(
    request_body=operations.UploadInvoiceAttachmentRequestBody(
        content="totam".encode(),
        request_body="recusandae",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.invoices.upload_invoice_attachment(req)

if res.status_code == 200:
    # handle response
```
