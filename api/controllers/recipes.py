from sqlalchemy.orm import Session
from api.models import models, schemas

def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(sandwich_id=recipe.sandwich_id, resource_id=recipe.resource_id, quantity=recipe.quantity)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def get_all_recipes(db: Session):
    return db.query(models.Recipe).all()

def get_recipe_by_id(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def update_recipe(db: Session, recipe_id: int, recipe: schemas.RecipeUpdate):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    if not db_recipe.first():
        return None
    db_recipe.update(recipe.dict(), synchronize_session=False)
    db.commit()
    return db_recipe.first()

def delete_recipe(db: Session, recipe_id: int):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    if not db_recipe.first():
        return None
    db_recipe.delete(synchronize_session=False)
    db.commit()
    return True
