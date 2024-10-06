import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Sample EV sales data for 2016-2019
ev_sales_data = {
    'YEAR': [2016, 2017, 2018, 2019],
    'SALES': [72332, 95418, 203219, 233365]
}

# Create a DataFrame
df = pd.DataFrame(ev_sales_data)
df.set_index('YEAR', inplace=True)

# Fit ARIMA model (1, 1, 1)
model = ARIMA(df['SALES'], order=(1, 1, 1))
model_fit = model.fit()

# Forecast the next 3 years (2020-2022)
forecast = model_fit.forecast(steps=3)

# Plot historical data and forecasted values
plt.figure(figsize=(10, 6))
plt.plot(df, label="Actual EV Sales (2016-2019)", marker='o')
plt.plot(range(2020, 2023), forecast, label="Forecasted EV Sales (2020-2022)", marker='x', linestyle='--')
plt.xlabel('Year')
plt.ylabel('EV Sales')
plt.title('EV Sales Forecast (ARIMA Model)')
plt.legend()
plt.grid(True)
plt.show()

# Print forecasted values
print(forecast)
