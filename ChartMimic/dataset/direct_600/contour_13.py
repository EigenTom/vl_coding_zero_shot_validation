# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np


# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(42)
# Create a grid of x and y values representing enzyme activity in biochemical reactions
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Function representing the enzyme activity distribution influenced by different factors
def enzyme_activity_distribution(X, Y):
    return (
        np.cos(np.sqrt(X**2 + Y**2) / 2) 
        + 0.4 * np.sin(3*X) * np.cos(2*Y)
    )

# Calculate the function values on the grid
Z_values = enzyme_activity_distribution(X, Y)
xlabel = "Concentration (mM)"
ylabel = "Time (s)"
title = "Enzyme Activity Distribution"
cbar_label = 'Activity Level'

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the contour plot
plt.figure(figsize=(8, 6))

# Using a colormap suitable for enzyme activity data
cmap = plt.cm.get_cmap("coolwarm")

contour = plt.contourf(X, Y, Z_values, levels=25, cmap=cmap)

# Add a color bar
cbar = plt.colorbar(contour)
cbar.set_label(cbar_label)

# Label the axes
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

# Enhance grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()

# Show the plot
plt.savefig("contour_13.pdf", bbox_inches="tight")
