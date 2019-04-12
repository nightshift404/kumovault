from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title="KumoVault API",
    description="Internal workspace service for document synchronization and project coordination",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {
        "service": "KumoVault",
        "version": "0.1.0",
        "status": "operational"
    }
