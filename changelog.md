# Changelog

All notable changes to the U.S. Medical Insurance Costs Analysis project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-09-09

### Added
- Standardized `README.md` layout adhering to the repository documentation template.
- Automated Docker execution workflow and helper scripts (`run_report_docker.sh`, `run_report_docker.ps1`).
- GitHub Actions CI pipeline configuration (`.github/workflows/ci.yml`).
- Testing infrastructure under `tests/` and formatting hooks (`black`, `ruff`, `isort`).

### Changed
- Refactored notebook logic by extracting `BMI_BINS` and `BMI_LABELS` into module constants.
- Updated metadata definitions (`requirements.txt`, dependencies, build targets).
- Consolidated repository branches into `master`.

### Removed
- Removed raw CSV data files from version tracking.