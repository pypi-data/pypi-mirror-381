from datetime import datetime
from typing import Self


class Parameter:
    """
    Base class for query parameters.

    This class provides the foundation for all query parameter types
    used in 42 API requests.
    """

    def __init__(self: Self, name: str, value: str | int | datetime) -> None:
        self.name = name
        self.value = value

    @staticmethod
    def _serialize_to_string(value: str | int | datetime | None) -> str:
        if value is None:
            return ""
        if isinstance(value, datetime):
            return value.isoformat()
        return str(value)

    def to_query_param(self: Self) -> tuple[str, str]:
        """
        Convert the parameter to a query parameter tuple.

        Returns:
            A tuple of (parameter_name, parameter_value) for URL encoding.
        """

        return (self.name, self._serialize_to_string(self.value))


class Sort(Parameter):
    """
    Sort query parameter.

    Used to sort API results by one or more fields.

    Example:
        Sort(by=["login", "-created_at"])  # Sort by login asc, created_at desc
    """

    def __init__(self: Self, by: list[str]) -> None:
        self.by = by

    def to_query_param(self: Self) -> tuple[str, str]:
        return ("sort", ",".join(self.by))


class Filter(Parameter):
    """
    Filter query parameter.

    Used to filter API results by specific field values.

    Example:
        Filter(by="campus_id", values=[1, 2])
    """

    def __init__(self: Self, by: str, values: list[str | int | datetime]) -> None:
        self.by = by
        self.values = values

    def to_query_param(self: Self) -> tuple[str, str]:
        values = [self._serialize_to_string(v) for v in self.values]
        return (f"filter[{self.by}]", ",".join(values))


class Range(Parameter):
    """
    Range query parameter.

    Used to filter API results by a range of values for a specific field.

    Example:
        Range(by="created_at", values=["2024-01-01", "2024-12-31"])
    """

    def __init__(self: Self, by: str, values: list[str | int | datetime]) -> None:
        self.by = by
        self.values = values

    def to_query_param(self: Self) -> tuple[str, str]:
        values = [self._serialize_to_string(v) for v in self.values]
        return (f"range[{self.by}]", ",".join(values))


class PageNumber(Parameter):
    """
    Page number query parameter.

    Specifies which page of results to retrieve (1-indexed).

    Args:
        page_number: The page number to fetch (must be >= 1).

    Example:
        PageNumber(1)  # First page
        PageNumber(5)  # Fifth page
    """

    def __init__(self: Self, page_number: int) -> None:
        self.page_number = page_number

    def to_query_param(self: Self) -> tuple[str, str]:
        return ("page[number]", str(self.page_number))


class PageSize(Parameter):
    """
    Page size query parameter.

    Specifies how many items to return per page.

    Args:
        page_size: Number of items per page (must be between 1 and 100).

    Raises:
        ValueError: If page_size is not between 1 and 100.

    Example:
        PageSize(50)  # 50 items per page
        PageSize(100)  # Maximum 100 items per page
    """

    def __init__(self: Self, page_size: int) -> None:
        if page_size < 1 or page_size > 100:
            raise ValueError("Page size must be between 1 and 100.")

        self.page_size = page_size

    def to_query_param(self: Self) -> tuple[str, str]:
        return ("page[size]", str(self.page_size))
