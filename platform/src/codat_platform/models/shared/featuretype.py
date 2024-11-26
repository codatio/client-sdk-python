"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class FeatureType(str, Enum):
    r"""The type of feature."""

    GET = "Get"
    POST = "Post"
    CATEGORIZATION = "Categorization"
    DELETE = "Delete"
    PUT = "Put"
    GET_AS_PDF = "GetAsPdf"
    DOWNLOAD_ATTACHMENT = "DownloadAttachment"
    GET_ATTACHMENT = "GetAttachment"
    GET_ATTACHMENTS = "GetAttachments"
    UPLOAD_ATTACHMENT = "UploadAttachment"
