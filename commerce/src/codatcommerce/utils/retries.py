"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import random
import time

import requests


class BackoffStrategy:
    initial_interval: int
    max_interval: int
    exponent: float
    max_elapsed_time: int

    def __init__(self, initial_interval: int, max_interval: int, exponent: float, max_elapsed_time: int):
        self.initial_interval = initial_interval
        self.max_interval = max_interval
        self.exponent = exponent
        self.max_elapsed_time = max_elapsed_time


class RetryConfig:
    strategy: str
    backoff: BackoffStrategy
    retry_connection_errors: bool

    def __init__(self, strategy: str, retry_connection_errors: bool):
        self.strategy = strategy
        self.retry_connection_errors = retry_connection_errors


class Retries:
    config: RetryConfig
    status_codes: list[str]

    def __init__(self, config: RetryConfig, status_codes: list[str]):
        self.config = config
        self.status_codes = status_codes


class TemporaryError(Exception):
    response: requests.Response

    def __init__(self, response: requests.Response):
        self.response = response


class PermanentError(Exception):
    inner: Exception

    def __init__(self, inner: Exception):
        self.inner = inner


def retry(func, retries: Retries):
    if retries.config.strategy == 'backoff':
        def do_request():
            res: requests.Response
            try:
                res = func()

                for code in retries.status_codes:
                    if "X" in code.upper():
                        code_range = int(code[0])

                        status_major = res.status_code / 100

                        if status_major >= code_range and status_major < code_range + 1:
                            raise TemporaryError(res)
                    else:
                        parsed_code = int(code)

                        if res.status_code == parsed_code:
                            raise TemporaryError(res)
            except requests.exceptions.ConnectionError as exception:
                if not retries.config.config.retry_connection_errors:
                    raise

                raise PermanentError(exception) from exception
            except requests.exceptions.Timeout as exception:
                if not retries.config.config.retry_connection_errors:
                    raise

                raise PermanentError(exception) from exception
            except TemporaryError:
                raise
            except Exception as exception:
                raise PermanentError(exception) from exception

            return res

        return retry_with_backoff(do_request, retries.config.backoff.initial_interval, retries.config.backoff.max_interval, retries.config.backoff.exponent, retries.config.backoff.max_elapsed_time)

    return func()


def retry_with_backoff(func, initial_interval=500, max_interval=60000, exponent=1.5, max_elapsed_time=3600000):
    start = round(time.time()*1000)
    retries = 0

    while True:
        try:
            return func()
        except PermanentError as exception:
            raise exception.inner
        except Exception as exception:  # pylint: disable=broad-exception-caught
            now = round(time.time()*1000)
            if now - start > max_elapsed_time:
                if isinstance(exception, TemporaryError):
                    return exception.response

                raise
            sleep = ((initial_interval/1000) *
                     exponent**retries + random.uniform(0, 1))
            if sleep > max_interval/1000:
                sleep = max_interval/1000
            time.sleep(sleep)
            retries += 1