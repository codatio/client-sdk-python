"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accounttransactionline import AccountTransactionLine, AccountTransactionLineTypedDict
from .bankaccountref import BankAccountRef, BankAccountRefTypedDict
from .metadata import Metadata, MetadataTypedDict
from codat_lending.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
from enum import Enum
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AccountingAccountTransactionStatus(str, Enum):
    r"""The status of the account transaction."""
    UNKNOWN = "Unknown"
    UNRECONCILED = "Unreconciled"
    RECONCILED = "Reconciled"
    VOID = "Void"

class AccountingAccountTransactionTypedDict(TypedDict):
    r"""> **Language tip:** In Codat, account transactions represent all transactions posted to a bank account within an accounting software. For bank transactions posted within a banking platform, refer to [Banking transactions](https://docs.codat.io/lending-api#/operations/list-all-banking-transactions).

    > View the coverage for account transactions in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=accountTransactions\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    In Codat’s data model, account transactions represent bank activity within an accounting software. All transactions that go through a bank account are recorded as account transactions.

    Account transactions are created as a result of different business activities, for example:

    * Payments: for example, receiving money for payment against an invoice.
    * Bill payments: for example, spending money for a payment against a bill.
    * Direct costs: for example, withdrawing money from a bank account, either for cash purposes or to make a payment.
    * Direct incomes: for example, selling an item directly to a contact and receiving payment at point of sale.
    * Transfers: for example, transferring money between two bank accounts.

    Account transactions is the parent data type of [payments](https://docs.codat.io/lending-api#/schemas/Payment), [bill payments](https://docs.codat.io/lending-api#/schemas/BillPayment), [direct costs](https://docs.codat.io/lending-api#/schemas/DirectCost), [direct incomes](https://docs.codat.io/lending-api#/schemas/DirectIncome), and [transfers](https://docs.codat.io/lending-api#/schemas/Transfer).
    """
    
    bank_account_ref: NotRequired[BankAccountRefTypedDict]
    r"""Links to the Account transactions data type."""
    currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    currency_rate: NotRequired[Nullable[Decimal]]
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.

    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.

    It is not possible to perform the currency conversion with two or more non-base currencies participating in the transaction. For example, if a company's base currency is USD, and it has a bill issued in EUR, then the bill payment must happen in USD or EUR.

    Where the currency rate is provided by the underlying accounting software, it will be available from Codat with the same precision (up to a maximum of 9 decimal places).

    For accounting software which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.

    ## Examples with base currency of GBP

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |

    ## Examples with base currency of USD

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |


    ### Integration-specific details

    | Integration       | Scenario                                        | System behavior                                                                                                                                                      |
    |-------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | QuickBooks Online | Transaction currency differs from base currency | If currency rate value is left `null`, a rate of 1 will be used by QBO by default. To override this, specify a currencyRate in the request body.  |
    """
    date_: NotRequired[str]
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
    id: NotRequired[str]
    r"""Identifier of the direct cost (unique to the company)."""
    lines: NotRequired[Nullable[List[AccountTransactionLineTypedDict]]]
    r"""Array of account transaction lines."""
    metadata: NotRequired[MetadataTypedDict]
    modified_date: NotRequired[str]
    note: NotRequired[Nullable[str]]
    r"""Additional information about the account transaction, if available."""
    source_modified_date: NotRequired[str]
    status: NotRequired[AccountingAccountTransactionStatus]
    r"""The status of the account transaction."""
    total_amount: NotRequired[Decimal]
    r"""Total amount of the account transactions, inclusive of tax."""
    transaction_id: NotRequired[Nullable[str]]
    r"""Identifier of the transaction (unique to the company)."""
    

class AccountingAccountTransaction(BaseModel):
    r"""> **Language tip:** In Codat, account transactions represent all transactions posted to a bank account within an accounting software. For bank transactions posted within a banking platform, refer to [Banking transactions](https://docs.codat.io/lending-api#/operations/list-all-banking-transactions).

    > View the coverage for account transactions in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=accountTransactions\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    In Codat’s data model, account transactions represent bank activity within an accounting software. All transactions that go through a bank account are recorded as account transactions.

    Account transactions are created as a result of different business activities, for example:

    * Payments: for example, receiving money for payment against an invoice.
    * Bill payments: for example, spending money for a payment against a bill.
    * Direct costs: for example, withdrawing money from a bank account, either for cash purposes or to make a payment.
    * Direct incomes: for example, selling an item directly to a contact and receiving payment at point of sale.
    * Transfers: for example, transferring money between two bank accounts.

    Account transactions is the parent data type of [payments](https://docs.codat.io/lending-api#/schemas/Payment), [bill payments](https://docs.codat.io/lending-api#/schemas/BillPayment), [direct costs](https://docs.codat.io/lending-api#/schemas/DirectCost), [direct incomes](https://docs.codat.io/lending-api#/schemas/DirectIncome), and [transfers](https://docs.codat.io/lending-api#/schemas/Transfer).
    """
    
    bank_account_ref: Annotated[Optional[BankAccountRef], pydantic.Field(alias="bankAccountRef")] = None
    r"""Links to the Account transactions data type."""
    currency: Optional[str] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    currency_rate: Annotated[Annotated[OptionalNullable[Decimal], BeforeValidator(validate_decimal), PlainSerializer(serialize_decimal(False))], pydantic.Field(alias="currencyRate")] = UNSET
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.

    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.

    It is not possible to perform the currency conversion with two or more non-base currencies participating in the transaction. For example, if a company's base currency is USD, and it has a bill issued in EUR, then the bill payment must happen in USD or EUR.

    Where the currency rate is provided by the underlying accounting software, it will be available from Codat with the same precision (up to a maximum of 9 decimal places).

    For accounting software which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.

    ## Examples with base currency of GBP

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |

    ## Examples with base currency of USD

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |


    ### Integration-specific details

    | Integration       | Scenario                                        | System behavior                                                                                                                                                      |
    |-------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | QuickBooks Online | Transaction currency differs from base currency | If currency rate value is left `null`, a rate of 1 will be used by QBO by default. To override this, specify a currencyRate in the request body.  |
    """
    date_: Annotated[Optional[str], pydantic.Field(alias="date")] = None
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
    id: Optional[str] = None
    r"""Identifier of the direct cost (unique to the company)."""
    lines: OptionalNullable[List[AccountTransactionLine]] = UNSET
    r"""Array of account transaction lines."""
    metadata: Optional[Metadata] = None
    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None
    note: OptionalNullable[str] = UNSET
    r"""Additional information about the account transaction, if available."""
    source_modified_date: Annotated[Optional[str], pydantic.Field(alias="sourceModifiedDate")] = None
    status: Optional[AccountingAccountTransactionStatus] = None
    r"""The status of the account transaction."""
    total_amount: Annotated[Annotated[Optional[Decimal], BeforeValidator(validate_decimal), PlainSerializer(serialize_decimal(False))], pydantic.Field(alias="totalAmount")] = None
    r"""Total amount of the account transactions, inclusive of tax."""
    transaction_id: Annotated[OptionalNullable[str], pydantic.Field(alias="transactionId")] = UNSET
    r"""Identifier of the transaction (unique to the company)."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["bankAccountRef", "currency", "currencyRate", "date", "id", "lines", "metadata", "modifiedDate", "note", "sourceModifiedDate", "status", "totalAmount", "transactionId"]
        nullable_fields = ["currencyRate", "lines", "note", "transactionId"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
