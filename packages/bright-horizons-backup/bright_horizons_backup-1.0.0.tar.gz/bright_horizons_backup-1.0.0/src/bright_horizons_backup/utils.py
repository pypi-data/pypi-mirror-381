import os
from datetime import datetime, timezone
from typing import Optional


def env(name: str) -> Optional[str]:
    """Get environment variable with optional stripping."""
    v = os.getenv(name)
    if v is None:
        return None
    stripped = v.strip()
    return stripped if stripped else None


def ts() -> str:
    """Generate timestamp string with timezone awareness."""
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
