from pydantic import BaseModel
from typing import Optional

# Sandwiches schemas (already defined)
class SandwichBase(BaseModel):
    name: str
    ingredients: str
    price: float

class SandwichCreate(SandwichBase):
    pass

class SandwichUpdate(SandwichBase):
    pass

class Sandwich(SandwichBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True

# Resources schemas
class ResourceBase(BaseModel):
    name: str
    quantity: int

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True

# Recipes schemas
class RecipeBase(BaseModel):
    sandwich_id: int
    resource_id: int
    quantity: int

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True

# Order Details schemas
class OrderDetailBase(BaseModel):
    order_id: int
    sandwich_id: int
    quantity: int

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailUpdate(OrderDetailBase):
    pass

class OrderDetail(OrderDetailBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True
