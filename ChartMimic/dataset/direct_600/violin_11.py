
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


# ===================
# Part 2: Data Preparation
# ===================
import numpy as np; np.random.seed(0)
# Generate sample data for health metrics
data = np.random.beta(a=[2, 2, 3], b=[5, 3, 2], size=(100, 3))
data_memory = np.random.beta(a=[3, 4, 2], b=[2, 2, 3], size=(100, 3))
kde_x = np.linspace(0, 1, 300)

# Define the categories and the colors for each group
categories = ["Marketing Budget", "R&D Spending", "Operational Costs"]
title = "Financial Metrics Analysis with and without Investment"
offsets = [-0.05, 0, 0.05]
ylabel = "Percentage of Total Expenditure (%)"
labels = ["Without Investment", "With Investment"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, ax = plt.subplots(figsize=(8, 6))
colors = ["salmon", "limegreen"] 

# The scaling factor is used to ensure the violins do not overlap
scaling_factor = 1
violin_width = 0.015

# Plot the half-violins with an offset
for i, category in enumerate(categories):
    offset = offsets[i]
    # Plot data without memory
    kde_data = gaussian_kde(data[:, i])
    kde_data_y = kde_data(kde_x)
    kde_data_y_scaled = kde_data_y / max(kde_data_y) * violin_width
    ax.fill_betweenx(
        kde_x,
        kde_data_y_scaled * scaling_factor + offset,
        offset,
        color=colors[0],
        edgecolor="black",
    )

    # Plot data with memory
    kde_data_memory = gaussian_kde(data_memory[:, i])
    kde_data_memory_y = kde_data_memory(kde_x)
    kde_data_memory_y_scaled = kde_data_memory_y / max(kde_data_memory_y) * violin_width
    ax.fill_betweenx(
        kde_x,
        offset,
        -kde_data_memory_y_scaled * scaling_factor + offset,
        color=colors[1],
        edgecolor="black",
    )

    # Plot the mean as a star marker for data without memory
    ax.plot(
        offset,
        np.mean(data[:, i]),
        "*",
        color="white",
        markersize=12,
        markeredgecolor="black",
    )
    # Plot the mean as a star marker for data with memory
    ax.plot(
        offset,
        np.mean(data_memory[:, i]),
        "*",
        color="white",
        markersize=12,
        markeredgecolor="black",
    )

    ax.text(
        offset, -0.1, category, ha="center", va="top", fontsize=9
    )  # Add the category label below the violin plot

# Add title
ax.set_title(title, fontsize=14)

# Add grid
ax.grid(True, linestyle='--', alpha=0.7)

# Set x and y axis labels and limits
ax.set_xlim(
    min(offsets) - scaling_factor * violin_width - 0.06,
    max(offsets) + scaling_factor * violin_width + 0.06,
)
y_margin = 0.02  # Adding margin at top and bottom of the y-axis
y_min, y_max = ax.get_ylim()
ax.set_ylim(y_min - y_margin, y_max + y_margin)
ax.set_ylabel(ylabel, fontsize=12)
ax.set_xticks([])  # Remove x-ticks as they are not meaningful here

# Adjust the legend
handles = [
    plt.Rectangle((0, 0), 1, 1, color=color, edgecolor="black") for color in colors
]

ax.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, -0.15), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the figure
plt.tight_layout()
plt.savefig('violin_11.pdf', bbox_inches='tight')
