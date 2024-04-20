from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Documentation: https://fastapi.tiangolo.com/tutorial/cors/

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

@app.get("/data")
async def home():
    return {"message": "Hello Rehaan"}