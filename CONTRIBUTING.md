# Contributing to eea.waterhub.policy

Thank you for contributing to the WaterHub backend policy package.

## Set up the development environment

Python 3.12 is the documented development version. Create the local virtual
environment and install the package with its test dependencies:

```shell
make install
```

The equivalent commands are:

```shell
python3.12 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install --editable ".[test]"
```

## Make a change

- Keep changes focused on WaterHub-specific Plone configuration.
- Add tests for new or changed behavior.
- Update the unreleased section of `CHANGES.md` for user-visible changes.
- Reference the relevant issue in commits and pull requests when available,
  following the established `Refs #<issue>` convention.

Apply safe formatting and import fixes before committing:

```shell
make format
```

Then run the strict package checks:

```shell
make ci
```

This verifies Ruff formatting and lint rules, runs tests with coverage, builds
the source and wheel distributions, and validates their metadata.

## Run individual checks

```shell
make lint
make test
make test-ci
make package
```

Generated JUnit and coverage reports are written below
`xunit-reports-current/`. These files are ignored by Git.

## Pull requests

Open pull requests against `main`. Describe the intended behavior, link the
related issue, and include the checks you ran. Do not include generated build,
package metadata, or coverage artifacts.

Package publishing and automated release steps are intentionally not
documented until the EEA release infrastructure for this repository has been
confirmed.
