"""Tests for cli module."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bright_horizons_backup.cli import main, parse_args, run_backup


class TestParseArgs:
    def test_parse_args_defaults(self):
        with patch("sys.argv", ["bright-horizons-backup"]):
            args = parse_args()
            assert args.batch_days == 30
            assert args.max_concurrent == 16
            assert args.verbose is False

    def test_parse_args_with_options(self):
        with patch(
            "sys.argv",
            [
                "bright-horizons-backup",
                "--output-dir",
                "/tmp/backup",
                "--email",
                "test@example.com",
                "--password",
                "password",
                "--batch-days",
                "60",
                "--max-concurrent",
                "10",
                "--verbose",
            ],
        ):
            args = parse_args()
            assert args.output_dir == "/tmp/backup"
            assert args.email == "test@example.com"
            assert args.password == "password"
            assert args.batch_days == 60
            assert args.max_concurrent == 10
            assert args.verbose is True


class TestRunBackup:
    @pytest.mark.asyncio
    async def test_run_backup_success(self):
        args = MagicMock()
        args.email = "test@example.com"
        args.password = "password"
        args.output_dir = None
        args.batch_days = 30
        args.max_concurrent = 5

        mock_profile = MagicMock()
        mock_profile.first_name = "John"
        mock_profile.last_name = "Doe"

        mock_dependent = MagicMock()
        mock_dependent.first_name = "Jane"
        mock_dependent.last_name = "Doe"
        mock_dependent.stage = "toddler"

        with patch("bright_horizons_backup.cli.BrightHorizonsClient") as mock_client_class:
            mock_client = MagicMock()
            mock_client.scrape_data = AsyncMock(return_value=(mock_profile, [mock_dependent]))
            mock_client.fetch_all_daily_reports = AsyncMock(return_value=[])
            mock_client.output_dir = "/tmp/test"
            mock_client_class.return_value.__aenter__.return_value = mock_client

            result = await run_backup(args)
            assert result is True

    @pytest.mark.asyncio
    async def test_run_backup_no_profile(self):
        args = MagicMock()
        args.email = "test@example.com"
        args.password = "password"
        args.output_dir = None

        with patch("bright_horizons_backup.cli.BrightHorizonsClient") as mock_client_class:
            mock_client = MagicMock()
            mock_client.scrape_data = AsyncMock(return_value=(None, []))
            mock_client_class.return_value.__aenter__.return_value = mock_client

            result = await run_backup(args)
            assert result is False

    @pytest.mark.asyncio
    async def test_run_backup_value_error(self):
        args = MagicMock()
        args.email = None
        args.password = None
        args.output_dir = None

        with patch("bright_horizons_backup.cli.BrightHorizonsClient") as mock_client_class:
            mock_client_class.side_effect = ValueError("Missing credentials")

            result = await run_backup(args)
            assert result is False


class TestMain:
    def test_main_success(self):
        with patch("bright_horizons_backup.cli.parse_args") as mock_parse:
            with patch("bright_horizons_backup.cli.asyncio.run") as mock_run:
                with patch("sys.exit") as mock_exit:
                    mock_parse.return_value = MagicMock(verbose=False)
                    mock_run.return_value = True

                    main()

                    mock_exit.assert_called_once_with(0)

    def test_main_failure(self):
        with patch("bright_horizons_backup.cli.parse_args") as mock_parse:
            with patch("bright_horizons_backup.cli.asyncio.run") as mock_run:
                with patch("sys.exit") as mock_exit:
                    mock_parse.return_value = MagicMock(verbose=False)
                    mock_run.return_value = False

                    main()

                    mock_exit.assert_called_once_with(1)
