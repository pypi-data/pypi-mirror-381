import time
from typing import Any, Optional, Self

from fortytwo.default import (
    FORTYTWO_RATE_LIMIT_PER_HOUR,
    FORTYTWO_RATE_LIMIT_PER_SECOND,
)
from fortytwo.request.rate_limiter.rate_limiter import RateLimiter


class RedisRateLimiter(RateLimiter):
    """
    A rate limiter that tracks both requests per hour and per second using Redis for distributed rate limiting.
    """

    def __init__(
        self: Self,
        redis_client: Any,
        key_prefix: Optional[str] = "fortytwo_rate_limit",
        requests_per_hour: Optional[int] = FORTYTWO_RATE_LIMIT_PER_HOUR,
        requests_per_second: Optional[int] = FORTYTWO_RATE_LIMIT_PER_SECOND,
    ) -> None:
        """
        Initialize the Redis rate limiter.

        Args:
            redis_client: Redis client instance (e.g., redis.Redis()).
            key_prefix: Prefix for Redis keys to avoid collisions.
            requests_per_hour: Maximum number of requests allowed per hour.
            requests_per_second: Maximum number of requests allowed per second.
        """
        super().__init__(requests_per_hour, requests_per_second)
        self.redis = redis_client
        self.key_prefix = key_prefix

    def record_request(self: Self) -> None:
        """
        Record that a request was made at the current time.
        """
        super().record_request()
        key = self._get_hour_key()

        current_hour_start = self._get_current_hour_start()
        expire_at = int(current_hour_start + 3600)

        # Use Redis pipeline for atomic operations
        pipe = self.redis.pipeline()
        pipe.incr(key)
        pipe.expireat(key, expire_at)
        pipe.execute()

    def can_make_request(self: Self) -> bool:
        """
        Check if a request can be made without exceeding both hourly and per-second rate limits.

        Returns:
            True if request can be made, False otherwise.
        """
        key = self._get_hour_key()
        count = int(self.redis.get(key) or 0)
        return count < self.requests_per_hour

    def get_hourly_wait_time(self: Self) -> float:
        """
        Get the number of seconds to wait before the hourly rate limit resets.

        Returns:
            Number of seconds to wait for hourly reset, 0 if hourly limit not exceeded.
        """
        hour_key = self._get_hour_key()
        hour_count = int(self.redis.get(hour_key) or 0)

        if hour_count < self.requests_per_hour:
            return 0.0

        current_hour_start = self._get_current_hour_start()
        reset_time = current_hour_start + 3600
        current_time = time.time()
        return max(0.0, reset_time - current_time)

    def get_request_count(self: Self) -> int:
        """
        Get the current number of requests made in the current hour.

        Returns:
            Number of requests made in the current hour.
        """
        hour_key = self._get_hour_key()
        return int(self.redis.get(hour_key) or 0)

    def _get_hour_key(self: Self) -> str:
        """
        Generate the Redis key for the current hour.

        Returns:
            Redis key string for the current hour.
        """
        hour_start = int(self._get_current_hour_start())
        return f"{self.key_prefix}:hour:{hour_start}"
