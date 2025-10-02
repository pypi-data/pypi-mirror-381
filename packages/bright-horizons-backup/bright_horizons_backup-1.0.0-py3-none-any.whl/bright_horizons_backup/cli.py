import argparse
import asyncio
import logging
import sys

from .client import BrightHorizonsClient


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Backup daily reports and media from Bright Horizons")
    parser.add_argument(
        "--output-dir",
        type=str,
        help="Output directory for backup files (default: output_TIMESTAMP)",
    )
    parser.add_argument("--email", type=str, help="Bright Horizons email (overrides BH_EMAIL env var)")
    parser.add_argument("--password", type=str, help="Bright Horizons password (overrides BH_PASSWORD env var)")
    parser.add_argument(
        "--batch-days",
        type=int,
        default=30,
        help="Number of days per batch for fetching reports (default: 30)",
    )
    parser.add_argument("--max-concurrent", type=int, default=16, help="Maximum concurrent requests (default: 16)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
    return parser.parse_args()


async def run_backup(args: argparse.Namespace) -> bool:
    """Run the backup process."""
    try:
        async with BrightHorizonsClient(email=args.email, password=args.password, output_dir=args.output_dir) as client:
            # Authenticate and fetch profile data
            profile, dependents = await client.scrape_data()

            if not profile:
                logging.error("Failed to authenticate or fetch profile data")
                return False

            logging.info(f"Login successful! User: {profile.first_name} {profile.last_name}")
            logging.info(f"Found {len(dependents)} dependent(s)")

            for dep in dependents:
                logging.info(f"  - {dep.first_name} {dep.last_name} ({dep.stage})")

            # Fetch daily reports for all dependents
            logging.info("\nFetching daily reports for all dependents...")

            try:
                await client.fetch_all_dependents_reports(dependents=dependents, max_concurrent=args.max_concurrent)
            except Exception as e:
                logging.error(f"❌ Failed to backup everything.\n{e}")

            logging.info("\n🎉 Backup completed!")
            logging.info(f"📁 Files saved to: {client.output_dir}")
            return True

    except ValueError as e:
        logging.error(f"Configuration error: {e}")
        logging.error("Please set BH_EMAIL and BH_PASSWORD environment variables or use --email/--password")
        return False
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return False


def main() -> None:
    """Main entry point for the CLI."""
    args = parse_args()

    # Configure logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Run the backup
    success = asyncio.run(run_backup(args))
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
