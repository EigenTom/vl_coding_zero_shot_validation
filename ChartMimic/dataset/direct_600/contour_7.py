# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)
# Simulated data generation for temperature and humidity levels
temp = np.linspace(-20, 50, 400)
humidity = np.linspace(0, 100, 400)
TEMP, HUM = np.meshgrid(temp, humidity)
pos = np.dstack((TEMP, HUM))

# Simulate Gaussian distributions for temperature and humidity
def gaussian(x, y, mean, cov):
    return np.exp(-((x-mean[0])**2/(2*cov[0][0]) + (y-mean[1])**2/(2*cov[1][1])))

Z_temp = gaussian(TEMP, HUM, [25, 50], [[100, 0], [0, 250]])
Z_hum = gaussian(TEMP, HUM, [10, 80], [[80, 0], [0, 100]])

# Extracted variables
title = "Distribution of Temperature and Humidity Levels"
labels = ["Temperature", "Humidity"]
xlabel = "Temperature (°C)"
ylabel = "Humidity (%)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
plt.figure(figsize=(10, 6))

# Contour plots for the distributions
contour_temp = plt.contourf(TEMP, HUM, Z_temp, cmap="Blues", alpha=0.6)
contour_hum = plt.contourf(TEMP, HUM, Z_hum, cmap="Oranges", alpha=0.6)
plt.title(title)

# Create legend with color patches
legend_patches = [
    Patch(color="blue", label=labels[0]),
    Patch(color="orange", label=labels[1]),
]
plt.legend(handles=legend_patches)

# Axis labels
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Adjust plot to be visually appealing
plt.gca().set_aspect("equal", adjustable="box")

# ===================
# Part 4: Saving Output
# ===================
# Reduce whitespace around the plot
plt.tight_layout()
plt.savefig("contour_7.pdf", bbox_inches="tight")