"""
Resources for fetching location data from the 42 API.
"""

from typing import Any, Self

from fortytwo.resources.location.location import Location
from fortytwo.resources.resource import Resource, ResourceTemplate


class GetLocationsByUserId(Resource[list[Location]]):
    """
    Resource for fetching locations for a specific user.

    Returns a list of location records showing where and when
    the user has logged in at 42 campuses.

    Args:
        user_id: The ID of the user whose locations to fetch.
    """

    method: str = "GET"
    _url: str = "/users/%s/locations"

    def __init__(self: Self, user_id: int) -> None:
        self.user_id = user_id

    @property
    def url(self: Self) -> str:
        return self.config.request_endpoint + self._url % self.user_id

    def parse_response(self: Self, response_data: Any) -> ResourceTemplate:
        return [Location(location) for location in response_data]
