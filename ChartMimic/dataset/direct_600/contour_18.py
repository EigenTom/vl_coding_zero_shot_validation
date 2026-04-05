# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data: Simulate temperature distribution over a surface
np.random.seed(1)
X, Y = np.meshgrid(np.linspace(-3, 3, 300), np.linspace(-3, 3, 300))

# Simulate varying temperature distribution
Z1 = np.sin(np.pi * X) * np.cos(np.pi * Y)
Z2 = np.exp(-(X ** 2 + Y ** 2) / 2)
Z = Z1 * Z2

# Extracted strings
title_text = "Temperature Distribution"
xlabel_text = "X Axis"
ylabel_text = "Y Axis"
colorbar_label_text = "Temperature"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Filled contour with custom colormap
fig, ax = plt.subplots(figsize=(8, 6))
cnt = ax.contour(X, Y, Z, levels=15, colors="black", linewidths=0.8)
ax.clabel(cnt, cnt.levels, inline=True, fontsize=8, fmt="%.2f")
contour_filled = ax.contourf(X, Y, Z, levels=15, cmap="viridis")

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
plt.savefig("contour_18.pdf", bbox_inches="tight")