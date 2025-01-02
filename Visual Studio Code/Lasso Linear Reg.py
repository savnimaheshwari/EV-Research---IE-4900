import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'DatFile.xlsx'
data = pd.read_excel(file_path)

# Drop rows with missing values in 'EVREG' or 'SALES'
cleaned_data = data[['EVREG', 'SALES']].dropna()

# Reverse independent and dependent variables
X = cleaned_data[['SALES']]  # Independent variable (now SALES)
y = cleaned_data['EVREG']    # Dependent variable (now EVREG)

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Lasso Regression model with a regularization parameter alpha
lasso_model = Lasso(alpha=1.0)

# Train the model using the training data
lasso_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = lasso_model.predict(X_test)

# Calculate the model's performance using Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Print the model's coefficients, intercept, and MSE
print(f"Lasso Model Coefficients: {lasso_model.coef_}")
print(f"Lasso Model Intercept: {lasso_model.intercept_}")
print(f"Mean Squared Error: {mse}")

# Create a scatter plot of actual vs. predicted values
plt.scatter(X_test, y_test, color='blue', label='Actual EVREG')
plt.scatter(X_test, y_pred, color='red', label='Predicted EVREG')
plt.plot(X_test, y_pred, color='green', label='Regression Line')

# Adding labels and title
plt.xlabel('EV Sales')
plt.ylabel('EV Registrations (EVREG)')
plt.title('Lasso Regression: Actual vs Predicted EV Registrations')
plt.legend()

# Show the plot
plt.show()
