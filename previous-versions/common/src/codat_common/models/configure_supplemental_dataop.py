"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .supplementaldataconfiguration import (
    SupplementalDataConfiguration,
    SupplementalDataConfigurationTypedDict,
)
from codat_common.types import BaseModel
from codat_common.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from enum import Enum
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ConfigureSupplementalDataPathParamDataType(str, Enum):
    r"""Data types that support supplemental data"""

    CHART_OF_ACCOUNTS = "chartOfAccounts"
    BILLS = "bills"
    COMPANY = "company"
    CREDIT_NOTES = "creditNotes"
    CUSTOMERS = "customers"
    INVOICES = "invoices"
    ITEMS = "items"
    JOURNAL_ENTRIES = "journalEntries"
    SUPPLIERS = "suppliers"
    TAX_RATES = "taxRates"
    COMMERCE_COMPANY_INFO = "commerce-companyInfo"
    COMMERCE_CUSTOMERS = "commerce-customers"
    COMMERCE_DISPUTES = "commerce-disputes"
    COMMERCE_LOCATIONS = "commerce-locations"
    COMMERCE_ORDERS = "commerce-orders"
    COMMERCE_PAYMENTS = "commerce-payments"
    COMMERCE_PAYMENT_METHODS = "commerce-paymentMethods"
    COMMERCE_PRODUCTS = "commerce-products"
    COMMERCE_PRODUCT_CATEGORIES = "commerce-productCategories"
    COMMERCE_TAX_COMPONENTS = "commerce-taxComponents"
    COMMERCE_TRANSACTIONS = "commerce-transactions"


class ConfigureSupplementalDataRequestTypedDict(TypedDict):
    data_type: ConfigureSupplementalDataPathParamDataType
    r"""Supported supplemental data data type."""
    platform_key: str
    r"""A unique 4-letter key to represent a platform in each integration."""
    supplemental_data_configuration: NotRequired[SupplementalDataConfigurationTypedDict]
    r"""The configuration for the specified platform and data type."""


class ConfigureSupplementalDataRequest(BaseModel):
    data_type: Annotated[
        ConfigureSupplementalDataPathParamDataType,
        pydantic.Field(alias="dataType"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Supported supplemental data data type."""

    platform_key: Annotated[
        str,
        pydantic.Field(alias="platformKey"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""A unique 4-letter key to represent a platform in each integration."""

    supplemental_data_configuration: Annotated[
        Optional[SupplementalDataConfiguration],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""The configuration for the specified platform and data type."""
