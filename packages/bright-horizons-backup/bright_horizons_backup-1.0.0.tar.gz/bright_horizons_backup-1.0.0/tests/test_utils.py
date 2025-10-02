"""Tests for utils module."""

import os
from unittest.mock import patch

from bright_horizons_backup.utils import env, ts


class TestEnv:
    def test_env_existing_variable(self):
        with patch.dict(os.environ, {"TEST_VAR": "test_value"}):
            assert env("TEST_VAR") == "test_value"

    def test_env_nonexistent_variable(self):
        assert env("NONEXISTENT_VAR") is None

    def test_env_strips_whitespace(self):
        with patch.dict(os.environ, {"TEST_VAR": "  test_value  "}):
            assert env("TEST_VAR") == "test_value"

    def test_env_empty_string(self):
        with patch.dict(os.environ, {"TEST_VAR": ""}):
            assert env("TEST_VAR") is None  # Empty string becomes None after strip()


class TestTimestamp:
    def test_ts_format(self):
        timestamp = ts()
        assert len(timestamp) == 15  # YYYYMMDD_HHMMSS
        assert "_" in timestamp
        assert timestamp.count("_") == 1

    def test_ts_contains_valid_date_parts(self):
        timestamp = ts()
        date_part, time_part = timestamp.split("_")
        assert len(date_part) == 8  # YYYYMMDD
        assert len(time_part) == 6  # HHMMSS
        assert date_part.isdigit()
        assert time_part.isdigit()
