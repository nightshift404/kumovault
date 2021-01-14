# KumoVault System Architecture

## Overview
KumoVault coordinates document synchronization across internal engineering nodes.

```
+-------------------------------------------------------------+
|                      Client Workstations                    |
+-------------------------------------------------------------+
                              | HTTPS
                              v
                 +--------------------------+
                 |  Reverse Proxy / Ingress  |
                 +--------------------------+
                              |
               +--------------+--------------+
               |                             |
               v                             v
     +-------------------+         +-------------------+
     |  KumoVault API 1  |         |  KumoVault API 2  |
     +-------------------+         +-------------------+
               |                             |
               +--------------+--------------+
                              |
       +----------------------+----------------------+
       |                      |                      |
       v                      v                      v
+--------------+      +--------------+      +-----------------+
|  PostgreSQL  |      |  Redis Sync  |      | Local / Cluster |
|   Metadata   |      |  Event Bus   |      | Storage Volumes |
+--------------+      +--------------+      +-----------------+
```

## Core Components
- **API Service:** Stateless REST endpoints built with FastAPI.
- **Storage Subsystem:** Local volume mount with SHA-256 verification and path isolation.
- **Metadata Database:** Relational records tracking project workspaces, users, and version histories.
- **Sync Event Bus:** Redis-backed event distribution for multi-node workspace cache invalidation.
