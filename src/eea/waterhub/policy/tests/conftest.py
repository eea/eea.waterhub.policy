"""Pytest fixtures for the WaterHub policy integration layer."""

from pytest_plone import fixtures_factory

from .layer import WATERHUB_POLICY_INTEGRATION_TESTING

pytest_plugins = ["pytest_plone"]

globals().update(
    fixtures_factory(((WATERHUB_POLICY_INTEGRATION_TESTING, "integration"),))
)
