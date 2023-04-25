# list_product_categories
Available in: `products`

Product categories are used to classify a group of products together, either by type (eg "Furniture"), or sometimes by tax profile.

## Example Usage
```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListProductCategoriesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="nulla",
)

res = s.products.list_product_categories(req)

if res.product_categories is not None:
    # handle response
```