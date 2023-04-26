# suppliers

## Overview

Suppliers

### Available Operations

* [create](#create) - Create supplier
* [download_attachment](#download_attachment) - Download supplier attachment
* [get](#get) - Get supplier
* [get_attachment](#get_attachment) - Get supplier attachment
* [get_create_update_model](#get_create_update_model) - Get create/update supplier model
* [list](#list) - List suppliers
* [list_attachments](#list_attachments) - List supplier attachments
* [update](#update) - Update supplier

## create

Push suppliers

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating suppliers.

### Example Usage

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
                city="Thousand Oaks",
                country="Papua New Guinea",
                line1="amet",
                line2="tempore",
                postal_code="81317",
                region="adipisci",
                type="Unknown",
            ),
        ],
        contact_name="alias",
        default_currency="occaecati",
        email_address="perspiciatis",
        id="83663c66-dcbb-47df-acb0-9c8b408e0713",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="molestiae",
        phone="489.499.8000 x854",
        registration_number="praesentium",
        source_modified_date="aperiam",
        status="Archived",
        supplemental_data=shared.SupplementalData(
            content={
                "doloremque": {
                    "eius": "odio",
                    "rerum": "provident",
                    "nostrum": "perferendis",
                    "aliquam": "accusantium",
                },
            },
        ),
        supplier_name="possimus",
        tax_number="vel",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=796063,
)

res = s.suppliers.create(req)

if res.create_supplier_response is not None:
    # handle response
```

## download_attachment

Download supplier attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadSupplierAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    supplier_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.suppliers.download_attachment(req)

if res.data is not None:
    # handle response
```

## get

Gets a single supplier corresponding to the given ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSupplierRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    supplier_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.suppliers.get(req)

if res.supplier is not None:
    # handle response
```

## get_attachment

Get supplier attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSupplierAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    supplier_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.suppliers.get_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_create_update_model

Get create/update supplier model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating and updating suppliers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateUpdateSuppliersModelRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.suppliers.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

## list

Gets the latest suppliers for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListSuppliersRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="blanditiis",
)

res = s.suppliers.list(req)

if res.suppliers is not None:
    # handle response
```

## list_attachments

Get supplier attachments

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListSupplierAttachmentsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    supplier_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.suppliers.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## update

Update supplier

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support updating suppliers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateSupplierRequest(
    supplier=shared.Supplier(
        addresses=[
            shared.Addressesitems(
                city="Lake Gabriellashire",
                country="Afghanistan",
                line1="perferendis",
                line2="aspernatur",
                postal_code="04820",
                region="dolore",
                type="Billing",
            ),
            shared.Addressesitems(
                city="Mountain View",
                country="Armenia",
                line1="alias",
                line2="sit",
                postal_code="98150-1458",
                region="quidem",
                type="Unknown",
            ),
            shared.Addressesitems(
                city="Watersfurt",
                country="Syrian Arab Republic",
                line1="suscipit",
                line2="ut",
                postal_code="40961",
                region="corporis",
                type="Unknown",
            ),
        ],
        contact_name="alias",
        default_currency="ratione",
        email_address="sed",
        id="3b2c09b9-2477-41f5-a69e-5b7ec7626649",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="possimus",
        phone="487-692-7981 x1448",
        registration_number="sit",
        source_modified_date="expedita",
        status="Active",
        supplemental_data=shared.SupplementalData(
            content={
                "repellat": {
                    "atque": "iure",
                    "nulla": "aliquid",
                    "asperiores": "similique",
                },
                "veniam": {
                    "vel": "earum",
                    "corrupti": "temporibus",
                    "libero": "sapiente",
                },
                "praesentium": {
                    "qui": "asperiores",
                },
            },
        ),
        supplier_name="blanditiis",
        tax_number="nesciunt",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    supplier_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    timeout_in_minutes=721212,
)

res = s.suppliers.update(req)

if res.update_supplier_response is not None:
    # handle response
```
