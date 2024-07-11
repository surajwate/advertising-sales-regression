import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load the data
data = pd.read_csv('Advertising.csv', index_col=0)

df = data.copy()

cols = [col for col in df.columns if col != 'Sales']

# Dependent variable
y = df['Sales']

for col in cols:
    # Indepentent variable
    X = df[[col]]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, f'models/simple_linear_regression_{col}.pkl')
