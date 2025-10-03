"""
Rate limiting functionality for the 42 API client.
"""

import time
from typing import Self

from fortytwo.logger import logger


class RateLimiter:
    """
    Abstract interface for rate limiting implementations, handles both hourly and per-second rate limits.
    """

    request_time: float = 0.0

    def __init__(self: Self, requests_per_hour: int, requests_per_second: int) -> None:
        self.requests_per_hour = requests_per_hour
        self.requests_per_second = requests_per_second

    def record_request(self) -> None:
        """
        Record that a request was made at the current time.
        """
        self.request_time = time.perf_counter()
        logger.debug("Request recorded at %.3f", self.request_time)

    def can_make_request(self) -> bool:
        """
        Check if a request can be made without exceeding both hourly and per-second rate limits.

        Returns:
            True if request can be made, False otherwise.
        """
        raise NotImplementedError

    def get_hourly_wait_time(self: Self) -> float:
        """
        Get the number of seconds to wait before the hourly rate limit resets.

        Returns:
            Number of seconds to wait for hourly reset, 0 if hourly limit not exceeded.
        """
        raise NotImplementedError

    def get_request_count(self: Self) -> int:
        """
        Get the current number of requests made in the current hour.

        Returns:
            Number of requests made in the current hour.
        """
        raise NotImplementedError

    def enforce_secondly_rate_limit(self: Self) -> None:
        """
        This function ensures that the rate limit is respected.

        Args:
            request_time (float): The time at which the request was made.
            rate_limit (int): The number of requests allowed per second.
        """

        time_elapsed = time.perf_counter() - self.request_time
        sleep_duration = (1 / self.requests_per_second) - time_elapsed

        if sleep_duration > 0:
            logger.debug(
                "Sleeping for %.3f seconds to respect rate limit", sleep_duration
            )
            time.sleep(sleep_duration)

    def _get_current_hour_start(self: Self) -> float:
        """
        Get the timestamp of the start of the current hour.

        Returns:
            Timestamp of the current hour start (e.g., 14:00:00).
        """
        current_time = time.time()
        return current_time - (current_time % 3600)
