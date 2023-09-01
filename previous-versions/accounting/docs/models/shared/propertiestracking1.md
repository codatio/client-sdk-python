# Propertiestracking1

Categories, and a project and customer, against which the item is tracked.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `category_refs`                                                         | list[[TrackingCategoryRef](../../models/shared/trackingcategoryref.md)] | :heavy_check_mark:                                                      | N/A                                                                     |
| `customer_ref`                                                          | [Optional[CustomerRef]](../../models/shared/customerref.md)             | :heavy_minus_sign:                                                      | N/A                                                                     |
| `is_billed_to`                                                          | [BilledToType1](../../models/shared/billedtotype1.md)                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `is_rebilled_to`                                                        | [BilledToType1](../../models/shared/billedtotype1.md)                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `project_ref`                                                           | [Optional[ProjectRef]](../../models/shared/projectref.md)               | :heavy_minus_sign:                                                      | N/A                                                                     |