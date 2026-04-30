import pandas as pd
import numpy as np
import os

np.random.seed(42)

n = 300

data = pd.DataFrame({
    "study_hours": np.random.uniform(1, 10, n),
    "attendance": np.random.uniform(50, 100, n),
    "sleep_hours": np.random.uniform(4, 9, n),
    "previous_marks": np.random.uniform(40, 90, n),
    "social_media_hours": np.random.uniform(1, 5, n),
    "mental_health_score": np.random.uniform(1, 10, n)
})

# Target generation (realistic logic)
data["final_score"] = (
    data["study_hours"] * 5 +
    data["attendance"] * 0.3 +
    data["sleep_hours"] * 2 +
    data["previous_marks"] * 0.5 -
    data["social_media_hours"] * 2 +
    data["mental_health_score"] * 1.5 +
    np.random.normal(0, 5, n)
)

os.makedirs("data", exist_ok=True)
data.to_csv("data/student_data.csv", index=False)

print("✅ Dataset generated!")