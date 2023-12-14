# setup.py

from setuptools import setup

setup(
    name='kings',
    version='0.1',
    packages=['kings'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'queen=kings:queen_cli',
        ],
    },
)
