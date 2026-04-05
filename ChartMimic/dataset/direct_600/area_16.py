# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np


# ===================
# Part 2: Data Preparation
# ===================
# Set the seed for reproducibility
np.random.seed(1)

# Data
years = np.arange(2010, 2020)
temperatures = np.random.uniform(low=15, high=35, size=len(years))
humidity = np.random.uniform(low=40, high=80, size=len(years))
pollution = np.random.uniform(low=30, high=100, size=len(years))

# Variables for plot configuration
temp_label = "Temperature (°C)"
humidity_label = "Humidity (%)"
pollution_label = "Pollution (AQI)"
xlabel_text = "Years"
ylabel_text = "Environmental Metrics"
title_text = "Environmental Trends Over Years"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
ylim_values = (0, 150)
xticks_values = years
yticks_values = [0, 25, 50, 75, 100, 125, 150]
legend_location = "upper right"
legend_fontsize = 12
# Plot
fig, ax = plt.subplots(figsize=(10, 6))  # Adjusted for better aspect ratio

# Stack the data
stack_data = np.vstack((temperatures, humidity, pollution))

# Colors for each stack
colors = ["#ff9999", "#66b3ff", "#99ff99"]

# Area plot
ax.stackplot(years, stack_data, labels=[temp_label, humidity_label, pollution_label], colors=colors, alpha=0.7)

# Remove top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Setting the x-axis and y-axis limits and ticks
ax.set_ylim(*ylim_values)
ax.set_xticks(xticks_values)
ax.set_yticks(yticks_values)

# Adding labels and title
ax.set_xlabel(xlabel_text, fontsize=14)
ax.set_ylabel(ylabel_text, fontsize=14)
ax.set_title(title_text, fontsize=16, y=1.05)

# Custom legend
ax.legend(loc=legend_location, fontsize=legend_fontsize, frameon=False)

# Grid
ax.grid(True, linestyle="--", alpha=0.5, which="both")

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to reduce white space
plt.tight_layout()
plt.savefig("area_16.pdf", bbox_inches="tight")
