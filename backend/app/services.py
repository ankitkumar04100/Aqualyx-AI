import joblib
import os
import numpy as np
from .utils import classify_risk, calculate_savings

MODEL_PATH = os.getenv("MODEL_PATH", "ml/model.pkl")

model = None

def load_model():
    global model
    if model is None:
        model = joblib.load(MODEL_PATH)
    return model


def predict_leak(usage_liters: float):
    model = load_model()

    # Feature vector (expandable later)
    features = np.array([[usage_liters]])

    probability = model.predict_proba(features)[0][1]

    status = classify_risk(probability)
    water_saved, cost_saved, env_score = calculate_savings(probability, usage_liters)

    return {
        "leak_probability": round(float(probability), 4),
        "status": status,
        "water_saved_liters": round(water_saved, 2),
        "cost_saved": round(cost_saved, 4),
        "environmental_impact_score": round(env_score, 2),
    }
