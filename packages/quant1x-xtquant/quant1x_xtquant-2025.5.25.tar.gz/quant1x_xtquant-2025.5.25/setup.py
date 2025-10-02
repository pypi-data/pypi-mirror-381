#!/usr/bin/env python
# coding=utf-8
"""The setup script."""
import setuptools
from q1x.base.version import project_version

try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import find_packages, setup

latest, author = project_version()
__version__ = latest

app__version__ = latest


def parse_requirements(filename):
    line_iter = (line.strip() for line in open(filename))
    return [line for line in line_iter if line and not line.startswith("#")]


with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md", encoding="utf-8") as history_file:
    history = history_file.read()

requirements = parse_requirements("requirements.txt")
test_requirements = requirements

setuptools.setup(
    name="quant1x-xtquant",
    description="Quant1X XtQuant",
    author_email="wangfengxy@sina.cn",
    url="https://gitee.com/quant1x/xtquant",
    version=app__version__,
    author='wangfeng',
    long_description=readme,
    packages=setuptools.find_packages(include=["xtquant", "xtquant.*"]),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords="quant1x xtquant",
    entry_points={
        # "console_scripts": [
        #     "quant1x-qmt=qmt.__main__:main",
        # ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    data_files=[
        # ('xtquant', ['xtquant/xtdata.ini', 'xtquant/xtdata.log4cxx']),
    ],
    package_data={
        '': ['*.dll', '*.pyd', '*.ini', '*.log4cxx'],
    },
    test_suite="tests",
    tests_require=test_requirements,
    setup_requires=requirements,
)
