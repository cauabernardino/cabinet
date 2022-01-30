from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="cabinet",
    version="0.0.1",
    description="A simple wrapper tool to run scripts easily from CLI.",
    long_description=readme,
    author="Cauã Bernardino",
    author_email="",
    url="https://github.com/cauabernardino/cabinet",
    license=license,
    packages=find_packages(exclude=("tests")),
    entry_points={
        "console_scripts": [
            "cab = cabinet.main:main",
        ],
    },
)
