"""
main.py — FastAPI Application Entry Point
Bootstraps the app, applies CORS, registers routes, and creates DB tables.
"""

import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.database.connection import engine, create_database_if_not_exists
from app.models.chat import ChatMessage          # registers model with Base
from app.database.connection import Base
from app.routes.chat import router as chat_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Creates SQLite DB file and tables on first startup."""
    print("🚀 Starting Food Ordering Chatbot API...")
    create_database_if_not_exists()
    Base.metadata.create_all(bind=engine)
    print("✅ Database and tables ready.")
    yield
    print("🛑 Shutting down...")


app = FastAPI(
    title="AI Food Ordering Chatbot API",
    description="Powered by FastAPI, SQLite, and OpenAI GPT.",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS — allows the frontend to call the API from any origin (dev mode)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register chat routes
app.include_router(chat_router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "service": "AI Food Ordering Chatbot"}
