from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from app.models.user import User, UserRole

router = APIRouter(prefix="/api/v1/users", tags=["users"])

# Team directory seed
_USERS: Dict[str, Dict[str, Any]] = {
    "ravi-menon": {
        "id": 1,
        "username": "ravi-menon",
        "email": "ravi.menon@kumosec.example",
        "full_name": "Ravi Menon",
        "role": UserRole.ENGINEER,
        "is_active": True
    },
    "maya-chen": {
        "id": 2,
        "username": "maya-chen",
        "email": "maya.chen@kumosec.example",
        "full_name": "Maya Chen",
        "role": UserRole.ENGINEER,
        "is_active": True
    },
    "kaito-dev": {
        "id": 3,
        "username": "kaito-dev",
        "email": "kaito.sato@kumosec.example",
        "full_name": "Kaito Sato",
        "role": UserRole.ENGINEER,
        "is_active": True
    }
}

@router.get("/", response_model=List[User])
async def list_users():
    return list(_USERS.values())

@router.get("/{username}", response_model=User)
async def get_user(username: str):
    if username not in _USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return _USERS[username]
