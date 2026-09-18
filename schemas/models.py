from typing import Optional
from pydantic import BaseModel, Field #allows us to define the structure of incoming JSON data.

# Create a Pydantic Model
class User(BaseModel):
    name: str
    age: int
    email: str

class Product(BaseModel):
    name: str
    price: int = Field(gt=0)
    category: str
    description: Optional[str] = None

class ProductResponse(BaseModel):
    name: str
    price: int
    category: str

class Order(BaseModel):
    product_name: str
    quantity: int = Field(gt=0)
    price: int = Field(gt=0)
    note: Optional[str] = None   

class OrderResponse(BaseModel):
    product_name: str
    quantity: int
    price: int