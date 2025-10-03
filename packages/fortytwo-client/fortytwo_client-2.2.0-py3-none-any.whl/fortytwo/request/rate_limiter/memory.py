import time
from typing import Optional, Self

from fortytwo.default import (
    FORTYTWO_RATE_LIMIT_PER_HOUR,
    FORTYTWO_RATE_LIMIT_PER_SECOND,
)
from fortytwo.request.rate_limiter.rate_limiter import RateLimiter


class MemoryRateLimiter(RateLimiter):
    """
    A rate limiter that tracks both requests per hour and per second with appropriate time windows.
    """

    def __init__(
        self: Self,
        requests_per_hour: Optional[int] = FORTYTWO_RATE_LIMIT_PER_HOUR,
        requests_per_second: Optional[int] = FORTYTWO_RATE_LIMIT_PER_SECOND,
    ) -> None:
        """
        Initialize the rate limiter.

        Args:
            requests_per_hour: Maximum number of requests allowed per hour.
            requests_per_second: Maximum number of requests allowed per second.
        """
        super().__init__(requests_per_hour, requests_per_second)
        self.request_count = 0
        self.current_hour_start = self._get_current_hour_start()

    def record_request(self: Self) -> None:
        """
        Record that a request was made at the current time.
        """
        super().record_request()
        self.request_count += 1

    def can_make_request(self: Self) -> bool:
        """
        Check if a request can be made without exceeding the hourly rate limit.

        Returns:
            True if request can be made, False otherwise.
        """
        self._reset_if_new_hour()
        return self.request_count < self.requests_per_hour

    def get_hourly_wait_time(self: Self) -> float:
        """
        Get the number of seconds to wait before the hourly rate limit resets.

        Returns:
            Number of seconds to wait for hourly reset, 0 if hourly limit not exceeded.
        """
        self._reset_if_new_hour()

        if self.request_count < self.requests_per_hour:
            return 0.0

        reset_time = self.current_hour_start + 3600
        current_time = time.time()
        return max(0.0, reset_time - current_time)

    def get_request_count(self: Self) -> int:
        """
        Get the current number of requests made in the current hour.

        Returns:
            Number of requests made in the current hour.
        """
        self._reset_if_new_hour()
        return self.request_count

    def _reset_if_new_hour(self: Self) -> None:
        """
        Reset the request counter if we've entered a new hour.
        """
        current_hour_start = self._get_current_hour_start()

        if current_hour_start > self.current_hour_start:
            self.request_count = 0
            self.current_hour_start = current_hour_start
