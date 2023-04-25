# customers

## Overview

Customers

### Available Operations

* [create_customer](#create_customer) - Create customer
* [download_customer_attachment](#download_customer_attachment) - Download customer attachment
* [get_create_update_customers_model](#get_create_update_customers_model) - Get create/update customer model
* [get_customer](#get_customer) - Get customer
* [get_customer_attachment](#get_customer_attachment) - Get customer attachment
* [get_customer_attachments](#get_customer_attachments) - List customer attachments
* [get_customers](#get_customers) - List customers
* [update_customer](#update_customer) - Update customer

## create_customer

Posts an individual customer for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating customers.

### Example Usage

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
                city="Jerrodfield",
                country="Morocco",
                line1="maxime",
                line2="culpa",
                postal_code="90218-8486",
                region="est",
                type="Delivery",
            ),
        ],
        contact_name="occaecati",
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city="Port Malachi",
                    country="New Zealand",
                    line1="beatae",
                    line2="quod",
                    postal_code="95903-8950",
                    region="amet",
                    type="Billing",
                ),
                email="Jerome49@gmail.com",
                modified_date="deleniti",
                name="Anna Mayer",
                phone=[
                    shared.PhoneNumbersitems(
                        number="eius",
                        type="Primary",
                    ),
                    shared.PhoneNumbersitems(
                        number="recusandae",
                        type="Landline",
                    ),
                    shared.PhoneNumbersitems(
                        number="aliquam",
                        type="Fax",
                    ),
                    shared.PhoneNumbersitems(
                        number="voluptatum",
                        type="Landline",
                    ),
                ],
                status="Unknown",
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city="Hayleeborough",
                    country="Montenegro",
                    line1="iusto",
                    line2="optio",
                    postal_code="01218",
                    region="inventore",
                    type="Unknown",
                ),
                email="Bertha9@yahoo.com",
                modified_date="dolorum",
                name="Shaun Johnston",
                phone=[
                    shared.PhoneNumbersitems(
                        number="nemo",
                        type="Fax",
                    ),
                    shared.PhoneNumbersitems(
                        number="quidem",
                        type="Unknown",
                    ),
                    shared.PhoneNumbersitems(
                        number="aliquid",
                        type="Landline",
                    ),
                    shared.PhoneNumbersitems(
                        number="atque",
                        type="Mobile",
                    ),
                ],
                status="Archived",
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city="Fort Odie",
                    country="Bulgaria",
                    line1="nobis",
                    line2="voluptatum",
                    postal_code="16007",
                    region="saepe",
                    type="Delivery",
                ),
                email="Laurie4@yahoo.com",
                modified_date="quae",
                name="Veronica Kutch",
                phone=[
                    shared.PhoneNumbersitems(
                        number="libero",
                        type="Unknown",
                    ),
                ],
                status="Archived",
            ),
        ],
        customer_name="nihil",
        default_currency="similique",
        email_address="repellat",
        id="ded84a35-a412-438e-9a73-5ac26ae33bef",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="provident",
        phone="265.924.7861 x004",
        registration_number="delectus",
        source_modified_date="officiis",
        status="Active",
        supplemental_data=shared.SupplementalData(
            content={
                "ipsam": {
                    "esse": "vitae",
                    "beatae": "pariatur",
                    "voluptatem": "blanditiis",
                },
                "eligendi": {
                    "deleniti": "deleniti",
                    "necessitatibus": "cumque",
                    "iste": "reiciendis",
                    "nihil": "libero",
                },
            },
        ),
        tax_number="perspiciatis",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=577273,
)

res = s.customers.create_customer(req)

if res.create_customer_response is not None:
    # handle response
```

## download_customer_attachment

Download customer attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadCustomerAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    customer_id="officia",
)

res = s.customers.download_customer_attachment(req)

if res.data is not None:
    # handle response
```

## get_create_update_customers_model

Get create/update customer model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating and updating customers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateUpdateCustomersModelRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.customers.get_create_update_customers_model(req)

if res.push_option is not None:
    # handle response
```

## get_customer

Gets a single customer corresponding to the given ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCustomerRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    customer_id="nemo",
)

res = s.customers.get_customer(req)

if res.customer is not None:
    # handle response
```

## get_customer_attachment

Get  customer attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCustomerAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    customer_id="quis",
)

res = s.customers.get_customer_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_customer_attachments

Get customer attachments

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCustomerAttachmentsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    customer_id="doloremque",
)

res = s.customers.get_customer_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## get_customers

Gets the latest customers for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCustomersRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="similique",
)

res = s.customers.get_customers(req)

if res.customers is not None:
    # handle response
```

## update_customer

Posts an updated customer for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support updating customers.

### Example Usage

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
                city="South Sydni",
                country="Somalia",
                line1="dolor",
                line2="ratione",
                postal_code="77078",
                region="laudantium",
                type="Delivery",
            ),
            shared.Addressesitems(
                city="Jonesborough",
                country="Eritrea",
                line1="consectetur",
                line2="qui",
                postal_code="55487-4912",
                region="quisquam",
                type="Billing",
            ),
        ],
        contact_name="ipsam",
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city="North Kamron",
                    country="Nauru",
                    line1="beatae",
                    line2="nemo",
                    postal_code="06400",
                    region="unde",
                    type="Billing",
                ),
                email="Julianne_Wintheiser@gmail.com",
                modified_date="earum",
                name="Tomas Kiehn",
                phone=[
                    shared.PhoneNumbersitems(
                        number="perferendis",
                        type="Landline",
                    ),
                    shared.PhoneNumbersitems(
                        number="saepe",
                        type="Primary",
                    ),
                    shared.PhoneNumbersitems(
                        number="architecto",
                        type="Primary",
                    ),
                ],
                status="Unknown",
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city="Port Clifford",
                    country="Lithuania",
                    line1="excepturi",
                    line2="alias",
                    postal_code="03183-7963",
                    region="blanditiis",
                    type="Billing",
                ),
                email="Winona49@gmail.com",
                modified_date="quidem",
                name="Teri Abshire",
                phone=[
                    shared.PhoneNumbersitems(
                        number="numquam",
                        type="Mobile",
                    ),
                ],
                status="Unknown",
            ),
        ],
        customer_name="hic",
        default_currency="blanditiis",
        email_address="at",
        id="e30f069d-8106-418d-97e1-52297510da80",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="amet",
        phone="(315) 377-3071",
        registration_number="laborum",
        source_modified_date="in",
        status="Unknown",
        supplemental_data=shared.SupplementalData(
            content={
                "distinctio": {
                    "sint": "odio",
                    "repudiandae": "accusamus",
                    "quasi": "accusantium",
                },
            },
        ),
        tax_number="dolores",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    customer_id="fugiat",
    force_update=False,
    timeout_in_minutes=664312,
)

res = s.customers.update_customer(req)

if res.update_customer_response is not None:
    # handle response
```
