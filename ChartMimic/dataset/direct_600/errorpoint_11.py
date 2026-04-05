
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)
categories = [
    "Router Throughput", 
    "Server Latency", 
    "Database IOPS", 
    "API Response Time", 
    "Energy Consumption", 
    "Memory Bandwidth"
]

means = np.random.uniform(0.4, 2.5, len(categories))
std_devs = np.random.uniform(0.1, 0.3, len(categories))
dataset_mean = np.mean(means)

# Labels and Plot Types
label_Mean = "Mean Performance"
label_Dataset_mean = "Average Performance"

# Axes Limits and Labels
ylabel_value = "Performance Metric"
ylim_values = [0.0, 3]

title = "Agricultural Yield by Crop Type"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Error bar plot with optimized style
ax.errorbar(
    categories,
    means,
    yerr=std_devs,
    fmt="s",
    color="yellow",
    ecolor="darkgreen",
    elinewidth=2,
    capsize=5,
    markerfacecolor='lightgreen',
    label=label_Mean,
)

# Dataset mean line
ax.axhline(y=dataset_mean, color="brown", linestyle="--", linewidth=1.5, label=label_Dataset_mean)

# Customizing the plot
ax.set_ylabel(ylabel_value, fontsize=12)
ax.set_xticklabels(categories, rotation=45, ha="right", fontsize=10)
ax.legend(fontsize=10)
ax.set_ylim(ylim_values)

# Title for the plot
ax.set_title(title, fontsize=14, fontweight='bold')

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent clipping of tick-labels
plt.tight_layout()
plt.savefig("errorpoint_11.pdf", bbox_inches="tight")
