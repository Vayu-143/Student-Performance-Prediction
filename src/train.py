import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load data
data = pd.read_csv("data/student_data.csv")

X = data.drop("final_score", axis=1)
y = data["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Models
lr = LinearRegression()
rf = RandomForestRegressor(n_estimators=100, random_state=42)

# Train
lr.fit(X_train, y_train)
rf.fit(X_train, y_train)

# Predict
lr_pred = lr.predict(X_test)
rf_pred = rf.predict(X_test)

# Evaluate
lr_mse = mean_squared_error(y_test, lr_pred)
rf_mse = mean_squared_error(y_test, rf_pred)

print(f"Linear Regression MSE: {lr_mse}")
print(f"Random Forest MSE: {rf_mse}")

# Select best model
best_model = rf if rf_mse < lr_mse else lr
model_name = "Random Forest" if rf_mse < lr_mse else "Linear Regression"

print(f"✅ Best Model: {model_name}")

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(best_model, "models/best_model.pkl")

# Save metrics
metrics = {
    "Linear Regression": lr_mse,
    "Random Forest": rf_mse
}

joblib.dump(metrics, "models/metrics.pkl")

# Feature Importance (only for RF)
if model_name == "Random Forest":
    importance = rf.feature_importances_
    joblib.dump(importance, "models/feature_importance.pkl")

print("✅ Training completed!")