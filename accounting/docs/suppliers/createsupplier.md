# create_supplier
Available in: `suppliers`

Push suppliers

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating suppliers.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateSupplierRequest(
    supplier=shared.Supplier(
        addresses=[
            shared.Addressesitems(
                city="Corpus Christi",
                country="Gambia",
                line1="incidunt",
                line2="eos",
                postal_code="40680-2176",
                region="optio",
                type="Delivery",
            ),
        ],
        contact_name="debitis",
        default_currency="corporis",
        email_address="neque",
        id="2b6526f8-6285-43fe-a859-ce322231fe66",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        phone="1-472-281-9763 x876",
        registration_number="sit",
        source_modified_date="2022-10-23T00:00:00Z",
        status="Active",
        supplemental_data=shared.SupplementalData(
            content={
                "tempore": {
                    "at": "fugit",
                    "cupiditate": "dicta",
                    "libero": "recusandae",
                },
                "libero": {
                    "quae": "eaque",
                    "est": "sed",
                    "dolorum": "laborum",
                },
                "atque": {
                    "aliquam": "perspiciatis",
                    "labore": "esse",
                },
            },
        ),
        supplier_name="unde",
        tax_number="recusandae",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=842306,
)

res = s.suppliers.create_supplier(req)

if res.create_supplier_response is not None:
    # handle response
```