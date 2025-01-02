import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
file_path = 'DataFile.xlsx'
data = pd.read_excel(file_path)

# Drop rows with missing EV sales/reg data
data_clean = data.dropna(subset=['EVREG'])

# Select relevant features for prediction (including TIME, DETACH_PER, RANGE, ELECTRIC)
features = ['SOLAR', 'WIND', 'OOH_PER', 'TIME', 'DETACH_PER', 'RANGE', 'ELEC', 'POVERTY']
X = data_clean[features]
y = data_clean['EVREG']

# Handle missing values in the feature columns (if any)
X.fillna(0, inplace=True)

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Predict EV sales on the test data
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output the results
print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")

# Plot: Impact of all features on EV Sales (based on coefficients)
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])

# Plot the coefficients
plt.figure(figsize=(10,6))
sns.barplot(x=coefficients.index, y=coefficients['Coefficient'], palette='viridis')
plt.title('Impact of Features on EV REG')
plt.xlabel('Features')
plt.ylabel('Coefficient')
plt.xticks(rotation=45)
plt.show()
