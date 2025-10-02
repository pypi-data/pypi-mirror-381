import json
import logging
from pathlib import Path
from typing import List, Optional

import httpx
from playwright.async_api import BrowserContext

from .constants import PROFILE_API_URL
from .models import Dependent, ParentProfile


async def fetch_parent_profile(context: BrowserContext, output_dir: Path) -> Optional[ParentProfile]:
    """Fetch parent profile using httpx with playwright cookies."""
    try:
        cookies = await context.cookies()
        cookie_dict = {cookie["name"]: cookie["value"] for cookie in cookies}

        async with httpx.AsyncClient() as client:
            response = await client.get(PROFILE_API_URL, cookies=cookie_dict)
            response.raise_for_status()

            raw_data = response.json()

            output_dir.mkdir(parents=True, exist_ok=True)
            profile_file = output_dir / "parent_profile.json"
            profile_file.write_text(json.dumps(raw_data, indent=2))
            logging.info(f"Profile data saved to {profile_file}")

            profile = ParentProfile(
                id=raw_data["id"],
                first_name=raw_data["first_name"],
                last_name=raw_data["last_name"],
                email=raw_data["email"],
                brightstar_id=raw_data["brightstar_id"],
                employer=raw_data.get("employer", ""),
                mobile_phone=raw_data.get("phone_numbers", {}).get("mobile"),
                raw_data=raw_data,
            )

            logging.info(f"Profile: {profile.first_name} {profile.last_name} ({profile.email})")
            logging.info(f"User ID: {profile.id}, Brightstar ID: {profile.brightstar_id}")

            return profile

    except Exception as e:
        logging.error(f"Failed to fetch parent profile: {e}")
        return None


async def fetch_dependents(context: BrowserContext, parent_id: str, output_dir: Path) -> List[Dependent]:
    """Fetch dependents using httpx with playwright cookies."""
    try:
        cookies = await context.cookies()
        cookie_dict = {cookie["name"]: cookie["value"] for cookie in cookies}

        url = f"https://mybrightday.brighthorizons.com/api/v2/dependents/guardian/{parent_id}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, cookies=cookie_dict)
            response.raise_for_status()

            raw_data = response.json()

            output_dir.mkdir(parents=True, exist_ok=True)
            dependents_file = output_dir / "dependents.json"
            dependents_file.write_text(json.dumps(raw_data, indent=2))
            logging.info(f"Dependents data saved to {dependents_file}")

            dependents = []
            for dep_data in raw_data:
                # Save individual dependent raw data
                dependent = Dependent(
                    id=dep_data["id"],
                    first_name=dep_data["first_name"],
                    last_name=dep_data["last_name"],
                    stage=dep_data["stage"],
                    status=dep_data["status"],
                    birth_date=dep_data["birth_date"],
                    enrollment_date=dep_data["enrollment_date"],
                    graduation_date=dep_data["graduation_date"],
                    homeroom_id=dep_data["homeroom_id"],
                    center=dep_data["center"],
                    raw_data=dep_data,
                )

                dep_dir = output_dir / dependent.folder
                dep_dir.mkdir(parents=True, exist_ok=True)
                dep_file = dep_dir / "dependent.json"
                dep_file.write_text(json.dumps(dep_data, indent=2))
                dependents.append(dependent)
                logging.info(f"Dependent: {dependent.first_name} {dependent.last_name} (Stage: {dependent.stage})")

            return dependents

    except Exception as e:
        logging.error(f"Failed to fetch dependents: {e}")
        return []
