# Customers


## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `links`                                                                                           | [models.Links](../models/links.md)                                                                | :heavy_check_mark:                                                                                | N/A                                                                                               | {<br/>"self": {<br/>"href": "/companies"<br/>},<br/>"current": {<br/>"href": "/companies?page=1\u0026pageSize=10"<br/>}<br/>} |
| `page_number`                                                                                     | *int*                                                                                             | :heavy_check_mark:                                                                                | Current page number.                                                                              |                                                                                                   |
| `page_size`                                                                                       | *int*                                                                                             | :heavy_check_mark:                                                                                | Number of items to return in results array.                                                       |                                                                                                   |
| `total_results`                                                                                   | *int*                                                                                             | :heavy_check_mark:                                                                                | Total number of items.                                                                            |                                                                                                   |
| `results`                                                                                         | List[[models.Customer](../models/customer.md)]                                                    | :heavy_minus_sign:                                                                                | N/A                                                                                               |                                                                                                   |