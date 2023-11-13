"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import supplementaldataconfiguration as shared_supplementaldataconfiguration
from enum import Enum
from typing import Optional

class DataType(str, Enum):
    r"""Data types that support supplemental data"""
    CHART_OF_ACCOUNTS = 'chartOfAccounts'
    BILLS = 'bills'
    COMPANY = 'company'
    CREDIT_NOTES = 'creditNotes'
    CUSTOMERS = 'customers'
    INVOICES = 'invoices'
    ITEMS = 'items'
    JOURNAL_ENTRIES = 'journalEntries'
    SUPPLIERS = 'suppliers'
    TAX_RATES = 'taxRates'
    COMMERCE_COMPANY_INFO = 'commerce-companyInfo'
    COMMERCE_CUSTOMERS = 'commerce-customers'
    COMMERCE_DISPUTES = 'commerce-disputes'
    COMMERCE_LOCATIONS = 'commerce-locations'
    COMMERCE_ORDERS = 'commerce-orders'
    COMMERCE_PAYMENTS = 'commerce-payments'
    COMMERCE_PAYMENT_METHODS = 'commerce-paymentMethods'
    COMMERCE_PRODUCTS = 'commerce-products'
    COMMERCE_PRODUCT_CATEGORIES = 'commerce-productCategories'
    COMMERCE_TAX_COMPONENTS = 'commerce-taxComponents'
    COMMERCE_TRANSACTIONS = 'commerce-transactions'


@dataclasses.dataclass
class ConfigureSupplementalDataRequest:
    data_type: DataType = dataclasses.field(metadata={'path_param': { 'field_name': 'dataType', 'style': 'simple', 'explode': False }})
    r"""Supported supplemental data data type."""
    platform_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'platformKey', 'style': 'simple', 'explode': False }})
    r"""A unique 4-letter key to represent a platform in each integration. View [accounting](https://docs.codat.io/integrations/accounting/overview#platform-keys), [banking](https://docs.codat.io/integrations/banking/overview#platform-keys), and [commerce](https://docs.codat.io/integrations/commerce/overview#platform-keys) platform keys."""
    supplemental_data_configuration: Optional[shared_supplementaldataconfiguration.SupplementalDataConfiguration] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""The configuration for the specified platform and data type."""
    



@dataclasses.dataclass
class ConfigureSupplementalDataResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

