# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np


import matplotlib.lines as mlines

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(1)
# Sample data for 12 months
months = np.arange(1, 13)
humidity = np.random.uniform(50, 100, size=12)
temperature = 10 + 10 * np.sin(np.pi * months / 6)

# Extracted variables for labels and settings
humidity_label = "Humidity (%)"
temperature_label = "Temperature (°C)"

legend_labels = ["Humidity", "Temperature"]
humidity_ylabel = "Humidity (%)"
temperature_ylabel = "Temperature (°C)"
temperature_xlabel = "Month"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
humidity_ylim = [40, 110]
temperature_ylim = [0, 30]
humidity_xticks = np.arange(1, 13, 1)
temperature_xlim = [1, 12]
temperature_xticks = np.arange(1, 13, 1)
yticks_temperature = np.arange(0, 31, 5)
legend_loc = "lower center"
legend_bbox_to_anchor = (0.5, -0.2)
legend_ncol = 2
legend_frameon = False

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 23))

# Plot Humidity
ax1.plot(months, humidity, "o--", color="#89CFF0", label=humidity_label)
ax1.set_ylim(humidity_ylim)
ax1.set_xlim(temperature_xlim)
ax1.set_xticks(humidity_xticks)
ax1.set_ylabel(humidity_ylabel)
ax1.tick_params(axis="both", which="both", length=0)
ax1.grid(True)

# Plot Temperature
ax2.plot(months, temperature, "s-", color="#D62728", label=temperature_label)
ax2.set_ylim(temperature_ylim)
ax2.set_xlim(temperature_xlim)
ax2.set_yticks(yticks_temperature)
ax2.set_xticks(temperature_xticks)
ax2.set_xlabel(temperature_xlabel)
ax2.set_ylabel(temperature_ylabel)
ax2.tick_params(axis="both", which="both", length=0)
ax2.grid(True)

# Create custom legend
blue_dot = mlines.Line2D(
    [], [], color="#89CFF0", marker="o", markersize=8, label=legend_labels[0], linestyle='None'
)
red_square = mlines.Line2D(
    [], [], color="#D62728", marker="s", markersize=8, label=legend_labels[1]
)
plt.legend(
    handles=[blue_dot, red_square],
    loc=legend_loc,
    bbox_to_anchor=legend_bbox_to_anchor,
    ncol=legend_ncol,
    frameon=legend_frameon,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("area_9.pdf", bbox_inches="tight")