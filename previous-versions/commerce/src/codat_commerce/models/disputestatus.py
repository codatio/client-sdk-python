"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class DisputeStatus(str, Enum):
    r"""Current status of the dispute"""

    WON = "Won"
    LOST = "Lost"
    ACCEPTED = "Accepted"
    PROCESSING = "Processing"
    CHARGE_REFUNDED = "ChargeRefunded"
    EVIDENCE_REQUIRED = "EvidenceRequired"
    INQUIRY_EVIDENCE_REQUIRED = "InquiryEvidenceRequired"
    INQUIRY_PROCESSING = "InquiryProcessing"
    INQUIRY_CLOSED = "InquiryClosed"
    WAITING_THIRD_PARTY = "WaitingThirdParty"
    UNKNOWN = "Unknown"