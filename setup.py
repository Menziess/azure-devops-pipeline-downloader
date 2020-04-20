"""Setuptools script."""

from setuptools import find_packages, setup

if __name__ == '__main__':
    setup(
        name='devops-exporter',
        version='0.0.dev0',
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'devops_exporter*'
        ]),
        install_requires=[]
    )
