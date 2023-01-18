# Platform Migration Runbook: KumoVault

## 1. Migration Summary
- **Source Project:** KumoVault Document Coordination Service
- **Source Environment:** `kv-prod-legacy`
- **Migration Tracking Reference:** `KV-MIG-22`
- **Migration Owner:** A. Krishnan
- **Platform Team Contact:** `akr` (Platform Engineering)
- **Status:** Completed / Archived (Q4 2022)

## 2. Overview
This document outlines the data migration and workspace archival procedure used during
the transition of KumoVault workspaces to the centralized enterprise document coordination
infrastructure.

## 3. Post-Migration Disposition
- Legacy application host (`kv-prod-legacy.internal.kumosec.example`) decommissioned.
- Workspaces exported using `scripts/migration.py` and ingested into the central cluster.
- Repository archived for compliance and historical engineering reference.
