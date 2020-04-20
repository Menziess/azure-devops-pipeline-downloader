"""Main program."""

import argparse
from itertools import islice


def get_args():
    """Get the users arguments."""
    parser = argparse.ArgumentParser('app')
    parser.add_argument('n', type=int)
    return parser.parse_args()



if __name__ == "__main__":
    n = get_args().n
    print(n)
