# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(1)
# Hypothetical ccompany stock data over a year
x = np.linspace(0, 365, 100)  # days of the year
y = np.linspace(0, 100, 100)  # stock value in $
X, Y = np.meshgrid(x, y)
Z1 = 50 + 20 * np.exp(-((X - 150) ** 2 + (Y - 50) ** 2) / 4000)  # early year stock value
Z2 = 55 + 25 * np.exp(-((X - 250) ** 2 + (Y - 50) ** 2) / 4000)  # mid-year stock value
labels = ["Early Year", "Mid Year"]
xlabel = "Days of the Year"
ylabel = "Stock Value ($)"
title = "Company Stock Value Over a Year"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Contour lines for Early Year (blue) and Mid Year (red)
CS1 = ax.contour(X, Y, Z1, colors="blue", linestyles="solid", linewidths=1.5, label=labels[0])
CS2 = ax.contour(X, Y, Z2, colors="red", linestyles="dashed", linewidths=1.5, label=labels[1])

# Labels for x and y axes and title
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

# Adding a legend manually
h1, _ = CS1.legend_elements()
h2, _ = CS2.legend_elements()
ax.legend([h1[0], h2[0]], labels)

# Set the aspect of the plot for better readability
ax.set_aspect("auto")
ax.grid(True)
ax.set_facecolor("#e5e5e5")
ax.set_ylim(0, 100)
ax.set_xlim(0, 365)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("contour_14.pdf", bbox_inches="tight")

