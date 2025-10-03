from __future__ import annotations

from typing import TYPE_CHECKING, Generic, List, Optional, Self, TypeVar

import requests

if TYPE_CHECKING:
    from fortytwo.config import FortyTwoConfig
    from fortytwo.request.authentication import FortyTwoTokens
    from fortytwo.request.parameter.parameter import FortyTwoParam
    from fortytwo.resources.ressource import FortyTwoRessource

RequestTemplate = TypeVar("RequestTemplate")


class FortyTwoRequest(Generic[RequestTemplate]):
    ressource: FortyTwoRessource[RequestTemplate]
    params: List[FortyTwoParam] = []

    def __init__(
        self: Self, ressource: FortyTwoRessource, *params: FortyTwoParam
    ) -> None:
        self.ressource = ressource
        self.params = list(params)

    def add_params(self: Self, *params: FortyTwoParam) -> None:
        """
        This function adds parameters to the request.

        Args:
            *params (FortyTwoParam): The parameters to add.
        """

        self.params.extend(params)

    def request(
        self: Self,
        tokens: FortyTwoTokens,
        config: FortyTwoConfig,
    ) -> Optional[RequestTemplate]:
        """
        This function sends a request to the API and returns the response.

        Args:
            tokens (FortyTwoTokens): The access and refresh tokens.

        Returns:
            Optional[T]: The response from the request.
        """

        headers = {"Authorization": f"Bearer {tokens.access_token}"}

        response = requests.request(
            method=self.ressource.method,
            url=self.ressource.url,
            headers=headers,
            params=[param.to_query_param() for param in self.params],
            timeout=config.request_timeout,
        )

        response.raise_for_status()

        return self.ressource.parse_response(response.json())
