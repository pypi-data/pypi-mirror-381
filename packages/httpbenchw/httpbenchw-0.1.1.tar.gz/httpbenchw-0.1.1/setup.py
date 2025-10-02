# setup.py
from setuptools import setup, find_packages

setup(
    name='httpbenchw',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'httpbenchw_test=httpbenchw.main:main',
        ],
    },
)
