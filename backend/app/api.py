from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import UsageInput, PredictionResponse
from .database import get_db
from .services import predict_leak

router = APIRouter()


@router.get("/")
def health_check():
    return {"status": "Aqualyx AI backend running 🚀"}


@router.post("/predict", response_model=PredictionResponse)
def predict(data: UsageInput, db: Session = Depends(get_db)):
    try:
        result = predict_leak(data.usage_liters)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
