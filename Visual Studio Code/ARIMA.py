import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Historical EV sales data for 2012-2015
data = {
    'YEAR': [2012, 2013, 2014, 2015],
    'SALES': [54000, 97000, 118773, 679235]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Fit ARIMA model (using (1,1,1) as a simple approach)
model = ARIMA(df['SALES'], order=(1, 1, 1))
model_fit = model.fit()

# Forecast the next 3 years (2016-2018)
forecast = model_fit.forecast(steps=3)

# Prepare forecast index (for 2016, 2017, 2018)
forecast_index = [2016, 2017, 2018]

# Print the forecasted sales
for year, sales in zip(forecast_index, forecast):
    print(f"Forecasted EV Sales for {year}: {sales:.0f}")

# Optional: Plot the results
plt.figure(figsize=(8, 5))
plt.plot(df['YEAR'], df['SALES'], marker='o', label='Actual Sales (2012-2015)')
plt.plot(forecast_index, forecast, marker='x', linestyle='--', color='orange', label='Forecasted Sales (2016-2018)')
plt.xlabel('Year')
plt.ylabel('EV Sales')
plt.title('EV Sales Forecast')
plt.xticks(forecast_index + df['YEAR'].tolist())  # Show all years on x-axis
plt.legend()
plt.grid()
plt.show()
