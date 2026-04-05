# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(1)
# Create some data representing temperature and humidity over time
time = np.linspace(0, 24, 100)
temperature = 10 + 15 * np.sin(np.pi * time / 12)
humidity = 60 + 20 * np.sin(np.pi * time / 6)

# Extracted strings into variables
xlabel_text = 'Time of Day (hours)'
ylabel_text = 'Values'
title_text = 'Temperature and Humidity over Time'
temperature_label = 'Temperature (°C)'
humidity_label = 'Humidity (%)'

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
legend_location = 'upper left'
# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 5))  # Setting a figure size that’s suitable for the new data

# Plot the data
ax.plot(time, temperature, color="red", linestyle='-', linewidth=2, label=temperature_label)
ax.plot(time, humidity, color="blue", linestyle='--', linewidth=2, label=humidity_label)

# Customize the plot to make it visually appealing and informative
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(True)
ax.spines["bottom"].set_visible(True)
ax.tick_params(left=True, labelleft=True, bottom=True, labelbottom=True)

# Adding grid lines for better readability
ax.grid(True, linestyle=':', alpha=0.5)

# Adding labels and title
ax.set_xlabel(xlabel_text, fontsize=12)
ax.set_ylabel(ylabel_text, fontsize=12)
ax.set_title(title_text, fontsize=16)

# Adding a legend
ax.legend(loc=legend_location)

# Set y-limits to ensure the plot is within a specific range
ax.set_ylim(-15, 100)

# Set x-limits to focus on the 24 hours period
ax.set_xlim(0, 24)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_12.pdf", bbox_inches="tight")