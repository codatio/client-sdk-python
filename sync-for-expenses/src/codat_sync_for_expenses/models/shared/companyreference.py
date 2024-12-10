"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_expenses.types import BaseModel
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class CompanyReferenceLinksTypedDict(TypedDict):
    r"""A collection of links for the company."""

    portal: NotRequired[str]
    r"""Link to the company page in the portal."""


class CompanyReferenceLinks(BaseModel):
    r"""A collection of links for the company."""

    portal: Optional[str] = None
    r"""Link to the company page in the portal."""


class CompanyReferenceTypedDict(TypedDict):
    description: NotRequired[str]
    r"""Additional information about the company. This can be used to store foreign IDs, references, etc."""
    id: NotRequired[str]
    r"""Unique identifier for your SMB in Codat."""
    links: NotRequired[CompanyReferenceLinksTypedDict]
    r"""A collection of links for the company."""
    name: NotRequired[str]
    r"""The name of the company"""
    tags: NotRequired[Dict[str, str]]
    r"""A collection of user-defined key-value pairs that store custom metadata against the company."""


class CompanyReference(BaseModel):
    description: Optional[str] = None
    r"""Additional information about the company. This can be used to store foreign IDs, references, etc."""

    id: Optional[str] = None
    r"""Unique identifier for your SMB in Codat."""

    links: Optional[CompanyReferenceLinks] = None
    r"""A collection of links for the company."""

    name: Optional[str] = None
    r"""The name of the company"""

    tags: Optional[Dict[str, str]] = None
    r"""A collection of user-defined key-value pairs that store custom metadata against the company."""