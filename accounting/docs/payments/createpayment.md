# create_payment
Available in: `payments`

Posts a new payment to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create payment model](https://docs.codat.io/accounting-api#/operations/get-create-payments-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) for integrations that support creating payments.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreatePaymentRequest(
    payment=shared.Payment(
        account_ref=shared.AccountRef(
            id="60629451-4c3d-4b9c-a9f3-8bd2be878703",
            name="Cora Ferry",
        ),
        currency="provident",
        currency_rate=6660.49,
        customer_ref=shared.CustomerRef(
            company_name="mollitia",
            id="8465a328-3279-4b71-9d1c-ea673d86e3b3",
        ),
        date_="2022-10-23T00:00:00Z",
        id="5e49a313-5778-4ce5-8cac-b0e3ea975045",
        lines=[
            shared.PaymentLine(
                allocated_on_date="2022-10-23T00:00:00Z",
                amount=6257.74,
                links=[
                    shared.PaymentLineLink(
                        amount=9916.87,
                        currency_rate=4113.08,
                        id="3b215186-ab5e-43a0-a261-4315d1568299",
                        type="Discount",
                    ),
                    shared.PaymentLineLink(
                        amount=3778.77,
                        currency_rate=1003.06,
                        id="afc7186f-f20b-47a7-bdf4-0ca0d7657c16",
                        type="Invoice",
                    ),
                    shared.PaymentLineLink(
                        amount=698.78,
                        currency_rate=7166.01,
                        id="bf055271-b251-41dd-a06d-d1b28272bc9c",
                        type="Unlinked",
                    ),
                    shared.PaymentLineLink(
                        amount=1694.68,
                        currency_rate=1257.69,
                        id="1697b188-0fcb-4b2b-93c1-5f670bd17848",
                        type="Unlinked",
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date="2022-10-23T00:00:00Z",
                amount=1228.58,
                links=[
                    shared.PaymentLineLink(
                        amount=3516.07,
                        currency_rate=2234.48,
                        id="eeb3b6e2-41c3-4109-9836-63c66dcbb7df",
                        type="CreditNote",
                    ),
                    shared.PaymentLineLink(
                        amount=7852.92,
                        currency_rate=7427.38,
                        id="09c8b408-e071-4377-8de4-fee101d9780a",
                        type="Unlinked",
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date="2022-10-23T00:00:00Z",
                amount=434.45,
                links=[
                    shared.PaymentLineLink(
                        amount=2602.42,
                        currency_rate=4839.58,
                        id="b95040d6-c8b2-4a5f-8022-07e4048f9000",
                        type="Payment",
                    ),
                    shared.PaymentLineLink(
                        amount=9351.45,
                        currency_rate=8479.43,
                        id="290278eb-4ae9-4d64-961e-91500323b2c0",
                        type="Refund",
                    ),
                    shared.PaymentLineLink(
                        amount=7176.59,
                        currency_rate=6050.35,
                        id="24771f56-69e5-4b7e-8762-6649d84eb9e4",
                        type="PaymentOnAccount",
                    ),
                    shared.PaymentLineLink(
                        amount=9525.87,
                        currency_rate=8696.62,
                        id="2276e0b8-8fb8-47d6-ba5b-6e8dbf812f83",
                        type="PaymentOnAccount",
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="inventore",
        payment_method_ref=shared.PaymentMethodRef(
            id="ca6a9ffc-5619-429c-8a95-60a1395918da",
            name="Hope Gusikowski",
        ),
        reference="nihil",
        source_modified_date="2022-10-23T00:00:00Z",
        supplemental_data=shared.SupplementalData(
            content={
                "officiis": {
                    "quisquam": "asperiores",
                },
                "praesentium": {
                    "inventore": "ab",
                    "dolore": "amet",
                    "nulla": "officia",
                    "natus": "nesciunt",
                },
                "eaque": {
                    "nobis": "magni",
                    "nihil": "laborum",
                    "aut": "voluptatum",
                },
            },
        ),
        total_amount=6542.99,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=969433,
)

res = s.payments.create_payment(req)

if res.create_payment_response is not None:
    # handle response
```