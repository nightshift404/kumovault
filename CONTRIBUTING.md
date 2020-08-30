# Contributing to KumoVault

Internal contribution guidelines for KumoSec engineering personnel.

## Code Standards
- Adhere to PEP 8 styling.
- All routes must validate payloads using Pydantic models.
- Any modifications affecting storage paths or permissions must pass test suites:
  ```bash
  pytest tests/
  ```

## Issue Tracking
Internal tasks and enhancements are tracked via the platform ticketing board (tickets: `CORE-*`, `INFRA-*`, `SEC-*`).
