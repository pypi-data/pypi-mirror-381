from __future__ import annotations

import time
from typing import TYPE_CHECKING, Optional

from requests.exceptions import HTTPError, RequestException

from fortytwo.logger import logger
from fortytwo.request.authentication import FortyTwoAuthentication
from fortytwo.request.request import FortyTwoRequest
from fortytwo.resources.ressource import RessourceTemplate

if TYPE_CHECKING:
    from requests import Response

    from fortytwo.config import FortyTwoConfig
    from fortytwo.request.authentication import FortyTwoSecrets, FortyTwoTokens
    from fortytwo.request.parameter.parameter import FortyTwoParam
    from fortytwo.resources.ressource import FortyTwoRessource


class FortyTwoRequestHandler:
    """
    Handles request execution, authentication, and error handling for the 42 API.
    """

    def __init__(
        self,
        secrets: FortyTwoSecrets,
        config: FortyTwoConfig,
    ) -> None:
        """
        Initialize the request handler.

        Args:
            secrets: Authentication secrets for the 42 API.
            config: Configuration for API requests.
        """
        self._secrets = secrets
        self._config = config
        self._rate_limiter = config.rate_limiter

        self._tokens: Optional[FortyTwoTokens] = None
        self._is_rate_limited: bool = False

    def execute(
        self,
        ressource: FortyTwoRessource[RessourceTemplate],
        *params: FortyTwoParam,
    ) -> RessourceTemplate:
        """
        Execute a request to the 42 API.

        Args:
            ressource: The resource to fetch.
            params: The parameters for the request.

        Returns:
            The response from the API.
        """
        if self._tokens is None:
            self._tokens = FortyTwoAuthentication.get_tokens(self._secrets)

        self._request = FortyTwoRequest[RessourceTemplate](
            ressource.set_config(self._config), *params
        )

        return self._make_request()

    def _make_request(self) -> Optional[RessourceTemplate]:
        """
        Execute the request with rate limiting and error handling.
        """
        if not self._rate_limiter.can_make_request():
            return self._handle_hourly_rate_limit()

        self._rate_limiter.enforce_secondly_rate_limit()

        try:
            response = self._request.request(
                self._tokens,
                self._config,
            )

            self._rate_limiter.record_request()
            self._is_rate_limited = False

            return response

        except HTTPError as e:
            return self._handle_http_exception(e.response)

        except RequestException as e:
            logger.error("Failed to fetch from the API: %s", e)
            return self._make_request()

    def _handle_http_exception(self, response: Response) -> Optional[RessourceTemplate]:
        """
        Handle HTTP exceptions based on status codes.
        """
        if response.status_code == 429:
            return self._handle_rate_limit()

        self._is_rate_limited = False

        logger.error(
            "Failed to fetch from the API (%s): %s.",
            response.status_code,
            response.reason,
        )

        if response.status_code == 401:
            return self._handle_unauthorized(response)

        return None

    def _handle_unauthorized(self, response: Response) -> Optional[RessourceTemplate]:
        """
        Handle 401 unauthorized responses by refreshing the token.
        """
        logger.info("Access token expired, fetching a new one.")
        self._tokens = FortyTwoAuthentication.get_tokens(self._secrets)

        return self._make_request()

    def _handle_rate_limit(self) -> Optional[RessourceTemplate]:
        """
        Handle 429 rate limit responses.
        """
        if self._is_rate_limited:
            return self._handle_hourly_rate_limit()
        else:
            logger.debug("Temporary rate limit exceeded, retrying in 1 second...")
            time.sleep(1)

        self._is_rate_limited = True
        return self._make_request()

    def _handle_hourly_rate_limit(self) -> Optional[RessourceTemplate]:
        """
        Handle hourly rate limit by waiting until quota is available.
        """
        current_count = self._rate_limiter.get_request_count()
        wait_time = self._rate_limiter.get_hourly_wait_time()

        logger.warning(
            "Hourly rate limit exceeded (%d/%d requests used). "
            "Waiting %.1f seconds until next request is available...",
            current_count,
            self._rate_limiter.requests_per_hour,
            wait_time,
        )

        # Wait until we can make the next request
        time.sleep(wait_time + 1)  # Add 1 second buffer

        return self._make_request()
