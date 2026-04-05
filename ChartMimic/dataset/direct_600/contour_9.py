# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# ===================
# Part 2: Data Preparation
# ===================
# Sample data generation for Gaussian Peaks
x = np.linspace(-100, 100, 500)
y = np.linspace(-100, 100, 500)
X, Y = np.meshgrid(x, y)

# Define Gaussian Functions for data representation
def gaussian(x, y, x0, y0, sx, sy):
    return np.exp(-(((x - x0) ** 2) / (2 * sx ** 2) + ((y - y0) ** 2) / (2 * sy ** 2)))

# Generate data
Z1 = gaussian(X, Y, -20, 30, 40, 20)
Z2 = gaussian(X, Y, 50, -50, 30, 70)
Z3 = gaussian(X, Y, 0, 0, 60, 60)

# Chart titles and labels
title = "Gaussian Peaks Distribution"
xlabel = "X-axis"
ylabel = "Y-axis"
labels = ["Peak A", "Peak B", "Peak C"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
legend_fontsize = 12
title_fontsize = 16
label_fontsize = 14

# Plotting
plt.figure(figsize=(12, 8))
contour1 = plt.contourf(X, Y, Z1, cmap="Blues", alpha=0.6)
contour2 = plt.contourf(X, Y, Z2, cmap="Reds", alpha=0.4)
contour3 = plt.contourf(X, Y, Z3, cmap="Purples", alpha=0.3)

# Title and labels
plt.title(title, fontsize=title_fontsize)
plt.xlabel(xlabel, fontsize=label_fontsize)
plt.ylabel(ylabel, fontsize=label_fontsize)

# Create legend with color patches
legend_patches = [
    Patch(color="blue", label=labels[0]),
    Patch(color="red", label=labels[1]),
    Patch(color="purple", label=labels[2]),
]
plt.legend(handles=legend_patches, fontsize=legend_fontsize)

# Additional plot adjustments
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Reduce whitespace around the plot
plt.tight_layout()
plt.savefig("contour_9.pdf", bbox_inches="tight")