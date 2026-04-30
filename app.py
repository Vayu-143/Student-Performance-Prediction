import streamlit as st
import pandas as pd
import joblib
import os
from src.train import train_model

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# -------------------------------
# HEADER
# -------------------------------
st.markdown(
    """
    <h1 style='text-align: center;'>🎓 Student Performance Prediction System</h1>
    <p style='text-align: center; color: gray;'>
    Predict student performance using Machine Learning
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# -------------------------------
# MODEL HANDLING (DEPLOYMENT FIX)
# -------------------------------
MODEL_PATH = "models/best_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.warning("⚙️ Model not found. Training model... Please wait.")

    try:
        model = train_model()
        st.success("✅ Model trained successfully!")
    except Exception as e:
        st.error(f"❌ Training failed: {e}")
        st.stop()
else:
    try:
        model = joblib.load(MODEL_PATH)
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        st.stop()

# -------------------------------
# INPUT SECTION
# -------------------------------
st.subheader("📊 Input Student Details")

col1, col2 = st.columns(2)

with col1:
    study_hours = st.slider("Study Hours", 1.0, 10.0, 5.0)
    attendance = st.slider("Attendance (%)", 50.0, 100.0, 75.0)
    sleep_hours = st.slider("Sleep Hours", 4.0, 9.0, 7.0)

with col2:
    previous_marks = st.slider("Previous Marks", 40.0, 90.0, 60.0)
    social_media_hours = st.slider("Social Media Hours", 1.0, 5.0, 2.0)
    mental_health_score = st.slider("Mental Health Score", 1.0, 10.0, 7.0)

st.markdown("---")

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("🚀 Predict Performance"):

    input_data = pd.DataFrame({
        "study_hours": [study_hours],
        "attendance": [attendance],
        "sleep_hours": [sleep_hours],
        "previous_marks": [previous_marks],
        "social_media_hours": [social_media_hours],
        "mental_health_score": [mental_health_score]
    })

    try:
        prediction = model.predict(input_data)[0]

        st.success(f"🎯 Predicted Score: {prediction:.2f}")

        if prediction > 100:
            st.info("🚀 Excellent performance")
        elif prediction > 80:
            st.info("👍 Good performance")
        else:
            st.warning("📚 Needs improvement")

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Machine Learning & Streamlit")