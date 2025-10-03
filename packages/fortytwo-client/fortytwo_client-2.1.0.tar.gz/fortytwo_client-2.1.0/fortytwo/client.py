from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Self

from fortytwo.config import FortyTwoConfig
from fortytwo.request.authentication import (
    FortyTwoSecrets,
)
from fortytwo.request.handler import FortyTwoRequestHandler
from fortytwo.request.rate_limiter import MemoryRateLimiter, RedisRateLimiter
from fortytwo.resources.location import LocationManager
from fortytwo.resources.project import ProjectManager
from fortytwo.resources.project_user import ProjectUserManager
from fortytwo.resources.token import TokenManager
from fortytwo.resources.user import UserManager

if TYPE_CHECKING:
    from fortytwo.request.parameter.parameter import FortyTwoParam
    from fortytwo.resources.ressource import FortyTwoRessource, RessourceTemplate


class FortyTwoClient:
    """
    This class provides a client for the 42 School API.
    """

    Config = FortyTwoConfig

    class RateLimiter:
        Memory = MemoryRateLimiter
        Redis = RedisRateLimiter

    def __init__(
        self: Self,
        client_id: str,
        client_secret: str,
        config: Optional[FortyTwoConfig] = None,
    ) -> None:
        """
        Initialize the FortyTwoClient with authentication and configuration.

        Args:
            client_id (str): The client ID for authentication.
            client_secret (str): The client secret for authentication.
            config (Optional[FortyTwoConfig]): Optional configuration object. If not provided, a
        """
        self._config = config or FortyTwoConfig()
        self.secrets = FortyTwoSecrets(client_id, client_secret)

        self._request_handler = FortyTwoRequestHandler(self.secrets, self._config)

        self.users = UserManager(self)
        self.locations = LocationManager(self)
        self.projects = ProjectManager(self)
        self.project_users = ProjectUserManager(self)
        self.tokens = TokenManager(self)

    def request(
        self: Self,
        ressource: FortyTwoRessource[RessourceTemplate],
        *params: FortyTwoParam,
    ) -> RessourceTemplate:
        """
        This function sends a request to the API and returns the response

        Args:
            ressource (FortyTwoRessource): The ressource to fetch.
            params (FortyTwoParam): The parameters for the request.

        Returns:
            RessourceTemplate: The response from the API.
        """

        return self._request_handler.execute(ressource, *params)
