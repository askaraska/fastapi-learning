from fastapi import FastAPI
from typing import Optional
from routers import users, products, orders

# from schemas import (
#     User,
#     Product,
#     ProductResponse,
#     Order,
#     OrderResponse
# )


app = FastAPI(
   title="FastAPI Learning Project"   
)

app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)



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



@app.get("/search") 
def search(name: Optional[str] = None):
    return {
        "search_name": name
    }



