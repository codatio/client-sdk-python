"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errormessage as shared_errormessage
from ..shared import supplier as shared_supplier
from ..shared import updatesupplierresponse as shared_updatesupplierresponse
from typing import Optional



@dataclasses.dataclass
class UpdateSupplierRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    supplier_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'supplierId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a supplier"""
    force_update: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'forceUpdate', 'style': 'form', 'explode': True }})
    r"""When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check."""
    supplier: Optional[shared_supplier.Supplier] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class UpdateSupplierResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""The request made is not valid."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    update_supplier_response: Optional[shared_updatesupplierresponse.UpdateSupplierResponse] = dataclasses.field(default=None)
    r"""Success"""
    
