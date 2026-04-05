# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Create a grid of x and y values
x = np.linspace(-1, 1, 200)
y = np.linspace(-1, 1, 200)
X, Y = np.meshgrid(x, y)

# Adjust the lambda function to reflect temperature distribution in a circular pattern
def temperature_distribution_function(X, Y):
    # Simulate temperature data using a combination of Gaussian peaks representing heat sources
    return (
        np.exp(-((X - 0.3) ** 2 + (Y - 0.3) ** 2) / 0.02) * 0.5 +
        np.exp(-((X + 0.3) ** 2 + (Y - 0.3) ** 2) / 0.03) * 0.8 +
        np.exp(-((X) ** 2 + (Y + 0.4) ** 2) / 0.01) * 0.7
    )

# Calculate the function values on the grid
Z = temperature_distribution_function(X, Y)
xlabel = "X Coordinate"
ylabel = "Y Coordinate"
title = "Temperature Distribution"
colorbar_label = "Temperature Level"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the contour plot
plt.figure(figsize=(10, 8))

# Using a colormap that suits temperature visualization
n_colors = 10  # Number of discrete colors in the colormap
discrete_cmap = plt.cm.get_cmap("plasma", n_colors)

contour = plt.contourf(X, Y, Z, levels=n_colors, cmap=discrete_cmap)

# Add a color bar
cbar = plt.colorbar(contour, ticks=np.linspace(Z.min(), Z.max(), n_colors))
cbar.set_label(colorbar_label)

# Label the axes
plt.xlabel(xlabel, fontsize=14)
plt.ylabel(ylabel, fontsize=14)
plt.title(title, fontsize=16)

# Style adjustments
plt.grid(True, linestyle='--', alpha=0.7)  # Add a grid for better readability
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()

# Show the plot
plt.savefig("contour_10.pdf", bbox_inches="tight")
