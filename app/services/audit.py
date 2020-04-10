import logging
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

class AuditService:
    def __init__(self, log_path: str = "./data/audit.log"):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        self.logger = logging.getLogger("kumovault.audit")
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            handler = logging.FileHandler(str(self.log_path))
            formatter = logging.Formatter('%(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def record_event(self, action: str, actor: str, project_key: str, doc_path: str, details: Dict[str, Any] = None):
        payload = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "action": action,
            "actor": actor,
            "project_key": project_key,
            "document_path": doc_path,
            "details": details or {}
        }
        self.logger.info(json.dumps(payload))
        return payload

audit_service = AuditService()
