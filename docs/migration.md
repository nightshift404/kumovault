# Platform Migration Runbook: KumoVault

## 1. Migration Summary
- **Source Project:** KumoVault Document Coordination Service
- **Source Environment:** `kv-prod-legacy`
- **Migration Tracking Reference:** `KV-MIG-22`
- **Migration Owner:** A. Krishnan
- **Platform Team Contact:** `akr` (Platform Engineering)
- **Status:** Active Transition to Central Engineering Workspace

## 2. Transition Plan
Due to internal infrastructure consolidation across KumoSec engineering divisions,
KumoVault workspaces are scheduled for phased transition to the unified documentation cluster.

### Phase Schedule:
- **Phase A (Q2 2022):** Workspace inventory and export tool validation (`scripts/migration.py`).
- **Phase B (Q3 2022):** Read-only mode activated on legacy host `kv-prod-legacy`.
- **Phase C (Q4 2022):** Final database dump and decommissioning of legacy environment.

## 3. Data Export Procedure
To generate an archive of workspace documents for target platform ingestion:
```bash
python scripts/migration.py --project-key INFRA --export-dir /srv/migration/KV-MIG-22/
```
