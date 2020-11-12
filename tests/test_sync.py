from app.services.sync import DocumentSyncManager

def test_sync_enqueue_and_process():
    mgr = DocumentSyncManager(max_retries=3)
    assert mgr.pending_count() == 0
    mgr.enqueue_change("INFRA", "topology.md", "create")
    assert mgr.pending_count() == 1
    processed = mgr.process_next()
    assert processed is True
    assert mgr.pending_count() == 0
