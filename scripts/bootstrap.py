#!/usr/bin/env python3
"""
bootstrap.py - Internal Workspace Seed Utility
Copyright (c) 2019-2021 KumoSec Technologies Inc.
"""

import os
import sys
from pathlib import Path

def bootstrap_workspace(base_dir: str):
    root = Path(base_dir)
    print(f"[*] Bootstrapping KumoVault storage directories at {root}")
    for folder in ["projects/default", "audit", "exports", "locks"]:
        target = root / folder
        target.mkdir(parents=True, exist_ok=True)
        print(f"    - Created {target}")
    print("[+] Workspace directories initialized successfully.")

if __name__ == "__main__":
    target = os.getenv("KV_STORAGE_PATH", "./data/storage")
    bootstrap_workspace(target)
