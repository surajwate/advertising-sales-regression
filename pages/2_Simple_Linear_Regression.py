import streamlit as st
import joblib
import pandas as pd

# Title of the app
st.title("Simple Linear Regression Prediction")

st.write(
    """
    The prediction on this models are based on simple linear regression models. 
    The models has been created using a single variable. 
    It means we will predict the sales based on the spending on single advertising medium.

    We have created three models for three different advertising mediums using 80% of the data.
    """
    )

ad_medium = st.selectbox("Select Advertising Medium", ["TV", "Radio", "Newspaper"])

# Load the model
model = joblib.load(f"models/simple_linear_regression_{ad_medium}.pkl")

# Performance of the model
st.subheader(f"Performance of the model for {ad_medium} Advertisement")
metrics = pd.read_csv(f"models/metrics_simple_linear_regression_{ad_medium}.csv")
st.write(metrics)

st.subheader(f"Predict Sales based on {ad_medium} Advertisement")

# Function to predict sales
def predict_sales(budget):
    input_data = pd.DataFrame({ad_medium: [budget]})
    # Predict sales
    sales = model.predict(input_data)
    return sales[0]

# Collect input data from the user
if ad_medium == "TV":
    max_value=300.0
    value=150.0
    step=1.0
elif ad_medium == "Radio":
    max_value=50.0
    value=25.0
    step=0.5
else:
    max_value=120.0
    value=30.0
    step=1.0

user_budget = st.number_input(f"Enter Budget for {ad_medium} advertisement in 1000$ (between 0 and {max_value}):", min_value=0.0, max_value=max_value, value=value, step=step)

if st.button("Predict Sales"):
    # Predict sales
    sales = predict_sales(user_budget)
    st.write(f"Predicted Sales: {sales:.2f} M$")