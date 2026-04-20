import streamlit as st
import numpy as np
import pickle

# Load model
with open('heart_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

st.title("Heart Disease Prediction App")

st.write("Enter patient details:")

age = st.number_input("Age")
sex = st.number_input("Sex (0=Female,1=Male)")
cp = st.number_input("Chest Pain Type")
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.number_input("Fasting Blood Sugar")
restecg = st.number_input("Rest ECG")
thalach = st.number_input("Max Heart Rate")
exang = st.number_input("Exercise Angina")
oldpeak = st.number_input("Oldpeak")
slope = st.number_input("Slope")
ca = st.number_input("CA")
thal = st.number_input("Thal")

if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease")
