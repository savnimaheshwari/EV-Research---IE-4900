import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# Load the Excel file
file_path = 'DataFile.xlsx'
data = pd.read_excel(file_path)

# Convert the YEAR column to datetime format and set it as the index
data['YEAR'] = pd.to_datetime(data['YEAR'], format='%Y')  # Ensure format matches your data
data.set_index('YEAR', inplace=True)

# Select the relevant columns and drop missing values
data = data[['EVREG', 'SALES']].dropna()

# Define the independent and dependent variables
X = data[['SALES']]  # Independent variable
y = data['EVREG']    # Dependent variable

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Ridge Regression model with a regularization parameter alpha
ridge_model = Ridge(alpha=1.0)

# Train the model using the training data
ridge_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = ridge_model.predict(X_test)

# Calculate the model's performance using Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Print the model's coefficients, intercept, and MSE
print(f"Ridge Model Coefficients: {ridge_model.coef_}")
print(f"Ridge Model Intercept: {ridge_model.intercept_}")
print(f"Mean Squared Error: {mse}")

# Calculate the mean of actual and predicted values
actual_mean = y_test.mean()
predicted_mean = y_pred.mean()

print(f"Mean of Actual EVREG: {actual_mean}")
print(f"Mean of Predicted EVREG: {predicted_mean}")

# Plot the results
plt.figure(figsize=(12, 6))
plt.scatter(y_test, y_pred, color='blue', label='Predicted vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', label='Perfect Prediction')
plt.xlabel('Actual EVREG')
plt.ylabel('Predicted EVREG')
plt.title('Ridge Regression: Actual vs Predicted EVREG')
plt.legend()
plt.show()
