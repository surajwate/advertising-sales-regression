import streamlit as st
import joblib
import pandas as pd

# Title of the app
st.title("Multiple Linear Regression Prediction")

st.write(
    """
    The predictions on this page are based on multiple linear regression models. 
    The models have been created using 80% of the advertising budget data. 
    We will predict the sales based on the spending on all advertising mediums.
    """
)

# Function to load the model and metrics
def load_model_and_metrics():
    try:
        model = joblib.load("models/multiple_linear_regression.pkl")
        metrics = pd.read_csv("models/metrics_multiple_linear_regression.csv")
        scaler = joblib.load("models/scaler_multiple_linear_regression.pkl")
        return model, metrics, scaler
    except FileNotFoundError as e:
        st.error(f"Error loading model or metrics: {e}")
        return None, None

# Load the model and metrics
model, metrics, scaler = load_model_and_metrics()

if model is not None and metrics is not None:
    # Performance metrics of the model
    st.subheader("Performance of the model")
    mse = metrics["MSE"][0]
    r2 = metrics["R2"][0]

    metrics_dict = {
        "Metric": ["Mean Squared Error", "R-squared (R2) Score"],
        "Value": [mse, r2]
    }
    st.dataframe(pd.DataFrame(metrics_dict, index=[1, 2]))

    st.subheader("Predict Sales based on Total Advertisement Budget")

    # Function to predict sales
    def predict_sales(model, scaler, budget):
        # Convert the user budget dictionary to a DataFrame
        input_data = pd.DataFrame([budget], index=[0])
        input_data_scaled = scaler.transform(input_data)
        # Predict sales
        sales = model.predict(input_data_scaled)
        return sales[0]

    ad_mediums = ["TV", "Radio", "Newspaper"]
    user_budget = {}

    for ad_medium in ad_mediums:
        if ad_medium == "TV":
            max_value = 300.0
            value = 150.0
            step = 1.0
        elif ad_medium == "Radio":
            max_value = 50.0
            value = 25.0
            step = 0.5
        else:
            max_value = 120.0
            value = 30.0
            step = 1.0

        user_budget[ad_medium] = st.number_input(
            f"Enter Budget for {ad_medium} advertisement in $1000s (between 0 and {max_value}):",
            min_value=0.0,
            max_value=max_value,
            value=value,
            step=step,
        )

    if st.button("Predict Sales"):
        # Predict sales
        sales = predict_sales(model, scaler, user_budget)
        st.write(f"Predicted Sales: {sales:.2f} M$")
else:
    st.error("Model or metrics could not be loaded.")
