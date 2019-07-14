import pytest
from app.services.storage import DocumentStorageService

def test_document_write_and_read(tmp_path):
    storage = DocumentStorageService(str(tmp_path))
    content = "# Architecture Note\n\nInternal document sync specification."
    size, sha = storage.write_document("ENG", "specs/architecture.md", content)
    assert size == len(content.encode("utf-8"))
    assert len(sha) == 64

    retrieved = storage.read_document("ENG", "specs/architecture.md")
    assert retrieved == content

def test_document_path_traversal_prevention(tmp_path):
    storage = DocumentStorageService(str(tmp_path))
    with pytest.raises(ValueError):
        storage.write_document("ENG", "../../../etc/shadow", "test")
