# Gender -> 1 Female 0 Male
# Churn ->  1 Yes 0 No
# Scaler is exported as scaler.pkl
# Model is exported as model.pk
# Order of the X => 'Age', 'Gender', 'Tenure', 'MonthlyCharges'

import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkt")

st.title("Customer Churn Prediction")

st.divider()

st.write("Please provide the following details to predict if a customer will churn:")

st.divider()

age = st.number_input("Age", min_value=10, max_value=100, value=30)

gender = st.selectbox("Enter the gender", ["Male", "Female"])

tenure = st.number_input("Tenure", min_value=0, max_value=130, value=10)

monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=1000.0)

st.divider()

predict_button = st.button("Predict!")

if predict_button:

    gender_selected = 1 if gender == "Female" else 0

    X = [age, gender_selected, tenure, monthly_charges]

    X1 = np.array(X)

    x_array = scaler.transform([X1])

    prediction = model.predict(x_array)[0]

    predicted = "Yes" if prediction == 1 else "No"
    
    # st.balloons()

    st.write(f"Predicted: {predicted}")

else:
    st.write("Please enter the values & use predict button")
    
