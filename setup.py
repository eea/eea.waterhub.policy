"""Compatibility entry point for the legacy EEA release tooling."""

from pathlib import Path

from setuptools import find_namespace_packages, setup


ROOT = Path(__file__).parent
VERSION = (ROOT / "src/eea/waterhub/policy/version.txt").read_text().strip()

setup(
    name="eea.waterhub.policy",
    version=VERSION,
    description="Plone policy package for the Copernicus Thematic Water Hub",
    long_description=(ROOT / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="European Environment Agency",
    url="https://github.com/eea/eea.waterhub.policy",
    license="MIT",
    python_requires=">=3.12,<3.14",
    package_dir={"": "src"},
    packages=find_namespace_packages(
        where="src",
        include=["eea.waterhub.policy*"],
    ),
    include_package_data=True,
    package_data={
        "eea.waterhub.policy": ["*.txt", "*.zcml", "profiles/**/*.xml"],
    },
    install_requires=[
        "Plone>=6.1.4,<6.2",
        "eea.volto.policy==12.7",
        "plone.volto",
        "setuptools",
    ],
    entry_points={"z3c.autoinclude.plugin": ["target = plone"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Addon",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
