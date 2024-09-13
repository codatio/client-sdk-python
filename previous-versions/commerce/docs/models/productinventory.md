# ProductInventory

Information about the total inventory as well as the locations inventory is in.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `locations`                                                                    | List[[models.ProductInventoryLocation](../models/productinventorylocation.md)] | :heavy_minus_sign:                                                             | N/A                                                                            |
| `total_quantity`                                                               | *OptionalNullable[Decimal]*                                                    | :heavy_minus_sign:                                                             | The total quantity of stock remaining across locations.                        |