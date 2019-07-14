from app.models.project import ProjectCreate, ProjectVisibility

def test_project_model_creation():
    data = {
        "key": "CORE",
        "name": "Core Platform",
        "description": "Backend services",
        "visibility": ProjectVisibility.INTERNAL
    }
    proj = ProjectCreate(**data)
    assert proj.key == "CORE"
    assert proj.visibility == ProjectVisibility.INTERNAL
