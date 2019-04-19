from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum
from datetime import datetime, timezone

class UserRole(str, Enum):
    ADMIN = "admin"
    ENGINEER = "engineer"
    VIEWER = "viewer"
    SERVICE = "service_account"

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    role: UserRole = UserRole.ENGINEER

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    is_active: bool = True
    created_at: datetime = datetime.now(timezone.utc)

    class Config:
        from_attributes = True
        orm_mode = True
