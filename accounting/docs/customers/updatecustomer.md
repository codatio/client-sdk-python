# update_customer
Available in: `customers`

Posts an updated customer for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support updating customers.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateCustomerRequest(
    customer=shared.Customer(
        addresses=[
            shared.Addressesitems(
                city="Southaven",
                country="Nicaragua",
                line1="dolorem",
                line2="velit",
                postal_code="88422-5292",
                region="dolorum",
                type="Billing",
            ),
            shared.Addressesitems(
                city="Morissettestad",
                country="Trinidad and Tobago",
                line1="modi",
                line2="assumenda",
                postal_code="24833-7563",
                region="nostrum",
                type="Delivery",
            ),
            shared.Addressesitems(
                city="North Cristina",
                country="Tuvalu",
                line1="inventore",
                line2="ipsum",
                postal_code="25121-0504",
                region="cum",
                type="Delivery",
            ),
        ],
        contact_name="ratione",
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city="Port Adriana",
                    country="Mongolia",
                    line1="sed",
                    line2="harum",
                    postal_code="42290-1225",
                    region="pariatur",
                    type="Billing",
                ),
                email="Virgie_Gleichner15@yahoo.com",
                modified_date="2022-10-23T00:00:00Z",
                name="Tabitha Toy",
                phone=[
                    shared.PhoneNumbersitems(
                        number="veritatis",
                        type="Primary",
                    ),
                    shared.PhoneNumbersitems(
                        number="quod",
                        type="Fax",
                    ),
                    shared.PhoneNumbersitems(
                        number="sapiente",
                        type="Unknown",
                    ),
                ],
                status="Active",
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city="New Raleigh",
                    country="Palau",
                    line1="voluptatibus",
                    line2="modi",
                    postal_code="61494",
                    region="error",
                    type="Delivery",
                ),
                email="Pierce.McCullough83@gmail.com",
                modified_date="2022-10-23T00:00:00Z",
                name="Michelle Trantow",
                phone=[
                    shared.PhoneNumbersitems(
                        number="neque",
                        type="Fax",
                    ),
                    shared.PhoneNumbersitems(
                        number="repellendus",
                        type="Landline",
                    ),
                    shared.PhoneNumbersitems(
                        number="quisquam",
                        type="Mobile",
                    ),
                ],
                status="Archived",
            ),
        ],
        customer_name="doloremque",
        default_currency="adipisci",
        email_address="quasi",
        id="08d9c337-4730-482b-94f2-ab1fd5671e9c",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        phone="342.406.2441",
        registration_number="aliquam",
        source_modified_date="2022-10-23T00:00:00Z",
        status="Unknown",
        supplemental_data=shared.SupplementalData(
            content={
                "blanditiis": {
                    "quisquam": "itaque",
                    "consequatur": "recusandae",
                    "iste": "error",
                },
                "dicta": {
                    "unde": "numquam",
                    "temporibus": "omnis",
                },
            },
        ),
        tax_number="amet",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    customer_id="deserunt",
    force_update=False,
    timeout_in_minutes=495515,
)

res = s.customers.update_customer(req)

if res.update_customer_response is not None:
    # handle response
```