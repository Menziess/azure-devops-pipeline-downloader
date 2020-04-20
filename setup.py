"""Setuptools script."""

import os

from setuptools import find_packages, setup

if __name__ == '__main__':
    package_name = os.getenv('PACKAGE_NAME')
    setup(
        name=package_name,
        version='0.0.dev0',
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            f'{package_name}*'
        ]),
        install_requires=[]
    )
