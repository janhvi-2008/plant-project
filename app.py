import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("car_price_model.pkl", "rb"))

# Page title
st.title("🚗 Car Price Prediction")

st.write("Predict car price based on kilometers driven.")

# Input
kms = st.number_input(
    "Enter Kilometers Driven",
    min_value=0,
    max_value=500000,
    value=50000,
    step=1000
)

# Prediction
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "kms_driven": [kms]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Car Price: ₹ {prediction[0]:,.2f}")