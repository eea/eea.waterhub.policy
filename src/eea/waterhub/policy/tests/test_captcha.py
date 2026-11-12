"""Friendly Captcha provider tests."""

from unittest import mock

import pytest
import requests
from collective.volto.formsupport.interfaces import ICaptchaSupport
from plone import api
from zExceptions import BadRequest
from zope.component import getMultiAdapter, getUtility
from zope.schema.interfaces import IVocabularyFactory

from eea.waterhub.policy.captcha import VERIFY_URL
from eea.waterhub.policy.controlpanel import FRIENDLY_CAPTCHA_PREFIX

from .layer import WATERHUB_POLICY_INTEGRATION_TESTING


def set_keys(site_key="site-key", secret="api-key"):
    api.portal.set_registry_record(f"{FRIENDLY_CAPTCHA_PREFIX}.site_key", site_key)
    api.portal.set_registry_record(f"{FRIENDLY_CAPTCHA_PREFIX}.secret", secret)


def verify_response(payload, status_code=200):
    response = mock.Mock(status_code=status_code)
    response.json.return_value = payload
    return response


class TestFriendlyCaptcha:
    """Verify the friendly_captcha ICaptchaSupport adapter."""

    layer = WATERHUB_POLICY_INTEGRATION_TESTING

    @pytest.fixture(autouse=True)
    def _integration_layer(self, integration):
        """Run every captcha test inside the policy integration layer."""

    @pytest.fixture
    def captcha(self):
        portal = self.layer["portal"]
        return getMultiAdapter(
            (portal, self.layer["request"]), ICaptchaSupport, name="friendly_captcha"
        )

    @pytest.fixture
    def post(self):
        with mock.patch("eea.waterhub.policy.captcha.requests.post") as post:
            yield post

    def test_disabled_without_keys(self, captcha):
        assert not captcha.isEnabled()

    def test_enabled_with_keys(self, captcha):
        set_keys()
        assert captcha.isEnabled()

    def test_serialize_exposes_only_site_key(self, captcha):
        set_keys()
        props = captcha.serialize()
        assert props["provider"] == "friendly_captcha"
        assert props["site_key"] == "site-key"
        assert "api-key" not in props.values()

    def test_verify_accepts_valid_solution(self, captcha, post):
        set_keys()
        post.return_value = verify_response({"success": True})

        captcha.verify({"provider": "friendly_captcha", "token": "solution"})

        post.assert_called_once_with(
            VERIFY_URL,
            data={"solution": "solution", "secret": "api-key", "sitekey": "site-key"},
            timeout=15,
        )

    def test_verify_rejects_missing_token(self, captcha, post):
        set_keys()
        with pytest.raises(BadRequest):
            captcha.verify({"provider": "friendly_captcha"})
        with pytest.raises(BadRequest):
            captcha.verify(None)
        post.assert_not_called()

    def test_verify_rejects_invalid_solution(self, captcha, post):
        set_keys()
        post.return_value = verify_response(
            {"success": False, "errors": ["solution_invalid"]}, status_code=400
        )
        with pytest.raises(BadRequest):
            captcha.verify({"token": "solution"})

    def test_verify_rejects_on_request_error(self, captcha, post):
        set_keys()
        post.side_effect = requests.ConnectionError()
        with pytest.raises(BadRequest):
            captcha.verify({"token": "solution"})

    def test_verify_rejects_non_json_response(self, captcha, post):
        set_keys()
        post.return_value.json.side_effect = ValueError()
        with pytest.raises(BadRequest):
            captcha.verify({"token": "solution"})

    def test_provider_vocabulary_lists_configured_captcha(self):
        portal = self.layer["portal"]
        factory = getUtility(
            IVocabularyFactory, name="collective.volto.formsupport.captcha.providers"
        )
        assert "friendly_captcha" not in factory(portal)

        set_keys()

        assert "friendly_captcha" in factory(portal)
