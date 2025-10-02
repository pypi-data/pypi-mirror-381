import asyncio
import json
import logging
import mimetypes
from datetime import timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import httpx
from dotenv import find_dotenv, load_dotenv
from playwright.async_api import Browser, BrowserContext, Page, Playwright, async_playwright

from .api_client import fetch_dependents, fetch_parent_profile
from .auth import perform_fresh_login
from .browser_utils import (
    execute_step,
    maybe_accept_cookies,
    navigate_to_bright_day,
    setup_page_logging,
    wait_bright_day,
    wait_signed_in,
)
from .constants import BRIGHT_DAY_HOME, FIC_LOGIN, HEADLESS, STATE_FILE
from .models import Activity, DailyReportData, Dependent, ParentProfile, Snapshot, TeacherNote
from .utils import env, ts


class BrightHorizonsClient:
    """Client for Bright Horizons authentication and data scraping."""

    def __init__(
        self, email: Optional[str] = None, password: Optional[str] = None, output_dir: Optional[str] = None
    ) -> None:
        load_dotenv(find_dotenv(usecwd=True))
        self.email = email or env("BH_EMAIL")
        self.password = password or env("BH_PASSWORD")
        if not self.email or not self.password:
            raise ValueError("Set BH_EMAIL and BH_PASSWORD in .env or pass as parameters")

        if output_dir is None:
            output_dir = f"output_{ts()}"
        self.output_dir = Path(output_dir)
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None
        self.artifacts_dir: Optional[Path] = None
        self.authenticated = False
        self.playwright: Optional[Playwright] = None

    async def __aenter__(self) -> "BrightHorizonsClient":
        await self._setup_browser()
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        await self._cleanup()

    async def _setup_browser(self) -> None:
        """Initialize browser and context."""
        run_id = ts()
        self.artifacts_dir = Path(f"run_{run_id}")
        self.artifacts_dir.mkdir(exist_ok=True)

        p = async_playwright()
        self.playwright = await p.start()
        self.browser = await self.playwright.chromium.launch(
            headless=HEADLESS,
            args=["--disable-blink-features=AutomationControlled"],
            slow_mo=50 if not HEADLESS else 0,
        )

    async def _cleanup(self) -> None:
        """Clean up browser resources."""
        if self.context:
            try:
                if self.artifacts_dir:
                    await self.context.tracing.stop(path=str(self.artifacts_dir / "trace.zip"))
            except Exception as e:
                logging.error(f"Failed to stop tracing: {e}")
                pass
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

    async def authenticate(self) -> bool:
        """Authenticate with Bright Horizons."""
        # Try existing session first
        if await self._try_existing_session():
            self.authenticated = True
            return True

        # Fresh login required
        await self._create_new_context()
        if self.page and self.artifacts_dir and self.email and self.password:
            await self._perform_fresh_login()

        if self.page and await wait_signed_in(self.page):
            logging.info("Sign-in to bright horizon successful.")
            if self.artifacts_dir:
                await navigate_to_bright_day(self.page, self.artifacts_dir)
            if self.context:
                await self.context.storage_state(path=STATE_FILE)
            self.authenticated = True
            return True

        logging.error("Login failed - could not verify sign-in")
        self.authenticated = False
        return False

    async def _try_existing_session(self) -> bool:
        """Try to reuse existing session state."""
        if not STATE_FILE.exists():
            return False

        try:
            state = json.loads(STATE_FILE.read_text())
            if self.browser and self.artifacts_dir:
                self.context = await self.browser.new_context(
                    storage_state=state,
                    record_video_dir=str(self.artifacts_dir / "video"),
                    record_video_size={"width": 1280, "height": 800},
                )
            if self.context:
                await self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
                self.page = await self.context.new_page()
            if self.page:
                await setup_page_logging(self.page)

            # Test Bright Day access
            if self.page and self.artifacts_dir:
                await execute_step(
                    self.page,
                    self.artifacts_dir,
                    "open_bright_day",
                    self.page.goto(BRIGHT_DAY_HOME, wait_until="domcontentloaded"),
                )
            if self.page and await wait_bright_day(self.page):
                logging.info("Already signed into bright day. ✅")
                if self.context:
                    await self.context.storage_state(path=STATE_FILE)
                return True

            # Test Family Info Center access
            if self.page and self.artifacts_dir:
                await execute_step(
                    self.page,
                    self.artifacts_dir,
                    "goto_fic",
                    self.page.goto(FIC_LOGIN, wait_until="domcontentloaded"),
                )
            if self.page:
                await maybe_accept_cookies(self.page)
            if self.page and await wait_signed_in(self.page):
                logging.info("Already signed into bright horizon. ✅")
                if self.artifacts_dir:
                    await navigate_to_bright_day(self.page, self.artifacts_dir)
                if self.context:
                    await self.context.storage_state(path=STATE_FILE)
                return True

        except Exception as e:
            logging.error(f"Session reuse failed: {e}")

        return False

    async def _create_new_context(self) -> None:
        """Create new browser context for fresh login."""
        if self.context:
            await self.context.close()

        if self.browser and self.artifacts_dir:
            self.context = await self.browser.new_context(
                record_video_dir=str(self.artifacts_dir / "video"),
                record_video_size={"width": 1280, "height": 800},
            )
        if self.context:
            await self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
            self.page = await self.context.new_page()
        if self.page:
            await setup_page_logging(self.page)

    async def _perform_fresh_login(self) -> None:
        """Perform fresh login process."""
        logging.info("Session invalid; logging in fresh…")
        if self.page and self.artifacts_dir and self.email and self.password:
            await perform_fresh_login(self.page, self.artifacts_dir, self.email, self.password)

    async def scrape_data(self, max_retries: int = 2) -> Tuple[Optional[ParentProfile], List[Dependent]]:
        """Scrape profile and dependents data with retry logic."""
        for attempt in range(max_retries + 1):
            try:
                if not self.authenticated:
                    if not await self.authenticate():
                        return None, []

                if not self.context:
                    return None, []

                profile = await fetch_parent_profile(self.context, self.output_dir)
                if not profile:
                    raise Exception("Failed to fetch parent profile")

                dependents = await fetch_dependents(self.context, profile.id, self.output_dir)
                return profile, dependents

            except Exception as e:
                logging.error(f"Scraping attempt {attempt + 1} failed: {e}")

                if attempt < max_retries:
                    logging.info(f"Retrying after re-authentication... (attempt {attempt + 2}/{max_retries + 1})")
                    self.authenticated = False
                    await self._create_new_context()
                else:
                    logging.error("All scraping attempts failed")
                    return None, []

        return None, []

    async def fetch_daily_reports_batch(
        self, dependent_id: str, start_date: str, end_date: str, dep_dir: Path
    ) -> List[Dict[str, Any]]:
        """Fetch daily reports for a date range."""
        # Check if data exists on disk first
        batch_file = dep_dir / "raw" / f"batch_{start_date}_{end_date}.json"
        if batch_file.exists():
            logging.info(f"Loading batch from disk: {start_date} to {end_date}")
            cached_data: List[Dict[str, Any]] = json.loads(batch_file.read_text())
            return cached_data

        if not self.context:
            return []

        try:
            cookies = await self.context.cookies()
            cookie_dict = {cookie["name"]: cookie["value"] for cookie in cookies}

            url = f"https://mybrightday.brighthorizons.com/api/v2/dependent/{dependent_id}/daily_reports"
            params = {"start": start_date, "end": end_date}

            async with httpx.AsyncClient() as client:
                response = await client.get(url, cookies=cookie_dict, params=params)
                response.raise_for_status()
                data: List[Dict[str, Any]] = response.json()

                # Save batch to disk
                batch_file.parent.mkdir(parents=True, exist_ok=True)
                batch_file.write_text(json.dumps(data, indent=2))
                return data

        except Exception as e:
            logging.error(f"Failed to fetch daily reports for {dependent_id} ({start_date} to {end_date}): {e}")
            return []

    async def fetch_all_daily_reports(
        self, dependent: Dependent, batch_days: int = 30, max_concurrent: int = 5
    ) -> Dict[str, Tuple[DailyReportData, Dict[str, Any]]]:
        """Fetch all daily reports for a dependent in parallel batches."""
        start_date = dependent.enrollment_date.date()
        end_date = dependent.graduation_date.date()

        # Create dependent directory
        dep_dir = self.output_dir / dependent.folder
        dep_dir.mkdir(parents=True, exist_ok=True)

        # Create date ranges for batching
        date_ranges = []
        current_date = start_date
        while current_date <= end_date:
            batch_end = min(current_date + timedelta(days=batch_days - 1), end_date)
            date_ranges.append((current_date.isoformat(), batch_end.isoformat()))
            current_date = batch_end + timedelta(days=1)

        logging.info(f"Fetching reports for {dependent.first_name} {dependent.last_name} in {len(date_ranges)} batches")

        # Create semaphore to limit concurrent requests
        semaphore = asyncio.Semaphore(max_concurrent)

        async def fetch_batch(start_str: str, end_str: str) -> List[Dict[str, Any]]:
            async with semaphore:
                return await self.fetch_daily_reports_batch(dependent.id, start_str, end_str, dep_dir)

        # Fetch all batches in parallel
        tasks = [fetch_batch(start_str, end_str) for start_str, end_str in date_ranges]
        batch_results = await asyncio.gather(*tasks)

        # Merge and deduplicate reports
        all_reports = []
        for batch in batch_results:
            all_reports.extend(batch)

        # Deduplicate by date (keep latest version)
        reports_by_date: Dict[str, Dict[str, Any]] = {}
        for report in all_reports:
            date = report["for_date"]
            if date not in reports_by_date or report["updated"] > reports_by_date[date]["updated"]:
                reports_by_date[date] = report

        # Sort by date
        sorted_reports = dict(sorted(reports_by_date.items()))

        # Process into structured data
        processed_reports: Dict[str, Tuple[DailyReportData, Dict[str, Any]]] = {}
        for date, report in sorted_reports.items():
            processed_reports[date] = (self._process_daily_report(report), report)

        logging.info(f"Processed {len(processed_reports)} unique daily reports for {dependent.first_name}")
        return processed_reports

    def _process_daily_report(self, raw_report: Dict[str, Any]) -> DailyReportData:
        """Process raw daily report into structured data."""
        # Extract teacher notes
        teacher_notes = []
        for note_entry in raw_report.get("note_entries", []):
            if note_entry.get("note") and not note_entry.get("is_from_parent", True):
                teacher_notes.append(
                    TeacherNote(
                        id=note_entry["id"],
                        note=note_entry["note"],
                        actor=note_entry.get("actor"),
                        attachment_id=note_entry.get("attachment_id"),
                        capture_time=note_entry["capture_time"],
                        is_from_parent=note_entry.get("is_from_parent", False),
                    )
                )

        # Extract activities with snapshots
        activities = []
        for activity_entry in raw_report.get("activity_entries", []):
            snapshots = []
            for snapshot_data in activity_entry.get("snapshots", []):
                snapshots.append(
                    Snapshot(
                        id=snapshot_data["id"],
                        note=snapshot_data.get("note"),
                        attachment_id=snapshot_data.get("attachment_id"),
                        created_by=snapshot_data.get("created_by"),
                        capture_time=snapshot_data["capture_time"],
                    )
                )

            activities.append(
                Activity(
                    id=activity_entry["id"],
                    description=activity_entry.get("description", ""),
                    subject_names=activity_entry.get("subject_names", []),
                    snapshots=snapshots,
                    entry_time=activity_entry.get("entry_time"),
                )
            )

        # Extract standalone snapshots
        standalone_snapshots = []
        for snapshot_entry in raw_report.get("snapshot_entries", []):
            standalone_snapshots.append(
                Snapshot(
                    id=snapshot_entry["id"],
                    note=snapshot_entry.get("note"),
                    attachment_id=snapshot_entry.get("attachment_id"),
                    created_by=snapshot_entry.get("created_by"),
                    capture_time=snapshot_entry["capture_time"],
                )
            )

        return DailyReportData(
            date=raw_report["for_date"],
            dependent_id=raw_report["dependent_id"],
            teacher_notes=teacher_notes,
            activities=activities,
            snapshots=standalone_snapshots,
        )

    async def _download_attachment(
        self,
        attachment_id: str,
        media_dir: Path,
        semaphore: asyncio.Semaphore,
        max_retries: int = 3,
    ) -> Optional[str]:
        """Download attachment and return filename."""
        if not attachment_id:
            return None

        filename = media_dir / attachment_id
        if any(
            filename.with_suffix(ext).exists()
            for ext in [
                ".jpg",
                ".jpeg",
                ".png",
                ".gif",
                ".mp4",
                ".mov",
                ".webp",
                ".bmp",
                ".tiff",
                ".avi",
                ".mkv",
                ".webm",
            ]
        ):
            return next(f.name for f in media_dir.glob(f"{attachment_id}.*"))

        if not self.context:
            return None

        async with semaphore:
            for attempt in range(max_retries):
                try:
                    cookies = await self.context.cookies()
                    cookie_dict = {cookie["name"]: cookie["value"] for cookie in cookies}

                    url = (
                        f"https://mybrightday.brighthorizons.com/remote/v1/obj_attachment?"
                        f"obj={attachment_id}&key={attachment_id}"
                    )

                    async with httpx.AsyncClient() as client:
                        response = await client.get(url, cookies=cookie_dict)
                        response.raise_for_status()

                        content_type = response.headers.get("content-type", "").split(";")[0]
                        ext = mimetypes.guess_extension(content_type) or ".bin"

                        file_path = filename.with_suffix(ext)
                        file_path.write_bytes(response.content)
                        return file_path.name

                except Exception as e:
                    if attempt == max_retries - 1:
                        logging.error(
                            f"Failed to download attachment {attachment_id} " f"after {max_retries} attempts: {e}"
                        )
                        return None
                    await asyncio.sleep(2**attempt)  # Exponential backoff
        return None

    async def save_reports_to_files(
        self, dependent: Dependent, reports: Dict[str, Tuple[DailyReportData, Dict[str, Any]]]
    ) -> None:
        """Save reports to organized file structure."""
        # Use existing dependent directory
        reports_dir = self.output_dir / dependent.folder

        # Save raw data files
        raw_dir = reports_dir / "raw"
        raw_dir.mkdir(exist_ok=True)

        # Save processed data files
        processed_dir = reports_dir / "processed"
        processed_dir.mkdir(exist_ok=True)

        # Create media directory
        media_dir = reports_dir / "media"
        media_dir.mkdir(exist_ok=True)

        # Collect all attachment IDs
        attachment_ids = set()
        for _, (report_data, _) in reports.items():
            for note in report_data.teacher_notes:
                if note.attachment_id:
                    attachment_ids.add(note.attachment_id)
            for activity in report_data.activities:
                for snapshot in activity.snapshots:
                    if snapshot.attachment_id:
                        attachment_ids.add(snapshot.attachment_id)
            for snapshot in report_data.snapshots:
                if snapshot.attachment_id:
                    attachment_ids.add(snapshot.attachment_id)

        # Download attachments
        if attachment_ids:
            logging.info(f"Downloading {len(attachment_ids)} attachments...")
            semaphore = asyncio.Semaphore(5)  # Limit to 5 concurrent downloads
            tasks = [self._download_attachment(aid, media_dir, semaphore) for aid in attachment_ids]
            await asyncio.gather(*tasks, return_exceptions=True)

        for date, (report_data, raw_data) in reports.items():
            # Save raw data
            raw_file = raw_dir / f"{date}.json"
            raw_file.write_text(json.dumps(raw_data, indent=2))

            # Save processed data
            processed_file = processed_dir / f"{date}.json"
            processed_data = {
                "date": report_data.date,
                "dependent_id": report_data.dependent_id,
                "teacher_notes": [note.model_dump(mode="json") for note in report_data.teacher_notes],
                "activities": [activity.model_dump(mode="json") for activity in report_data.activities],
                "snapshots": [snapshot.model_dump(mode="json") for snapshot in report_data.snapshots],
            }
            processed_file.write_text(json.dumps(processed_data, indent=2))

        logging.info(f"Saved {len(reports)} reports to {reports_dir}")

    async def fetch_all_dependents_reports(
        self, dependents: List[Dependent], batch_days: int = 30, max_concurrent: int = 3
    ) -> None:
        """Fetch and save daily reports for all dependents."""
        for dependent in dependents:
            logging.info(f"\nProcessing reports for {dependent.first_name} {dependent.last_name}...")
            reports = await self.fetch_all_daily_reports(dependent, batch_days, max_concurrent)
            await self.save_reports_to_files(dependent, reports)


async def login() -> Tuple[Optional[ParentProfile], List[Dependent]]:
    """Legacy function for backward compatibility."""
    async with BrightHorizonsClient() as client:
        return await client.scrape_data()
