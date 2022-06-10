#!/usr/bin/env python3
"""
migration.py - KumoVault Workspace Export and Migration Utility
Copyright (c) 2019-2022 KumoSec Technologies Inc.

Usage:
    python scripts/migration.py --project-key INFRA --export-dir /tmp/kv-export
"""

import os
import sys
import json
import argparse
from pathlib import Path

def export_workspace(project_key: str, storage_root: str, output_dir: str):
    src = Path(storage_root) / project_key
    out = Path(output_dir) / project_key
    out.mkdir(parents=True, exist_ok=True)

    manifest = {
        "source_project": project_key,
        "migration_tool": "kv-migrate-v1",
        "exported_files": []
    }

    if src.exists():
        for item in src.rglob("*"):
            if item.is_file():
                rel = item.relative_to(src)
                dest = out / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(item.read_bytes())
                manifest["exported_files"].append(str(rel))

    manifest_path = out / "migration_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"[+] Exported workspace {project_key} to {out}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KumoVault Workspace Exporter")
    parser.add_argument("--project-key", required=True, help="Project key to export")
    parser.add_argument("--storage-root", default="./data/storage", help="Storage root")
    parser.add_argument("--export-dir", default="./data/exports", help="Export target")
    args = parser.parse_args()
    export_workspace(args.project_key, args.storage_root, args.export_dir)
