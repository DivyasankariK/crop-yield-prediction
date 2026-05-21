import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Load Model
# -----------------------------
model = pickle.load(open("yield_prediction_model.pkl", "rb"))

# -----------------------------
# Streamlit Page
# -----------------------------
st.set_page_config(page_title="Yield Prediction App")

st.title("🌾 Yield Prediction App")

st.write("Enter the year to predict crop yield")

# -----------------------------
# User Input
# -----------------------------
year = st.number_input(
    "Enter Year",
    min_value=2000,
    max_value=2100,
    value=2025
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Yield"):

    input_data = np.array([[year]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Yield: {prediction[0]:.2f}")
