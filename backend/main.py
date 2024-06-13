from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Documentation: https://fastapi.tiangolo.com/tutorial/cors/

# Create virtual environment: python3 -m venv venv

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:8000",
    "http://localhost",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# uvicorn main:app --reload

@app.get("/")
def ok():
    return {"data": "hello rehaan"}

@app.get("/data")
async def home():
    return {"message": "Hello Rehaan"}

@app.get("/login/{email}/{password}")
async def login(email: str, password: str):
    # print(f"Email: {email}\nPassword: {password}")
    return {"email": email, "password": password}

print("OK")