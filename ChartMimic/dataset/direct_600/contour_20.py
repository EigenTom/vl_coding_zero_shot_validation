# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(42)
# Sample data to create contour lines for environmental impact assessment
x = np.linspace(0, 100, 150)
y = np.linspace(0, 50, 150)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-((X - 30)**2 + (Y - 20)**2) / 250)
Z2 = np.exp(-((X - 80)**2 + (Y - 40)**2) / 150)

# Labels and texts
labels = ["Region A", "Region B"]
xlabel = "Pollution Level (µg/m³)"
ylabel = "Biodiversity Index"
title = "Environmental Impact Assessment"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
legend_loc = 'upper left'
legend_fontsize = 10
xlabel_fontsize = 12
ylabel_fontsize = 12
title_fontsize = 16
fontweight = 'bold'

# Create the plot
fig, ax = plt.subplots(figsize=(12, 10))

# Contour lines for Region A (blue) and Region B (red)
CS1 = ax.contour(X, Y, Z1, colors="blue", linestyles='-', linewidths=1.5, label=labels[0])
CS2 = ax.contour(X, Y, Z2, colors="red", linestyles='--', linewidths=1.5, label=labels[1])

# Labels for x and y axes
plt.xlabel(xlabel, fontsize=xlabel_fontsize, fontweight=fontweight)
plt.ylabel(ylabel, fontsize=ylabel_fontsize, fontweight=fontweight)

# Adding a legend manually
h1, _ = CS1.legend_elements()
h2, _ = CS2.legend_elements()
ax.legend([h1[0], h2[0]], labels, loc=legend_loc, fontsize=legend_fontsize)

# Set the aspect of the plot to match the original image
ax.set_aspect("auto")
ax.grid(True)
ax.set_facecolor("#e0e0e0")  # Light gray background
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)

# Title of the plot
plt.title(title, fontsize=title_fontsize, fontweight=fontweight)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("contour_20.pdf", bbox_inches="tight")