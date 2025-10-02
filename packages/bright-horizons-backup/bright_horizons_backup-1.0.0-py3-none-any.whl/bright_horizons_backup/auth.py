import logging
from pathlib import Path

from playwright.async_api import Page

from .browser_utils import click_first, execute_step, fill_first, is_okta_page, maybe_accept_cookies
from .constants import FIC_LOGIN, LOGIN_SELECTOR, OKTA_PASSWORD_SEL, OKTA_USERNAME_SEL


async def perform_fresh_login(page: Page, artifacts_dir: Path, email: str, password: str) -> None:
    """Perform fresh login process."""
    logging.info("Session invalid; logging in fresh…")

    await execute_step(page, artifacts_dir, "goto_fic", page.goto(FIC_LOGIN, wait_until="domcontentloaded"))
    await execute_step(page, artifacts_dir, "accept_cookies", maybe_accept_cookies(page))

    try:
        await page.wait_for_load_state("networkidle", timeout=15000)
    except Exception as e:
        logging.debug(f"Network idle timeout: {e}")

    # Trigger Okta redirect if needed
    if not await is_okta_page(page):
        await execute_step(page, artifacts_dir, "click_login_button", click_first(page, LOGIN_SELECTOR))
        try:
            await page.wait_for_load_state("networkidle", timeout=10000)
        except Exception as e:
            logging.debug(f"Network idle timeout after login click: {e}")

    # Okta authentication
    if await is_okta_page(page):
        await execute_step(page, artifacts_dir, "okta_fill_username", fill_first(page, OKTA_USERNAME_SEL, email))
        await execute_step(page, artifacts_dir, "okta_submit_username", click_first(page, ["._button-login-id"]))
        await execute_step(page, artifacts_dir, "okta_fill_password", fill_first(page, OKTA_PASSWORD_SEL, password))
        await execute_step(
            page,
            artifacts_dir,
            "okta_submit_password",
            click_first(page, ["button[type='submit']"]),
        )
