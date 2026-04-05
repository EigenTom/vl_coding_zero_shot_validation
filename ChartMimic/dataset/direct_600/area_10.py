# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(42)
# Data representing average temperatures in different cities over years (in °C)
years = np.array([2000, 2005, 2010, 2015, 2020])

city1_temps = np.array([14.2, 14.5, 14.7, 15.0, 15.3]) + np.random.normal(0, 0.3, 5)
city2_temps = np.array([10.4, 10.6, 10.8, 11.2, 11.5]) + np.random.normal(0, 0.3, 5)
city3_temps = np.array([8.1, 8.4, 8.7, 9.0, 9.3]) + np.random.normal(0, 0.3, 5)
city4_temps = np.array([12.5, 12.6, 12.8, 13.1, 13.5]) + np.random.normal(0, 0.3, 5)

# Extracted variables
fill_label_city1 = "City 1"
fill_label_city2 = "City 2"
fill_label_city3 = "City 3"
fill_label_city4 = "City 4"
title_text = "Average Temperature Over Years"
xlabel_text = "Year"
ylabel_text = "Temperature (°C)"
legend_title = "City"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
xlim_values = (min(years), max(years))
ylim_values = (7.0, 16.0)
xticks_values = years
yticks_values = np.arange(7.0, 16.1, 1.0)
legend_loc = "upper left"
legend_bbox_to_anchor = (1, 1)
legend_ncol = 1

# Create the plot with a different visualization style
plt.figure(figsize=(10, 7))
plt.fill_between(
    years, city1_temps, color="#FF6347", alpha=0.5, label=fill_label_city1
)
plt.fill_between(
    years, city2_temps, color="#4682B4", alpha=0.5, label=fill_label_city2
)
plt.fill_between(
    years, city3_temps, color="#32CD32", alpha=0.5, label=fill_label_city3
)
plt.fill_between(
    years, city4_temps, color="#FFD700", alpha=0.5, label=fill_label_city4
)

# Add a title and labels
plt.title(title_text, fontsize=16, y=1.05)
plt.xlabel(xlabel_text, fontsize=14)
plt.ylabel(ylabel_text, fontsize=14)
plt.xticks(xticks_values, fontsize=12)
plt.yticks(yticks_values, fontsize=12)

# Setting the limits explicitly to prevent cut-offs
plt.xlim(*xlim_values)
plt.ylim(*ylim_values)

# Adding a legend with a title
plt.legend(
    title=legend_title,
    frameon=False,
    loc=legend_loc,
    bbox_to_anchor=legend_bbox_to_anchor,
    ncol=legend_ncol,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to ensure no clipping
plt.tight_layout()
plt.savefig("area_10.pdf", bbox_inches="tight")
