from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, computed_field


class ParentProfile(BaseModel):
    """Parent profile data structure."""

    id: str
    first_name: str
    last_name: str
    email: str
    brightstar_id: str
    employer: str = ""
    mobile_phone: Optional[str] = None
    raw_data: Optional[dict] = None


class Dependent(BaseModel):
    """Dependent data structure."""

    id: str
    first_name: str
    last_name: str
    stage: str
    status: str
    birth_date: datetime
    enrollment_date: datetime
    graduation_date: datetime
    homeroom_id: str
    center: str
    raw_data: Optional[dict] = None

    @computed_field  # type: ignore
    @property
    def folder(self) -> str:
        """Generate folder name for dependent."""
        return f"{self.first_name}_{self.last_name}_{self.id}"


class Snapshot(BaseModel):
    """Snapshot data structure."""

    id: str
    note: Optional[str] = None
    attachment_id: Optional[str] = None
    created_by: Optional[Dict[str, Any]] = None
    capture_time: str


class Activity(BaseModel):
    """Activity data structure."""

    id: str
    description: Optional[str] = None
    subject_names: list[str] = Field(default_factory=list)
    snapshots: list[Snapshot] = Field(default_factory=list)
    entry_time: Optional[str] = None


class TeacherNote(BaseModel):
    """Teacher note data structure."""

    id: str
    note: str
    actor: Optional[str] = None
    attachment_id: Optional[str] = None
    capture_time: str
    is_from_parent: bool


class DailyReportData(BaseModel):
    """Processed daily report data structure."""

    date: str
    dependent_id: str
    teacher_notes: List[TeacherNote]
    activities: List[Activity]
    snapshots: List[Snapshot]
