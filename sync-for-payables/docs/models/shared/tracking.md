# Tracking

Categories, and a project and customer, against which the item is tracked.


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `category_refs`                                                             | list[[TrackingCategoryRef](../../models/shared/trackingcategoryref.md)]     | :heavy_check_mark:                                                          | N/A                                                                         |
| `customer_ref`                                                              | [Optional[TrackingCustomerRef]](../../models/shared/trackingcustomerref.md) | :heavy_minus_sign:                                                          | N/A                                                                         |
| `is_billed_to`                                                              | [BilledToType](../../models/shared/billedtotype.md)                         | :heavy_check_mark:                                                          | N/A                                                                         |
| `is_rebilled_to`                                                            | [BilledToType](../../models/shared/billedtotype.md)                         | :heavy_check_mark:                                                          | N/A                                                                         |
| `project_ref`                                                               | [Optional[TrackingProjectRef]](../../models/shared/trackingprojectref.md)   | :heavy_minus_sign:                                                          | N/A                                                                         |