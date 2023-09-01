"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import accountingsupplier as shared_accountingsupplier
from ..shared import errormessage as shared_errormessage
from typing import Optional



@dataclasses.dataclass
class GetAccountingSupplierRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    supplier_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'supplierId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a supplier"""
    




@dataclasses.dataclass
class GetAccountingSupplierResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    accounting_supplier: Optional[shared_accountingsupplier.AccountingSupplier] = dataclasses.field(default=None)
    r"""Success"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

