# create_bill_payment
Available in: `bill_payments`

Posts a new bill payment to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create bill payment model](https://docs.codat.io/accounting-api#/operations/get-create-billPayments-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating bill payments.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateBillPaymentRequest(
    bill_payment=shared.BillPayment(
        account_ref=shared.AccountRef(
            id="825c1fc0-e115-4c80-bff9-18544ec42def",
            name="Gregg Torp",
        ),
        currency="ab",
        currency_rate=5734.44,
        date_="2022-10-23T00:00:00Z",
        id="77773e63-562a-47b4-88f0-5e3d48fdaf31",
        lines=[
            shared.BillPaymentLine(
                allocated_on_date="2022-10-23T00:00:00Z",
                amount=6308.32,
                links=[
                    shared.BillPaymentLineLink(
                        amount=9979.95,
                        currency_rate=3632.14,
                        id="fd94259c-0b36-4f25-aa94-4f3b756c11f6",
                        type="Refund",
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="dolor",
        payment_method_ref=shared.PaymentMethodRef(
            id="7a512624-3835-4bbc-85a2-3a45cefc5fde",
            name="Miss Linda Nader",
        ),
        reference="quia",
        source_modified_date="2022-10-23T00:00:00Z",
        supplemental_data=shared.SupplementalData(
            content={
                "vel": {
                    "debitis": "ullam",
                    "architecto": "accusantium",
                    "perferendis": "veritatis",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="9c6dc5e3-4762-4799-bfbb-e6949fb2bb4e",
            supplier_name="quod",
        ),
        total_amount=6646.66,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=904440,
)

res = s.bill_payments.create_bill_payment(req)

if res.create_bill_payment_response is not None:
    # handle response
```