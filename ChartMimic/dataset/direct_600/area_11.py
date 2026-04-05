# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(42)
# Data for the plot with different environmental metrics
months = np.array([1, 2, 3, 4, 5, 6])
temperature = np.array([14, 16, 15, 18, 20, 22]) + np.random.uniform(-1, 1, 6)
humidity = np.array([70, 65, 68, 64, 60, 58]) + np.random.uniform(-3, 3, 6)
precipitation = np.array([90, 100, 85, 110, 95, 105]) + np.random.uniform(-10, 10, 6)
air_quality = np.array([45, 50, 55, 60, 65, 70]) + np.random.uniform(-5, 5, 6)
benchmark_environment = np.linspace(60, 60, len(months))  # Benchmark line

# Extracted variables for labels
fill_label_temperature = "Temperature"
fill_label_humidity = "Humidity"
fill_label_precipitation = "Precipitation"
fill_label_air_quality = "Air Quality Index"
plot_label_benchmark = "Benchmark"
title_text = "Environmental Metrics Over 6 Months"
xlabel_text = "Months"
ylabel_text = "Measurements"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
xlim_values = (1, 6)
ylim_values = (50, 130)
xticks_values = months
yticks_values = [50, 60, 70, 80, 90, 100, 110, 120, 130]
legend_loc = "upper center"
legend_bbox_to_anchor = (0.5, 1.08)
legend_ncol = 5

# Create the plot with an environmental style
plt.figure(figsize=(10, 6))
plt.fill_between(months, temperature, color="forestgreen", alpha=0.3, label=fill_label_temperature)
plt.fill_between(months, humidity, color="royalblue", alpha=0.3, label=fill_label_humidity)
plt.fill_between(months, precipitation, color="gold", alpha=0.3, label=fill_label_precipitation)
plt.fill_between(months, air_quality, color="darkorange", alpha=0.3, label=fill_label_air_quality)
plt.plot(months, benchmark_environment, color="black", linestyle="--", linewidth=2, label=plot_label_benchmark)

# Add a title and labels with enhanced formatting
plt.title(title_text, fontsize=16, y=1.05)
plt.xlabel(xlabel_text, fontsize=14)
plt.ylabel(ylabel_text, fontsize=14)
plt.xticks(xticks_values, fontsize=12)
plt.yticks(yticks_values, fontsize=12)
plt.gca().tick_params(axis="both", which="both", length=0)

# Setting the limits explicitly to prevent cut-offs
plt.xlim(*xlim_values)
plt.ylim(*ylim_values)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Adding a legend with a title
plt.legend(
    frameon=False,
    reverse=True,
    framealpha=0.8,
    loc=legend_loc,
    bbox_to_anchor=legend_bbox_to_anchor,
    ncol=legend_ncol,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to ensure no clipping
plt.tight_layout()
plt.savefig("area_11.pdf", bbox_inches="tight")
