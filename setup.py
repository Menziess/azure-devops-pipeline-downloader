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
        install_requires=[
            'azure-devops==6.0.0b2',
            'certifi==2020.4.5.1',
            'chardet==3.0.4',
            'idna==2.9',
            'isodate==0.6.0',
            'msrest==0.6.13',
            'oauthlib==3.1.0',
            'python-dotenv==0.13.0',
            'requests-oauthlib==1.3.0',
            'requests==2.23.0',
            'six==1.14.0',
            'urllib3==1.25.9'
        ],
        entry_points={
            'console_scripts': [
                'devops_exporter=devops_exporter.main:main'
            ]
        }
    )
