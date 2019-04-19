from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from datetime import datetime, timezone

class ProjectVisibility(str, Enum):
    INTERNAL = "internal"
    RESTRICTED = "restricted"
    CONFIDENTIAL = "confidential"

class ProjectBase(BaseModel):
    key: str
    name: str
    description: Optional[str] = None
    visibility: ProjectVisibility = ProjectVisibility.INTERNAL

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    owner_id: int
    created_at: datetime = datetime.now(timezone.utc)
    is_archived: bool = False

    class Config:
        from_attributes = True
        orm_mode = True
