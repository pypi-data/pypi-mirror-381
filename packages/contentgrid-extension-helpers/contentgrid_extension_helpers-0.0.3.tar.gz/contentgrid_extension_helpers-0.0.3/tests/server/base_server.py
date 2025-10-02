from fastapi import Depends, FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from contentgrid_extension_helpers.middleware.exception_middleware import (
    catch_exceptions_middleware,
)
from dotenv import load_dotenv

load_dotenv(".env.test")
load_dotenv(".env.secret", override=True)


app = FastAPI()
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:9085",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_exception_middleware(request: Request, call_next):
    return await catch_exceptions_middleware(request, call_next, "https://problems.contentgrid.test")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}