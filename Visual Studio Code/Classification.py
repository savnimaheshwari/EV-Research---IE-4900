import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel('DataFile.xlsx')

# List of variables to classify
variables = ['EMPLOY', 'PUBTR', 'LAND']

# Initialize a list to hold the results
results = []

for var in variables:
    # Define the independent variable (X)
    X = df[[var]].dropna()  # Remove rows with missing values
    y = np.arange(len(X))  # Use the index as the dependent variable for comparison

    # Ensure y has the same length as X
    if len(X) != len(y):
        print(f"Skipping {var} due to mismatched lengths after dropping NaN values.")
        continue

    # Fit a linear regression model
    linear_model = LinearRegression()
    linear_model.fit(X, y)
    y_pred_linear = linear_model.predict(X)
    mse_linear = mean_squared_error(y, y_pred_linear)

    # Fit a quadratic regression model
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)
    quadratic_model = LinearRegression()
    quadratic_model.fit(X_poly, y)
    y_pred_quadratic = quadratic_model.predict(X_poly)
    mse_quadratic = mean_squared_error(y, y_pred_quadratic)

    # Compare MSE of linear and quadratic models
    classification = 'Linear' if mse_linear < mse_quadratic else 'Quadratic'
    results.append((var, classification))

    # Optional: Plot the variable against its index
    plt.scatter(X, y, label=f'{var} Data', alpha=0.5)
    plt.plot(X, y_pred_linear, color='red', label='Linear Fit', linewidth=2)
    plt.plot(X, y_pred_quadratic, color='green', label='Quadratic Fit', linewidth=2)
    plt.title(f'{var} Classification')
    plt.xlabel(var)
    plt.ylabel('Index')
    plt.legend()
    plt.show()

# Print the results list
print("Classification Results:")
for var, classification in results:
    print(f'{var}: {classification}')
