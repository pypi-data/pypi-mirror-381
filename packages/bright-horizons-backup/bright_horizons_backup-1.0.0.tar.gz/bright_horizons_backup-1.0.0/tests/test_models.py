"""Tests for models module."""

from datetime import datetime

from bright_horizons_backup.models import Activity, DailyReportData, Dependent, ParentProfile, Snapshot, TeacherNote


class TestParentProfile:
    def test_create_parent_profile(self):
        profile = ParentProfile(
            id="123",
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            brightstar_id="456",
        )
        assert profile.id == "123"
        assert profile.first_name == "John"
        assert profile.email == "john@example.com"

    def test_parent_profile_with_optional_fields(self):
        profile = ParentProfile(
            id="123",
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            brightstar_id="456",
            employer="Test Corp",
            mobile_phone="555-1234",
        )
        assert profile.employer == "Test Corp"
        assert profile.mobile_phone == "555-1234"


class TestDependent:
    def test_create_dependent(self):
        dependent = Dependent(
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
        assert dependent.id == "789"
        assert dependent.first_name == "Jane"
        assert dependent.stage == "toddler"

    def test_dependent_folder_property(self):
        dependent = Dependent(
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
        assert dependent.folder == "Jane_Doe_789"


class TestSnapshot:
    def test_create_snapshot(self):
        snapshot = Snapshot(id="snap1", note="Test note", attachment_id="att1", capture_time="2023-01-01T10:00:00Z")
        assert snapshot.id == "snap1"
        assert snapshot.note == "Test note"
        assert snapshot.attachment_id == "att1"


class TestActivity:
    def test_create_activity(self):
        snapshot = Snapshot(id="snap1", capture_time="2023-01-01T10:00:00Z")
        activity = Activity(id="act1", description="Playing", subject_names=["art", "music"], snapshots=[snapshot])
        assert activity.id == "act1"
        assert activity.description == "Playing"
        assert len(activity.snapshots) == 1
        assert activity.subject_names == ["art", "music"]


class TestTeacherNote:
    def test_create_teacher_note(self):
        note = TeacherNote(id="note1", note="Great day!", capture_time="2023-01-01T10:00:00Z", is_from_parent=False)
        assert note.id == "note1"
        assert note.note == "Great day!"
        assert not note.is_from_parent


class TestDailyReportData:
    def test_create_daily_report(self):
        note = TeacherNote(id="note1", note="Great day!", capture_time="2023-01-01T10:00:00Z", is_from_parent=False)
        report = DailyReportData(
            date="2023-01-01", dependent_id="789", teacher_notes=[note], activities=[], snapshots=[]
        )
        assert report.date == "2023-01-01"
        assert report.dependent_id == "789"
        assert len(report.teacher_notes) == 1
