# create_item
Available in: `items`

Posts a new item to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create item model](https://docs.codat.io/accounting-api#/operations/get-create-items-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items) for integrations that support creating items.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateItemRequest(
    item=shared.Item(
        bill_item=shared.BillItem(
            account_ref=shared.AccountRef(
                id="2743fd6c-2a10-4e6c-a978-ec256a5b0922",
                name="Melba Schmeler",
            ),
            description="dignissimos",
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=6172.71,
                id="96c977bb-c57f-4389-a8a8-600c58d67d63",
                name="Eddie Murphy",
            ),
            unit_price=3900.58,
        ),
        code="quos",
        id="464579cf-c6c0-4e50-bf56-831f1d8ed87b",
        invoice_item=shared.InvoiceItem(
            account_ref=shared.AccountRef(
                id="28e8afab-c986-4e24-9e43-b2342417d13e",
                name="Miss Jeannie Hudson",
            ),
            description="cupiditate",
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=6338.87,
                id="e4ae8ab4-a9c4-492c-9e8b-a5d4aa4a508b",
                name="Miss Rodney Ledner",
            ),
            unit_price=5704.27,
        ),
        is_bill_item=False,
        is_invoice_item=False,
        item_status="Active",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        name="Jordan Stiedemann",
        source_modified_date="2022-10-23T00:00:00Z",
        type="beatae",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=697543,
)

res = s.items.create_item(req)

if res.create_item_response is not None:
    # handle response
```