# create_invoice
Available in: `invoices`

Posts a new invoice to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support creating invoices.

## Example Usage
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
        additional_tax_amount=5328.66,
        additional_tax_percentage=7276.55,
        amount_due=952.32,
        currency="quidem",
        currency_rate=7452.74,
        customer_ref=shared.CustomerRef(
            company_name="exercitationem",
            id="5a292b0b-c3bb-4744-a64e-b1d03388b0d1",
        ),
        discount_percentage=7272.56,
        due_date="2022-10-23T00:00:00Z",
        id="b17afee7-4b6f-4eb9-857c-7edaf39d16fb",
        invoice_number="asperiores",
        issue_date="2022-10-23T00:00:00Z",
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id="6fd162b3-03e3-4023-b93e-34316cf55b43",
                    name="Edith Herman",
                ),
                description="porro",
                discount_amount=7629.28,
                discount_percentage=9383.57,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="1c204c4a-dcc9-4904-8519-5b8648cefa78",
                    name="Raymond Von",
                ),
                quantity=2009.91,
                sub_total=7268.55,
                tax_amount=6231.48,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=200.26,
                    id="1e0952bb-b4cb-4b19-b713-d95a4169c138",
                    name="Dr. Marilyn Kuhn V",
                ),
                total_amount=9110.26,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="9e45118c-2cc5-47fb-960b-1a78ed29a9d4",
                            name="Dexter O'Kon",
                        ),
                        shared.TrackingCategoryRef(
                            id="658c2d4f-4c88-4be4-b278-fd9667e46c51",
                            name="Ernest Wolf",
                        ),
                        shared.TrackingCategoryRef(
                            id="a58dcef2-34c9-455b-9bdf-2190abd9bbcc",
                            name="Stella Cole",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="impedit",
                        id="2659ce02-8084-40c6-9ef6-8e45c8addfac",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="4500430c-6632-4b43-91fd-f01c3e91e8f7",
                        name="Jermaine Jenkins",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="60a77ece-b26d-410f-9ef2-631c7c0f0f87",
                        name="Dixie Mueller",
                    ),
                    shared.TrackingCategoryRef(
                        id="c25fd3e0-b4a4-4a42-93c3-025711f42c7e",
                        name="Mercedes Sauer",
                    ),
                ],
                unit_amount=5293.03,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id="be09e41a-7a21-45ca-92a4-ba9d59988192",
                    name="Miss Darrin Shanahan",
                ),
                description="iusto",
                discount_amount=7563.43,
                discount_percentage=3550.92,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="3e7e7d4e-e6e8-4b90-bac3-84e2396703fe",
                    name="Jeff Casper",
                ),
                quantity=246.9,
                sub_total=5343.17,
                tax_amount=1834.8,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2965.94,
                    id="d189a36a-6b2d-427e-b707-aa60c8fe46e6",
                    name="Colleen Klein",
                ),
                total_amount=6100.01,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="b3b70ffb-b697-40ee-b70e-36097ef7c206",
                            name="Ricardo Brown PhD",
                        ),
                        shared.TrackingCategoryRef(
                            id="308714c2-0a3d-4986-b7ca-85c3fe65574d",
                            name="Shannon Witting",
                        ),
                        shared.TrackingCategoryRef(
                            id="a7c98f13-af28-4db2-8f2b-f4f3ded356d7",
                            name="Lawrence Gleichner",
                        ),
                        shared.TrackingCategoryRef(
                            id="1cd98196-d55a-4f69-a1c4-b79ae33681c2",
                            name="Marianne Effertz",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="voluptate",
                        id="c0e17cb1-2c5b-4a82-9fe2-2cd5cba6fbfe",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="32af6813-d65b-4fec-ac2d-d6916f7fc7dd",
                        name="Clinton Beer",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="0e607589-4d61-4c14-8d90-227e37c0d977",
                        name="Douglas Nicolas",
                    ),
                    shared.TrackingCategoryRef(
                        id="91abe975-1b10-46d2-be03-e69815aae99f",
                        name="Levi Tremblay",
                    ),
                ],
                unit_amount=4467.12,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="odit",
        paid_on_date="2022-10-23T00:00:00Z",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="eligendi",
                    currency_rate=6230.66,
                    total_amount=8582.27,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="4f2d8a44-640c-4a60-9b73-a2f93f467dc0",
                        name="Max Schuppe",
                    ),
                    currency="voluptas",
                    currency_rate=885.63,
                    id="22026ab8-f277-4485-8197-6af980da7a08",
                    note="unde",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="hic",
                    total_amount=8024.26,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="numquam",
                    currency_rate=2838.48,
                    total_amount=8519.16,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="b274530e-5cc7-4c6d-8cbc-fdcd334b6f62",
                        name="Whitney Schiller",
                    ),
                    currency="mollitia",
                    currency_rate=7064.71,
                    id="50aee5e0-da8b-49af-aad0-5486e7b413cb",
                    note="saepe",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="magni",
                    total_amount=8253.89,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="et",
                    currency_rate=4767.65,
                    total_amount=4100.45,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="dc1c43d4-0f61-4d17-9157-cbe5ee4f7211",
                        name="Miguel Adams",
                    ),
                    currency="quia",
                    currency_rate=9804.11,
                    id="32e3b49d-be0f-423b-bb6d-9948d6eded47",
                    note="odio",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="voluptas",
                    total_amount=5378.51,
                ),
            ),
        ],
        sales_order_refs=[
            "reiciendis",
        ],
        source_modified_date="2022-10-23T00:00:00Z",
        status="Paid",
        sub_total=4379.2,
        supplemental_data=shared.SupplementalData(
            content={
                "ab": {
                    "deserunt": "blanditiis",
                    "dolores": "necessitatibus",
                },
                "nemo": {
                    "totam": "eos",
                    "delectus": "illum",
                    "consequuntur": "praesentium",
                    "fugiat": "beatae",
                },
                "perferendis": {
                    "aperiam": "harum",
                    "iusto": "debitis",
                },
            },
        ),
        total_amount=5723.68,
        total_discount=1083.49,
        total_tax_amount=1890.08,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=1850.41,
                name="Preston Gorczany",
            ),
            shared.WithholdingTaxitems(
                amount=7102.56,
                name="Lena Fisher Jr.",
            ),
            shared.WithholdingTaxitems(
                amount=5027.38,
                name="Miss Ray Hoeger",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=336692,
)

res = s.invoices.create_invoice(req)

if res.create_invoice_response is not None:
    # handle response
```