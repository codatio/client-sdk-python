# create_customer
Available in: `customers`

Posts an individual customer for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating customers.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateCustomerRequest(
    customer=shared.Customer(
        addresses=[
            shared.Addressesitems(
                city="Pasco",
                country="French Polynesia",
                line1="unde",
                line2="consequatur",
                postal_code="74731",
                region="culpa",
                type="Delivery",
            ),
            shared.Addressesitems(
                city="Port Marcoschester",
                country="Democratic People's Republic of Korea",
                line1="totam",
                line2="incidunt",
                postal_code="76181-2098",
                region="tenetur",
                type="Billing",
            ),
        ],
        contact_name="dolor",
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city="North Margieland",
                    country="Botswana",
                    line1="veniam",
                    line2="non",
                    postal_code="17849-8333",
                    region="voluptatem",
                    type="Billing",
                ),
                email="Bridget.Bogan53@yahoo.com",
                modified_date="2022-10-23T00:00:00Z",
                name="Clifford Stiedemann",
                phone=[
                    shared.PhoneNumbersitems(
                        number="voluptas",
                        type="Landline",
                    ),
                    shared.PhoneNumbersitems(
                        number="eum",
                        type="Landline",
                    ),
                    shared.PhoneNumbersitems(
                        number="cumque",
                        type="Primary",
                    ),
                ],
                status="Unknown",
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city="Batzport",
                    country="Bouvet Island (Bouvetoya)",
                    line1="veritatis",
                    line2="similique",
                    postal_code="41812-6487",
                    region="libero",
                    type="Billing",
                ),
                email="Emil82@hotmail.com",
                modified_date="2022-10-23T00:00:00Z",
                name="Freddie Conroy",
                phone=[
                    shared.PhoneNumbersitems(
                        number="atque",
                        type="Primary",
                    ),
                    shared.PhoneNumbersitems(
                        number="dolores",
                        type="Unknown",
                    ),
                ],
                status="Archived",
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city="North Carrie",
                    country="Samoa",
                    line1="deleniti",
                    line2="esse",
                    postal_code="12079-3259",
                    region="corrupti",
                    type="Billing",
                ),
                email="Joan68@hotmail.com",
                modified_date="2022-10-23T00:00:00Z",
                name="James Reynolds",
                phone=[
                    shared.PhoneNumbersitems(
                        number="dicta",
                        type="Unknown",
                    ),
                    shared.PhoneNumbersitems(
                        number="dolores",
                        type="Primary",
                    ),
                    shared.PhoneNumbersitems(
                        number="eum",
                        type="Unknown",
                    ),
                    shared.PhoneNumbersitems(
                        number="corporis",
                        type="Unknown",
                    ),
                ],
                status="Active",
            ),
        ],
        customer_name="sequi",
        default_currency="illo",
        email_address="temporibus",
        id="0081090f-6706-4673-b3a6-81c5768dce74",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        phone="1-405-711-3805",
        registration_number="voluptas",
        source_modified_date="2022-10-23T00:00:00Z",
        status="Unknown",
        supplemental_data=shared.SupplementalData(
            content={
                "tempora": {
                    "cupiditate": "officia",
                    "minima": "doloribus",
                    "suscipit": "sequi",
                },
            },
        ),
        tax_number="debitis",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=207202,
)

res = s.customers.create_customer(req)

if res.create_customer_response is not None:
    # handle response
```