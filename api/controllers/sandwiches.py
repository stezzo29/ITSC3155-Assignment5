from sqlalchemy.orm import Session
from api.models import models, schemas

def create_sandwich(db: Session, sandwich: schemas.SandwichCreate):
    db_sandwich = models.Sandwich(name=sandwich.name, ingredients=sandwich.ingredients, price=sandwich.price)
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def get_all_sandwiches(db: Session):
    return db.query(models.Sandwich).all()

def get_sandwich_by_id(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update_sandwich(db: Session, sandwich_id: int, sandwich: schemas.SandwichUpdate):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    if not db_sandwich.first():
        return None
    db_sandwich.update(sandwich.dict(), synchronize_session=False)
    db.commit()
    return db_sandwich.first()

def delete_sandwich(db: Session, sandwich_id: int):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    if not db_sandwich.first():
        return None
    db_sandwich.delete(synchronize_session=False)
    db.commit()
    return True
