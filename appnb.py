import streamlit as st
import pandas as pd
import joblib

# Load the trained Naive Bayes model
model = joblib.load("naive_bayes_model.pkl")

st.title("USD/MYR Risk Level Classifier")
st.markdown("Enter today's and yesterday's macroeconomic indicators to predict the USD/MYR risk level.")

# Feature input section
def input_feature(name):
    col1, col2 = st.columns(2)
    with col1:
        today = st.number_input(f"{name} - Today", key=f"{name}_today", value=0.0)
    with col2:
        yesterday = st.number_input(f"{name} - Yesterday", key=f"{name}_yesterday", value=0.0)
    return today - yesterday

# Collect differences
features = {
    "difference_MSIA_UR_lag1": input_feature("Malaysia Unemployment Rate"),
    "difference_MSIA_CPI_lag1": input_feature("Malaysia CPI"),
    "difference_GVZ_lag1": input_feature("Gold Volatility Index (GVZ)"),
    "difference_USA_IR_lag1": input_feature("US Interest Rate"),
    "difference_USA_M1_lag1": input_feature("US M1 Money Supply"),
    "difference_VIX_lag1": input_feature("VIX (Volatility Index)"),
    "difference_MSIA_NetTrade_lag1": input_feature("Malaysia Net Trade")
}

# Convert input to DataFrame
input_df = pd.DataFrame([features])

# Predict on button click
if st.button("Predict Risk Level"):
    prediction = model.predict(input_df)[0]
    risk_map = {1: "Low Risk", 2: "Medium Risk", 3: "High Risk"}
    
    st.subheader("Prediction Result")
    st.write(f"The predicted USD/MYR risk level is: **{risk_map.get(prediction, 'Unknown')}**")
