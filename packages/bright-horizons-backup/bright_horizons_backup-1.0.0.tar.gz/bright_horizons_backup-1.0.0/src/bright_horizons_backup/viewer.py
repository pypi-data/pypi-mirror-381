#!/usr/bin/env python3
import glob
import json
import logging
import os
import random
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from flask import Flask, render_template, send_from_directory

from bright_horizons_backup import DailyReportData, Dependent, ParentProfile

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, root_path=os.getcwd(), template_folder=os.path.join(basedir, "templates"))
BACKUP_DIR = None

# Cache for image mappings
_image_cache: dict = {}


def load_parent_profile() -> Optional[ParentProfile]:
    """Load parent profile from backup directory."""
    if not BACKUP_DIR:
        return None
    profile_file = BACKUP_DIR / "parent_profile.json"
    if profile_file.exists():
        with open(profile_file) as f:
            profile_data = json.load(f)
            return ParentProfile(**profile_data)
    return None


def load_dependents() -> List[Dependent]:
    """Load all dependents from backup directory."""
    dependents: List[Dependent] = []
    if not BACKUP_DIR:
        return dependents
    for dep_dir in BACKUP_DIR.iterdir():
        if dep_dir.is_dir() and "_" in dep_dir.name:
            dep_file = dep_dir / "dependent.json"
            if dep_file.exists():
                with open(dep_file) as f:
                    dep_data = json.load(f)
                    dep = Dependent(**dep_data)
                    dependents.append(dep)
    return dependents


def load_reports(dep_folder: str) -> List[DailyReportData]:
    """Load all reports for a dependent."""
    if not BACKUP_DIR:
        return []
    processed_dir = BACKUP_DIR / dep_folder / "processed"
    if not processed_dir.exists():
        return []

    reports = []
    for report_file in processed_dir.glob("*.json"):
        with open(report_file) as f:
            report_data = json.load(f)
            report = DailyReportData(**report_data)
            reports.append(report)

    return sorted(reports, key=lambda x: x.date, reverse=True)


@app.route("/")
def index() -> Any:
    profile = load_parent_profile()
    dependents = load_dependents()
    return render_template("index.html", profile=profile, dependents=dependents)


@app.route("/dependent/<dep_folder>")
def dependent_months(dep_folder: str) -> Any:
    reports = load_reports(dep_folder)
    dep_name_parts = dep_folder.replace("_", " ").split(" ")
    dep_name = f"{dep_name_parts[0]} {dep_name_parts[1]}"

    # Group reports by month with random images
    months: Dict[str, Any] = {}
    for report in reports:
        month_key = report.date[:7]  # YYYY-MM
        if month_key not in months:
            months[month_key] = []
        months[month_key].append(report)

    # Add random image and format dates for each month
    months_with_images = {}
    for month, month_reports in months.items():
        from datetime import datetime

        date_obj = datetime.strptime(month, "%Y-%m")
        months_with_images[month] = {
            "reports": month_reports,
            "random_image": get_random_image_from_reports(month_reports, dep_folder),
            "display_name": date_obj.strftime("%B %Y"),
            "year": date_obj.year,
        }

    # Sort by date ascending
    sorted_months = dict(sorted(months_with_images.items()))

    return render_template("months.html", months=sorted_months, dep_name=dep_name, dep_folder=dep_folder)


@app.route("/dependent/<dep_folder>/month/<month>")
def month_reports(dep_folder: str, month: str) -> Any:
    reports = load_reports(dep_folder)
    dep_name_parts = dep_folder.replace("_", " ").split(" ")
    dep_name = f"{dep_name_parts[0]} {dep_name_parts[1]}"

    # Filter reports for the specific month and add random images
    month_reports = [r for r in reports if r.date.startswith(month)]
    # Sort by date ascending
    month_reports.sort(key=lambda x: x.date)

    reports_with_images = []
    for report in month_reports:
        from datetime import datetime

        date_obj = datetime.strptime(report.date, "%Y-%m-%d")
        reports_with_images.append(
            {
                "report": report,
                "random_image": get_random_image_from_reports([report], dep_folder),
                "display_date": date_obj.strftime("%A, %B %d"),
            }
        )

    from datetime import datetime

    month_obj = datetime.strptime(month, "%Y-%m")
    month_display = month_obj.strftime("%B %Y")

    return render_template(
        "month_reports.html",
        reports=reports_with_images,
        dep_name=dep_name,
        dep_folder=dep_folder,
        month=month,
        month_display=month_display,
    )


@app.route("/dependent/<dep_folder>/report/<date>")
def report_detail(dep_folder: str, date: str) -> Any:
    reports = load_reports(dep_folder)
    dep_name_parts = dep_folder.replace("_", " ").split(" ")
    dep_name = f"{dep_name_parts[0]} {dep_name_parts[1]}"

    # Find the specific report
    report = next((r for r in reports if r.date == date), None)
    if not report:
        from flask import abort

        abort(404)

    return render_template(
        "report_detail.html",
        report=report,
        dep_name=dep_name,
        dep_folder=dep_folder,
        is_image=is_image,
        is_video=is_video,
    )


@app.route("/dependent/<dep_folder>/gallery")
def gallery(dep_folder: str) -> Any:
    reports = load_reports(dep_folder)
    dep_name_parts = dep_folder.replace("_", " ").split(" ")
    dep_name = f"{dep_name_parts[0]} {dep_name_parts[1]}"

    # Get cached image set for efficient lookup
    image_cache = get_image_cache(dep_folder)

    # Collect all snapshots with dates and media types
    all_snapshots = []
    for report in reports:
        for note in report.teacher_notes:
            if note.attachment_id:
                all_snapshots.append(
                    {
                        "date": report.date,
                        "attachment_id": note.attachment_id,
                        "note": note.note or "",
                        "type": "teacher_note",
                        "media_type": "image" if note.attachment_id in image_cache else "video",
                    }
                )
        for activity in report.activities:
            for snapshot in activity.snapshots:
                if snapshot.attachment_id:
                    all_snapshots.append(
                        {
                            "date": report.date,
                            "attachment_id": snapshot.attachment_id,
                            "note": snapshot.note or "",
                            "type": "activity_snapshot",
                            "media_type": ("image" if snapshot.attachment_id in image_cache else "video"),
                        }
                    )
        for snapshot in report.snapshots:
            if snapshot.attachment_id:
                all_snapshots.append(
                    {
                        "date": report.date,
                        "attachment_id": snapshot.attachment_id,
                        "note": snapshot.note or "",
                        "type": "snapshot",
                        "media_type": "image" if snapshot.attachment_id in image_cache else "video",
                    }
                )

    # Sort by date ascending
    all_snapshots.sort(key=lambda x: x["date"])

    # Get unique dates for scrollbar
    unique_dates = sorted(list(set(s["date"] for s in all_snapshots)))

    return render_template(
        "gallery.html",
        snapshots=all_snapshots,
        dates=unique_dates,
        dep_name=dep_name,
        dep_folder=dep_folder,
        is_image=is_image,
        is_video=is_video,
    )


@app.route("/media/<dep_folder>/<attachment_id>")
def serve_media(dep_folder: str, attachment_id: str) -> Any:
    if not BACKUP_DIR:
        return "Media not found", 404
    media_dir = BACKUP_DIR / dep_folder / "media"
    filename = next(iter(glob.glob(f"{media_dir}/{attachment_id}*")), None)
    if not filename:
        logging.error(f"Could not find {attachment_id} from {media_dir}")
        return "Media not found", 404
    else:
        return send_from_directory(str(BACKUP_DIR), str(Path(dep_folder) / "media" / Path(filename).name))


def find_latest_backup() -> Optional[Path]:
    """Find the latest backup directory in current directory."""
    current_dir = Path(".")
    backup_dirs = [d for d in current_dir.iterdir() if d.is_dir() and d.name.startswith("output_")]
    if not backup_dirs:
        return None
    return max(backup_dirs, key=lambda x: x.stat().st_mtime)


def is_image(attachment_id: str, dep_folder: str) -> bool:
    """Check if attachment is an image."""
    if not BACKUP_DIR:
        return False
    media_dir = BACKUP_DIR / dep_folder / "media"
    filename = next(iter(glob.glob(f"{media_dir}/{attachment_id}*")), None)
    if not filename:
        return False
    ext = Path(filename).suffix.lower()
    return ext in [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff"]


def is_video(attachment_id: str, dep_folder: str) -> bool:
    """Check if attachment is a video."""
    if not BACKUP_DIR:
        return False
    media_dir = BACKUP_DIR / dep_folder / "media"
    filename = next(iter(glob.glob(f"{media_dir}/{attachment_id}*")), None)
    if not filename:
        return False
    ext = Path(filename).suffix.lower()
    return ext in [".mp4", ".mov", ".avi", ".mkv", ".webm"]


def get_image_cache(dep_folder: str) -> set[str]:
    """Get or create cached image mapping for a dependent."""
    if dep_folder in _image_cache:
        cached_result: set[str] = _image_cache[dep_folder]
        return cached_result

    if not BACKUP_DIR:
        empty_set: set[str] = set()
        _image_cache[dep_folder] = empty_set
        return empty_set

    media_dir = BACKUP_DIR / dep_folder / "media"
    if not media_dir.exists():
        empty_set2: set[str] = set()
        _image_cache[dep_folder] = empty_set2
        return empty_set2

    # Build mapping of attachment_id -> is_image
    image_patterns = ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.webp", "*.bmp", "*.tiff"]
    image_set: set[str] = set()
    for pattern in image_patterns:
        for img_file in media_dir.glob(pattern):
            image_set.add(img_file.stem)

    _image_cache[dep_folder] = image_set
    return image_set


def get_random_image_from_reports(reports: List[DailyReportData], dep_folder: str) -> Optional[str]:
    """Get a random image from given reports using cache."""
    image_cache = get_image_cache(dep_folder)

    # Get attachment IDs from reports that are images
    images = []
    for report in reports:
        for note in report.teacher_notes:
            if note.attachment_id and note.attachment_id in image_cache:
                images.append(note.attachment_id)
        for activity in report.activities:
            for snapshot in activity.snapshots:
                if snapshot.attachment_id and snapshot.attachment_id in image_cache:
                    images.append(snapshot.attachment_id)
        for snapshot in report.snapshots:
            if snapshot.attachment_id and snapshot.attachment_id in image_cache:
                images.append(snapshot.attachment_id)

    return random.choice(images) if images else None  # nosec B311


def main() -> None:
    global BACKUP_DIR
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) == 2:
        BACKUP_DIR = Path(sys.argv[1])
    else:
        BACKUP_DIR = find_latest_backup()
        if not BACKUP_DIR:
            logging.error("No backup directory found. Usage: python viewer.py [backup_directory]")
            sys.exit(1)
        logging.info(f"Auto-detected backup directory: {BACKUP_DIR}")

    if not BACKUP_DIR.exists():
        logging.error(f"Backup directory {BACKUP_DIR} does not exist")
        sys.exit(1)

    logging.info(f"Starting viewer for backup directory: {BACKUP_DIR}")
    logging.info("Open http://localhost:5000 in your browser")
    app.run(host="0.0.0.0", port=5000)  # nosec B104


if __name__ == "__main__":
    main()
