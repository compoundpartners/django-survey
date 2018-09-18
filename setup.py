
import sys

from setuptools import find_packages, setup


if sys.version_info < (2, 6):
    sys.exit('Sorry, Python < 2.6 is not supported')


def add_package(package_list, package):
    package = package.replace("\n", "").split("#")[0]
    if package:
        package_list.append(package)

setup(
    name='django-survey',
    version='0.0.2',
    description=open('README.md').read(),
    author='Compound Partners Ltd',
    author_email='hello@compoundpartners.co.uk',
    license="LGPLv3",
    url="https://github.com/compoundpartners/js-survey",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Natural Language :: French",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        'Programming Language :: Python :: 3',
        "Framework :: Django",
    ],
    install_requires=[
        "Django", "django-bootstrap-form", "django-tastypie",
        "django-registration", "pytz", "future", "ordereddict", "PyYAML",
        "matplotlib", "seaborn", "numpy"
    ],
    extras_require={
        'dev': ["django-rosetta", "pylint", "coverage", "mock"],
    },
    zip_safe=False,
)
