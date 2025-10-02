import logging
from pathlib import Path
from typing import Awaitable, List, Optional

from playwright.async_api import Page
from playwright.async_api import TimeoutError as PWTimeout

from .constants import COOKIE_ACCEPT_SEL


async def click_first(page: Page, selectors: List[str], timeout: int = 6000) -> bool:
    """Click the first visible element matching any of the selectors."""
    for s in selectors:
        try:
            await page.locator(s).first.wait_for(state="visible", timeout=timeout)
            await page.locator(s).first.click()
            logging.info(f'Found "{s}"')
            return True
        except PWTimeout:
            continue
        except Exception as e:
            logging.debug(f"Error clicking selector {s}: {e}")
            continue
    return False


async def fill_first(page: Page, selectors: List[str], text: str, timeout: int = 8000) -> bool:
    """Fill the first visible input element matching any of the selectors."""
    for s in selectors:
        try:
            loc = page.locator(s).first
            await loc.wait_for(state="visible", timeout=timeout)
            await loc.fill("")
            await loc.type(text, delay=12)
            logging.info(f'Found "{s}"')
            return True
        except PWTimeout:
            continue
        except Exception as e:
            logging.debug(f"Error filling selector {s}: {e}")
            continue
    return False


async def maybe_accept_cookies(page: Page) -> None:
    """Accept cookies if the cookie banner is present."""
    try:
        await click_first(page, COOKIE_ACCEPT_SEL, timeout=1000)
    except Exception as e:
        logging.debug(f"No cookie banner found or error accepting cookies: {e}")


async def is_okta_page(page: Page) -> bool:
    """Check if the current page is an Okta login page."""
    return "bhloginsso.brighthorizons.com" in page.url.lower()


async def wait_signed_in(page: Page) -> bool:
    """Wait for signed-in indicators in Family Info Center."""
    candidates = [".myChildren"]
    for s in candidates:
        try:
            await page.locator(s).first.wait_for(timeout=2500)
            logging.info(f'Found "{s}"')
            return True
        except PWTimeout:
            continue
        except Exception as e:
            logging.debug(f"Error waiting for sign-in indicator {s}: {e}")
            continue
    return False


async def wait_bright_day(page: Page) -> bool:
    """Wait for Bright Day page indicators."""
    candidates = ['h2:has-text("timeline")']
    for s in candidates:
        try:
            await page.locator(s).first.wait_for(timeout=2500)
            logging.info(f'Found "{s}"')
            return True
        except PWTimeout:
            continue
        except Exception as e:
            logging.debug(f"Error waiting for Bright Day indicator {s}: {e}")
            continue
    return False


async def setup_page_logging(page: Page) -> None:
    """Set up page event logging."""
    page.on("console", lambda msg: logging.debug(f"[console] {msg}"))
    page.on("pageerror", lambda err: logging.error(f"[pageerror] {err}"))
    page.on("requestfailed", lambda req: logging.warning(f"[requestfailed] {req.url} — {req.failure}"))


async def take_screenshot(page: Page, artifacts_dir: Path, name: str) -> None:
    """Take a screenshot with error handling."""
    path = artifacts_dir / f"{name}.png"
    try:
        await page.screenshot(path=str(path), full_page=True)
        logging.info(f"[snap] {path}")
    except Exception as e:
        logging.error(f"Screenshot error: {e}")


async def execute_step(page: Page, artifacts_dir: Path, name: str, coro: Optional[Awaitable] = None) -> None:
    """Execute a step with logging and screenshot."""
    logging.info(f"\n=== STEP: {name} ===")
    logging.info(f"URL before: {page.url}")
    if coro:
        try:
            await coro
        except Exception as e:
            logging.error(f"Step error [{name}]: {e}")
    await page.wait_for_timeout(300)
    logging.info(f"URL after: {page.url}")
    await take_screenshot(page, artifacts_dir, name.replace(" ", "_"))


async def navigate_to_bright_day(page: Page, artifacts_dir: Path) -> None:
    """Navigate from Family Info Center to Bright Day."""
    await execute_step(
        page,
        artifacts_dir,
        "child_card_drop_down",
        click_first(
            page,
            ["app-child:first-of-type div section div div.childCard div.actions-button-menu a"],
        ),
    )
    await execute_step(
        page,
        artifacts_dir,
        "my_bright_day",
        click_first(page, ["#mat-menu-panel-2 div button:nth-child(2) span span"]),
    )
    if await wait_bright_day(page):
        logging.info("Successfully signed into brightday.")
