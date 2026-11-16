"""Policy upgrade tests."""

from unittest.mock import Mock

from eea.waterhub.policy.upgrades import (
    import_copernicus_taxonomies,
    import_user_profile_taxonomies,
    install_eea_volto_policy,
)


def test_install_eea_volto_policy_runs_dependency_profile():
    """The 1000-to-1001 upgrade installs the shared EEA policy."""
    setup_tool = Mock()

    install_eea_volto_policy(setup_tool)

    setup_tool.runAllImportStepsFromProfile.assert_called_once_with(
        "profile-eea.volto.policy:default"
    )


def test_import_copernicus_taxonomies_runs_taxonomy_import_step():
    """The 1001-to-1002 upgrade imports this package's taxonomies."""
    setup_tool = Mock()

    import_copernicus_taxonomies(setup_tool)

    setup_tool.runImportStepFromProfile.assert_called_once_with(
        "profile-eea.waterhub.policy:default", "collective.taxonomy"
    )


def test_import_user_profile_taxonomies_runs_taxonomy_import_step():
    """The 1002-to-1003 upgrade imports the User Profile taxonomies."""
    setup_tool = Mock()

    import_user_profile_taxonomies(setup_tool)

    setup_tool.runImportStepFromProfile.assert_called_once_with(
        "profile-eea.waterhub.policy:default", "collective.taxonomy"
    )
