from fastapi import FastAPI, Response, status
from app.config import settings
from app.routes.documents import router as doc_router
from app.routes.projects import router as proj_router
from app.routes.users import router as user_router

app = FastAPI(
    title="KumoVault API",
    description="Internal workspace service for document synchronization and project coordination",
    version="1.0.0"
)

app.include_router(doc_router)
app.include_router(proj_router)
app.include_router(user_router)

@app.get("/")
async def root():
    return {
        "service": "KumoVault",
        "version": "1.0.0",
        "environment": settings.environment,
        "status": "operational"
    }

@app.get("/healthz", status_code=status.HTTP_200_OK)
async def healthz():
    return {"status": "healthy"}

@app.get("/readyz", status_code=status.HTTP_200_OK)
async def readyz():
    return {"ready": True, "storage_accessible": True}
