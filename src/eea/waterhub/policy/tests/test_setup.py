"""Policy installation tests."""

import pytest
from collective.taxonomy.interfaces import ITaxonomy
from plone.browserlayer.utils import registered_layers
from Products.CMFCore.utils import getToolByName

from eea.waterhub.policy.interfaces import IWaterHubPolicyLayer

from .layer import WATERHUB_POLICY_INTEGRATION_TESTING


class TestSetup:
    """Verify the default and uninstall profiles."""

    layer = WATERHUB_POLICY_INTEGRATION_TESTING

    @pytest.fixture(autouse=True)
    def _integration_layer(self, integration):
        """Run every setup test inside the policy integration layer."""

    def test_package_is_installed(self):
        portal = self.layer["portal"]
        setup_tool = getToolByName(portal, "portal_setup")
        profile = "eea.waterhub.policy:default"
        assert setup_tool.getLastVersionForProfile(profile) != "unknown"

    def test_browser_layer_is_installed(self):
        assert IWaterHubPolicyLayer in registered_layers()

    def test_eea_volto_policy_dependency_is_installed(self):
        portal = self.layer["portal"]
        setup_tool = getToolByName(portal, "portal_setup")
        profile = "eea.volto.policy:default"
        assert setup_tool.getLastVersionForProfile(profile) != "unknown"

    @pytest.mark.parametrize(
        ("name", "title", "expected_terms"),
        (
            ("copernicus_services", "Copernicus Services", 6),
            ("copernicus_components", "Copernicus Components", 26),
            ("copernicus_themes", "Copernicus themes", 36),
        ),
    )
    def test_copernicus_taxonomy_is_installed(self, name, title, expected_terms):
        portal = self.layer["portal"]
        taxonomy = portal.getSiteManager().queryUtility(
            ITaxonomy, name=f"collective.taxonomy.{name}"
        )

        assert taxonomy is not None
        assert taxonomy.title == title
        assert len(taxonomy.data["en"]) == expected_terms

    def test_taxonomy_upgrade_is_available_from_profile_1001(self):
        portal = self.layer["portal"]
        setup_tool = getToolByName(portal, "portal_setup")
        profile = "eea.waterhub.policy:default"

        setup_tool.setLastVersionForProfile(profile, "1001")
        upgrades = setup_tool.listUpgrades(profile, simple=True)
        setup_tool.setLastVersionForProfile(profile, "1002")

        assert [step.dest for step in upgrades] == [("1002",)]
        assert upgrades[0].title == "Import the Copernicus taxonomies"

    def test_uninstall_profile_cleans_up_only_waterhub_configuration(self):
        portal = self.layer["portal"]
        setup_tool = getToolByName(portal, "portal_setup")
        setup_tool.runAllImportStepsFromProfile("profile-eea.waterhub.policy:uninstall")
        assert IWaterHubPolicyLayer not in registered_layers()
        assert (
            setup_tool.getLastVersionForProfile("eea.volto.policy:default") != "unknown"
        )
