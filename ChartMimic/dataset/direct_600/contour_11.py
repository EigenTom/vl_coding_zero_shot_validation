# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
# Create a grid of x (wind speed) and z (humidity) values
np.random.seed(1)  # Different seed for different data
x = np.linspace(0, 2, 120)
z = np.linspace(0, 2, 120)
X, Z = np.meshgrid(x, z)

# Define the landscape function with different peaks
def landscape_function(X, Z):
    return (
        np.exp(-((X - 0.5) ** 2 + (Z - 0.7) ** 2) / 0.015)
        + np.exp(-((X - 1.2) ** 2 + (Z - 1.5) ** 2) / 0.03)
        + np.exp(-((X - 1.8) ** 2 + (Z - 0.3) ** 2) / 0.04)
    )

# Calculate the function values on the grid
Z_values = landscape_function(X, Z)
xlabel = 'Wind Speed (normalized)'
ylabel = 'Humidity (normalized)'
title = 'Performance Landscape of Wind Turbines'

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the contour plot
plt.figure(figsize=(10, 8))

# Using a different colormap with "Blues"
n_colors = 12  # Number of discrete colors in the colormap
discrete_cmap = plt.cm.get_cmap("Blues", n_colors)

contour = plt.contourf(X, Z, Z_values, levels=n_colors, cmap=discrete_cmap)

# Add a color bar
cbar = plt.colorbar(
    contour, ticks=np.linspace(Z_values.min(), Z_values.max(), n_colors)
)

# Label the axes
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()

# Show the plot
plt.savefig("contour_11.pdf", bbox_inches="tight")
