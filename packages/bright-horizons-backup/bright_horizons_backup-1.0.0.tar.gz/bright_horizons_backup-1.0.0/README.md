# Bright Horizons Backup

Backup your child's daily reports, photos, and activities from Bright Horizons daycare centers.

## Installation

### Using pip
```bash
pip install bright-horizons-backup
playwright install chromium
```

### Using uv (recommended)
```bash
uv add bright-horizons-backup
uv run playwright install chromium
```

## Setup

Create a `.env` file with your Bright Horizons login:

```env
BH_EMAIL=your_email@example.com
BH_PASSWORD=your_password
```

## Usage

### 1. Backup Your Data

```bash
# Basic backup
bright-horizons-backup

# Custom output folder
bright-horizons-backup --output-dir ./my_backup

# Use different credentials
bright-horizons-backup --email user@example.com --password mypassword
```

### 2. View Your Backups

```bash
# Install with viewer support
pip install bright-horizons-backup[viewer]
# Or with uv: uv add bright-horizons-backup[viewer]

# Launch web viewer
bright-horizons-viewer

# View specific backup
bright-horizons-viewer ./output_20240101_120000
```

The viewer opens at http://localhost:5000 with a timeline view, photo gallery, and monthly organization.

## What Gets Backed Up

- Daily reports with teacher notes
- Photos and videos
- Activity descriptions
- All organized by child and date

## Output Files

The backup creates organized folders:

```
output_20240101_120000/
├── parent_profile.json          # Your account information
├── dependents.json              # List of your children
└── Child_Name_ID/
    ├── dependent.json          # Child's profile info
    ├── raw/
    │   └── batch_*.json        # Raw API responses
    ├── processed/
    │   └── 2023-01-15.json     # Daily reports with notes
    └── media/
        ├── photo_*.jpg         # Downloaded photos
        └── video_*.mp4         # Downloaded videos
```

Additional files created:
- `bh_state.json` - Saved login session (reused for future runs)
- `run_*` folders - Browser screenshots, videos, and debug traces from login process

## Development

### Setup
```bash
# Clone repository
git clone https://github.com/marsuleouf/bright-horizons-backup.git
cd bright-horizons-backup

# Install with uv (recommended)
uv sync --extra dev --extra viewer
playwright install chromium

# Setup pre-commit hooks
uv run pre-commit install
```

### Testing
```bash
# Run tests
uv run pytest

# Run with coverage
uv run pytest --cov

# Run across Python versions
uv run tox
```

## Troubleshooting

**Login issues:** Check your email/password in the `.env` file. Inspect the `run_*` folder for screenshots and videos of the login process.
**Browser errors:** Run `playwright install chromium`
**Permission errors:** Make sure you have write access to the output directory

## License

MIT License - see [LICENSE](LICENSE) file.

## Disclaimer

For personal use only. Respect Bright Horizons' terms of service. Not affiliated with Bright Horizons.