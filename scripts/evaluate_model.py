"""
Evaluate trained Random Forest model
"""

import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle

# Load model
with open("../backend/model.pkl", "rb") as f:
    model = pickle.load(f)

# Load dataset
df = pd.read_csv("../dataset/sample_water_usage.csv")
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
df['usage_diff'] = df['usage_liters'].diff().fillna(0)
X = df[['usage_liters', 'hour', 'usage_diff']]
y = df['leak']

# Predict
y_pred = model.predict(X)

# Metrics
accuracy = accuracy_score(y, y_pred)
precision = precision_score(y, y_pred)
recall = recall_score(y, y_pred)
f1 = f1_score(y, y_pred)

print(f"Accuracy: {accuracy*100:.2f}%")
print(f"Precision: {precision*100:.2f}%")
print(f"Recall: {recall*100:.2f}%")
print(f"F1 Score: {f1*100:.2f}%")
