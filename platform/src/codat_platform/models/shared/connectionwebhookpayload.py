"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .companyreference import CompanyReference, CompanyReferenceTypedDict
from .connection import Connection, ConnectionTypedDict
from codat_platform.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ConnectionWebhookPayloadTypedDict(TypedDict):
    connection: NotRequired[ConnectionTypedDict]
    r"""A connection represents a [company's](https://docs.codat.io/platform-api#/schemas/Company) connection to a data source and allows you to synchronize data (pull and/or push) with that source.

    A company can have multiple data connections depending on the type of data source it is connecting to. For example, a single company can link to:

    - [Accounting data](https://docs.codat.io/accounting-api/overview) - 1 active connection.
    - [Banking data](https://docs.codat.io/banking-api/overview) - Multiple active connections.
    - [Commerce data](https://docs.codat.io/commerce-api/overview) - Multiple active connections.
    Any combination of accounting, banking, and commerce data connections is allowed.

    Before you can use a data connection to pull or push data, the company must grant you access to their business data by [linking the connection](https://docs.codat.io/auth-flow/overview).
    """
    reference_company: NotRequired[CompanyReferenceTypedDict]


class ConnectionWebhookPayload(BaseModel):
    connection: Optional[Connection] = None
    r"""A connection represents a [company's](https://docs.codat.io/platform-api#/schemas/Company) connection to a data source and allows you to synchronize data (pull and/or push) with that source.

    A company can have multiple data connections depending on the type of data source it is connecting to. For example, a single company can link to:

    - [Accounting data](https://docs.codat.io/accounting-api/overview) - 1 active connection.
    - [Banking data](https://docs.codat.io/banking-api/overview) - Multiple active connections.
    - [Commerce data](https://docs.codat.io/commerce-api/overview) - Multiple active connections.
    Any combination of accounting, banking, and commerce data connections is allowed.

    Before you can use a data connection to pull or push data, the company must grant you access to their business data by [linking the connection](https://docs.codat.io/auth-flow/overview).
    """

    reference_company: Annotated[
        Optional[CompanyReference], pydantic.Field(alias="referenceCompany")
    ] = None
