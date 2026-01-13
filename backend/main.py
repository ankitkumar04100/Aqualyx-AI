"""
Aqualyx AI Backend
FastAPI server for leak prediction
"""

from fastapi import FastAPI, UploadFile, File
import pandas as pd
import pickle
from utils import preprocess_data, predict_leak

# Load pre-trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI(title="Aqualyx AI Backend")

@app.get("/")
def home():
    return {"message": "Welcome to Aqualyx AI Backend!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Upload CSV of water usage to get leak predictions
    """
    df = pd.read_csv(file.file)
    X = preprocess_data(df)
    predictions = predict_leak(model, X)
    df["Leak_Risk"] = predictions
    return df.to_dict(orient="records")
