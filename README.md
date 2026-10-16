# eea.waterhub.policy

Plone 6 policy package for the Copernicus Thematic Water Hub.

The package owns WaterHub-specific backend configuration, including
GenericSetup profiles, registry settings, content types, workflows, upgrade
steps, and REST API customizations.

## Installation

Add `eea.waterhub.policy` to the backend requirements and install the
`eea.waterhub.policy:default` GenericSetup profile.

For editable backend development, add this repository to the backend's
`mx.ini` and rebuild its development image.

## Development

Create a Python 3.12 virtual environment and install the test dependencies:

```shell
python3.12 -m venv .venv
.venv/bin/pip install -e ".[test]"
.venv/bin/pytest
```

Run the static checks with:

```shell
.venv/bin/ruff check src tests
.venv/bin/ruff format --check src tests
```

