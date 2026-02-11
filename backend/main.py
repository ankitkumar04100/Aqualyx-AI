from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import logging
import time

from app.api import router as api_router
from app.database import init_db
from config import settings

# ---------------------------------------------------------
# Logging Configuration
# ---------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger("aqualyx-ai")


# ---------------------------------------------------------
# Application Lifespan (Startup & Shutdown)
# ---------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Starting Aqualyx AI Backend...")
    
    # Initialize database
    init_db()
    logger.info("✅ Database initialized successfully")

    yield

    logger.info("🛑 Shutting down Aqualyx AI Backend...")


# ---------------------------------------------------------
# FastAPI App Initialization
# ---------------------------------------------------------
app = FastAPI(
    title="Aqualyx AI",
    description="Real-Time Intelligent Water Monitoring & Leak Prediction API",
    version="1.0.0",
    lifespan=lifespan,
)


# ---------------------------------------------------------
# CORS Configuration
# ---------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------
# Middleware - Request Timer
# ---------------------------------------------------------
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = round(time.time() - start_time, 4)
    response.headers["X-Process-Time"] = str(process_time)
    return response


# ---------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------
@app.get("/", tags=["Root"])
def read_root():
    return {
        "project": "Aqualyx AI",
        "status": "Running",
        "version": "1.0.0",
        "message": "AI-powered predictive water monitoring system."
    }


# ---------------------------------------------------------
# Health Check Endpoint
# ---------------------------------------------------------
@app.get("/health", tags=["Monitoring"])
def health_check():
    return {
        "status": "healthy",
        "service": "Aqualyx AI Backend",
    }


# ---------------------------------------------------------
# API Router Registration
# ---------------------------------------------------------
app.include_router(api_router, prefix="/api/v1")


# ---------------------------------------------------------
# Global Exception Handler
# ---------------------------------------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "Something went wrong. Please try again later."
        },
    )
