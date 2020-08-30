# Changelog

All notable changes to KumoVault will be documented in this file.

## [1.0.0] - 2020-08-30

### Added
- Multi-stage Dockerfile and container deployment configuration
- PostgreSQL connection pooling and connection management
- Structured audit logging service for compliance and change tracking
- Health and readiness endpoints (`/healthz`, `/readyz`)
- Comprehensive deployment and operations runbooks

### Changed
- Migrated default storage limits from 25MB to 50MB per workspace document
- Stabilized REST API endpoints for projects, users, and documents

## [0.1.0] - 2019-11-08
### Added
- Initial prototype release and REST API skeleton
