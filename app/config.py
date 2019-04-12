import os
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings:
    def __init__(self):
        self.app_name = "KumoVault"
        self.environment = os.getenv("KV_ENV", "development")
        self.host = os.getenv("KV_HOST", "127.0.0.1")
        self.port = int(os.getenv("KV_PORT", "8080"))
        self.storage_path = os.getenv("KV_STORAGE_PATH", str(BASE_DIR / "data" / "documents"))
        self.max_document_size_mb = int(os.getenv("KV_MAX_DOC_SIZE_MB", "25"))
        self.database_url = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/data/kumovault.db")

    @classmethod
    def load_from_yaml(cls, path: str):
        settings = cls()
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
                server = data.get("server", {})
                settings.host = server.get("host", settings.host)
                settings.port = server.get("port", settings.port)
                storage = data.get("storage", {})
                settings.storage_path = storage.get("path", settings.storage_path)
        return settings

settings = Settings()
