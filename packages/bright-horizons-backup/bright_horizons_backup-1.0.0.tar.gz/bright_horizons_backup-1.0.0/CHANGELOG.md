# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0]

### Added
- **Backup Tool**: Complete daily reports, photos, and activities backup
- **Web Viewer**: Beautiful web interface to browse backed up data
- **CLI Commands**: `bright-horizons-backup` and `bright-horizons-viewer`
- **Automated Authentication**: Handles Bright Horizons login with session persistence
- **Parallel Processing**: Efficient batch processing for large datasets
- **Media Downloads**: Automatic photo and video downloading
- **Organized Storage**: Structured folders by child and date
- **Session Reuse**: Saves login state to avoid repeated authentication
- **Debug Artifacts**: Browser screenshots and videos for troubleshooting

### Features
- **Backup Command**: Downloads all data from Bright Horizons
- **Viewer Command**: Web interface with timeline, gallery, and monthly views
- **Optional Dependencies**: Flask for viewer (`pip install bright-horizons-backup[viewer]`)
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Error Handling**: Comprehensive retry logic and debugging support

### Technical Details
- Python 3.8+ support
- Playwright for web automation
- Flask for web viewer
- Pydantic for data validation
- Async/await for performance