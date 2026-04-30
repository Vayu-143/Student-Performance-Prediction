# 🎓 Student Performance Prediction System

🚀 **Live Demo:**  
👉 https://student-performance-prediction-ausqqqytng7mgevjouczkq.streamlit.app/

📂 **GitHub Repository:**  
👉 https://github.com/Vayu-143/Student-Performance-Prediction

---

## 📌 Overview

The **Student Performance Prediction System** is an end-to-end Machine Learning project that predicts a student's final score based on academic and behavioral factors.

This project demonstrates:
- Data generation (synthetic dataset)
- Data preprocessing
- Model training & evaluation
- Model deployment using Streamlit

---

## 🎯 Problem Statement

Educational institutions often struggle to identify students who may need additional support.

This system helps by:
- Predicting student performance  
- Identifying weak students early  
- Supporting data-driven decision-making  

---

## 🧠 Features

✅ Real-time prediction  
✅ Interactive Streamlit UI  
✅ Auto model training (if model not found)  
✅ Synthetic dataset generation  
✅ Clean & modern UI  
✅ Deployed on cloud  

---

## 🖥️ Web App Preview

### 🔹 Home Page
![Home Page](images/app_home.png)

### 🔹 Prediction Result
![Prediction](images/prediction.png)

---

## 📊 Data & Features

The model uses:

- Study Hours  
- Attendance (%)  
- Previous Marks  
- Sleep Hours  
- Social Media Usage  
- Mental Health Score  

---

## 🤖 Machine Learning Model

- Model: **Linear Regression**
- Metric: **Mean Squared Error (MSE)**
- Split: **80% Train / 20% Test**

---

## 📈 Visualizations

### 🔹 Model Comparison
![Model Comparison](outputs/model_comparison.png)

### 🔹 Scatter Plot
![Scatter Plot](outputs/scatter_plot.png)

---

## 📂 Project Structure


Student-Performance-Prediction/
│
├── data/
│ └── student_data.csv
│
├── images/
│ ├── app_home.png
│ ├── prediction.png
│ ├── graphs.png
│ └── folder_structure.png
│
├── models/
│ └── best_model.pkl
│
├── notebooks/
│
├── outputs/
│ ├── model_comparison.png
│ └── scatter_plot.png
│
├── src/
│ ├── data_generator.py
│ ├── train.py
│ ├── predict.py
│ └── visualize.py
│
├── app.py
├── main.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Vayu-143/Student-Performance-Prediction.git
cd Student-Performance-Prediction
2️⃣ Create Virtual Environment
python -m venv .venv
3️⃣ Activate Environment (Windows)
.venv\Scripts\activate
4️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run the Project
Run ML Pipeline
python main.py
Run Web App
streamlit run app.py
🌐 Deployment

This project is deployed on Streamlit Cloud for real-time usage.

🧪 How It Works
Generate synthetic student data
Train machine learning model
Save trained model (.pkl)
Load model in Streamlit app
Take user input
Predict student performance
🚀 Future Improvements
Add classification (Pass/Fail)
Use real-world dataset
Feature importance visualization
FastAPI backend integration
Teacher dashboard
👨‍💻 Author

Vayunandan Mishra

💡 Tech Stack
Python
Pandas
NumPy
Scikit-learn
Streamlit
❤️ Acknowledgment

This project is built for learning, portfolio, and real-world ML demonstration.

⭐ If you like this project, give it a star!