"""Upgrade steps for eea.waterhub.policy."""


def install_eea_volto_policy(context):
    """Install the EEA Volto policy on existing WaterHub sites."""
    context.runAllImportStepsFromProfile("profile-eea.volto.policy:default")


def import_copernicus_taxonomies(context):
    """Import the Copernicus taxonomies from the WaterHub profile."""
    context.runImportStepFromProfile(
        "profile-eea.waterhub.policy:default", "collective.taxonomy"
    )
