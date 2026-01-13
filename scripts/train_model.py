"""
Train Random Forest model for Aqualyx AI
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("../dataset/sample_water_usage.csv")

# Feature engineering
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
df['usage_diff'] = df['usage_liters'].diff().fillna(0)
X = df[['usage_liters', 'hour', 'usage_diff']]
y = df['leak']  # Assume 'leak' column exists in dataset

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
with open("../backend/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved to backend/model.pkl")
