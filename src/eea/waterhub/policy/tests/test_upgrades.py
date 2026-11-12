"""Policy upgrade tests."""

from unittest.mock import Mock

from eea.waterhub.policy.upgrades import (
<<<<<<< Updated upstream
    import_copernicus_taxonomies,
    install_eea_volto_policy,
=======
    install_eea_volto_policy,
    install_friendly_captcha,
>>>>>>> Stashed changes
)


def test_install_eea_volto_policy_runs_dependency_profile():
    """The 1000-to-1001 upgrade installs the shared EEA policy."""
    setup_tool = Mock()

    install_eea_volto_policy(setup_tool)

    setup_tool.runAllImportStepsFromProfile.assert_called_once_with(
        "profile-eea.volto.policy:default"
    )


<<<<<<< Updated upstream
def test_import_copernicus_taxonomies_runs_taxonomy_import_step():
    """The 1001-to-1002 upgrade imports this package's taxonomies."""
    setup_tool = Mock()

    import_copernicus_taxonomies(setup_tool)

    setup_tool.runImportStepFromProfile.assert_called_once_with(
        "profile-eea.waterhub.policy:default", "collective.taxonomy"
    )
=======
def test_install_friendly_captcha_installs_formsupport_and_settings():
    """The 1001-to-1002 upgrade installs form support and the captcha settings."""
    setup_tool = Mock()

    install_friendly_captcha(setup_tool)

    setup_tool.runAllImportStepsFromProfile.assert_called_once_with(
        "profile-collective.volto.formsupport:default"
    )
    assert [c.args for c in setup_tool.runImportStepFromProfile.call_args_list] == [
        ("profile-eea.waterhub.policy:default", "plone.app.registry"),
        ("profile-eea.waterhub.policy:default", "controlpanel"),
    ]
>>>>>>> Stashed changes
