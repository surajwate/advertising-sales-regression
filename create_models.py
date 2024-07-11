import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import mean_squared_error, r2_score

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

    y_pred = model.predict(X_test)

    # Evaluate the model
    metrics = {
        'MSE': mean_squared_error(y_test, y_pred),
        'R2': r2_score(y_test, y_pred)
    }
    metrics_df = pd.DataFrame(metrics, index=[0])
    metrics_df.to_csv(f'models/metrics_simple_linear_regression_{col}.csv', index=False)

    # Save the model
    joblib.dump(model, f'models/simple_linear_regression_{col}.pkl')
