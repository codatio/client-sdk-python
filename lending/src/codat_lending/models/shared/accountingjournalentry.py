"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .journalentryrecordref import JournalEntryRecordRef, JournalEntryRecordRefTypedDict
from .journalline import JournalLine, JournalLineTypedDict
from .journalref import JournalRef, JournalRefTypedDict
from .metadata import Metadata, MetadataTypedDict
from .supplementaldata import SupplementalData, SupplementalDataTypedDict
from codat_lending.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountingJournalEntryTypedDict(TypedDict):
    r"""> **Language tip:** For the top-level record of a company's financial transactions, refer to the [Journals](https://docs.codat.io/lending-api#/schemas/Journal) data type

    ## Overview

    A journal entry report shows the entries made in a company's general ledger, or [accounts](https://docs.codat.io/lending-api#/schemas/Account), when transactions are approved. The journal line items for each journal entry should balance.

    A journal entry line item is a single transaction line on the journal entry. For example:

    - When a journal entry is recording a receipt of cash, the credit to accounts receivable and the debit to cash are separate line items.
    - When a company needs to recognise revenue from an annual contract on a monthly basis, on receipt of cash for month one, they make a debit to deferred income and a credit to revenue.

    In Codat a journal entry contains details of:

    - The date on which the entry was created and posted.
    - Itemised lines, including amounts and currency.
    - A reference to the associated accounts.
    - A reference to the underlying record. For example, the invoice, bill, or other data type that triggered the posting of the journal entry to the general ledger.

    > **Pushing journal entries**
    > Codat only supports journal entries in the base currency of the company that are pushed into accounts denominated in the same base currency.
    """

    created_on: NotRequired[str]
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
    description: NotRequired[Nullable[str]]
    r"""Optional description of the journal entry."""
    id: NotRequired[str]
    r"""Unique identifier of the journal entry for the company in the accounting software."""
    journal_lines: NotRequired[Nullable[List[JournalLineTypedDict]]]
    r"""An array of journal lines."""
    journal_ref: NotRequired[JournalRefTypedDict]
    r"""Links journal entries to the relevant journal in accounting integrations that use multi-book accounting (multiple journals)."""
    metadata: NotRequired[MetadataTypedDict]
    modified_date: NotRequired[str]
    posted_on: NotRequired[str]
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
    record_ref: NotRequired[JournalEntryRecordRefTypedDict]
    r"""Links a journal entry to the underlying record that created it."""
    source_modified_date: NotRequired[str]
    supplemental_data: NotRequired[SupplementalDataTypedDict]
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """
    updated_on: NotRequired[str]
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


class AccountingJournalEntry(BaseModel):
    r"""> **Language tip:** For the top-level record of a company's financial transactions, refer to the [Journals](https://docs.codat.io/lending-api#/schemas/Journal) data type

    ## Overview

    A journal entry report shows the entries made in a company's general ledger, or [accounts](https://docs.codat.io/lending-api#/schemas/Account), when transactions are approved. The journal line items for each journal entry should balance.

    A journal entry line item is a single transaction line on the journal entry. For example:

    - When a journal entry is recording a receipt of cash, the credit to accounts receivable and the debit to cash are separate line items.
    - When a company needs to recognise revenue from an annual contract on a monthly basis, on receipt of cash for month one, they make a debit to deferred income and a credit to revenue.

    In Codat a journal entry contains details of:

    - The date on which the entry was created and posted.
    - Itemised lines, including amounts and currency.
    - A reference to the associated accounts.
    - A reference to the underlying record. For example, the invoice, bill, or other data type that triggered the posting of the journal entry to the general ledger.

    > **Pushing journal entries**
    > Codat only supports journal entries in the base currency of the company that are pushed into accounts denominated in the same base currency.
    """

    created_on: Annotated[Optional[str], pydantic.Field(alias="createdOn")] = None
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

    description: OptionalNullable[str] = UNSET
    r"""Optional description of the journal entry."""

    id: Optional[str] = None
    r"""Unique identifier of the journal entry for the company in the accounting software."""

    journal_lines: Annotated[
        OptionalNullable[List[JournalLine]], pydantic.Field(alias="journalLines")
    ] = UNSET
    r"""An array of journal lines."""

    journal_ref: Annotated[Optional[JournalRef], pydantic.Field(alias="journalRef")] = (
        None
    )
    r"""Links journal entries to the relevant journal in accounting integrations that use multi-book accounting (multiple journals)."""

    metadata: Optional[Metadata] = None

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None

    posted_on: Annotated[Optional[str], pydantic.Field(alias="postedOn")] = None
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

    record_ref: Annotated[
        Optional[JournalEntryRecordRef], pydantic.Field(alias="recordRef")
    ] = None
    r"""Links a journal entry to the underlying record that created it."""

    source_modified_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceModifiedDate")
    ] = None

    supplemental_data: Annotated[
        Optional[SupplementalData], pydantic.Field(alias="supplementalData")
    ] = None
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """

    updated_on: Annotated[Optional[str], pydantic.Field(alias="updatedOn")] = None
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

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "createdOn",
            "description",
            "id",
            "journalLines",
            "journalRef",
            "metadata",
            "modifiedDate",
            "postedOn",
            "recordRef",
            "sourceModifiedDate",
            "supplementalData",
            "updatedOn",
        ]
        nullable_fields = ["description", "journalLines"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
