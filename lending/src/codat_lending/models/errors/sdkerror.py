"""SDKError — fallback exception for any HTTP error."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from .codatlendingerror import CodatLendingError


MAX_MESSAGE_LEN = 10_000


class SDKError(CodatLendingError):
    """The fallback error class if no more specific error class is matched."""

    def __init__(
        self,
        message: str,
        raw_response: Optional[Any] = None,
        body: Optional[str] = None,
        status_code: Optional[int] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        # `raw_response` is the 2nd positional arg to match Speakeasy
        # (`SDKError(message, raw_response, body)`); existing consumer code that
        # re-raises via `SDKError(msg, response)` then stores the response in
        # `raw_response`, not `status_code`. status_code / body are derived from
        # raw_response when not passed explicitly.
        if status_code is None:
            status_code = getattr(raw_response, "status_code", None) or getattr(raw_response, "status", None) or 0
        body_display = body or (getattr(raw_response, "text", "") if raw_response is not None else "") or ""
        if message:
            message += ": "
        message += f"Status {status_code}"
        if body_display:
            if len(body_display) > MAX_MESSAGE_LEN:
                body_display = body_display[:MAX_MESSAGE_LEN] + f"...and {len(body_display) - MAX_MESSAGE_LEN} more chars"
            message += f". Body: {body_display}"
        super().__init__(message.strip(), status_code=status_code, body=body or "", headers=headers, raw_response=raw_response)
