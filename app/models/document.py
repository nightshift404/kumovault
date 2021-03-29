from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime, timezone

class DocumentLock(BaseModel):
    locked: bool = False
    locked_by: Optional[str] = None
    locked_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None

class DocumentBase(BaseModel):
    project_key: str
    title: str
    path: str
    content_type: str = "text/markdown"

class DocumentCreate(DocumentBase):
    content: str
    metadata: Optional[Dict[str, Any]] = None

class Document(DocumentBase):
    id: int
    version: int = 1
    size_bytes: int
    sha256_hash: str
    created_by: str
    lock: DocumentLock = DocumentLock()
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)

    class Config:
        from_attributes = True
        orm_mode = True
