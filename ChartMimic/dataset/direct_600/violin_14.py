
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
import numpy as np; np.random.seed(0)
# Generate synthetic data for education domain
data_traditional = np.random.beta(a=[3, 2, 4], b=[4, 5, 2], size=(100, 3))
data_innovative = np.random.beta(a=[4, 5, 2], b=[3, 2, 4], size=(100, 3))

categories = ["Task Efficiency", "Collaboration", "Punctuality"]
violin_width = 0.02

# Axes Limits and Labels
ylabel_value = "Performance Score"
labels = ["Traditional Office", "Remote Work"]
title ="Performance Comparison Between Work Environments"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, ax = plt.subplots(figsize=(7, 6))  # Slightly larger figure for better readability

# Define the categories and the colors for each group
colors = ["plum", "bisque"]  # Blue and green shades suitable for education theme

# The scaling factor is used to ensure the violins do not overlap
scaling_factor = 1

# Define offset to separate the half violin plots in the single Axes object
offsets = [-0.05, 0, 0.05]

# Plot the half-violins with an offset
for i, category in enumerate(categories):
    offset = offsets[i]

    # Plot data for traditional teaching
    kde_data_traditional = gaussian_kde(data_traditional[:, i])
    kde_x = np.linspace(0, 1, 300)
    kde_data_traditional_y = kde_data_traditional(kde_x)
    kde_data_traditional_y_scaled = kde_data_traditional_y / max(kde_data_traditional_y) * violin_width
    ax.fill_betweenx(
        kde_x,
        kde_data_traditional_y_scaled * scaling_factor + offset,
        offset,
        color=colors[0],
        edgecolor="#5a5a5a",  # Adjust edge color for better contrast
    )

    # Plot data for innovative teaching
    kde_data_innovative = gaussian_kde(data_innovative[:, i])
    kde_data_innovative_y = kde_data_innovative(kde_x)
    kde_data_innovative_y_scaled = kde_data_innovative_y / max(kde_data_innovative_y) * violin_width
    ax.fill_betweenx(
        kde_x,
        offset,
        -kde_data_innovative_y_scaled * scaling_factor + offset,
        color=colors[1],
        edgecolor="#5a5a5a",
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

# Add a meaningful chart title
ax.set_title(title)

# Adjust the legend
handles = [
    plt.Rectangle((0, 0), 1, 1, color=color, edgecolor="#5a5a5a") for color in colors
]
ax.legend(handles, labels, loc="lower left", bbox_to_anchor=(0.6, -0.2), ncol=1)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the plot
plt.tight_layout()
plt.savefig('violin_14.pdf', bbox_inches='tight')
