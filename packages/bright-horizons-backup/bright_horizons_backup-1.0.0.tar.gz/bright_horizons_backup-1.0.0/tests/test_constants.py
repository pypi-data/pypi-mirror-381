"""Tests for constants module."""

from pathlib import Path

from bright_horizons_backup.constants import (
    BRIGHT_DAY_HOME,
    COOKIE_ACCEPT_SEL,
    FIC_LOGIN,
    LOGIN_SELECTOR,
    OKTA_PASSWORD_SEL,
    OKTA_USERNAME_SEL,
    PROFILE_API_URL,
    STATE_FILE,
)


class TestConstants:
    def test_urls_are_strings(self):
        assert isinstance(FIC_LOGIN, str)
        assert isinstance(BRIGHT_DAY_HOME, str)
        assert isinstance(PROFILE_API_URL, str)

    def test_urls_are_valid_format(self):
        assert FIC_LOGIN.startswith("https://")
        assert BRIGHT_DAY_HOME.startswith("https://")
        assert PROFILE_API_URL.startswith("https://")

    def test_state_file_is_path(self):
        assert isinstance(STATE_FILE, Path)
        assert STATE_FILE.name == "bh_state.json"

    def test_selectors_are_lists(self):
        assert isinstance(LOGIN_SELECTOR, list)
        assert isinstance(OKTA_USERNAME_SEL, list)
        assert isinstance(OKTA_PASSWORD_SEL, list)
        assert isinstance(COOKIE_ACCEPT_SEL, list)

    def test_selectors_not_empty(self):
        assert len(LOGIN_SELECTOR) > 0
        assert len(OKTA_USERNAME_SEL) > 0
        assert len(OKTA_PASSWORD_SEL) > 0
        assert len(COOKIE_ACCEPT_SEL) > 0
