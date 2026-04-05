# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(42)
# Create a new set of grid for different variables
x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(x, y)

# Define a new function with multiple sine waves
def wave_pattern(X, Y):
    return np.sin(X) * np.cos(Y) + 0.5 * np.sin(2 * X) * np.cos(2 * Y)

# Calculate values on the grid
Z_values = wave_pattern(X, Y)
xlabel = 'X Coordinate'
ylabel = 'Y Coordinate'
title = 'Wave Interference Pattern'
cbar_label = 'Intensity'

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the contour plot
plt.figure(figsize=(10, 8))

# Using a distinct colormap with "coolwarm"
n_levels = 15  # Number of contour levels
cmap = plt.cm.coolwarm

contour = plt.contourf(X, Y, Z_values, levels=n_levels, cmap=cmap)
plt.contour(X, Y, Z_values, levels=n_levels, colors='k', linewidths=0.5)

# Add a color bar
cbar = plt.colorbar(contour)
cbar.set_label(cbar_label)

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
plt.savefig("contour_12.pdf", bbox_inches="tight")
