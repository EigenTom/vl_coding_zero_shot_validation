
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


# ===================
# Part 2: Data Preparation
# ===================
import numpy as np; np.random.seed(0)
# Generate synthetic data for energy domain
efficiency_scores = np.random.beta(a=2, b=5, size=100)
reliability_scores = np.random.beta(a=5, b=2, size=100)
cost_scores = np.random.beta(a=3, b=3, size=100)
data = np.vstack([efficiency_scores, reliability_scores, cost_scores]).T

efficiency_scores_memory = np.random.beta(a=5, b=2, size=100)
reliability_scores_memory = np.random.beta(a=2, b=5, size=100)
cost_scores_memory = np.random.beta(a=3, b=3, size=100)
data_memory = np.vstack([efficiency_scores_memory, reliability_scores_memory, cost_scores_memory]).T

categories = ["Production Speed", "Product Quality", "Cost Efficiency"]
violin_width = 0.015

# Axes Limits and Labels
ylabel_value = "Performance Score"
labels = ["Manual Process", "Automated Process"]
title = "Performance Comparison Between Production Processes"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, ax = plt.subplots(figsize=(6, 6))  # Use the subplots function to create a figure and single axes

# Define the categories and the colors for each group
colors = ["#76c7c0", "#f4a582"]

# The scaling factor is used to ensure the violins do not overlap
scaling_factor = 1

# Define offset to separate the half violin plots in the single Axes object
offsets = [-0.05, 0, 0.05]

# Plot the half-violins with an offset
for i, category in enumerate(categories):
    offset = offsets[i]

    # Plot data without optimization
    kde_data = gaussian_kde(data[:, i])
    kde_x = np.linspace(0, 1, 300)
    kde_data_y = kde_data(kde_x)
    kde_data_y_scaled = kde_data_y / max(kde_data_y) * violin_width
    ax.fill_betweenx(
        kde_x,
        kde_data_y_scaled * scaling_factor + offset,
        offset,
        color=colors[0],
        edgecolor="#3d6d6e",
    )

    # Plot data with optimization
    kde_data_memory = gaussian_kde(data_memory[:, i])
    kde_data_memory_y = kde_data_memory(kde_x)
    kde_data_memory_y_scaled = kde_data_memory_y / max(kde_data_memory_y) * violin_width
    ax.fill_betweenx(
        kde_x,
        offset,
        -kde_data_memory_y_scaled * scaling_factor + offset,
        color=colors[1],
        edgecolor="#8b4a34",
    )
    ax.text(
        offset, -0.1, category, ha="center", va="top"
    )  # Add the category label below the violin plot

# Set x and y axis labels and limits
ax.set_xlim(
    min(offsets) - scaling_factor * violin_width - 0.01,
    max(offsets) + scaling_factor * violin_width + 0.01,
)
y_margin = 0.01  # Adding 5% margin at top and bottom of the y-axis
y_min, y_max = ax.get_ylim()
ax.set_ylim(y_min - y_margin, y_max + y_margin)
ax.set_ylabel(ylabel_value)
ax.set_xticks([])  # Remove x-ticks as they are not meaningful here

# Set a title for the chart
ax.set_title(title)

# Adjust the legend
handles = [
    plt.Rectangle((0, 0), 1, 1, color=color, edgecolor="#9e8d8b") for color in colors
]
ax.legend(handles, labels, loc="lower left", bbox_to_anchor=(0.6, -0.2), ncol=1)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the plot
plt.tight_layout()
plt.savefig('violin_15.pdf', bbox_inches='tight')
