"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_payables_version_1.models.shared import supplier as shared_supplier
from codat_sync_for_payables_version_1.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_sync_for_payables_version_1.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateSupplierRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    supplier_id: str
    r"""Unique identifier for a supplier."""
    supplier: NotRequired[Nullable[shared_supplier.SupplierTypedDict]]
    force_update: NotRequired[bool]
    r"""When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting software, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check."""
    timeout_in_minutes: NotRequired[int]
    r"""Time limit for the push operation to complete before it is timed out."""


class UpdateSupplierRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    connection_id: Annotated[
        str,
        pydantic.Field(alias="connectionId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a connection."""

    supplier_id: Annotated[
        str,
        pydantic.Field(alias="supplierId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a supplier."""

    supplier: Annotated[
        OptionalNullable[shared_supplier.Supplier],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = UNSET

    force_update: Annotated[
        Optional[bool],
        pydantic.Field(alias="forceUpdate"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting software, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check."""

    timeout_in_minutes: Annotated[
        Optional[int],
        pydantic.Field(alias="timeoutInMinutes"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Time limit for the push operation to complete before it is timed out."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["Supplier", "forceUpdate", "timeoutInMinutes"]
        nullable_fields = ["Supplier"]
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
