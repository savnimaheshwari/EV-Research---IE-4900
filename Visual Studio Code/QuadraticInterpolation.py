import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
#PUBTR
# New first 50 values
first_50 = [
    0.4, 1, 1.7, 0.4, 5.2, 3.2, 4.5, 2.4, 1.6, 2,
    5.4, 0.8, 9.6, 0.9, 1.1, 0.5, 1, 1.2, 0.6, 8,
    10.4, 1.4, 3.4, 0.2, 1.1, 0.9, 0.8, 3.1, 0.9, 11.6,
    1.1, 27.7, 1.1, 0.7, 1.5, 0.4, 4.7, 5.7, 3.1, 0.6,
    0.4, 0.6, 1.3, 2.5, 1.6, 4.4, 7.1, 0.8, 1.7, 1.2
]

# New last 50 values
next_50 = [
    0.2, 0.9, 0.9, 0.2, 2.1, 1.3, 2.5, 1.6, 1, 0.7,
    3.3, 0.5, 3.8, 0.6, 0.5, 0.3, 0.5, 0.7, 0.3, 3,
    4.5, 0.8, 1.4, 0.2, 0.8, 0.4, 0.4, 2, 0.3, 5.9,
    0.4, 17.3, 0.5, 0.3, 0.8, 0.2, 1.7, 2.8, 1.2, 0.3,
    0.4, 0.4, 0.8, 1.3, 0.5, 1.5, 2.1, 0.4, 0.9, 0.8
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

# Create the interpolation function using quadratic interpolation
quadratic_interp = interp1d(x_valid, y_valid, kind='quadratic', fill_value="extrapolate")

# Interpolate over the full range of x values
y_interp = quadratic_interp(x)

# Print the interpolated values
for i, val in enumerate(y_interp):
    print(f"Value at index {i}: {val:.2f}")

# Optional: Plot the results
plt.plot(x, data, 'o', label='Original data (missing values as NaN)', color='blue')
plt.plot(x, y_interp, '-', label='Interpolated data', color='orange')
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Quadratic Interpolation of Missing Values')
plt.legend()
plt.grid()
plt.show()
