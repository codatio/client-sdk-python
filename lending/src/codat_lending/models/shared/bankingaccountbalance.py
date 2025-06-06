"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountbalanceamounts import AccountBalanceAmounts, AccountBalanceAmountsTypedDict
from codat_lending.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BankingAccountBalanceTypedDict(TypedDict):
    r"""The Banking Account Balances data type provides a list of balances for a bank account including end-of-day batch balance or running balances per transaction.

    Responses are paged, so you should provide `page` and `pageSize` query parameters in your request.

    > **How often should I pull Account Balances?**
    >
    > Because these balances are closing balances, we recommend you pull Account Balance no more frequently than daily. If you require a live intraday balance, this can be found for each account on the [Account](https://docs.codat.io/lending-api#/schemas/Account) data type.
    >
    > Whilst you can choose to sync hourly, this may incur usage charges from Plaid or TrueLayer.
    """

    account_id: str
    r"""The unique identifier of the account."""
    balance: AccountBalanceAmountsTypedDict
    r"""Depending on the data provided by the underlying bank, not all balances are always available."""
    date_: str
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```



    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:

    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`

    > Time zones
    >
    > Not all dates from Codat will contain information about time zones.
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """
    modified_date: NotRequired[str]
    source_modified_date: NotRequired[str]


class BankingAccountBalance(BaseModel):
    r"""The Banking Account Balances data type provides a list of balances for a bank account including end-of-day batch balance or running balances per transaction.

    Responses are paged, so you should provide `page` and `pageSize` query parameters in your request.

    > **How often should I pull Account Balances?**
    >
    > Because these balances are closing balances, we recommend you pull Account Balance no more frequently than daily. If you require a live intraday balance, this can be found for each account on the [Account](https://docs.codat.io/lending-api#/schemas/Account) data type.
    >
    > Whilst you can choose to sync hourly, this may incur usage charges from Plaid or TrueLayer.
    """

    account_id: Annotated[str, pydantic.Field(alias="accountId")]
    r"""The unique identifier of the account."""

    balance: AccountBalanceAmounts
    r"""Depending on the data provided by the underlying bank, not all balances are always available."""

    date_: Annotated[str, pydantic.Field(alias="date")]
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```



    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:

    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`

    > Time zones
    >
    > Not all dates from Codat will contain information about time zones.
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None

    source_modified_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceModifiedDate")
    ] = None
