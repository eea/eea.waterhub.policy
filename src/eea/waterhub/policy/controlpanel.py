"""Friendly Captcha control panel."""

from plone.app.registry.browser.controlpanel import (
    ControlPanelFormWrapper,
    RegistryEditForm,
)
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.restapi.controlpanels.interfaces import IControlpanel
from plone.z3cform import layout
from zope import schema
from zope.component import adapter
from zope.interface import Interface, implementer

from eea.waterhub.policy import _
from eea.waterhub.policy.interfaces import IWaterHubPolicyLayer

FRIENDLY_CAPTCHA_PREFIX = "eea.waterhub.policy.friendly_captcha"


class IFriendlyCaptchaSettings(Interface):
    """Friendly Captcha registry settings."""

    public_key = schema.TextLine(
        title=_("Public key"),
        description=_("Friendly Captcha application sitekey."),
        required=False,
        default="",
    )

    private_key = schema.TextLine(
        title=_("Private key"),
        description=_("Friendly Captcha API key used to verify solutions."),
        required=False,
        default="",
    )


class IFriendlyCaptchaControlPanel(IControlpanel):
    """Marker interface for the Friendly Captcha control panel."""


class FriendlyCaptchaEditForm(RegistryEditForm):
    """Classic Plone edit form for the Friendly Captcha settings."""

    schema = IFriendlyCaptchaSettings
    schema_prefix = FRIENDLY_CAPTCHA_PREFIX
    label = _("Friendly Captcha")


FriendlyCaptchaControlPanelView = layout.wrap_form(
    FriendlyCaptchaEditForm, ControlPanelFormWrapper
)


@adapter(Interface, IWaterHubPolicyLayer)
@implementer(IFriendlyCaptchaControlPanel)
class FriendlyCaptchaConfigletPanel(RegistryConfigletPanel):
    """Expose the Friendly Captcha settings through @controlpanels."""

    schema = IFriendlyCaptchaSettings
    schema_prefix = FRIENDLY_CAPTCHA_PREFIX
    configlet_id = "friendly-captcha-controlpanel"
    configlet_category_id = "Products"
    title = _("Friendly Captcha")
    group = "Add-on Configuration"
