# create_direct_income
Available in: `direct_incomes`

Posts a new direct income to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create direct income model](https://docs.codat.io/accounting-api#/operations/get-create-directIncomes-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating direct incomes.

## Example Usage
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
            data_type="est",
            id="aee79e3c-71ad-431b-acb8-3d2378ae3bfc",
        ),
        currency="sed",
        currency_rate=2220.93,
        id="d9450a98-6a49-45ba-8707-f06b28ecc864",
        issue_date="2022-10-23T00:00:00Z",
        line_items=[
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id="2386f62c-969c-44cc-ab78-890a3fd3c81d",
                    name="Samuel Aufderhar",
                ),
                description="optio",
                discount_amount=1614.81,
                discount_percentage=2485.3,
                item_ref=shared.ItemRef(
                    id="df931da3-edb5-41fa-994a-cc9435137726",
                    name="Peter Hand",
                ),
                quantity=1199.27,
                sub_total=7214.48,
                tax_amount=5545.08,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2429.72,
                    id="2a56d691-80ff-460e-b9a6-658e69a4b843",
                    name="Chad Leannon",
                ),
                total_amount=6893.09,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="c75c68c6-0659-4468-8e30-4d8849bf8214",
                        name="Vincent Erdman",
                    ),
                    shared.TrackingCategoryRef(
                        id="96bb0c69-e372-4db1-b44b-a9f78a5c0ed7",
                        name="Gerard Roberts DVM",
                    ),
                    shared.TrackingCategoryRef(
                        id="97261fb0-c58d-427b-9199-6b5b4b50eef7",
                        name="Christina Rice",
                    ),
                    shared.TrackingCategoryRef(
                        id="7ab0344b-1710-4688-9eeb-ef897f3dd0cc",
                        name="Curtis Fahey Sr.",
                    ),
                ],
                unit_amount=6984.45,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id="3e4e080a-a104-4186-ac75-9e02f3702c5c",
                    name="Clay Conn",
                ),
                description="consequatur",
                discount_amount=9158.97,
                discount_percentage=6344.86,
                item_ref=shared.ItemRef(
                    id="d3104fa4-4707-4bf3-b5b4-4282821fdb2f",
                    name="Velma Vandervort",
                ),
                quantity=1639.27,
                sub_total=3850.8,
                tax_amount=4833.56,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7908.48,
                    id="71cc8d3c-d425-48d0-b58a-82c808fe2751",
                    name="Billy Aufderhar",
                ),
                total_amount=7989.54,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="449e143f-9619-4bb7-940d-5a11fa436e62",
                        name="Faye Champlin",
                    ),
                ],
                unit_amount=9421.67,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id="95c9d237-397c-4785-b5db-4f500183febd",
                    name="Brett Kling",
                ),
                description="reprehenderit",
                discount_amount=1612.08,
                discount_percentage=378.34,
                item_ref=shared.ItemRef(
                    id="6dab7500-52a5-4647-adc4-39ed8c4320f4",
                    name="Dr. Julia Gibson",
                ),
                quantity=2790.04,
                sub_total=5208.11,
                tax_amount=4808.49,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6503.19,
                    id="c693b94c-3b9d-4248-8d79-5aa42fc40566",
                    name="Roman Kassulke",
                ),
                total_amount=604.91,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="6d212494-5081-49d7-83b1-b41844060e00",
                        name="Carolyn Bednar I",
                    ),
                ],
                unit_amount=2449.14,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="repellendus",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="error",
                    currency_rate=563.11,
                    total_amount=1094.16,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="f5afd2a6-c448-446a-a9d8-9253c8962f48",
                        name="Franklin Prohaska",
                    ),
                    currency="et",
                    currency_rate=9102.24,
                    id="4652d3c3-43d6-4177-8af4-91247725e621",
                    note="iste",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="aut",
                    total_amount=5779.63,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="vero",
                    currency_rate=6231.5,
                    total_amount=781.11,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="044a5de5-9ac7-4706-a70c-f1cf59326052",
                        name="Teresa VonRueden",
                    ),
                    currency="harum",
                    currency_rate=7414,
                    id="426897d9-9a2d-4335-a70e-93ee6cf59f35",
                    note="voluptatum",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="dolorum",
                    total_amount=6400.46,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="earum",
                    currency_rate=6662.73,
                    total_amount=7892.14,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="ae323a31-bf7b-4a1c-8977-16c802cc9e0c",
                        name="Marcella Monahan",
                    ),
                    currency="dolores",
                    currency_rate=2361.24,
                    id="f1aa63ed-9cf1-4c85-abcb-a51ef2454a47",
                    note="voluptatibus",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="dolorum",
                    total_amount=8037.82,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="repellat",
                    currency_rate=860.51,
                    total_amount=779.96,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="6cdd5444-a756-4287-bc7d-d9efaf43dc62",
                        name="Dr. Terri Collier",
                    ),
                    currency="et",
                    currency_rate=2236.18,
                    id="8f30df3d-b022-4faa-965f-b8f652ebb9d3",
                    note="praesentium",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="non",
                    total_amount=5332.9,
                ),
            ),
        ],
        reference="dolor",
        source_modified_date="2022-10-23T00:00:00Z",
        sub_total=5464.65,
        supplemental_data=shared.SupplementalData(
            content={
                "molestias": {
                    "fugit": "labore",
                },
                "neque": {
                    "sed": "error",
                    "ratione": "facere",
                    "est": "soluta",
                },
            },
        ),
        tax_amount=2065,
        total_amount=212.77,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=878395,
)

res = s.direct_incomes.create_direct_income(req)

if res.create_direct_income_response is not None:
    # handle response
```