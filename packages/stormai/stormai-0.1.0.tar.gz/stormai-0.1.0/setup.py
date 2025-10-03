from setuptools import setup, find_packages

setup(
    name="stormai",  # must be unique on PyPI
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # dependencies if any
    python_requires=">=3.8",
    description="name_reserve",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Vedant Pathak",
    url="https://github.com/ImVedantPathak/stormai",
    license="MIT"
)
