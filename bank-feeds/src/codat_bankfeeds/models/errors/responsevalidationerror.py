"""ResponseValidationError — raised when a successful HTTP response body cannot be parsed against the expected response model."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from .codatbankfeedserror import CodatBankFeedsError


class ResponseValidationError(CodatBankFeedsError):
    """Raised on a pydantic ValidationError when deserialising a Codat response body."""

    def __init__(
        self,
        message: str,
        raw_response: Optional[Any] = None,
        cause: Optional[Exception] = None,
        body: str = "",
        status_code: Optional[int] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        # `raw_response` is the 2nd positional arg, `cause` the 3rd, to match
        # Speakeasy (`ResponseValidationError(message, raw_response, cause, body)`).
        full_message = f"{message}: {cause}"
        super().__init__(
            full_message,
            raw_response=raw_response,
            body=body,
            status_code=status_code,
            headers=headers,
        )
        # Surface the underlying pydantic ValidationError via the standard `__cause__` mechanism
        # so callers can do `except errors.ResponseValidationError as e: print(e.cause)`.
        self.__cause__ = cause

    @property
    def cause(self) -> Optional[BaseException]:
        """Normally the underlying pydantic ValidationError."""
        return self.__cause__


__all__ = ["ResponseValidationError"]
