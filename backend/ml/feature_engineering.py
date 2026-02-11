import pandas as pd
import numpy as np


def create_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek
    return df


def create_usage_features(df: pd.DataFrame) -> pd.DataFrame:
    df["rolling_mean_3"] = df["usage_liters"].rolling(window=3, min_periods=1).mean()
    df["rolling_std_3"] = df["usage_liters"].rolling(window=3, min_periods=1).std().fillna(0)
    df["usage_diff"] = df["usage_liters"].diff().fillna(0)
    df["spike"] = np.where(df["usage_diff"] > df["usage_liters"].mean(), 1, 0)
    return df


def prepare_features(df: pd.DataFrame):
    df = create_time_features(df)
    df = create_usage_features(df)

    features = [
        "usage_liters",
        "hour",
        "day_of_week",
        "rolling_mean_3",
        "rolling_std_3",
        "usage_diff",
        "spike"
    ]

    return df[features]
