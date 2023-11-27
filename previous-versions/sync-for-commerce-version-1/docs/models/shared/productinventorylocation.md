# ProductInventoryLocation


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `location_ref`                                                     | [Optional[shared.LocationRef]](../../models/shared/locationref.md) | :heavy_minus_sign:                                                 | Reference to the geographic location where the order was placed.   |
| `quantity`                                                         | *Optional[Decimal]*                                                | :heavy_minus_sign:                                                 | The quantity of stock remaining at location.                       |