"""
Base secret manager interface for the 42 API client.
"""

from typing import Self

from fortytwo.request.authentication import FortyTwoTokens


class SecretManager:
    """
    Abstract base class for managing 42 API secrets.
    """

    def get_tokens(self: Self) -> FortyTwoTokens:
        """
        Retrieve the 42 API tokens.
        """
        raise NotImplementedError

    def refresh_tokens(self: Self) -> FortyTwoTokens:
        """
        Refresh and retrieve updated 42 API tokens.
        """
        raise NotImplementedError
