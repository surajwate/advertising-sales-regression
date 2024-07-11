import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="Exploratory Data Analysis",
    page_icon="📊",
)

# Page title
st.title("Exploratory Data Analysis (EDA)")

st.markdown(
    """
    Welcome to the Exploratory Data Analysis (EDA) page. This page is dedicated to understanding the data before building a machine learning model.
    Use the tabs below to explore the scatter plots of different advertising plotforms' budgets against sales. This plots will help you understand the trend of sales with respect to the advertising budgets.
    """
)

# Load the data
data = pd.read_csv("Advertising.csv", index_col=0)

# Get columns except "Sales" column, as "Sales" is the target variable
cols = [col for col in data.columns if col != "Sales"]

st.subheader("Scatter Plots of Budgets of different platforms vs Sales")

# Create tabs for each budget type
tabs = st.tabs(cols)

# Generate scatter plots in a loop
for col, tab in zip(cols, tabs):
    with tab:
        st.header(f"{col} Budget vs Sales")
        fig = px.scatter(
            data,
            x=col,
            y="Sales",
            title=f"Scatter plot of {col} Budget vs Sales",
            labels={col: f"{col} Budget", "Sales": "Sales"},
            trendline="ols",
        )
        st.plotly_chart(fig)

st.markdown(
    """
    **Note:** This app is a simple demonstration of EDA using scatter plots. 
    The trendline in the plots helps in understanding the correlation between 
    advertising budgets and sales.
    """
)