"""Main program."""

import argparse
from os import getenv
from typing import Union, Iterable, Any

from dotenv import load_dotenv
from azure.devops.connection import Connection
from azure.devops.released.build import BuildClient
from azure.devops.released.release import ReleaseClient
from msrest.authentication import BasicAuthentication


def get_args():
    """Get the users arguments."""
    parser = argparse.ArgumentParser('app')
    parser.add_argument('project', type=str)
    group = argparse.add_mutually_exclusive_group()
    group.add_argument('-b', '--build', action='store_true')
    group.add_argument('-r', '--release', action='store_false')
    parser.add_argument('-i', '--ids', type=int, nargs='+')
    return parser.parse_args()


def get_env(*keys: str) -> dict:
    """Return environment variables as dictionary."""
    load_dotenv()
    return {k: getenv(k) for k in keys}


def connect(token: str, url: str):
    """Create new connection."""
    return Connection(base_url=url,
                      creds=BasicAuthentication('', token))


def get_pipeline_definitions(
    client: Union[BuildClient, ReleaseClient],
    ids: Iterable[int] = []
) -> Iterable[int]:
    """Get pipeline ids."""
    if ids:
        return (client.get_definition(i) for i in ids)

    return iter(client.get_definitions())


if __name__ == "__main__":

    # Get secrets
    env = get_env('personal_access_token',
                  'organization_url')

    # Create connection to DevOps
    conn = connect(env.get('personal_access_token', ''),
                   env.get('organization_url', ''))

    # Get args
    n = get_args().n

    defs = get_pipeline_definitions()

    print(n)
