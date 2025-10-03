from dataclasses import dataclass, field
from typing import Optional

from fortytwo.default import FORTYTWO_ENDPOINT
from fortytwo.request.rate_limiter import MemoryRateLimiter, RateLimiter
from fortytwo.request.secret_manager import SecretManager


@dataclass
class FortyTwoConfig:
    """
    This class provides the configuration for the FortyTwoClient.
    """

    request_timeout: int = 10  # seconds
    request_endpoint: str = FORTYTWO_ENDPOINT

    rate_limiter: RateLimiter = field(default_factory=MemoryRateLimiter)
    secret_manager: Optional[SecretManager] = None
