from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from sendmail import send_mail, send_alt_mail
from vidsender import get_vid
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
import os

app = FastAPI()

# CORS Documentation: https://fastapi.tiangolo.com/tutorial/cors/

# Create virtual environment: python3 -m venv venv

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:8000",
    "http://localhost",
    "http://localhost:8080",
    "https://www.bosdroneworks.com"
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

@app.get("/getvid")
async def send_vid():
    vid = get_vid()
    return {"vid": vid}