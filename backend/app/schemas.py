from pydantic import BaseModel, Field
from datetime import datetime


class UsageInput(BaseModel):
    timestamp: datetime
    usage_liters: float = Field(..., gt=0, description="Water usage in liters")


class PredictionResponse(BaseModel):
    leak_probability: float
    status: str
    water_saved_liters: float
    cost_saved: float
    environmental_impact_score: float
