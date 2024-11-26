# ExpensesSyncWebhookPayload


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `reference_company`                                                          | [Optional[shared.CompanyReference]](../../models/shared/companyreference.md) | :heavy_minus_sign:                                                           | N/A                                                                          |
| `sync_id`                                                                    | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Unique identifier of the sync.                                               |
| `transactions`                                                               | List[[shared.Transaction](../../models/shared/transaction.md)]               | :heavy_minus_sign:                                                           | N/A                                                                          |