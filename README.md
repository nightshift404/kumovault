# KumoVault

> **Project Status: Archived**
> KumoVault is no longer under active development. This repository has been archived
> following the platform migration completed in Q4 2022. For historical documentation
> and export utilities, refer to the `docs/` and `scripts/` directories.
> For infrastructure inquiries regarding legacy archives, contact the Platform Engineering team.

## Overview
KumoVault is an internal document coordination and project workspace service developed
by KumoSec Technologies for distributed engineering teams. The service provides
workspace-based document storage, project metadata management, and document synchronization
across internal environments.

## Repository Contents
- `app/`: FastAPI application source code (models, routes, and storage services)
- `config/`: Configuration templates for development and historical deployments
- `docs/`: System architecture, deployment notes, and migration runbook
- `scripts/`: Workspace bootstrap and data export tools
- `tests/`: Test suite for document and sync validation

## Historical Architecture
- **Language / Framework:** Python 3 (FastAPI)
- **Primary Data Store:** PostgreSQL / SQLite
- **Storage Subsystem:** Local volume mount with SHA-256 integrity checks
- **Service Lifetime:** 2019 - 2022

## Documentation
- [System Architecture](docs/architecture.md)
- [Deployment History](docs/deployment.md)
- [Migration Runbook](docs/migration.md)
- [Operations Guide](docs/operations.md)

## License
Copyright (c) 2019-2023 KumoSec Technologies Inc.
Licensed under the Apache License, Version 2.0.
