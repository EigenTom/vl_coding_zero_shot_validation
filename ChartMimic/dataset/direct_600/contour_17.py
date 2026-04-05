# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data configuration
np.random.seed(42)

# Grid
x = np.linspace(-15, 15, 300)
y = np.linspace(-15, 15, 300)
X, Y = np.meshgrid(x, y)

# Landmark locations
landmarks = [(5, -5), (-5, 5), (-10, -10), (10, 10), (0, -15)]

# Influence strength function
def influence_strength(x, y, landmarks):
    Z = np.zeros_like(x)
    for lx, ly in landmarks:
        Z += np.exp(-((x - lx)**2 + (y - ly)**2) / 20)
    return Z

# Calculate Z as influence strength
Z = influence_strength(X, Y, landmarks)

# Text variables
title_text = "Commercial Influence Field Intensity"
xlabel_text = "X Coordinate"
ylabel_text = "Y Coordinate"
colorbar_label_text = "Influence Strength"
landmark_label_format = "Landmark ({},{})"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
legend_location = "lower left"
contour_label_format = "%.1f"
fig, ax = plt.subplots(figsize=(10, 10))

# Contour
cnt = ax.contour(X, Y, Z, cmap="plasma", linewidths=1)
contour_filled = ax.contourf(X, Y, Z, cmap="plasma", alpha=0.7)
ax.clabel(cnt, cnt.levels, inline=True, fontsize=10, fmt=contour_label_format)

# Landmark locations
for lx, ly in landmarks:
    ax.plot(lx, ly, 'bo', markersize=12, label=landmark_label_format.format(lx, ly))

# Adding color bar
cbar = fig.colorbar(contour_filled, ax=ax)
cbar.set_label(colorbar_label_text)

# Titles and labels
ax.set_title(title_text)
ax.set_xlabel(xlabel_text)
ax.set_ylabel(ylabel_text)
ax.legend(loc=legend_location)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("contour_17.pdf", bbox_inches="tight")