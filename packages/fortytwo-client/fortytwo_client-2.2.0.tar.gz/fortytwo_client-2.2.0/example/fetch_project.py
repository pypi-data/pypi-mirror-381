import json
import logging
import os
import sys

from dotenv import load_dotenv

from fortytwo import FortyTwoClient, logger, parameter
from fortytwo.json import default_serializer


def main() -> None:
    logger.setLevel(logging.DEBUG)
    load_dotenv(".env")

    client = FortyTwoClient(
        client_id=os.environ.get("42_SCHOOL_ID"),
        client_secret=os.environ.get("42_SCHOOL_SECRET"),
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
