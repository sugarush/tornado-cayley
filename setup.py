__author__ = 'Paul Severance'

from setuptools import setup

setup(
    name='tornado-cayley',
    version='0.0.1',
    author='Paul Severance',
    author_email='paulseverance@gmail.com',
    url='https://github.com/sugarush/tornado-cayley',
    packages=['tornado-cayley'],
    description='An asynchronous Cayley client for Tornado.',
    install_requires=[
        'python-cayley',
        'tornado'
    ],
    dependency_links=[
        'git+https://github.com/sugarush/python-cayley.git@a18592b49ee154cc1421d1bf99e9a6dd129f40bd#egg=python_cayley'
    ]
)
