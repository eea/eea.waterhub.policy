"""Integration test layer."""

from plone.app.testing import PLONE_FIXTURE, IntegrationTesting, PloneSandboxLayer

from eea.waterhub.policy import PACKAGE_NAME


class WaterHubPolicyLayer(PloneSandboxLayer):
    """Install the policy profile in an isolated Plone site."""

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configuration_context):
        import eea.waterhub.policy

        self.loadZCML(package=eea.waterhub.policy)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, f"{PACKAGE_NAME}:default")


WATERHUB_POLICY_FIXTURE = WaterHubPolicyLayer()
WATERHUB_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(WATERHUB_POLICY_FIXTURE,),
    name="WaterHubPolicyLayer:IntegrationTesting",
)
