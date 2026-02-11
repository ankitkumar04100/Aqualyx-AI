import pandas as pd
import joblib
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from feature_engineering import prepare_features

DATA_PATH = "sample_water_usage.csv"
MODEL_PATH = "model.pkl"
METRICS_PATH = "metrics.json"


def train():
    df = pd.read_csv(DATA_PATH)

    # Assume 'leak' column exists (0 or 1)
    X = prepare_features(df)
    y = df["leak"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred),
    }

    joblib.dump(model, MODEL_PATH)

    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=4)

    print("Model trained successfully.")
    print(metrics)


if __name__ == "__main__":
    train()
