from typing import Any

import backoff
import httpx
from forge_utils import logger


def log_backoff(details: Any) -> None:
    msg = (
        f"Tentativa {details['tries']} após {details['wait']:0.1f}s "
        f"por {details['target'].__name__}"
    )
    logger.warning(msg)

def is_retryable_error(exc: Exception) -> bool:
    if isinstance(exc, httpx.HTTPStatusError):
        return exc.response.status_code in {429, 500, 502, 503, 504}
    return isinstance(exc, httpx.RequestError)

def retry_with_backoff() -> Any:
    return backoff.on_exception(
        backoff.expo,
        (httpx.RequestError, httpx.HTTPStatusError),
        max_tries=4,
        jitter=backoff.full_jitter,
        on_backoff=log_backoff,
        giveup=lambda e: not is_retryable_error(e)
    )
