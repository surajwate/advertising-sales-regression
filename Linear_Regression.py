import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="Linear Regression",
    page_icon="🧊",
)

st.title("Linear Regression")

st.write("This is a simple example of a linear regression model.")

st.markdown(
    """
    Use this app to understand the concept of linear regression covered in following blogs:

    1. [Simple Linear Regression](https://surajwate.com/blog/SimpleLinearRegression/)
    2. [Multiple Linear Regression](https://surajwate.com/blog/MultipleLinearRegression/)
    """
)

st.subheader("Advertising Budget vs Sales Data")

st.write("The following data is taken from the kaggle [dataset](https://www.kaggle.com/datasets/tawfikelmetwally/advertising-dataset/data).")

data = pd.read_csv('Advertising.csv', index_col=0)

st.write(data.head())

st.write(data.describe())

# Additional analysis and plots can be added here

# For example, let's plot the data







# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))  # Set a specific figure size

# Scatter plots with different markers and transparency
ax.scatter(data['TV'], data['Sales'], label='TV', marker='o', alpha=0.7, s=10)  # Circle marker with transparency
ax.scatter(data['Radio'], data['Sales'], label='Radio', marker='s', alpha=0.8, color='violet', s=10)  # Square marker with transparency and red color
ax.scatter(data['Newspaper'], data['Sales'], label='Newspaper', marker='^', alpha=0.7, color='teal', s=10)  # Triangle marker with transparency and green color

# Set labels and title with improved formatting
ax.set_xlabel('Advertising Budget', fontsize=12)
ax.set_ylabel('Sales', fontsize=12)
ax.set_title('Sales vs. Advertising Budget (TV, Radio, Newspaper)', fontsize=14)

# Customize legend and grid
ax.legend(title='Advertising Medium', loc='lower right', fancybox=True, shadow=True)  # Add title and improve legend appearance
ax.grid(color='gray', linestyle='--', linewidth=0.5, which='both', alpha=0.7)  # Add grid with customization

# Display the plot using Streamlit
st.pyplot(fig)







