# update_invoice
Available in: `invoices`

Posts an updated invoice to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support updating invoices.

## Example Usage
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
        additional_tax_amount=8977.85,
        additional_tax_percentage=5673.2,
        amount_due=721.26,
        currency="tempora",
        currency_rate=2813.81,
        customer_ref=shared.CustomerRef(
            company_name="perspiciatis",
            id="8a9ba460-addf-4de4-90c3-7daa9182a49d",
        ),
        discount_percentage=5768.41,
        due_date="2022-10-23T00:00:00Z",
        id="625d3caf-fc19-48ee-a445-2792bcd440ea",
        invoice_number="occaecati",
        issue_date="2022-10-23T00:00:00Z",
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id="becce048-6de0-4d56-973b-005503e8dc62",
                    name="Ora Wuckert",
                ),
                description="impedit",
                discount_amount=4366.89,
                discount_percentage=3524.16,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="675f5b70-e3e4-4cfc-86a9-1ec52624d000",
                    name="Rhonda VonRueden",
                ),
                quantity=3242.38,
                sub_total=7743.39,
                tax_amount=8885.73,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6571.73,
                    id="11ac53eb-b658-47f3-8041-4c5b9acee400",
                    name="Noah Medhurst",
                ),
                total_amount=1671.44,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="af1b025f-1d14-4718-86fa-2fad0c06c5d9",
                            name="Gail King",
                        ),
                        shared.TrackingCategoryRef(
                            id="dd14fc43-b70b-4ca8-8fa7-0c43351c3dd1",
                            name="Kerry Lesch",
                        ),
                        shared.TrackingCategoryRef(
                            id="f75f4f23-f1c0-4a58-ac3a-e7d7b67feef5",
                            name="Eric Gibson",
                        ),
                        shared.TrackingCategoryRef(
                            id="95b1dbec-eff7-4c4b-956e-9278275eea76",
                            name="Carl Kozey",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="praesentium",
                        id="063f799b-7956-4c0b-8fa0-bb20a40e7c4a",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="40642726-57b0-41a0-bc08-fd3921c25793",
                        name="Mercedes Kemmer V",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="a3efa46d-366d-4fa1-811a-091b3ec8b538",
                        name="Bonnie Stokes MD",
                    ),
                ],
                unit_amount=5648.16,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id="d14fe72e-521f-4903-83df-c338397fffa6",
                    name="Justin Stroman",
                ),
                description="consequatur",
                discount_amount=5788.09,
                discount_percentage=9.47,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="fc157ac9-fe19-461c-a9be-41c869dd7d97",
                    name="Ms. Geneva Skiles",
                ),
                quantity=1382.61,
                sub_total=154.46,
                tax_amount=498.92,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6470.89,
                    id="58ffd296-7df8-4fd8-82a8-e60be620cd9c",
                    name="Brandi Williamson",
                ),
                total_amount=419.17,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="c3752512-beae-41d8-becc-5fdcea8e7a88",
                            name="Frances Bosco",
                        ),
                        shared.TrackingCategoryRef(
                            id="2cda6d77-c1d8-4606-a237-d4227866db8a",
                            name="Clara Mertz",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="provident",
                        id="84511cc7-5e4f-40c0-84b5-bb758cc94562",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="Unknown",
                    project_ref=shared.ProjectRef(
                        id="069685fc-d1a1-473d-84bb-e24f29834afb",
                        name="Viola Dicki",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="6285d4a2-9aaa-41e1-a915-6f7d2ee20950",
                        name="Mrs. Whitney Wuckert",
                    ),
                    shared.TrackingCategoryRef(
                        id="93e94480-ca37-4fb1-8789-032ac333172e",
                        name="Angelina Sporer",
                    ),
                    shared.TrackingCategoryRef(
                        id="ec74ba7e-88dd-4b36-bd1c-cc341c865734",
                        name="Miss Charlotte Yundt",
                    ),
                ],
                unit_amount=2786.03,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id="0fb4ab44-1c3a-409e-b639-95d808bbe794",
                    name="Joann Herman",
                ),
                description="quo",
                discount_amount=3668.22,
                discount_percentage=3290.47,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="0a1c426b-59c8-4366-bdcc-135582c1b855",
                    name="Dwight Lindgren",
                ),
                quantity=6061.92,
                sub_total=8896.83,
                tax_amount=9407.66,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6238.98,
                    id="32e9000a-13ad-4812-8208-efd23411898e",
                    name="Sylvia Lang",
                ),
                total_amount=9076.15,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="be8baeba-bb79-4453-ae90-351bb9763172",
                            name="Melody Kreiger",
                        ),
                        shared.TrackingCategoryRef(
                            id="5a5365a7-9f15-4271-b01c-0d361fed8dc5",
                            name="Tommie Wilkinson",
                        ),
                        shared.TrackingCategoryRef(
                            id="53e9089e-871f-4db4-9697-bdd9c985e437",
                            name="Marjorie Nitzsche",
                        ),
                        shared.TrackingCategoryRef(
                            id="72d9edd7-85be-45e7-afe5-5297ba6281f4",
                            name="Tricia Ebert",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="dolor",
                        id="394a68cc-80d3-40ff-b216-4d0a91fe9d96",
                    ),
                    is_billed_to="Unknown",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="3b89e000-9c66-492d-a7b3-562201a6aab4",
                        name="Noah Kirlin MD",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="b908d4e3-0491-4aa3-9d4a-839f03bab77b",
                        name="Ryan Labadie I",
                    ),
                    shared.TrackingCategoryRef(
                        id="13984507-e0e3-49c7-a23e-cb0604652e23",
                        name="Norman Stiedemann",
                    ),
                ],
                unit_amount=3772.06,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="quis",
        paid_on_date="2022-10-23T00:00:00Z",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="vero",
                    currency_rate=6032.05,
                    total_amount=8413.46,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="e8f7f002-d198-46aa-99d3-a1d32329e458",
                        name="Maureen Veum",
                    ),
                    currency="qui",
                    currency_rate=6377.7,
                    id="d6bb10e2-55fd-4c48-8d6e-3308675cbf18",
                    note="voluptas",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="molestias",
                    total_amount=3424.33,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="vel",
                    currency_rate=6468.22,
                    total_amount=4981.83,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="e82cdf9d-0fc2-482c-a66a-f3c3f5589bea",
                        name="Marcella Daniel",
                    ),
                    currency="voluptates",
                    currency_rate=2652.54,
                    id="1e2ca848-22e5-413f-ad9d-2ad37c309907",
                    note="esse",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="nobis",
                    total_amount=640.01,
                ),
            ),
        ],
        sales_order_refs=[
            "rerum",
        ],
        source_modified_date="2022-10-23T00:00:00Z",
        status="Submitted",
        sub_total=5362.23,
        supplemental_data=shared.SupplementalData(
            content={
                "iste": {
                    "veritatis": "commodi",
                },
                "amet": {
                    "autem": "nihil",
                    "repellendus": "non",
                    "rem": "voluptatum",
                    "vel": "quae",
                },
            },
        ),
        total_amount=3358.37,
        total_discount=2942.68,
        total_tax_amount=2316.11,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=470,
                name="Jeff Bailey",
            ),
            shared.WithholdingTaxitems(
                amount=7879.41,
                name="Traci Wolf",
            ),
            shared.WithholdingTaxitems(
                amount=251.21,
                name="Marcia Howe",
            ),
            shared.WithholdingTaxitems(
                amount=7295.54,
                name="Debra Purdy",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    timeout_in_minutes=590737,
)

res = s.invoices.update_invoice(req)

if res.update_invoice_response is not None:
    # handle response
```