# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in wadeem/__init__.py
from wadeem import __version__ as version

setup(
	name='wadeem',
	version=version,
	description='LMS Module',
	author='Siddhant',
	author_email='siddhant.sinha@oodlestechnologies.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
