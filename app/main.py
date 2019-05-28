from fastapi import FastAPI
from app.config import settings
from app.routes.documents import router as doc_router

app = FastAPI(
    title="KumoVault API",
    description="Internal workspace service for document synchronization and project coordination",
    version="0.1.0"
)

app.include_router(doc_router)

@app.get("/")
async def root():
    return {
        "service": "KumoVault",
        "version": "0.1.0",
        "status": "operational"
    }
