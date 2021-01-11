#!/usr/bin/env python3

import os

from setuptools import find_namespace_packages, setup

current_directory = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(current_directory, "lightctl", "version.py")) as f:
    exec(f.read(), version)

setup(
    name="lightctl",
    version=version["__version__"],
    description="Lightup CLI Tool",
    long_description="""lightctl manages Source, Metric, Rule etc""",
    url="https://www.lightup.ai/",
    license="Proprietary License",
    author="Lightup Data Inc",
    author_email="info@lightup.ai",
    packages=find_namespace_packages(include=["lightctl"]),
    scripts=["bin/lightctl"],
    install_requires=[
        "click>=7.0",
        "pyyaml>=5.3.1",
        "requests>=2.22.0",
    ],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "License :: Other/Proprietary License",
    ],
)
