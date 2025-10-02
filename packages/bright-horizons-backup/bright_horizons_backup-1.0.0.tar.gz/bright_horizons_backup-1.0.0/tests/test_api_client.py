"""Tests for api_client module."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bright_horizons_backup.api_client import fetch_dependents, fetch_parent_profile
from bright_horizons_backup.models import Dependent, ParentProfile


@pytest.fixture
def mock_context():
    context = MagicMock()
    context.cookies = AsyncMock(return_value=[{"name": "session", "value": "test_session"}])
    return context


@pytest.fixture
def sample_profile_data():
    return {
        "id": "123",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "brightstar_id": "456",
        "employer": "Test Corp",
        "phone_numbers": {"mobile": "555-1234"},
    }


@pytest.fixture
def sample_dependents_data():
    return [
        {
            "id": "789",
            "first_name": "Jane",
            "last_name": "Doe",
            "stage": "toddler",
            "status": "active",
            "birth_date": "2020-01-01T00:00:00Z",
            "enrollment_date": "2021-01-01T00:00:00Z",
            "graduation_date": "2025-01-01T00:00:00Z",
            "homeroom_id": "room1",
            "center": "Test Center",
        }
    ]


class TestFetchParentProfile:
    @pytest.mark.asyncio
    async def test_fetch_parent_profile_success(self, mock_context, sample_profile_data, tmp_path):
        with patch("bright_horizons_backup.api_client.httpx.AsyncClient") as mock_client:
            mock_response = MagicMock()
            mock_response.json.return_value = sample_profile_data
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response

            profile = await fetch_parent_profile(mock_context, tmp_path)

            assert isinstance(profile, ParentProfile)
            assert profile.id == "123"
            assert profile.first_name == "John"
            assert profile.email == "john@example.com"

            # Check file was created
            profile_file = tmp_path / "parent_profile.json"
            assert profile_file.exists()

    @pytest.mark.asyncio
    async def test_fetch_parent_profile_http_error(self, mock_context, tmp_path):
        with patch("bright_horizons_backup.api_client.httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value.get.side_effect = Exception("HTTP Error")

            profile = await fetch_parent_profile(mock_context, tmp_path)
            assert profile is None


class TestFetchDependents:
    @pytest.mark.asyncio
    async def test_fetch_dependents_success(self, mock_context, sample_dependents_data, tmp_path):
        with patch("bright_horizons_backup.api_client.httpx.AsyncClient") as mock_client:
            mock_response = MagicMock()
            mock_response.json.return_value = sample_dependents_data
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response

            dependents = await fetch_dependents(mock_context, "123", tmp_path)

            assert len(dependents) == 1
            assert isinstance(dependents[0], Dependent)
            assert dependents[0].id == "789"
            assert dependents[0].first_name == "Jane"

            # Check files were created
            dependents_file = tmp_path / "dependents.json"
            assert dependents_file.exists()

            dep_dir = tmp_path / "Jane_Doe_789"
            dep_file = dep_dir / "dependent.json"
            assert dep_file.exists()

    @pytest.mark.asyncio
    async def test_fetch_dependents_http_error(self, mock_context, tmp_path):
        with patch("bright_horizons_backup.api_client.httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value.get.side_effect = Exception("HTTP Error")

            dependents = await fetch_dependents(mock_context, "123", tmp_path)
            assert dependents == []
