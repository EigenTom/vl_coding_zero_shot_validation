# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

np.random.seed(123)

# ===================
# Part 2: Data Preparation
# ===================
# Generate new sample data for weekly exercise hours of different age groups
exercise_hours_young = np.random.normal(loc=7, scale=3, size=1000)  # Age 18-25
exercise_hours_mid = np.random.normal(loc=5, scale=2, size=1000)  # Age 26-40
exercise_hours_senior = np.random.normal(loc=4, scale=1.5, size=1000)  # Age 41-60

# Labels for the new data
labels = ["Age 18-25", "Age 26-40", "Age 41-60"]
avxlabel = "Average Exercise Hours"
xlabel = "Exercise Hours per Week"
ylabel = "Density"
title = "Weekly Exercise Hours Distribution by Age Group"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axis
fig, ax = plt.subplots(figsize=(9, 6))

# Define colors for the different age groups
colors = ["#d62728", "#9467bd", "#8c564b"]

# Plot the density plots
for data, color, label in zip([exercise_hours_young, exercise_hours_mid, exercise_hours_senior], colors, labels):
    density = gaussian_kde(data)
    xs = np.linspace(0, 15, 200)
    density.covariance_factor = lambda: 0.4
    density._compute_covariance()
    plt.fill_between(xs, density(xs), color=color, alpha=0.3, label=label)

# Plot the average exercise hours line
plt.axvline(x=5.33, color="green", linestyle="--", label=avxlabel)

# Set chart labels and title
ax.set_xlim(0, 15)
ax.set_xticks(np.arange(0, 16, 1))
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
plt.title(title)

# Show grid
plt.grid(True, linestyle="--", alpha=0.6)

# Add legend
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("density_17.pdf", bbox_inches="tight")