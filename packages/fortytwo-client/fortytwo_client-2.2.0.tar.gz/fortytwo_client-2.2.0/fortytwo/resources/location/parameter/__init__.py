from fortytwo.resources.location.parameter.filter import LocationFilter
from fortytwo.resources.location.parameter.parameter import LocationParameter
from fortytwo.resources.location.parameter.range import LocationRange
from fortytwo.resources.location.parameter.sort import LocationSort


class LocationParameters:
    """
    Namespace for location-specific query parameters.
    """

    Filter = LocationFilter
    Sort = LocationSort
    Range = LocationRange
    Parameter = LocationParameter


__all__ = ["LocationParameters"]
