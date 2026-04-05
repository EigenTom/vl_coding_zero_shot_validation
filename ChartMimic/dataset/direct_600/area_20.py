# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(42)
# Sample data for 24 hours, with half-hour steps
time_step = np.linspace(0, 24, 48)
pressure = 1010 + 20 * np.sin(np.pi * time_step / 12) + np.random.normal(0, 2, 48)
wind_speed = 5 + 3 * np.cos(np.pi * time_step / 12) + time_step * 0.05

# Extracted variables for labels and settings
pressure_label = "Pressure (hPa)"
wind_speed_label = "Wind Speed (km/h)"
pressure_ylabel = "Pressure (hPa)"
wind_speed_xlabel = "Time (hours)"
wind_speed_ylabel = "Wind Speed (km/h)"
legend_labels = ["Pressure", "Wind Speed"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
wind_speed_ylim = [0, 12]
wind_speed_xlim = [0, 24]
pressure_ylim = [980, 1040]
pressure_xlim = [0, 24]
pressure_yticks = [980, 990, 1000, 1010, 1020, 1030, 1040]
pressure_xticks = np.arange(0, 25, 4)
wind_speed_yticks = [0, 2, 4, 6, 8, 10, 12]
wind_speed_xticks = np.arange(0, 25, 4)

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Plot Pressure
ax1.plot(time_step, pressure, "o-", color="#d62728", label=pressure_label)
ax1.fill_between(time_step, pressure, color="#ff9896", alpha=0.3)
ax1.set_ylim(pressure_ylim)
ax1.set_xlim(pressure_xlim)
ax1.set_yticks(pressure_yticks)
ax1.set_xticks(pressure_xticks)
ax1.set_ylabel(pressure_ylabel)
ax1.tick_params(axis="both", which="both", length=0)
ax1.grid(True)

# Plot Wind Speed
ax2.plot(time_step, wind_speed, "s--", color="#2ca02c", label=wind_speed_label)
ax2.fill_between(time_step, wind_speed, color="#98df8a", alpha=0.3)
ax2.set_ylim(wind_speed_ylim)
ax2.set_xlim(wind_speed_xlim)
ax2.set_yticks(wind_speed_yticks)
ax2.set_xticks(wind_speed_xticks)
ax2.set_xlabel(wind_speed_xlabel)
ax2.set_ylabel(wind_speed_ylabel)
ax2.tick_params(axis="both", which="both", length=0)
ax2.grid(True)

# Create custom legend
red_line = mlines.Line2D(
    [], [], color="#d62728", marker="o", markersize=6, label=legend_labels[0]
)
green_line = mlines.Line2D(
    [], [], color="#2ca02c", marker="s", markersize=6, label=legend_labels[1]
)
plt.legend(
    handles=[red_line, green_line],
    loc="lower center",
    bbox_to_anchor=(0.5, -0.2),
    ncol=2,
    frameon=False,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("area_20.pdf", bbox_inches="tight")
