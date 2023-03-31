"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class InvoiceStatusEnum(str, Enum):
    r"""Current state of the invoice:
    
    - `Draft` - Invoice hasn't been submitted to the supplier. It may be in a pending state or is scheduled for future submission, for example by email.
    - `Submitted` - Invoice is no longer a draft. It has been processed and, or, sent to the customer. In this state, it will impact the ledger. It also has no payments made against it (amountDue == totalAmount).
    - `PartiallyPaid` - The balance paid against the invoice is positive, but less than the total invoice amount (0 < amountDue < totalAmount).
    - `Paid` - Invoice is paid in full. This includes if the invoice has been credited or overpaid (amountDue == 0).
    - `Void` - An invoice can become Void when it's deleted, refunded, written off, or cancelled. A voided invoice may still be PartiallyPaid, and so all outstanding amounts on voided invoices are removed from the accounts receivable account.
    """
    UNKNOWN = "Unknown"
    DRAFT = "Draft"
    SUBMITTED = "Submitted"
    PARTIALLY_PAID = "PartiallyPaid"
    PAID = "Paid"
    VOID = "Void"
