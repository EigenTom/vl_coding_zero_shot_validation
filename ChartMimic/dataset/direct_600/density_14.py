# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
# Fix a seed for reproducibility
np.random.seed(42)
# Generate bimodal distribution for AQI data
# Simulate AQI for two cities (City C and City D) 
aqi_city_c = np.random.normal(loc=30, scale=15, size=400)  # Lower AQI values
aqi_city_d = np.random.normal(loc=130, scale=25, size=400) # Higher AQI values
aqi_data = np.concatenate([aqi_city_c, aqi_city_d])

# X-axis values for KDE
xs = np.linspace(0, 200, 200)

# Axes Limits and Labels
title = "KDE Plot of AQI Distribution for Two Cities"
xlabel_value = "AQI Value"
ylabel_value = "Density"
legend_label = "AQI Density for Cities C and D"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
xticks_values = [0, 50, 100, 150, 200]
xticklabels = ["0", "50", "100", "150", "200"]
yticks_values = [0, 0.004, 0.008, 0.012, 0.016]
yticklabels = ["0", "0.004", "0.008", "0.012", "0.016"]
xlim_values = [0, 200]
ylim_values = [0, 0.018]
title_fontsize = 14
title_weight = 'bold'
label_fontsize = 12
legend_loc = 'upper right'
legend_fontsize = 12
# Set the figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Create the KDE plot with adjusted x-axis range
density = gaussian_kde(aqi_data)
density.covariance_factor = lambda: 0.3
density._compute_covariance()
plt.fill_between(xs, density(xs), color="#ff9999", edgecolor="dodgerblue")

# Customize ticks and labels
ax.set_xticks(xticks_values)
ax.set_xticklabels(xticklabels, fontsize=label_fontsize)

ax.set_yticks(yticks_values)
ax.set_yticklabels(yticklabels, fontsize=label_fontsize)

plt.xlim(xlim_values)
plt.ylim(ylim_values)

# Set the title and labels
plt.title(title, fontsize=title_fontsize, weight=title_weight)
plt.xlabel(xlabel_value, fontsize=label_fontsize)
plt.ylabel(ylabel_value, fontsize=label_fontsize)

# Add a legend
ax.legend([legend_label], loc=legend_loc, fontsize=legend_fontsize)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_14.pdf", bbox_inches="tight")