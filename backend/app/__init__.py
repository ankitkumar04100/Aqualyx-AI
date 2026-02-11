"""
Aqualyx AI - Backend Application Package

This package contains:
- API routes
- Database configuration
- Business logic services
- Utility functions
- Pydantic schemas
- ORM models

Author: Ankit Kumar
Project: Aqualyx AI
"""

from .api import router as api_router
from .database import Base, get_db
from .services import predict_leak_risk
from .schemas import PredictRequest, PredictResponse
from .models import WaterUsage

__all__ = [
    "api_router",
    "Base",
    "get_db",
    "predict_leak_risk",
    "PredictRequest",
    "PredictResponse",
    "WaterUsage",
]
