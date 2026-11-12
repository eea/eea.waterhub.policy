"""Friendly Captcha provider for collective.volto.formsupport."""

import logging

import requests
from collective.volto.formsupport.captcha import CaptchaSupport
from plone import api
from zExceptions import BadRequest
from zope.i18n import translate

from eea.waterhub.policy import _
from eea.waterhub.policy.controlpanel import FRIENDLY_CAPTCHA_PREFIX

logger = logging.getLogger(__name__)

VERIFY_URL = "https://api.friendlycaptcha.com/api/v1/siteverify"
VERIFY_TIMEOUT = 15


def get_setting(name):
    """Read a Friendly Captcha registry record."""
    return api.portal.get_registry_record(
        f"{FRIENDLY_CAPTCHA_PREFIX}.{name}", default=""
    )


class FriendlyCaptchaSupport(CaptchaSupport):
    """Verify Friendly Captcha v1 solutions submitted with Volto forms."""

    name = _("Friendly Captcha")

    def isEnabled(self):
        return bool(get_setting("public_key") and get_setting("private_key"))

    def serialize(self):
        return {
            "provider": "friendly_captcha",
            "id": "friendly_captcha",
            "title": "Friendly Captcha",
            "site_key": get_setting("public_key"),
        }

    def verify(self, data):
        token = (data or {}).get("token")
        if not token:
            self._fail(_("No captcha token provided."))

        payload = {
            "solution": token,
            "secret": get_setting("private_key"),
            "sitekey": get_setting("public_key"),
        }
        # Rejections come back as JSON with HTTP 200 (invalid solution) or 400
        # (bad configuration), so only network errors and non-JSON answers are
        # treated as request failures.
        try:
            response = requests.post(VERIFY_URL, data=payload, timeout=VERIFY_TIMEOUT)
            result = response.json()
        except (requests.RequestException, ValueError):
            logger.exception("Friendly Captcha verification request failed")
            self._fail(_("The captcha could not be verified, please try again."))

        if not result.get("success"):
            logger.warning(
                "Friendly Captcha rejected solution (HTTP %s): %s",
                response.status_code,
                result.get("errors"),
            )
            self._fail(_("The captcha verification failed, please try again."))

    def _fail(self, message):
        raise BadRequest(translate(message, context=self.request))
