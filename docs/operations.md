# KumoVault Operations Guide

## Service Endpoints
- `GET /`: Service metadata and active version.
- `GET /healthz`: Basic liveness probe.
- `GET /readyz`: Readiness check ensuring storage subsystem availability.

## Routine Monitoring
KumoVault exposes health endpoints for integration with internal Prometheus collectors
and Kubernetes / Nomad health monitors.

## Log Management
Log streams are separated into:
1. Application logs (stdout/stderr captured by container supervisor)
2. Audit events (JSON structured records sent to `/var/lib/kumovault/data/audit.log`)
