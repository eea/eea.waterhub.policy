"""Upgrade steps for eea.waterhub.policy."""


def install_eea_volto_policy(context):
    """Install the EEA Volto policy on existing WaterHub sites."""
    context.runAllImportStepsFromProfile("profile-eea.volto.policy:default")


<<<<<<< Updated upstream
def import_copernicus_taxonomies(context):
    """Import the Copernicus taxonomies from the WaterHub profile."""
    context.runImportStepFromProfile(
        "profile-eea.waterhub.policy:default", "collective.taxonomy"
=======
def install_friendly_captcha(context):
    """Install form support and the Friendly Captcha settings."""
    context.runAllImportStepsFromProfile("profile-collective.volto.formsupport:default")
    context.runImportStepFromProfile(
        "profile-eea.waterhub.policy:default", "plone.app.registry"
    )
    context.runImportStepFromProfile(
        "profile-eea.waterhub.policy:default", "controlpanel"
>>>>>>> Stashed changes
    )
