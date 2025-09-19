import streamlit as st
import joblib
import pandas as pd

model = joblib.load("../models/final_model.pkl")

st.title("Heart Disease Prediction App")
st.markdown("Enter patient details below to check for heart disease risk:")

age = st.number_input("Age", min_value=20, max_value=100, value=50)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200, value=120)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)", [0, 1])
restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", [0, 1])
oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox("Slope of the ST Segment", [0, 1, 2])
ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy (0–3)", min_value=0, max_value=3, value=0)
thal = st.selectbox("Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect)", [0, 1, 2])

input_df = pd.DataFrame({
    "age": [float(age)],
    "sex": [str(sex)],
    "cp": [str(cp)],
    "trestbps": [float(trestbps)],
    "chol": [float(chol)],
    "fbs": [str(fbs)],
    "restecg": [str(restecg)],
    "thalach": [float(thalach)],
    "exang": [str(exang)],
    "oldpeak": [float(oldpeak)],
    "slope": [str(slope)],
    "ca": [float(ca)],
    "thal": [str(thal)]
})

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    if prediction == 0:
        st.success("No Heart Disease Detected")
    else:
        st.error("High Risk of Heart Disease")
