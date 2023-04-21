"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class FeatureTypeEnum(str, Enum):
    GET = 'Get'
    POST = 'Post'
    CATEGORIZATION = 'Categorization'
    DELETE = 'Delete'
    PUT = 'Put'
    GET_AS_PDF = 'GetAsPdf'
    DOWNLOAD_ATTACHMENT = 'DownloadAttachment'
    GET_ATTACHMENT = 'GetAttachment'
    GET_ATTACHMENTS = 'GetAttachments'
    UPLOAD_ATTACHMENT = 'UploadAttachment'