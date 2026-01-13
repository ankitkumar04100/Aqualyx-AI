"""
Utility functions for Aqualyx AI
"""

import pandas as pd

def preprocess_data(df):
    """
    Feature engineering for leak prediction
    """
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    df['usage_diff'] = df['usage_liters'].diff().fillna(0)
    # Additional features can be added
    features = df[['usage_liters', 'hour', 'usage_diff']]
    return features

def predict_leak(model, X):
    """
    Predict leak probability (0-1) and convert to Risk category
    """
    prob = model.predict_proba(X)[:, 1]  # Probability of leak
    risk = []
    for p in prob:
        if p < 0.3:
            risk.append("Normal")
        elif p < 0.7:
            risk.append("Warning")
        else:
            risk.append("Critical")
    return risk
