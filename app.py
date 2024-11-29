import numpy as np
import pandas as pd
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the pre-trained model
model = pickle.load(open('calories.pkl', 'rb'))

# Title of the app
st.title("Calories Burn Prediction")

# Create columns for input
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    height = st.number_input("Height (cm)", min_value=0.0)


with col2:
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=0.0)
    body_temp = st.number_input("Body Temperature (°C)", min_value=0.0)
    weight = st.number_input("Weight (kg)", min_value=0.0)
    duration = st.number_input("Duration (minutes)", min_value=0.0)

# Convert gender to numerical value
if gender == "Male":
    gender = 0
else:
    gender = 1

# Predict button
if st.button("Predict Calories Burned"):
    # Create input array for prediction
    input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display prediction
    st.success(f"The predicted calories burned is: {prediction:.2f} kcal")
