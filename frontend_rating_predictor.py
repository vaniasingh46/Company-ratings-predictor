import streamlit as st
import joblib
import pandas as pd


model = joblib.load(r"C:\Users\Vania Singh\Downloads\company_rating_predictor_model .pkl")

st.title("Company Rating Predictor")

company = st.text_input("Company Name")
reviews = st.number_input("Total Reviews", min_value=0)

industry = st.text_input("Industry")
hq = st.text_input("Headquarters")
primary_hq = st.text_input("Primary HQ")

if st.button("Predict"):
    data = pd.DataFrame({
        "Company Name": [company],
        "Total Reviews": [reviews],
        "Industry": [industry],
        "Headquarters": [hq],
        "Primary HQ": [primary_hq]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Rating: {prediction[0]:.2f}")
