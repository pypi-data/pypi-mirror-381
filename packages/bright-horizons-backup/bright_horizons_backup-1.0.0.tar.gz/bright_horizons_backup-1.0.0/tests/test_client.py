"""Tests for client module."""

import json
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bright_horizons_backup.client import BrightHorizonsClient
from bright_horizons_backup.models import DailyReportData, Dependent


@pytest.fixture
def sample_dependent():
    return Dependent(
        id="789",
        first_name="Jane",
        last_name="Doe",
        stage="toddler",
        status="active",
        birth_date=datetime(2020, 1, 1),
        enrollment_date=datetime(2021, 1, 1),
        graduation_date=datetime(2025, 1, 1),
        homeroom_id="room1",
        center="Test Center",
    )


@pytest.fixture
def sample_daily_report():
    return {
        "for_date": "2023-01-01",
        "dependent_id": "789",
        "updated": "2023-01-01T12:00:00Z",
        "note_entries": [
            {
                "id": "note1",
                "note": "Great day!",
                "actor": "Teacher",
                "capture_time": "2023-01-01T10:00:00Z",
                "is_from_parent": False,
            }
        ],
        "activity_entries": [],
        "snapshot_entries": [],
    }


class TestBrightHorizonsClient:
    def test_init_with_credentials(self):
        client = BrightHorizonsClient(email="test@example.com", password="password")
        assert client.email == "test@example.com"
        assert client.password == "password"

    def test_init_without_credentials_raises_error(self):
        with patch("bright_horizons_backup.client.env", return_value=None):
            with pytest.raises(ValueError):
                BrightHorizonsClient()

    @pytest.mark.asyncio
    async def test_context_manager(self):
        with patch.object(BrightHorizonsClient, "_setup_browser", new_callable=AsyncMock):
            with patch.object(BrightHorizonsClient, "_cleanup", new_callable=AsyncMock):
                async with BrightHorizonsClient(email="test@example.com", password="password") as client:
                    assert client is not None

    @pytest.mark.asyncio
    async def test_process_daily_report(self):
        client = BrightHorizonsClient(email="test@example.com", password="password")
        raw_report = {
            "for_date": "2023-01-01",
            "dependent_id": "789",
            "note_entries": [
                {
                    "id": "note1",
                    "note": "Great day!",
                    "actor": "Teacher",
                    "capture_time": "2023-01-01T10:00:00Z",
                    "is_from_parent": False,
                }
            ],
            "activity_entries": [],
            "snapshot_entries": [],
        }

        processed = client._process_daily_report(raw_report)

        assert isinstance(processed, DailyReportData)
        assert processed.date == "2023-01-01"
        assert processed.dependent_id == "789"
        assert len(processed.teacher_notes) == 1
        assert processed.teacher_notes[0].note == "Great day!"

    @pytest.mark.asyncio
    async def test_fetch_daily_reports_batch_from_disk(self, sample_dependent, sample_daily_report, tmp_path):
        client = BrightHorizonsClient(email="test@example.com", password="password")
        client.output_dir = tmp_path

        # Create existing batch file
        dep_dir = tmp_path / sample_dependent.folder
        batch_dir = dep_dir / "raw"
        batch_dir.mkdir(parents=True)
        batch_file = batch_dir / "batch_2023-01-01_2023-01-31.json"
        batch_file.write_text(json.dumps([sample_daily_report]))

        result = await client.fetch_daily_reports_batch(sample_dependent.id, "2023-01-01", "2023-01-31", dep_dir)

        assert len(result) == 1
        assert result[0]["for_date"] == "2023-01-01"

    @pytest.mark.asyncio
    async def test_fetch_daily_reports_batch_http_error(self, sample_dependent, tmp_path):
        client = BrightHorizonsClient(email="test@example.com", password="password")
        client.output_dir = tmp_path
        client.context = MagicMock()
        client.context.cookies = AsyncMock(return_value=[])

        dep_dir = tmp_path / sample_dependent.folder

        with patch("bright_horizons_backup.client.httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value.get.side_effect = Exception("HTTP Error")

            result = await client.fetch_daily_reports_batch(sample_dependent.id, "2023-01-01", "2023-01-31", dep_dir)

            assert result == []


class TestClientAuthentication:
    @pytest.mark.asyncio
    async def test_try_existing_session_no_state_file(self):
        client = BrightHorizonsClient(email="test@example.com", password="password")
        client.browser = MagicMock()

        with patch("bright_horizons_backup.client.STATE_FILE") as mock_state_file:
            mock_state_file.exists.return_value = False

            result = await client._try_existing_session()
            assert result is False

    @pytest.mark.asyncio
    async def test_authenticate_existing_session_success(self):
        client = BrightHorizonsClient(email="test@example.com", password="password")

        with patch.object(client, "_try_existing_session", return_value=True):
            result = await client.authenticate()
            assert result is True
            assert client.authenticated is True

    @pytest.mark.asyncio
    async def test_authenticate_fresh_login_success(self):
        client = BrightHorizonsClient(email="test@example.com", password="password")

        with patch.object(client, "_try_existing_session", return_value=False):
            with patch.object(client, "_create_new_context", new_callable=AsyncMock):
                with patch.object(client, "_perform_fresh_login", new_callable=AsyncMock):
                    with patch("bright_horizons_backup.client.wait_signed_in", return_value=True):
                        with patch(
                            "bright_horizons_backup.client.navigate_to_bright_day",
                            new_callable=AsyncMock,
                        ):
                            client.page = MagicMock()
                            client.artifacts_dir = MagicMock()
                            client.context = MagicMock()
                            client.context.storage_state = AsyncMock()

                            result = await client.authenticate()
                            assert result is True
                            assert client.authenticated is True
