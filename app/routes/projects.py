from fastapi import APIRouter, HTTPException, status
from typing import List, Dict, Any
from app.models.project import Project, ProjectCreate, ProjectVisibility

router = APIRouter(prefix="/api/v1/projects", tags=["projects"])

_PROJECTS: Dict[str, Dict[str, Any]] = {
    "INFRA": {
        "id": 1,
        "key": "INFRA",
        "name": "Platform Infrastructure",
        "description": "Internal cluster orchestration, network topology and base images",
        "visibility": ProjectVisibility.INTERNAL,
        "owner_id": 1,
        "is_archived": False
    },
    "SEC": {
        "id": 2,
        "key": "SEC",
        "name": "Security Operations",
        "description": "Compliance tooling, scanning policies and audit artifacts",
        "visibility": ProjectVisibility.RESTRICTED,
        "owner_id": 2,
        "is_archived": False
    }
}

@router.get("/", response_model=List[Project])
async def list_projects():
    return list(_PROJECTS.values())

@router.post("/", response_model=Project, status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate, owner_id: int = 1):
    if project.key in _PROJECTS:
        raise HTTPException(status_code=400, detail="Project key already exists")
    record = {
        "id": len(_PROJECTS) + 1,
        "key": project.key,
        "name": project.name,
        "description": project.description,
        "visibility": project.visibility,
        "owner_id": owner_id,
        "is_archived": False
    }
    _PROJECTS[project.key] = record
    return record
