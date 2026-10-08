import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, BackgroundTasks
from typing import Optional
from routers import users, products, orders, auth

from database import engine, Base
from models import product, user

# from schemas import (
#     User,
#     Product,
#     ProductResponse,
#     Order,
#     OrderResponse
# )

Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Application starting...")

    yield

    print("🛑 Application shutting down...")

app = FastAPI(
   title="FastAPI Learning Project",
   lifespan=lifespan   
)

@app.middleware("http")
async def add_custom_header(request, call_next):
    response = await call_next(request)

    response.headers["X-App-Name"] = "FastAPI-Learning"

    return response

app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(auth.router)

def write_log(message: str):
    with open("background.log", "a") as file:
        file.write(message + "\n")

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

@app.get("/async-test")
async def async_test():
    return {
        "message": "This is an async endpoint"
    }

@app.get("/search") 
def search(name: Optional[str] = None):
    return {
        "search_name": name
    }


@app.get("/async-wait")
async def async_wait():
    await asyncio.sleep(2)

    return {
        "message": "Async operation completed"
    }

@app.post("/background-test")
def background_test(
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        write_log,
        "Background task executed successfully"
    )

    return {
        "message": "Response sent successfully"
    }