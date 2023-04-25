# create_direct_cost
Available in: `direct_costs`

Posts a new direct cost to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create direct cost model](https://docs.codat.io/accounting-api#/operations/get-create-directCosts-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support creating direct costs.

## Example Usage
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
            data_type="modi",
            id="c0252fe3-b4b4-4db8-b778-ebb6e1d2cf50",
        ),
        currency="aspernatur",
        currency_rate=7116.2,
        id="afb2cbc4-635d-45e6-9da0-28c3e951a1e3",
        issue_date="2022-10-23T00:00:00Z",
        line_items=[
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id="fda96648-9d7b-4786-b3e1-3a12a6b99249",
                    name="Renee Morissette",
                ),
                description="corrupti",
                discount_amount=4996.21,
                discount_percentage=9890.6,
                item_ref=shared.ItemRef(
                    id="5c843836-b86b-43cd-b641-5b0449f9df13",
                    name="Mario Torphy",
                ),
                quantity=7182.93,
                sub_total=9239.82,
                tax_amount=4493.31,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5339.88,
                    id="bf606825-894e-4a76-bd5c-72795b785148",
                    name="Andre Sporer",
                ),
                total_amount=5825.36,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingInvoiceTo(
                        data_type="debitis",
                        id="5635b33b-c0f9-470c-82fc-9f4844225e75",
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type="ducimus",
                            id="96065c0e-fa6f-493b-90a1-b8c95be1254b",
                        ),
                        shared.InvoiceTo(
                            data_type="nihil",
                            id="39f4fe77-210d-41f6-958c-99c722d2bc0f",
                        ),
                        shared.InvoiceTo(
                            data_type="excepturi",
                            id="4087d9ca-ae04-42dd-bcaa-c9b4caa1cfe9",
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="15df9039-07f3-4783-9983-d42e54a85466",
                        name="Ramona Kub",
                    ),
                    shared.TrackingCategoryRef(
                        id="0233c147-1d51-4aaa-addf-5abd6487c5fc",
                        name="Gayle Lehner",
                    ),
                    shared.TrackingCategoryRef(
                        id="a00bef69-e100-4157-a30b-da7afded84a3",
                        name="Mr. Sonya Gutmann",
                    ),
                    shared.TrackingCategoryRef(
                        id="8e1a735a-c26a-4e33-bef9-71a8f46bca11",
                        name="Tonya Wintheiser",
                    ),
                ],
                unit_amount=4078.27,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="ipsam",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="esse",
                    currency_rate=1133.82,
                    total_amount=1054.97,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="d08cf88e-c9f7-4b99-a550-a656ed333bb0",
                        name="Frankie Larkin",
                    ),
                    currency="autem",
                    currency_rate=3351.76,
                    id="432a986e-b7e1-44ca-9640-89150097019a",
                    note="eius",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="rem",
                    total_amount=9654.94,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="blanditiis",
                    currency_rate=5149.76,
                    total_amount=9368.8,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="ce7bf904-e011-405d-b890-8162c6beb68a",
                        name="Melba Keebler",
                    ),
                    currency="quidem",
                    currency_rate=4478.48,
                    id="d03a1480-f8de-430f-869d-810618d97e15",
                    note="quia",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="aspernatur",
                    total_amount=6114.23,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="molestiae",
                    currency_rate=3286.66,
                    total_amount=900.67,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="0da80312-292c-4c61-82a7-02bb97ee102d",
                        name="Aaron Stehr",
                    ),
                    currency="minima",
                    currency_rate=9483.74,
                    id="8e01bf33-eaab-4454-82ac-1704bf1cc9fc",
                    note="ex",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="dicta",
                    total_amount=6460.23,
                ),
            ),
        ],
        reference="laborum",
        source_modified_date="2022-10-23T00:00:00Z",
        sub_total=9299.41,
        supplemental_data=shared.SupplementalData(
            content={
                "voluptates": {
                    "quaerat": "delectus",
                    "sit": "porro",
                    "labore": "molestias",
                },
                "qui": {
                    "ullam": "nihil",
                    "ut": "incidunt",
                    "quibusdam": "doloremque",
                },
            },
        ),
        tax_amount=5244.63,
        total_amount=6772.03,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=129394,
)

res = s.direct_costs.create_direct_cost(req)

if res.create_direct_cost_response is not None:
    # handle response
```