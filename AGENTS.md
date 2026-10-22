# Project instructions

## Scope

This repository contains the `eea.waterhub.policy` Plone 6 policy package for
the Copernicus Thematic Water Hub. Runtime image and deployment configuration
belong in the separate `waterhub-backend` repository.

## Layout

- Python package: `src/eea/waterhub/policy`
- GenericSetup profiles: `src/eea/waterhub/policy/profiles`
- Tests: `tests`
- Package and tool configuration: `pyproject.toml`

## Development workflow

Use Python 3.12 and the project virtual environment:

```shell
make install
```

Before committing, apply safe mechanical fixes and run the complete preflight:

```shell
make format
make ci
```

`make ci` is the canonical strict quality command. It runs Ruff without
modifying files, executes tests with JUnit and coverage reports, and validates
the built distributions. Keep future Jenkins commands identical to the
underlying commands exposed by these Make targets.

## Change guidelines

- Keep WaterHub-specific behavior in this package; prefer shared behavior from
  `eea.volto.policy` where appropriate.
- Add or update tests for behavioral changes.
- Add an entry under the unreleased version in `CHANGES.md`.
- Restart Plone after Python or ZCML changes when testing through the backend.
- Do not edit generated `*.egg-info`, build, distribution, or coverage files.
- Do not add Jenkins, release, security-contact, or ownership configuration
  without confirming the corresponding EEA infrastructure values.
