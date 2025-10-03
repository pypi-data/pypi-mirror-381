import logging
from dataclasses import dataclass

import requests

from fortytwo.exceptions import FortyTwoAuthException


@dataclass
class FortyTwoTokens:
    """
    This class provides a container for 42 API tokens.
    """

    access_token: str
    token_type: str
    expires_in: int
    scope: str
    created_at: int
    secret_valid_until: int


class FortyTwoAuthentication:
    """
    This class handles authentication with the 42 API.
    """

    @staticmethod
    def fetch_tokens(client_id: str, client_secret: str) -> FortyTwoTokens:
        """
        Fetches an access token from the 42 API.

        Args:
            client_id: The 42 API client ID.
            client_secret: The 42 API client secret.

        Returns:
            FortyTwoTokens: The access and refresh tokens.

        Raises:
            FortyTwoAuthException: An error occurred when authenticating.
        """

        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        }

        try:
            logging.debug("Fetching access token.")

            response = requests.post(
                url="https://api.intra.42.fr/oauth/token", data=data, timeout=120
            )
            response.raise_for_status()

            response_json = response.json()

            tokens = FortyTwoTokens(
                access_token=response_json["access_token"],
                token_type=response_json["token_type"],
                expires_in=response_json["expires_in"],
                scope=response_json["scope"],
                created_at=response_json["created_at"],
                secret_valid_until=response_json.get("secret_valid_until", 0),
            )

            return tokens

        except requests.exceptions.HTTPError as e:
            raise FortyTwoAuthException from e
