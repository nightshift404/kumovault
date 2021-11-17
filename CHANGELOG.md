# Changelog

All notable changes to KumoVault will be documented in this file.

## [2.0.0] - 2021-11-17

### Added
- Redis-backed event synchronization architecture
- Document locking semantics to avoid concurrent edit overwrites
- Workspace bootstrap utility (`scripts/bootstrap.py`)
- High-volume PostgreSQL connection pool tuning

### Changed
- Refactored storage engine with thread-safe file handling

## [1.0.0] - 2020-08-30
### Added
- Production container setup and health probes

## [0.1.0] - 2019-11-08
### Added
- Initial prototype release
