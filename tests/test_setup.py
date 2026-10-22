"""Policy installation tests."""

from plone.browserlayer.utils import registered_layers
from Products.CMFCore.utils import getToolByName

from eea.waterhub.policy.interfaces import IWaterHubPolicyLayer

from .layer import WATERHUB_POLICY_INTEGRATION_TESTING


class TestSetup:
    """Verify the default and uninstall profiles."""

    layer = WATERHUB_POLICY_INTEGRATION_TESTING

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

    def test_uninstall_profile_cleans_up_only_waterhub_configuration(self):
        portal = self.layer["portal"]
        setup_tool = getToolByName(portal, "portal_setup")
        setup_tool.runAllImportStepsFromProfile("profile-eea.waterhub.policy:uninstall")
        assert IWaterHubPolicyLayer not in registered_layers()
        assert (
            setup_tool.getLastVersionForProfile("eea.volto.policy:default") != "unknown"
        )
