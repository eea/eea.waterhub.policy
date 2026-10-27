# eea.waterhub.policy

Plone 6 policy package for the Copernicus Thematic Water Hub.

The package owns WaterHub-specific backend configuration, including
GenericSetup profiles, registry settings, content types, workflows, upgrade
steps, and REST API customizations.

## Supported versions

The policy is developed and tested with the stack pinned by
`waterhub-backend`:

- Plone `6.1.4`
- Python `3.12`
- `eea.volto.policy` `12.7`

Package metadata accepts compatible Plone `6.1.x` releases, while the backend
image remains the source of the exact deployed Plone and Python versions.

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

The same commands are available through the Makefile:

```shell
make install
make test
```

Run the strict static checks with:

```shell
.venv/bin/ruff check src
.venv/bin/ruff format --check src
```

Apply safe formatting and import fixes before committing:

```shell
make format
```

## CI preflight

Run all package quality gates with:

```shell
make ci
```

This runs strict Ruff checks, the test suite with JUnit and coverage output,
and source/wheel package validation. It writes reports to:

- `xunit-reports-current/junit.xml`
- `xunit-reports-current/coverage/coverage.xml`
- `xunit-reports-current/coverage/lcov.info`
- `xunit-reports-current/coverage/lcov-report/index.html`

The commands are intentionally usable without Make as well. The test command
used by `make test-ci` is:

```shell
mkdir -p xunit-reports-current/coverage
.venv/bin/pytest \
  --junitxml=xunit-reports-current/junit.xml \
  --cov=eea.waterhub.policy \
  --cov-report=term-missing \
  --cov-report=xml:xunit-reports-current/coverage/coverage.xml \
  --cov-report=lcov:xunit-reports-current/coverage/lcov.info \
  --cov-report=html:xunit-reports-current/coverage/lcov-report
```

Python coverage for SonarQube is provided by `coverage.xml`; `lcov.info` and
the HTML report are retained for other reporting consumers and local review.

## Secret scanning

The Betterleaks GitHub Action scans the current repository content on every
push and pull request using `.gitleaks.toml`. When it finds a potential secret,
the check fails and uploads a redacted `betterleaks-report` artifact.

Optional failure emails require these repository or organization secrets:

- `SMTP_URL`
- `SMTP_PORT` (defaults to `25`)
- `SMTP_EMAIL`
- `SMTP_PASSWORD` (optional when the SMTP server needs no authentication)

For a real secret, remove it, rotate it, and move it to the approved secret
store. For a verified false positive, add `#betterleaks:allow` on the same line
and explain the exception in the pull request. Never allowlist a real secret.

## Contributing and releases

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution workflow. Package
release automation is not configured yet; see [CHANGES.md](CHANGES.md) for
the current release notes.

