#!/usr/bin/env python

from setuptools import setup

setup(
    name='TracDigestReporter',
    version='0.0.1',
    packages=['digest_reporter'],
    author='Max Kosyakov',
    maintainer='Max Kosyakov',
    maintainer_email='max@kosyakov.net',
    description='Digest reports for emailing to project watchers',
    url='http://',
    license='None',
    entry_points={
        'trac.plugins': [
            'digest_reporter = digest_reporter.main',
        ]
    },
    package_data={
        'digest_reporter': [
            'htdocs/*.css',
            'htdocs/*.js',
            'templates/digest_reporter/*.html',
        ],
    }
)
