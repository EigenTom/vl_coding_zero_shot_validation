# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# ===================
# Part 2: Data Preparation
# ===================
# Generating sample data for two different societal groups
x = np.linspace(-100, 100, 400)
y = np.linspace(-100, 100, 400)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

# Influence areas modeled using bivariate Gaussian functions
Z1 = np.exp(-0.01 * ((X - 30) ** 2 + (Y - 30) ** 2))
Z2 = np.exp(-0.01 * ((X + 30) ** 2 + (Y + 30) ** 2))

# Titles and labels
title = "Impact Zones of Societal Groups"
labels = ["Group A", "Group B"]
xlabel = "Longitude"
ylabel = "Latitude"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
legend_location = 'upper right'
plt.figure(figsize=(10, 6))

# Plot Group A influence area
contour1 = plt.contourf(X, Y, Z1, cmap="Oranges", alpha=0.6)  # Change to a different color

# Plot Group B influence area
contour2 = plt.contourf(X, Y, Z2, cmap="Purples", alpha=0.6)  # Change to a different color

# Set plot title and legend
plt.title(title, fontsize=16)

# Create legend with color patches
legend_patches = [
    Patch(color="orange", label=labels[0], alpha=0.6),
    Patch(color="purple", label=labels[1], alpha=0.6),
]
plt.legend(handles=legend_patches, fontsize=12, loc=legend_location)

# Set equal aspect ratio for the plot
plt.gca().set_aspect("equal", adjustable="box")

# Axis labels
plt.xlabel(xlabel, fontsize=14)
plt.ylabel(ylabel, fontsize=14)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()  # Reduce whitespace around the plot
plt.savefig("contour_8.pdf", bbox_inches="tight")