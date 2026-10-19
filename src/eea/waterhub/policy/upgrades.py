"""Upgrade steps for eea.waterhub.policy."""


def install_eea_volto_policy(context):
    """Install the EEA Volto policy on existing WaterHub sites."""
    context.runAllImportStepsFromProfile("profile-eea.volto.policy:default")
