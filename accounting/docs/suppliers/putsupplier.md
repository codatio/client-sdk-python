# put_supplier
Available in: `suppliers`

Push supplier

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support updating suppliers.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.PutSupplierRequest(
    supplier=shared.Supplier(
        addresses=[
            shared.Addressesitems(
                city="Roswell",
                country="United Kingdom",
                line1="ducimus",
                line2="libero",
                postal_code="07954",
                region="a",
                type="Unknown",
            ),
            shared.Addressesitems(
                city="Yvonneburgh",
                country="Mexico",
                line1="fugit",
                line2="esse",
                postal_code="04461",
                region="dolore",
                type="Delivery",
            ),
        ],
        contact_name="incidunt",
        default_currency="consequatur",
        email_address="porro",
        id="8f08bff1-081e-488f-8699-6c8e22be0a3c",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        phone="445.627.8129 x54400",
        registration_number="minus",
        source_modified_date="2022-10-23T00:00:00Z",
        status="Active",
        supplemental_data=shared.SupplementalData(
            content={
                "porro": {
                    "voluptatum": "consectetur",
                    "aliquam": "magni",
                },
            },
        ),
        supplier_name="in",
        tax_number="ipsum",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    supplier_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    timeout_in_minutes=774266,
)

res = s.suppliers.put_supplier(req)

if res.put_supplier_200_application_json_object is not None:
    # handle response
```