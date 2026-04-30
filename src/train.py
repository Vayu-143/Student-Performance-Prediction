import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib


def train_model():
    # -------------------------------
    # Create folders if not exist
    # -------------------------------
    os.makedirs("models", exist_ok=True)
    os.makedirs("data", exist_ok=True)

    # -------------------------------
    # If dataset not exists → create it
    # -------------------------------
    data_path = "data/student_data.csv"

    if not os.path.exists(data_path):
        import numpy as np

        np.random.seed(42)
        n = 200

        data = pd.DataFrame({
            "study_hours": np.random.uniform(1, 10, n),
            "attendance": np.random.uniform(50, 100, n),
            "sleep_hours": np.random.uniform(4, 9, n),
            "previous_marks": np.random.uniform(40, 90, n),
            "social_media_hours": np.random.uniform(1, 5, n),
            "mental_health_score": np.random.uniform(1, 10, n),
        })

        # Target variable
        data["final_score"] = (
            5 * data["study_hours"]
            + 0.3 * data["attendance"]
            + 2 * data["sleep_hours"]
            + 0.5 * data["previous_marks"]
            - 2 * data["social_media_hours"]
            + 1.5 * data["mental_health_score"]
            + np.random.normal(0, 5, n)
        )

        data.to_csv(data_path, index=False)

    # -------------------------------
    # Load dataset
    # -------------------------------
    df = pd.read_csv(data_path)

    X = df.drop("final_score", axis=1)
    y = df["final_score"]

    # -------------------------------
    # Train model
    # -------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    # -------------------------------
    # Save model
    # -------------------------------
    joblib.dump(model, "models/best_model.pkl")

    return model