"""
In-memory secret manager implementation for the 42 API client.
"""

from typing import Optional, Self

from fortytwo.request.authentication import FortyTwoAuthentication, FortyTwoTokens
from fortytwo.request.secret_manager.secret_manager import SecretManager


class MemorySecretManager(SecretManager):
    """
    A simple secret manager that stores credentials in memory.
    """

    def __init__(self: Self, client_id: str, client_secret: str) -> None:
        """
        Initialize the memory secret manager with static credentials.

        Args:
            client_id: The 42 API client ID.
            client_secret: The 42 API client secret.
        """
        self._client_id = client_id
        self._client_secret = client_secret
        self._token: Optional[FortyTwoTokens] = None

    def get_tokens(self: Self) -> FortyTwoTokens:
        """
        Retrieve the 42 API tokens.

        Returns:
            FortyTwoTokens: The access and refresh tokens.
        """

        if self._token is None:
            self.refresh_tokens()

        return self._token

    def refresh_tokens(self: Self) -> FortyTwoTokens:
        """
        Refresh tokens (returns new tokens using the same credentials).

        Returns:
            FortyTwoTokens: The refreshed access and refresh tokens.
        """
        self._token = FortyTwoAuthentication.fetch_tokens(
            client_id=self._client_id,
            client_secret=self._client_secret,
        )

        return self._token
