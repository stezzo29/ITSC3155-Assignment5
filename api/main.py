from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.controllers import resources, recipes, order_details
from api.dependencies.database import get_db
from api.models import schemas

# Initialize the FastAPI application
app = FastAPI()

# Create an APIRouter instance
router = APIRouter()

# Resources
@router.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create_resource(db, resource)

@router.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.get_all_resources(db)

@router.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def read_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.get_resource_by_id(db, resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@router.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def update_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    updated_resource = resources.update_resource(db, resource_id, resource)
    if not updated_resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return updated_resource

@router.delete("/resources/{resource_id}", tags=["Resources"])
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    success = resources.delete_resource(db, resource_id)
    if not success:
        raise HTTPException(status_code=404, detail="Resource not found")
    return {"detail": "Resource deleted successfully"}

# Add the router to the FastAPI application
app.include_router(router)
