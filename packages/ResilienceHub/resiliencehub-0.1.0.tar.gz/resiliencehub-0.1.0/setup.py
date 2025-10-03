from setuptools import setup, find_packages

setup(
    name="ResilienceHub",          # package name on PyPI
    version="0.1.0",
    packages=find_packages(),      # will find the inner ResilienceHub package
    install_requires=[],           # add dependencies if any
    python_requires=">=3.7",
)
