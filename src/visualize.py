import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os

os.makedirs("outputs", exist_ok=True)

data = pd.read_csv("data/student_data.csv")

# Scatter plot
plt.figure()
plt.scatter(data["study_hours"], data["final_score"])
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Score")
plt.savefig("outputs/scatter_plot.png")
plt.close()

# Model comparison
metrics = joblib.load("models/metrics.pkl")

plt.figure()
plt.bar(metrics.keys(), metrics.values())
plt.title("Model Comparison")
plt.ylabel("MSE")
plt.savefig("outputs/model_comparison.png")
plt.close()

# Feature importance (if exists)
try:
    importance = joblib.load("models/feature_importance.pkl")
    features = data.drop("final_score", axis=1).columns

    plt.figure()
    plt.barh(features, importance)
    plt.title("Feature Importance")
    plt.savefig("outputs/feature_importance.png")
    plt.close()
except:
    pass

print("✅ Visualizations saved!")