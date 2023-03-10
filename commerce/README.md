# codat-commerce

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install codat-commerce
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat()
s.config_security(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    )
)
   
req = operations.GetCommerceInfoRequest(
    path_params=operations.GetCommerceInfoPathParams(
        company_id="unde",
        connection_id="deserunt",
    ),
)
    
res = s.company_info.get_commerce_info(req)

if res.source_modified_date is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations


### company_info

* `get_commerce_info` - Get company info

### customers

* `list_commerce_customers` - List customers

### disputes

* `list_commerce_disputes` - List disputes

### locations

* `list_commerce_locations` - List locations

### orders

* `list_commerce_orders` - List orders

### payments

* `list_commerce_payment_methods` - List payment methods
* `list_commerce_payments` - List payments

### products

* `list_commerce_product_categories` - List product categories
* `list_commerce_products` - List products

### tax_components

* `get_companies_company_id_connections_connection_id_data_commerce_tax_components` - List tax components

### transactions

* `list_commerce_transactions` - List transactions
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
