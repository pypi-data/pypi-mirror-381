import json
import logging
import os
import sys
from contextlib import contextmanager
from typing import Generator

import redis
from dotenv import load_dotenv
from testcontainers.redis import RedisContainer

from fortytwo import FortyTwoClient, parameter
from fortytwo.json import default_serializer


@contextmanager
def redis_container() -> Generator[redis.Redis, None, None]:
    """
    Context manager for managing a Redis test container.

    Yields:
        Redis client connected to the test container
    """
    print("Starting Redis container...")

    with RedisContainer("redis:7-alpine") as container:
        redis_host = container.get_container_host_ip()
        redis_port = container.get_exposed_port(6379)

        redis_client = redis.Redis(
            host=redis_host,
            port=redis_port,
            decode_responses=True,
            health_check_interval=30,
        )

        redis_client.ping()
        print(f"Redis container ready at {redis_host}:{redis_port}")

        yield redis_client


def main() -> None:
    with redis_container() as redis_client:
        load_dotenv(".env")

        client = FortyTwoClient(
            client_id=os.environ.get("42_SCHOOL_ID"),
            client_secret=os.environ.get("42_SCHOOL_SECRET"),
            config=FortyTwoClient.Config(
                rate_limiter=FortyTwoClient.RateLimiter.Redis(
                    redis_client,
                    requests_per_hour=4,
                    key_prefix="fortytwo_test",
                ),
            ),
        )

        if len(sys.argv) != 2:
            logging.error("Please provide the cursus id as an argument.")
            sys.exit(2)

        cursus_id: int
        try:
            cursus_id = int(sys.argv[1])
        except ValueError:
            logging.error("Invalid cursus id provided.")
            sys.exit(2)

        projects = []
        for i in range(1, 10):
            print(f"Fetching page {i}...")

            project = client.projects.get_by_cursus_id(
                cursus_id,
                parameter.PageNumber(i),
                parameter.PageSize(1),
            )

            if project is None:
                break

            projects.extend(project)

    for project in projects:
        print(json.dumps(project, default=default_serializer, indent=4))


if __name__ == "__main__":
    main()
