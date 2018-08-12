import os
from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read()

setup(
    name='vertex_colorer',
    version='0.1',
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,
    author='Mohamed Leila',
    scripts=[],
    description='This package contains solvers for the vertex coloring problem'
)
