import pandas as pd
import os
import joblib


def train_model():
    print("🚀 Starting Training Pipeline...\n")

    # -------------------------------
    # Create folders
    # -------------------------------
    os.makedirs("models", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    print("📁 Folders checked/created")

    # -------------------------------
    # Dataset creation (if missing)
    # -------------------------------
    data_path = "data/student_data.csv"

    if not os.path.exists(data_path):
        print("📊 Dataset not found → Generating synthetic data...")

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

        # Target
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
        print("✅ Dataset generated and saved")

    else:
        print("📊 Dataset found")

    # -------------------------------
    # Load dataset
    # -------------------------------
    print("\n📥 Loading dataset...")
    df = pd.read_csv(data_path)

    X = df.drop("final_score", axis=1)
    y = df["final_score"]

    print(f"✅ Data loaded | Shape: {df.shape}")

    # -------------------------------
    # Train-test split
    # -------------------------------
    from sklearn.model_selection import train_test_split

    print("\n🔀 Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print("✅ Data split completed")

    # -------------------------------
    # Model training
    # -------------------------------
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error

    print("\n🤖 Training model (Linear Regression)...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("✅ Model training completed")

    # -------------------------------
    # Evaluation
    # -------------------------------
    print("\n📈 Evaluating model...")
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)

    print(f"📊 MSE: {mse:.2f}")

    # -------------------------------
    # Save model
    # -------------------------------
    print("\n💾 Saving model...")
    joblib.dump(model, "models/best_model.pkl")
    print("✅ Model saved at models/best_model.pkl")

    print("\n🎉 TRAINING COMPLETED SUCCESSFULLY!\n")

    return model


# -------------------------------
# Run standalone (optional)
# -------------------------------
if __name__ == "__main__":
    train_model()