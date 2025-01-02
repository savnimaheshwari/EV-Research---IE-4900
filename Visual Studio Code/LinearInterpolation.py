import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
#DETACH_PER
# Given data (first 50 values, missing 50, and next 50 values)
first_50 = [
    68.2, 62.8, 63.3, 69.7, 57.1, 62.4, 58.3, 59.1, 54.2, 66, 53.1,
    72.9, 58.4, 73.1, 72.2, 72, 67.2, 65.5, 70.4, 51.2, 51.8, 71.8,
    66.7, 68.8, 70.2, 68.7, 72.6, 59.3, 62.4, 53.1, 64.7, 41.4,
    65.1, 56.1, 68.6, 72.9, 63.1, 56.8, 53.9, 64.2, 67.2, 68.4,
    64.6, 67.8, 66.4, 61.6, 62.1, 71.3, 66.3, 65.4  # First 50 values
]

next_50 = [
    74, 72, 72, 74.1, 65.6, 71, 67, 76, 66, 73,
    65.1, 78.1, 66.3, 79.1, 78.8, 78.8, 71.9, 71.3, 71.2, 74,
    58.1, 77.5, 74.9, 72.8, 76.3, 74.3, 77.5, 68, 69.5, 63.8,
    69.7, 48.3, 71.1, 65.8, 75.3, 77.1, 69.3, 77.2, 60.7, 70.5,
    73.4, 74.3, 69.2, 76, 71.2, 73.9, 67.8, 75.5, 71.4, 75.2  # Next 50 values
]

# Combine the data, filling the missing values with np.nan
data = first_50 + [np.nan] * 50 + next_50

# Indices of the original values
x = np.arange(len(data))

# Create a mask for the non-missing values
mask = ~np.isnan(data)  # Mask for non-nan values

# x values where data is not missing
x_valid = x[mask]
y_valid = np.array(data)[mask]

# Create the interpolation function using linear interpolation
linear_interp = interp1d(x_valid, y_valid, kind='linear', fill_value="extrapolate")

# Interpolate over the full range of x values
y_interp = linear_interp(x)

# Print the interpolated values
for i, val in enumerate(y_interp):
    print(f"Value at index {i}: {val:.2f}")

# Optional: Plot the results
plt.plot(x, data, 'o', label='Original data (missing values as NaN)', color='blue')
plt.plot(x, y_interp, '-', label='Interpolated data', color='orange')
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Linear Interpolation of Missing Values')
plt.legend()
plt.grid()
plt.show()
