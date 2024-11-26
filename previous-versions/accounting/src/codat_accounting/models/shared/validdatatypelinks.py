"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_accounting.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, TypedDict
from typing_extensions import NotRequired


class ValidDataTypeLinksTypedDict(TypedDict):
    r"""When querying Codat's data model, some data types return `validDatatypeLinks` metadata in the JSON response. This indicates where that object can be used as a reference—a _valid link_—when creating or updating other data.

    For example, `validDatatypeLinks` might indicate the following references:

    - Which tax rates are valid to use on the line item of a bill.
    - Which items can be used when creating an invoice.

    You can use `validDatatypeLinks` to present your SMB customers with only valid choices when selecting objects from a list, for example.

    ## `validDatatypeLinks` example

    The following example uses the `Accounting.Accounts` data type. It shows that, on the linked integration, this account is valid as the account on a payment or bill payment; and as the account referenced on the line item of a direct income or direct cost. Because there is no valid link to Invoices or Bills, using this account on those data types will result in an error.

    ```json validDatatypeLinks for an account
    {
    \"id\": \"bd9e85e0-0478-433d-ae9f-0b3c4f04bfe4\",
    \"nominalCode\": \"090\",
    \"name\": \"Business Bank Account\",
    #...
    \"validDatatypeLinks\": [
    {
    \"property\": \"Id\",
    \"links\": [
    \"Payment.AccountRef.Id\",
    \"BillPayment.AccountRef.Id\",
    \"DirectIncome.LineItems.AccountRef.Id\",
    \"DirectCost.LineItems.AccountRef.Id\"
    ]
    }
    ]
    }
    ```



    ## Support for `validDatatypeLinks`

    Codat currently supports `validDatatypeLinks` for some data types on our Xero, QuickBooks Online, QuickBooks Desktop, Exact (NL), and Sage Business Cloud integrations.

    If you'd like us to extend support to more data types or integrations, suggest or vote for this on our <a href=\"https://portal.productboard.com/codat/5-product-roadmap\">Product Roadmap</a>.
    """

    links: NotRequired[Nullable[List[str]]]
    r"""Supported `dataTypes` that the record can be linked to."""
    property: NotRequired[Nullable[str]]
    r"""The property from the account that can be linked."""


class ValidDataTypeLinks(BaseModel):
    r"""When querying Codat's data model, some data types return `validDatatypeLinks` metadata in the JSON response. This indicates where that object can be used as a reference—a _valid link_—when creating or updating other data.

    For example, `validDatatypeLinks` might indicate the following references:

    - Which tax rates are valid to use on the line item of a bill.
    - Which items can be used when creating an invoice.

    You can use `validDatatypeLinks` to present your SMB customers with only valid choices when selecting objects from a list, for example.

    ## `validDatatypeLinks` example

    The following example uses the `Accounting.Accounts` data type. It shows that, on the linked integration, this account is valid as the account on a payment or bill payment; and as the account referenced on the line item of a direct income or direct cost. Because there is no valid link to Invoices or Bills, using this account on those data types will result in an error.

    ```json validDatatypeLinks for an account
    {
    \"id\": \"bd9e85e0-0478-433d-ae9f-0b3c4f04bfe4\",
    \"nominalCode\": \"090\",
    \"name\": \"Business Bank Account\",
    #...
    \"validDatatypeLinks\": [
    {
    \"property\": \"Id\",
    \"links\": [
    \"Payment.AccountRef.Id\",
    \"BillPayment.AccountRef.Id\",
    \"DirectIncome.LineItems.AccountRef.Id\",
    \"DirectCost.LineItems.AccountRef.Id\"
    ]
    }
    ]
    }
    ```



    ## Support for `validDatatypeLinks`

    Codat currently supports `validDatatypeLinks` for some data types on our Xero, QuickBooks Online, QuickBooks Desktop, Exact (NL), and Sage Business Cloud integrations.

    If you'd like us to extend support to more data types or integrations, suggest or vote for this on our <a href=\"https://portal.productboard.com/codat/5-product-roadmap\">Product Roadmap</a>.
    """

    links: OptionalNullable[List[str]] = UNSET
    r"""Supported `dataTypes` that the record can be linked to."""

    property: OptionalNullable[str] = UNSET
    r"""The property from the account that can be linked."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["links", "property"]
        nullable_fields = ["links", "property"]
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