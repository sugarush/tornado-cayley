__author__ = 'Paul Severance'

from setuptools import setup

setup(
    name='tornado-cayley',
    version='0.0.1',
    author='Paul Severance',
    author_email='paulseverance@gmail.com',
    url='https://github.com/sugarush/tornado-cayley',
    packages=['tornado_cayley'],
    description='An asynchronous Cayley client for Tornado.',
    install_requires=[
        'python-cayley',
        'tornado'
    ],
    dependency_links=[
        'git+https://github.com/sugarush/python-cayley.git@a0c56cc0c168ed624d91426d0dc5e788e9a9a3a7#egg=python-cayley'
    ]
)
