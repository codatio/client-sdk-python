"""Retry configuration matching Speakeasy SDK surface, with runtime backoff loop."""

from __future__ import annotations

import random
import time
import urllib3
from datetime import datetime
from email.utils import parsedate_to_datetime
from typing import Any, Callable, Iterable, List, Optional, Set


class BackoffStrategy:
    initial_interval: int
    max_interval: int
    exponent: float
    max_elapsed_time: int

    def __init__(
        self,
        initial_interval: int = 500,
        max_interval: int = 60000,
        exponent: float = 1.5,
        max_elapsed_time: int = 3600000,
    ):
        self.initial_interval = initial_interval
        self.max_interval = max_interval
        self.exponent = exponent
        self.max_elapsed_time = max_elapsed_time


class RetryConfig:
    strategy: str
    backoff: BackoffStrategy
    retry_connection_errors: bool

    def __init__(
        self,
        strategy: str = "backoff",
        backoff: Optional[BackoffStrategy] = None,
        retry_connection_errors: bool = True,
    ):
        self.strategy = strategy
        self.backoff = backoff if backoff is not None else BackoffStrategy()
        self.retry_connection_errors = retry_connection_errors


class Retries:
    config: RetryConfig
    status_codes: List[str]

    def __init__(self, config: RetryConfig, status_codes: List[str]):
        self.config = config
        self.status_codes = status_codes


# Default retryable status codes from the OAS (x-speakeasy-retries.statusCodes).
# Entries may be ints or strings like "5XX" denoting wildcards across a hundred-block.
DEFAULT_RETRY_STATUS_CODES: List[Any] = [408, 429, '5XX']


def _matches_status(code: int, retry_codes: Iterable[Any]) -> bool:
    for entry in retry_codes:
        if isinstance(entry, int) and entry == code:
            return True
        if isinstance(entry, str):
            entry_u = entry.upper()
            if entry_u.endswith("XX") and len(entry_u) == 3 and entry_u[0].isdigit():
                if (code // 100) == int(entry_u[0]):
                    return True
            else:
                try:
                    if int(entry_u) == code:
                        return True
                except ValueError:
                    pass
    return False


def _retry_after_ms(exc: Any) -> Optional[int]:
    """Milliseconds to wait from a response's Retry-After header, or None if absent.
    Accepts an integer number of seconds or an HTTP date, matching Speakeasy and the
    TypeScript runtime. A past date clamps to 0."""
    headers = getattr(exc, "headers", None)
    if not headers:
        return None
    getter = getattr(headers, "get", None)
    if getter is None:
        return None
    value = getter("Retry-After")
    if value is None:
        value = getter("retry-after")
    if value is None:
        return None
    text = str(value).strip()
    if text.isdigit():
        return int(text) * 1000
    try:
        parsed = parsedate_to_datetime(text)
    except (TypeError, ValueError):
        return None
    if parsed is None:
        return None
    now = datetime.now(parsed.tzinfo) if parsed.tzinfo is not None else datetime.utcnow()
    delta_ms = int((parsed - now).total_seconds() * 1000)
    return delta_ms if delta_ms > 0 else 0


def execute_with_retries(
    call_fn: Callable[[], Any],
    retry_config: Optional[RetryConfig],
    retry_status_codes: Optional[Iterable[Any]] = None,
) -> Any:
    """Run call_fn() and retry on retryable failures per retry_config.

    `retry_config=None` means nothing was supplied, so fall back to the default backoff
    policy (retry by default, matching Speakeasy). A RetryConfig with strategy "none"
    disables retries -> just one attempt. `retry_status_codes` falls back to
    DEFAULT_RETRY_STATUS_CODES.
    """
    if retry_config is None:
        retry_config = RetryConfig()
    if getattr(retry_config, "strategy", "backoff") == "none":
        return call_fn()

    codes = retry_status_codes if retry_status_codes is not None else DEFAULT_RETRY_STATUS_CODES
    backoff = retry_config.backoff
    elapsed_ms = 0
    attempt = 0
    last_exc: Optional[BaseException] = None
    while True:
        try:
            return call_fn()
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status is None:
                status = getattr(exc, "status_code", None)
            is_retryable_status = isinstance(status, int) and _matches_status(status, codes)
            is_conn_err = retry_config.retry_connection_errors and (
                status == 0 or isinstance(exc, urllib3.exceptions.HTTPError)
            )
            if not (is_retryable_status or is_conn_err):
                raise
            last_exc = exc

        # Decide sleep duration; abort if total elapsed exceeds budget
        retry_after_ms = _retry_after_ms(last_exc)
        if retry_after_ms is not None:
            sleep_ms = min(retry_after_ms, backoff.max_interval)
        else:
            interval = min(
                backoff.initial_interval * (backoff.exponent ** attempt),
                backoff.max_interval,
            )
            # half-jitter
            sleep_ms = int(interval / 2 + random.random() * (interval / 2))
        if elapsed_ms + sleep_ms > backoff.max_elapsed_time:
            if last_exc is not None:
                raise last_exc
            return None
        time.sleep(sleep_ms / 1000.0)
        elapsed_ms += sleep_ms
        attempt += 1


__all__ = [
    "BackoffStrategy",
    "RetryConfig",
    "Retries",
    "DEFAULT_RETRY_STATUS_CODES",
    "execute_with_retries",
]
