"""
A secret manager that retrieves credentials from HashiCorp Vault.
"""

from typing import Any, Optional, Self

from fortytwo.request.authentication import FortyTwoAuthentication, FortyTwoTokens
from fortytwo.request.secret_manager.secret_manager import SecretManager


class VaultSecretManager(SecretManager):
    """
    A secret manager that retrieves credentials from HashiCorp Vault.
    """

    def __init__(self: Self, vault_client: Any, path: str, mount_point: str) -> None:
        """
        Initialize the Vault secret manager.
        """
        self._vault = vault_client
        self._path = path
        self._mount_point = mount_point
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

        try:
            secrets = self._vault.secrets.kv.read_secret_version(
                path=self._path,
                mount_point=self._mount_point,
            )

            data = secrets["data"]["data"]
            client_id = data["client_id"]
            client_secret = data["client_secret"]

            self._token = FortyTwoAuthentication.fetch_tokens(
                client_id=client_id,
                client_secret=client_secret,
            )

            return self._token
        except Exception as e:
            raise RuntimeError("Failed to refresh tokens from Vault") from e
