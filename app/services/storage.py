import os
import hashlib
from pathlib import Path
from typing import Optional, Tuple

class DocumentStorageService:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def _resolve_path(self, project_key: str, doc_path: str) -> Path:
        clean_path = doc_path.lstrip("/")
        target = (self.base_path / project_key / clean_path).resolve()
        if not str(target).startswith(str(self.base_path.resolve())):
            raise ValueError("Directory traversal attempt detected in document path")
        return target

    def write_document(self, project_key: str, doc_path: str, content: str) -> Tuple[int, str]:
        target = self._resolve_path(project_key, doc_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        content_bytes = content.encode("utf-8")
        sha256 = hashlib.sha256(content_bytes).hexdigest()
        with open(target, "wb") as f:
            f.write(content_bytes)
        return len(content_bytes), sha256

    def read_document(self, project_key: str, doc_path: str) -> Optional[str]:
        target = self._resolve_path(project_key, doc_path)
        if not target.exists():
            return None
        with open(target, "r", encoding="utf-8") as f:
            return f.read()

    def delete_document(self, project_key: str, doc_path: str) -> bool:
        target = self._resolve_path(project_key, doc_path)
        if target.exists():
            target.unlink()
            return True
        return False
