from fastapi import FastAPI
from typing import Optional

app = FastAPI()

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
