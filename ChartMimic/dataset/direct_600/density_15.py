# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
# Set random seed for reproducibility
np.random.seed(100)

# Generate a normal distribution simulating sales spikes with different data
data1 = np.random.normal(loc=300, scale=70, size=500)
data2 = np.random.normal(loc=900, scale=150, size=300)
sales_data = np.concatenate([data1, data2])
xs = np.linspace(0, 1400, 300)

# Axes Limits and Labels
title = "KDE Plot of Modified Sales Data Distribution"
xlabel_value = "Sales Amount (in thousands)"
ylabel_value = "Density"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
xticks_values = [0, 200, 400, 600, 800, 1000, 1200, 1400]
xticklabels = ["0", "200", "400", "600", "800", "1000", "1200", "1400"]
yticks_values = [0, 0.0005, 0.001, 0.0015, 0.002]
yticklabels = ["0.0", "0.0005", "0.001", "0.0015", "0.002"]
xlim_values = [0, 1400]
ylim_values = [0, 0.0025]

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 5))

# Create the KDE plot with adjusted x-axis range
density = gaussian_kde(sales_data)
density.covariance_factor = lambda: 0.25
density._compute_covariance()
plt.fill_between(xs, density(xs), color="#ffe4e1", edgecolor="darkred")

ax.set_xticks(xticks_values)
ax.set_xticklabels(xticklabels)

ax.set_yticks(yticks_values)
ax.set_yticklabels(yticklabels)

plt.xlim(xlim_values)
plt.ylim(ylim_values)
# Set the title and labels
plt.title(title)
plt.xlabel(xlabel_value)
plt.ylabel(ylabel_value)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_15.pdf", bbox_inches="tight")