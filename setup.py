#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='website-fqt',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='FQT Website',
    # GETTING-STARTED: set author name (your name):
    author='Mint IT Media',
    # GETTING-STARTED: set author email (your email):
    author_email='info@mintitmedia.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'appdirs==1.4.3',
        'Django==1.4.6',
        'django-tinymce==2.0.5',
        'gdata==2.0.18',
        'packaging==16.8',
        'pyparsing==2.2.0',
        'python-slugify==1.1.4',
        'six==1.10.0',
        'South==1.0.2',
        'Unidecode==0.4.18'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
