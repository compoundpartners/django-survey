# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from survey import __version__


setup(
    name='django-survey',
    version=__version__,
    description=open('README.md').read(),
    author='Compound Partners Ltd',
    author_email='hello@compoundpartners.co.uk',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[
      "Django", "django-bootstrap-form", "django-tastypie",
      "django-registration", "pytz", "future", "ordereddict", "PyYAML",
      "matplotlib", "seaborn", "numpy"
    ],
    extras_require={
      'dev': ["django-rosetta", "pylint", "coverage", "mock"],
    },
    include_package_data=True,
    zip_safe=False,
)
