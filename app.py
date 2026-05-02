import streamlit as st
from src.predict import predict

st.title("AI Customer Churn Predictor")

tenure = st.number_input("Tenure")
monthly_charges = st.number_input("Monthly Charges")
total_charges = st.number_input("Total Charges")

if st.button("Predict"):
    result, prob = predict([tenure, monthly_charges, total_charges])

    if result == 1:
        st.error(f"Customer likely to churn (Prob: {prob:.2f})")
    else:
        st.success(f"Customer will stay (Prob: {prob:.2f})")
