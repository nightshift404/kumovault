# KumoVault Deployment Guide

> **Notice:** Standalone container deployment for KumoVault is deprecated.
> All production workspace services have migrated to the enterprise cluster.
> Historical deployment references are retained for maintenance and data recovery.
> Platform Engineering Contact: `akr` (Internal Infrastructure Team).

## Historical Container Deployment Reference
1. Image build:
   ```bash
   docker-compose build
   ```
2. Start service in local legacy mode:
   ```bash
   docker-compose up -d
   ```

## Infrastructure Ownership
- Lead Infrastructure Contact: A. Krishnan (Platform Engineering / akr)
- Migration Tracking: `KV-MIG-22`
- Legacy Target Host: `kv-prod-legacy.internal.kumosec.example` (Decommissioned)
