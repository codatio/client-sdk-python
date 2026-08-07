"""ErrorMessage — typed exception raised for structured Codat API errors.

Raised when an HTTP response body parses against the ErrorMessage schema
(i.e. Codat-shaped error envelopes with correlationId, statusCode, etc.).
"""

from __future__ import annotations

from typing import Any, Mapping, Optional

from .codatsyncpayableserror import CodatSyncPayablesError
from codat_sync_for_payables.models.error_message import ErrorMessage as ErrorMessageData


class ErrorMessage(CodatSyncPayablesError):
    """Typed Codat API error response. Access structured fields via `.data`."""

    data: ErrorMessageData

    def __init__(
        self,
        data: ErrorMessageData,
        raw_response: Optional[Any] = None,
        body: Optional[str] = None,
        status_code: Optional[int] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        # `raw_response` is the 2nd positional arg to match Speakeasy
        # (`ErrorMessage(data, raw_response, body)`).
        message = body or str(data)
        super().__init__(
            message,
            raw_response=raw_response,
            body=body,
            status_code=status_code,
            headers=headers,
        )
        self.data = data


__all__ = ["ErrorMessage", "ErrorMessageData"]
