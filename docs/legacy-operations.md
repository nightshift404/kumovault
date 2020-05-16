# Legacy Operations Runbook: KumoVault

## 1. System Ownership & Operations Contacts
- **Project:** KumoVault Core Service
- **Primary Infrastructure Maintainer:** Arun Krishnan
- **Internal Handle / Alias:** akr
- **Team:** Platform Engineering / Cloud Infrastructure
- **Email:** arun.krishnan@kumosec.example
- **Migration Reference:** KV-MIG-22
- **Legacy Host:** kv-prod-legacy.internal.kumosec.example
- **Target Storage Node:** storage01.infra.kumosec.example

## 2. Infrastructure Architecture
The legacy production environment (`kv-prod-legacy`) runs the KumoVault application server
bound to internal gateway proxies. Local filesystem storage is synchronized with the
primary platform object store.

### Automated Recovery
In case of host reboot on `kv-prod-legacy`, the legacy provisioning script located at
`scripts/old-bootstrap.sh` handles initial mount validation and directory hierarchy creation.

## 3. Routine Maintenance
- **Service Restart:**
  ```bash
  systemctl restart kumovault.service
  ```
- **Audit Verification:**
  Audit logs are retained locally under `/var/lib/kumovault/data/audit/` prior to syslog shipping.
- **Backup Verification:**
  Nightly snapshots are transmitted to `storage01.infra.kumosec.example` under project key `KV-22`.
