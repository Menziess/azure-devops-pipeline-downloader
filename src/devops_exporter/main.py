"""Main program."""

import argparse
import json
import requests
from os import getenv, path, makedirs
from typing import Any, Iterable, Union

from azure.devops.connection import Connection
from azure.devops.released.build import BuildClient
from azure.devops.released.release import ReleaseClient
from dotenv import load_dotenv
from msrest.authentication import BasicAuthentication


def get_args():
    """Get the users arguments."""
    parser = argparse.ArgumentParser('app')
    parser.add_argument('project', type=str)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--build', action='store_true')
    group.add_argument('--release', action='store_true')
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


def write_dict(folder: str, filename: str, d: dict) -> None:
    """Write definition to disk."""
    if not path.exists(folder):
        makedirs(folder)
    with open(path.join(folder, filename) + '.json', 'w') as f:
        json.dump(d, f)


def query_az_api(url: str, token: str):
    """Send request to Azure API using pat token."""
    return requests.get(url, auth=('', token))


def iterate_pipeline_definitions(
    client: Union[BuildClient, ReleaseClient],
    project: str,
    ids: Iterable[int],
    continuation_token=None
) -> Iterable[Any]:
    """Get pipeline ids."""
    get_definition = client.get_definition if isinstance(
        client, BuildClient) else client.get_release_definition
    get_definitions = client.get_definitions if isinstance(
        client, BuildClient) else client.get_release_definitions

    if ids:
        return (get_definition(project, i) for i in ids)

    batch = get_definitions(project)
    yield from batch.value

    if batch.continuation_token:
        yield from iterate_pipeline_definitions(
            client, project, [], batch.continuation_token)


if __name__ == "__main__":

    # Get secrets
    env = get_env('personal_access_token',
                  'organization_url')

    # Create connection to DevOps
    conn = connect(env.get('personal_access_token', ''),
                   env.get('organization_url', ''))

    # Get args
    args = get_args()

    # Pipeline type
    pipeline_type = 'build' if args.build else 'release'

    # Get build/release definitions iterable
    defs = iterate_pipeline_definitions(
        getattr(conn.clients, f'get_{pipeline_type}_client')(),
        args.project,
        args.ids)

    # Use definition url as python sdk doesn't offer definition json
    for d in defs:
        response = query_az_api(d.url, env.get('personal_access_token', ''))
        data = json.loads(response.content)
        filename = data['name'].replace('/', '.')
        write_dict(f'data/{pipeline_type}', filename, data)
        print(f'Downloaded {filename}')
