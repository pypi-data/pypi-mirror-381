"""Retry strategy for API requests with exponential backoff."""

import logging
from typing import List, Optional

logger = logging.getLogger(__name__)


class RetryStrategy:
    """
    Shared retry logic for both sync and async clients.

    Implements exponential backoff with configurable retry conditions.
    """

    def __init__(
        self,
        max_retries: int = 3,
        retry_on: Optional[List[int]] = None,
    ):
        """
        Initialize retry strategy.

        Args:
            max_retries: Maximum number of retry attempts
            retry_on: HTTP status codes to retry on (default: [500, 502, 503, 504])
        """
        self.max_retries = max_retries
        self.retry_on = retry_on or [500, 502, 503, 504]

    def should_retry(self, attempt: int, status_code: int) -> bool:
        """
        Determine if request should be retried.

        Args:
            attempt: Current attempt number (0-indexed)
            status_code: HTTP status code from response

        Returns:
            True if request should be retried, False otherwise
        """
        return (
            status_code in self.retry_on
            and attempt < self.max_retries - 1
        )

    def should_retry_on_exception(self, attempt: int) -> bool:
        """
        Determine if request should be retried on exception.

        Args:
            attempt: Current attempt number (0-indexed)

        Returns:
            True if request should be retried, False otherwise
        """
        return attempt < self.max_retries - 1

    def calculate_wait_time(self, attempt: int) -> float:
        """
        Calculate exponential backoff wait time.

        Args:
            attempt: Current attempt number (0-indexed)

        Returns:
            Wait time in seconds (capped at 60 seconds)
        """
        return min(2 ** attempt, 60)

    def log_retry(
        self,
        attempt: int,
        reason: str,
        wait_time: float,
        is_async: bool = False
    ) -> None:
        """
        Log retry attempt.

        Args:
            attempt: Current attempt number (0-indexed)
            reason: Reason for retry
            wait_time: Wait time before retry
            is_async: Whether this is an async client
        """
        client_type = "Async" if is_async else "Sync"
        logger.warning(
            f"[{client_type}] {reason}, retrying in {wait_time}s "
            f"(attempt {attempt + 1}/{self.max_retries})"
        )
