# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(42)
# Generate synthetic data for contour plots
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)

# Define two data surfaces for two teams
Z1 = np.exp(-3 * (X**2 + Y**2))  # Gaussian bump for Team A
Z2 = np.exp(-3 * ((X-1.5)**2 + (Y+1.5)**2))  # Gaussian bump for Team B

# Plot configuration variables
title = "Contour Plot of Team Performance"
labels = ["Team Alpha", "Team Beta"]
xlabel = "Metric X"
ylabel = "Metric Y"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
plt.figure(figsize=(10, 6))
contour1 = plt.contour(X, Y, Z1, colors='green', linestyles='-', linewidths=2)
contour2 = plt.contour(X, Y, Z2, colors='purple', linestyles='--', linewidths=2)
plt.contourf(X, Y, Z1, alpha=0.3, cmap='Greens')
plt.contourf(X, Y, Z2, alpha=0.3, cmap='Purples')
plt.title(title)

# Adding labels and legend
legend_patches = [
    Patch(color="green", label=labels[0], alpha=0.3),
    Patch(color="purple", label=labels[1], alpha=0.3),
]
plt.legend(handles=legend_patches)

# Customizing the plot appearance
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.grid(True, linestyle='-.', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# ===================
# Part 4: Saving Output
# ===================
# Reduce whitespace around the plot
plt.tight_layout()
plt.savefig("contour_6.pdf", bbox_inches="tight")