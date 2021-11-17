# KumoVault

Internal workspace service for document synchronization and project coordination across
KumoSec distributed engineering teams.

## Overview
KumoVault provides centralized, access-controlled workspace storage for technical
specifications, architectural decision records (ADRs), and internal project documentation.
Version 2.0 introduces multi-node synchronization with distributed locking and Redis
event streaming.

## Architecture
- **API Engine:** Python FastAPI with asynchronous request dispatch
- **Data Store:** PostgreSQL for metadata and SQLite for local development
- **Cache / Event Bus:** Redis 6.2 for sync event distribution
- **Storage Subsystem:** Chunked document engine with SHA-256 verification

## Documentation
- `docs/architecture.md`: System layout and data flow
- `docs/deployment.md`: Container deployment and infrastructure contacts
- `docs/operations.md`: Health monitoring and operational runbooks

## License
Copyright (c) 2019-2021 KumoSec Technologies Inc. Licensed under Apache 2.0.
