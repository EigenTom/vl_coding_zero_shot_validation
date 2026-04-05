# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np


# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(1)
# Sample data to create humidity distribution contour lines
x = np.linspace(-15, 15, 150)
y = np.linspace(-15, 30, 150)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-((X - 5) ** 2 + (Y - 6) ** 2) / 8)
Z2 = np.exp(-((X + 6) ** 2 + (Y + 7) ** 2) / 8)

# Labels and texts
labels = ["Region 1", "Region 2"]
xlabel = "Longitude"
ylabel = "Latitude"
title = "Humidity Distribution"
colorbar_label = "Humidity Intensity"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
legend_fontsize = 13
xlabel_fontsize = 15
ylabel_fontsize = 15
title_fontsize = 18
colorbar_fontsize = 14
# Create the plot
fig, ax = plt.subplots(figsize=(12, 9))

# Contour lines for Region 1 (cool colors) and Region 2 (warm colors)
CS1 = ax.contour(X, Y, Z1, colors="green", linestyles='dashed', linewidths=2)
CS2 = ax.contour(X, Y, Z2, colors="red", linestyles='solid', linewidths=2)

# Labels for x and y axes
ax.set_xlabel(xlabel, fontsize=xlabel_fontsize)
ax.set_ylabel(ylabel, fontsize=ylabel_fontsize)
ax.set_title(title, fontsize=title_fontsize)

# Adding a legend manually
h1, _ = CS1.legend_elements()
h2, _ = CS2.legend_elements()
ax.legend([h1[0], h2[0]], labels, fontsize=legend_fontsize)

# Set the aspect of the plot
ax.set_aspect("equal")
ax.grid(True)
ax.set_facecolor("#e0e0e0")
ax.set_ylim(-15, 15)
ax.set_xlim(-15, 15)

# Add color bar to represent humidity intensity
humidity = ax.contourf(X, Y, Z1 + Z2, alpha=0.4, cmap='viridis')
cbar = fig.colorbar(humidity, ax=ax)
cbar.set_label(colorbar_label, fontsize=colorbar_fontsize)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("contour_16.pdf", bbox_inches="tight")