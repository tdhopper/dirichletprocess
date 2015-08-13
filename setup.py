#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    "numpy",
]

test_requirements = ["pytest"
                     "flake8",
                     "tox"]



class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    name='dirichlet',
    version='0.1.0',
    description="Tools for Dirichlet Processes",
    long_description=readme + '\n\n' + history,
    author="Tim Hopper",
    author_email='tdhopper@gmail.com',
    url='https://github.com/tdhopper/dirichlet',
    packages=[
        'dirichlet',
    ],
    package_dir={'dirichlet':
                 'dirichlet'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='dirichlet',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    tests_require=test_requirements,
    cmdclass = {'test': PyTest},
)
