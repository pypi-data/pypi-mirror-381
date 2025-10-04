import time
from dataclasses import dataclass

import requests

from fortytwo.exceptions import FortyTwoAuthException
from fortytwo.logger import logger


@dataclass
class Tokens:
    """
    Container for 42 API authentication tokens.

    Attributes:
        access_token: The OAuth2 access token for API requests.
        token_type: The type of token (typically "bearer").
        expires_in: Token expiration time in seconds.
        scope: The scope of access granted by the token.
        created_at: Unix timestamp when the token was created.
        secret_valid_until: Unix timestamp until which the secret is valid.
    """

    access_token: str
    token_type: str
    expires_in: int
    scope: str
    created_at: int
    secret_valid_until: int

    def is_expired(self) -> bool:
        """
        Check if the token has expired.

        Returns:
            True if the token has expired, False otherwise.
        """
        expiration_time = self.created_at + self.expires_in
        return time.time() >= expiration_time


class Authentication:
    """
    Handles authentication with the 42 API using OAuth2 client credentials flow.
    """

    @staticmethod
    def fetch_tokens(client_id: str, client_secret: str, endpoint_oauth: str) -> Tokens:
        """
        Fetch an access token from the 42 API.

        Args:
            client_id: The 42 API client ID.
            client_secret: The 42 API client secret.

        Returns:
            Tokens object containing access token and metadata.

        Raises:
            FortyTwoAuthException: If authentication fails.
        """

        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        }

        try:
            logger.info("Fetching access token")
            response = requests.post(
                url=endpoint_oauth,
                data=data,
                timeout=120,
            )

            response.raise_for_status()
            response_json = response.json()

            tokens = Tokens(
                access_token=response_json["access_token"],
                token_type=response_json["token_type"],
                expires_in=response_json["expires_in"],
                scope=response_json["scope"],
                created_at=response_json["created_at"],
                secret_valid_until=response_json.get("secret_valid_until", 0),
            )
            logger.info("Access token fetched successfully")

            return tokens

        except requests.exceptions.HTTPError as e:
            logger.error("Failed to fetch access token: %s", e)
            raise FortyTwoAuthException from e
