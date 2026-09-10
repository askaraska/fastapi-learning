from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI learning journey",
            "name": "Sulthan"
            }

@app.get("/about")
def about():
    return {"name": "Sulthan",
            "role": "Python Developer"
            }
