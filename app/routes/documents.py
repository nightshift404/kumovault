from fastapi import APIRouter, HTTPException, status
from typing import List, Dict, Any
from app.models.document import Document, DocumentCreate
from app.services.storage import DocumentStorageService
from app.config import settings

router = APIRouter(prefix="/api/v1/documents", tags=["documents"])
storage = DocumentStorageService(settings.storage_path)

# In-memory document registry for prototype phase
_DOCUMENT_STORE: Dict[str, Dict[str, Any]] = {}

@router.post("/", response_model=Document, status_code=status.HTTP_201_CREATED)
async def create_document(doc: DocumentCreate, author: str = "system"):
    doc_key = f"{doc.project_key}:{doc.path}"
    if doc_key in _DOCUMENT_STORE:
        raise HTTPException(status_code=400, detail="Document path already exists in project")

    size, sha = storage.write_document(doc.project_key, doc.path, doc.content)
    record = {
        "id": len(_DOCUMENT_STORE) + 1,
        "project_key": doc.project_key,
        "title": doc.title,
        "path": doc.path,
        "content_type": doc.content_type,
        "version": 1,
        "size_bytes": size,
        "sha256_hash": sha,
        "created_by": author,
        "created_at": "2019-05-28T16:00:00Z",
        "updated_at": "2019-05-28T16:00:00Z"
    }
    _DOCUMENT_STORE[doc_key] = record
    return record

@router.get("/{project_key}/{doc_path:path}")
async def get_document(project_key: str, doc_path: str):
    doc_key = f"{project_key}:{doc_path}"
    if doc_key not in _DOCUMENT_STORE:
        raise HTTPException(status_code=404, detail="Document not found")
    content = storage.read_document(project_key, doc_path)
    return {
        "metadata": _DOCUMENT_STORE[doc_key],
        "content": content
    }
