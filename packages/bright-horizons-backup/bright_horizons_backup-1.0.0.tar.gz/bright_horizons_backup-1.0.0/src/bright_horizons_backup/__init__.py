"""
Bright Horizons Backup Client

A Python client for backing up daily reports, photos, and activities from Bright Horizons daycare centers.
"""

import logging

from .client import BrightHorizonsClient
from .models import Activity, DailyReportData, Dependent, ParentProfile, Snapshot, TeacherNote

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

__all__ = [
    "BrightHorizonsClient",
    "ParentProfile",
    "Dependent",
    "DailyReportData",
    "TeacherNote",
    "Activity",
    "Snapshot",
]
