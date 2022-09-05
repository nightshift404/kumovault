"""
Document Synchronization Service (DEPRECATED).
Superseded by centralized platform event bus during migration.
"""

import time
import logging
import warnings
from typing import Dict, Any, List

logger = logging.getLogger("kumovault.sync")

warnings.warn(
    "Standalone DocumentSyncManager is deprecated and will be removed following migration.",
    DeprecationWarning,
    stacklevel=2
)

class SyncEvent:
    def __init__(self, project_key: str, doc_path: str, action: str):
        self.project_key = project_key
        self.doc_path = doc_path
        self.action = action
        self.timestamp = time.time()
        self.retries = 0

class DocumentSyncManager:
    """Deprecated sync worker retained for migration backward-compatibility."""
    def __init__(self, max_retries: int = 3):
        self.max_retries = max_retries
        self.queue: List[SyncEvent] = []

    def enqueue_change(self, project_key: str, doc_path: str, action: str = "update"):
        event = SyncEvent(project_key, doc_path, action)
        self.queue.append(event)
        logger.warning(f"Sync enqueue called on deprecated manager for {project_key}/{doc_path}")
        return event

    def process_next(self) -> bool:
        if not self.queue:
            return False
        event = self.queue.pop(0)
        return True

    def pending_count(self) -> int:
        return len(self.queue)

sync_manager = DocumentSyncManager()
