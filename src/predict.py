import joblib
import pandas as pd

model = joblib.load("models/best_model.pkl")

# Example student
student = pd.DataFrame({
    "study_hours": [6],
    "attendance": [85],
    "sleep_hours": [7],
    "previous_marks": [70],
    "social_media_hours": [2],
    "mental_health_score": [8]
})

prediction = model.predict(student)

print(f"🎯 Predicted Score: {prediction[0]:.2f}")