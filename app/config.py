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
        self.max_document_size_mb = int(os.getenv("KV_MAX_DOC_SIZE_MB", "50"))
        self.database_url = os.getenv(
            "DATABASE_URL",
            f"sqlite:///{BASE_DIR}/data/kumovault.db"
        )
        self.pool_size = int(os.getenv("KV_DB_POOL_SIZE", "10"))
        self.max_overflow = int(os.getenv("KV_DB_MAX_OVERFLOW", "20"))

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
                db = data.get("database", {})
                if db.get("driver") == "postgresql":
                    settings.database_url = f"postgresql://{db.get('user')}:@{db.get('host')}:{db.get('port')}/{db.get('name')}"
                    settings.pool_size = db.get("pool_size", 10)
                    settings.max_overflow = db.get("max_overflow", 20)
        return settings

settings = Settings()
