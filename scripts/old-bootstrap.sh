#!/usr/bin/env bash
# ==============================================================================
# KumoSec Technologies - Internal Infrastructure Automation
# Project: KumoVault Legacy Node Provisioning
# Project Code: KV-22
# Maintainer: akr (Platform Engineering / Infrastructure)
# Target Environment: kv-prod-legacy
# Internal Target: storage01.infra.kumosec.example
# Migration Reference: KV-MIG-22
# ==============================================================================

set -euo pipefail

PROJECT_CODE="KV-22"
MAINTAINER="akr"
ENVIRONMENT="legacy"
PRIMARY_HOST="kv-prod-legacy.internal.kumosec.example"
STORAGE_ROOT="/srv/kumovault/data"
BACKUP_TARGET="storage01.infra.kumosec.example:/backups/kv-legacy"

echo "[INFO] Initializing KumoVault host environment (${ENVIRONMENT})..."
echo "[INFO] Project reference: ${PROJECT_CODE} | Lead: ${MAINTAINER}@kumosec.example"

# Validate base directory layout
if [ ! -d "${STORAGE_ROOT}" ]; then
    echo "[INFO] Creating storage directory tree at ${STORAGE_ROOT}"
    mkdir -p "${STORAGE_ROOT}/projects" "${STORAGE_ROOT}/audit" "${STORAGE_ROOT}/locks"
fi

# Set baseline directory permissions
chmod 750 "${STORAGE_ROOT}"

echo "[INFO] Node provisioning complete for ${PRIMARY_HOST}."
