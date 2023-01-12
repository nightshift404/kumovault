# KumoVault Operations Guide

> **Notice:** The service is operating in migration/read-only mode.
> Workspaces should be accessed via the central documentation platform.

## Service Endpoints
- `GET /`: Service metadata and active version.
- `GET /healthz`: Basic liveness probe.
- `GET /readyz`: Readiness check ensuring storage subsystem availability.

## Routine Monitoring
Legacy health metrics are collected by the platform monitoring stack.
Inquiries regarding archive access should be directed to Platform Engineering.
