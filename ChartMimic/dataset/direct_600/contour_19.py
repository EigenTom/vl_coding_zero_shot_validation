# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data: Simulate some other form of data using Gaussian functions
np.random.seed(10)
X, Y = np.meshgrid(np.linspace(-10, 10, 400), np.linspace(-10, 10, 400))

# Use differently parameterized Gaussian blobs representing some different distributed data
Z1 = np.exp(-(((X - 3) ** 2) / 4 + ((Y - 3) ** 2) / 6))
Z2 = np.exp(-(((X + 2) ** 2) / 6 + ((Y + 2) ** 2) / 8))
Z3 = np.exp(-(((X - 4) ** 2) / 8 + ((Y + 4) ** 2) / 4))
Z4 = np.exp(-(((X + 5) ** 2) / 10 + ((Y - 5) ** 2) / 12))
Z = Z1 + Z2 + Z3 + Z4

# Extracted variables
title_text = "Different Data Distribution"
xlabel_text = "X-axis"
ylabel_text = "Y-axis"
colorbar_label_text = "Data Value"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
contour_levels = 15
linewidths = 0.75
fontsize = 10
fmt = "%.2f"
figsize = (10, 8)
# Filled contour with labels
fig, ax = plt.subplots(figsize=figsize)
cnt = ax.contour(X, Y, Z, levels=contour_levels, colors="blue", linewidths=linewidths)
ax.clabel(cnt, cnt.levels, inline=True, fontsize=fontsize, fmt=fmt)
contour_filled = ax.contourf(X, Y, Z, levels=contour_levels, cmap='plasma')

# Title and Labels
ax.set_title(title_text)
ax.set_xlabel(xlabel_text)
ax.set_ylabel(ylabel_text)
cbar = fig.colorbar(contour_filled, ax=ax)
cbar.set_label(colorbar_label_text)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("contour_19.pdf", bbox_inches="tight")