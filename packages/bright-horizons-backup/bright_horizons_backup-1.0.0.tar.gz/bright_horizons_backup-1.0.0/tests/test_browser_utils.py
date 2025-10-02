"""Tests for browser_utils module."""

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest

from bright_horizons_backup.browser_utils import (
    click_first,
    execute_step,
    fill_first,
    is_okta_page,
    take_screenshot,
    wait_signed_in,
)


@pytest.fixture
def mock_page():
    page = MagicMock()
    page.url = "https://example.com"
    page.locator.return_value.first = MagicMock()
    page.locator.return_value.first.wait_for = AsyncMock()
    page.locator.return_value.first.click = AsyncMock()
    page.locator.return_value.first.fill = AsyncMock()
    page.locator.return_value.first.type = AsyncMock()
    page.wait_for_timeout = AsyncMock()
    page.screenshot = AsyncMock()
    return page


class TestClickFirst:
    @pytest.mark.asyncio
    async def test_click_first_success(self, mock_page):
        result = await click_first(mock_page, ["button"])
        assert result is True
        mock_page.locator.return_value.first.click.assert_called_once()

    @pytest.mark.asyncio
    async def test_click_first_timeout(self, mock_page):
        from playwright.async_api import TimeoutError as PWTimeout

        mock_page.locator.return_value.first.wait_for.side_effect = PWTimeout("timeout")
        result = await click_first(mock_page, ["button"])
        assert result is False


class TestFillFirst:
    @pytest.mark.asyncio
    async def test_fill_first_success(self, mock_page):
        result = await fill_first(mock_page, ["input"], "test")
        assert result is True
        mock_page.locator.return_value.first.fill.assert_called_once_with("")
        mock_page.locator.return_value.first.type.assert_called_once_with("test", delay=12)

    @pytest.mark.asyncio
    async def test_fill_first_timeout(self, mock_page):
        from playwright.async_api import TimeoutError as PWTimeout

        mock_page.locator.return_value.first.wait_for.side_effect = PWTimeout("timeout")
        result = await fill_first(mock_page, ["input"], "test")
        assert result is False


class TestIsOktaPage:
    @pytest.mark.asyncio
    async def test_is_okta_page_true(self, mock_page):
        mock_page.url = "https://bhloginsso.brighthorizons.com/login"
        result = await is_okta_page(mock_page)
        assert result is True

    @pytest.mark.asyncio
    async def test_is_okta_page_false(self, mock_page):
        mock_page.url = "https://example.com"
        result = await is_okta_page(mock_page)
        assert result is False


class TestWaitSignedIn:
    @pytest.mark.asyncio
    async def test_wait_signed_in_success(self, mock_page):
        result = await wait_signed_in(mock_page)
        assert result is True

    @pytest.mark.asyncio
    async def test_wait_signed_in_timeout(self, mock_page):
        from playwright.async_api import TimeoutError as PWTimeout

        mock_page.locator.return_value.first.wait_for.side_effect = PWTimeout("timeout")
        result = await wait_signed_in(mock_page)
        assert result is False


class TestTakeScreenshot:
    @pytest.mark.asyncio
    async def test_take_screenshot_success(self, mock_page):
        artifacts_dir = Path("/tmp/test")
        await take_screenshot(mock_page, artifacts_dir, "test")
        mock_page.screenshot.assert_called_once()

    @pytest.mark.asyncio
    async def test_take_screenshot_error(self, mock_page):
        mock_page.screenshot.side_effect = Exception("Screenshot failed")
        artifacts_dir = Path("/tmp/test")
        # Should not raise exception
        await take_screenshot(mock_page, artifacts_dir, "test")


class TestExecuteStep:
    @pytest.mark.asyncio
    async def test_execute_step_with_coroutine(self, mock_page):
        artifacts_dir = Path("/tmp/test")
        coro = AsyncMock()
        await execute_step(mock_page, artifacts_dir, "test_step", coro)
        # The coroutine is awaited, so we just check it was used
        mock_page.wait_for_timeout.assert_called_once_with(300)

    @pytest.mark.asyncio
    async def test_execute_step_without_coroutine(self, mock_page):
        artifacts_dir = Path("/tmp/test")
        await execute_step(mock_page, artifacts_dir, "test_step")
        mock_page.wait_for_timeout.assert_called_once_with(300)
