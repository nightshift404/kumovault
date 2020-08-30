# KumoVault

Internal workspace service for document synchronization and project coordination across
KumoSec distributed engineering teams.

## Overview
KumoVault provides centralized, access-controlled workspace storage for technical
specifications, architectural decision records (ADRs), and internal project documentation.

## Architecture
- **API Engine:** Python FastAPI with asynchronous request dispatch
- **Data Store:** PostgreSQL for workspace metadata and SQLite for local development
- **Storage Subsystem:** Chunked document engine with SHA-256 verification
- **Deployment:** Containerized multi-stage Docker builds

## Deployment
Refer to `docs/deployment.md` for production container deployment instructions.
Operational checks are detailed in `docs/operations.md`.

## License
Copyright (c) 2019-2020 KumoSec Technologies Inc. Licensed under the Apache License 2.0.
