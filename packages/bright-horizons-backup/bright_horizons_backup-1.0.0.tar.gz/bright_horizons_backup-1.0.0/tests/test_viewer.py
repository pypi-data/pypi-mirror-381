"""Tests for viewer module."""

import json
from time import sleep
from unittest.mock import patch

import pytest

from bright_horizons_backup.viewer import (
    find_latest_backup,
    get_image_cache,
    is_image,
    is_video,
    load_dependents,
    load_parent_profile,
    load_reports,
)


@pytest.fixture
def sample_profile_data():
    return {
        "id": "123",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "brightstar_id": "456",
    }


@pytest.fixture
def sample_dependent_data():
    return {
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


@pytest.fixture
def sample_report_data():
    return {
        "date": "2023-01-01",
        "dependent_id": "789",
        "teacher_notes": [],
        "activities": [],
        "snapshots": [],
    }


class TestLoadParentProfile:
    def test_load_parent_profile_success(self, sample_profile_data, tmp_path):
        global BACKUP_DIR
        BACKUP_DIR = tmp_path

        profile_file = tmp_path / "parent_profile.json"
        profile_file.write_text(json.dumps(sample_profile_data))

        with patch("bright_horizons_backup.viewer.BACKUP_DIR", tmp_path):
            profile = load_parent_profile()

            assert profile is not None
            assert profile.id == "123"
            assert profile.first_name == "John"

    def test_load_parent_profile_no_file(self, tmp_path):
        with patch("bright_horizons_backup.viewer.BACKUP_DIR", tmp_path):
            profile = load_parent_profile()
            assert profile is None


class TestLoadDependents:
    def test_load_dependents_success(self, sample_dependent_data, tmp_path):
        dep_dir = tmp_path / "Jane_Doe_789"
        dep_dir.mkdir()
        dep_file = dep_dir / "dependent.json"
        dep_file.write_text(json.dumps(sample_dependent_data))

        with patch("bright_horizons_backup.viewer.BACKUP_DIR", tmp_path):
            dependents = load_dependents()

            assert len(dependents) == 1
            assert dependents[0].id == "789"
            assert dependents[0].first_name == "Jane"

    def test_load_dependents_no_files(self, tmp_path):
        with patch("bright_horizons_backup.viewer.BACKUP_DIR", tmp_path):
            dependents = load_dependents()
            assert dependents == []


class TestLoadReports:
    def test_load_reports_success(self, sample_report_data, tmp_path):
        dep_folder = "Jane_Doe_789"
        processed_dir = tmp_path / dep_folder / "processed"
        processed_dir.mkdir(parents=True)
        report_file = processed_dir / "2023-01-01.json"
        report_file.write_text(json.dumps(sample_report_data))

        with patch("bright_horizons_backup.viewer.BACKUP_DIR", tmp_path):
            reports = load_reports(dep_folder)

            assert len(reports) == 1
            assert reports[0].date == "2023-01-01"

    def test_load_reports_no_directory(self, tmp_path):
        with patch("bright_horizons_backup.viewer.BACKUP_DIR", tmp_path):
            reports = load_reports("nonexistent")
            assert reports == []


class TestMediaHelpers:
    def test_is_image_true(self, tmp_path):
        dep_folder = "Jane_Doe_789"
        media_dir = tmp_path / dep_folder / "media"
        media_dir.mkdir(parents=True)
        image_file = media_dir / "att123.jpg"
        image_file.touch()

        with patch("bright_horizons_backup.viewer.BACKUP_DIR", tmp_path):
            with patch("glob.glob", return_value=[str(image_file)]):
                result = is_image("att123", dep_folder)
                assert result is True

    def test_is_image_false(self, tmp_path):
        dep_folder = "Jane_Doe_789"
        media_dir = tmp_path / dep_folder / "media"
        media_dir.mkdir(parents=True)
        video_file = media_dir / "att123.mp4"
        video_file.touch()

        with patch("bright_horizons_backup.viewer.BACKUP_DIR", tmp_path):
            with patch("glob.glob", return_value=[str(video_file)]):
                result = is_image("att123", dep_folder)
                assert result is False

    def test_is_video_true(self, tmp_path):
        dep_folder = "Jane_Doe_789"
        media_dir = tmp_path / dep_folder / "media"
        media_dir.mkdir(parents=True)
        video_file = media_dir / "att123.mp4"
        video_file.touch()

        with patch("bright_horizons_backup.viewer.BACKUP_DIR", tmp_path):
            with patch("glob.glob", return_value=[str(video_file)]):
                result = is_video("att123", dep_folder)
                assert result is True

    def test_get_image_cache(self, tmp_path):
        dep_folder = "Jane_Doe_789"
        media_dir = tmp_path / dep_folder / "media"
        media_dir.mkdir(parents=True)

        # Create some test files
        (media_dir / "img1.jpg").touch()
        (media_dir / "img2.png").touch()
        (media_dir / "vid1.mp4").touch()

        with patch("bright_horizons_backup.viewer.BACKUP_DIR", tmp_path):
            cache = get_image_cache(dep_folder)

            assert "img1" in cache
            assert "img2" in cache
            assert "vid1" not in cache


class TestFindLatestBackup:
    def test_find_latest_backup_success(self, tmp_path):
        # Create backup directories
        backup1 = tmp_path / "output_20230101_120000"
        backup2 = tmp_path / "output_20230102_120000"
        backup1.mkdir()
        sleep(2)
        backup2.mkdir()

        with patch("bright_horizons_backup.viewer.Path") as mock_path:
            mock_path.return_value.iterdir.return_value = [backup1, backup2]
            latest = find_latest_backup()
            assert latest is not None
            assert latest.name == "output_20230102_120000"

    def test_find_latest_backup_no_backups(self, tmp_path):
        with patch("bright_horizons_backup.viewer.Path.cwd", return_value=tmp_path):
            latest = find_latest_backup()
            assert latest is None
