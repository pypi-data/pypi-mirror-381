#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

# Read requirements
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name='django-cap-alerts',
    version='1.0.0',
    description='Django package for CAP (Common Alerting Protocol)',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='Orestis Tsagketas',
    author_email='otsagketas@getmap.gr',
    url='https://gitlab.com/otsagketas1/cap-package',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.2.0',
        'djangorestframework>=3.14.0',
        'djangorestframework-gis>=1.0.0',
        'psycopg2-binary>=2.9.0',
        'celery>=5.3.0',
        'redis>=5.0.0',
        'requests>=2.31.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-django>=4.5.0',
            'black>=23.0.0',
            'flake8>=6.0.0',
            'isort>=5.12.0',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.8',
    keywords='django cap alerts',
    project_urls={
        'Bug Reports': 'https://gitlab.com/otsagketas1/cap-package/-/issues',
        'Source': 'https://gitlab.com/otsagketas1/cap-package',
        'Documentation': 'https://gitlab.com/otsagketas1/cap-package/-/blob/main/django_cap_alerts/README.md',
        'API Documentation': 'https://gitlab.com/otsagketas1/cap-package/-/blob/main/django_cap_alerts/docs/MANAGER_DOCS.md',
    },
)
