import joblib
import pandas as pd
from feature_engineering import prepare_features

MODEL_PATH = "model.pkl"

model = joblib.load(MODEL_PATH)


def predict_from_dataframe(df: pd.DataFrame):
    X = prepare_features(df)
    probabilities = model.predict_proba(X)[:, 1]
    return probabilities


def predict_single(timestamp, usage_liters):
    df = pd.DataFrame({
        "timestamp": [timestamp],
        "usage_liters": [usage_liters]
    })

    probability = predict_from_dataframe(df)[0]
    return float(probability)
