#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import shutil
import sys
from io import open

from setuptools import setup

long_description = ''
try:
    from pypandoc import convert
    long_description = convert('README.md', 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


version = get_version('celerybeat_status')


if sys.argv[-1] == 'publish':
    try:
        import pypandoc
    except ImportError:
        print("pypandoc not installed.\nUse `pip install pypandoc`.\nExiting.")
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('django_celerybeat_status.egg-info')
    sys.exit()


setup(
    name='django-celerybeat-status',
    version=version,
    license='MIT',
    description='A simple django admin extension that shows when your periodic are going to run next',
    long_description=long_description,
    author='Vinta Software',
    author_email='contact@vinta.com.br',
    packages=get_packages('celerybeat_status'),
    package_data=get_package_data('celerybeat_status'),
    install_requires=[],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.6',
    ]
)
