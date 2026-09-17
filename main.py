from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field #allows us to define the structure of incoming JSON data.

app = FastAPI()

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

@app.post("/users")
def create_user(user: User): 
    # FastAPI, take the incoming JSON body and convert/validate it using the User model
    return{
        "message": "User created successfully",
        "user": user
    }

@app.post("/products", response_model=ProductResponse)
def create_product(product: Product):
    # return{
    #     "message": "Product created successfully",
    #     "product": product
    # }
    return product

@app.post("/orders", response_model=OrderResponse)
def order_process(order: Order):
    return order

@app.get("/")
def home():
    return {
        "message": "Welcome to my FastAPI learning journey",
        "name": "Sulthan"
            }

@app.get("/about")
def about():
    return {
        "name": "Sulthan",
        "role": "Python Developer"
            }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return{
        "user_id": user_id
    }

@app.get("/search")
def search(name: Optional[str] = None):
    return {
        "search_name": name
    }


@app.get("/products/search")
def search_product(category: str):
    return {
        "category": category,
        "message": "Searching products"
    }    


@app.get("/products/filter")
def filter_products(category: str, price: int):
    return {
        "category": category,
        "price": price
    }

@app.get("/products/{product_id}")
def get_productid(product_id: int):
    return {

        "product_id": product_id,
        "message": "Product found"
    }

@app.get("/users/{user_id}/orders")
def getuser_id(user_id: int, status: str, message: Optional[str] = None):
    return {
        "user_id": user_id,
        "status": status,
        "message": message
    }
