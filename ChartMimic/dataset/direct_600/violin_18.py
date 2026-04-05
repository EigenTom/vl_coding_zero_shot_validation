
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


# ===================
# Part 2: Data Preparation
# ===================
import numpy as np; np.random.seed(0)
import random
# Updated for a new domain: Energy Consumption Across Different Appliances
data = np.random.beta(a=[2, 5, 3, 7, 4], b=[7, 3, 6, 2, 5], size=(10, 5))
data_memory = np.random.beta(a=[8, 6, 4, 9, 3], b=[3, 5, 7, 2, 6], size=(40, 5))

xticklabels = ["Refrigerator", "Washing Machine", "Air Conditioner", "Heater", "Oven"]
legend_labels = ["Current Data", "Historical Data"]
scaling_factor = 1
violin_width = 0.5
xlabel = "Appliance Type"
ylabel = "Energy Consumption (kWh)"

# Adjust the offsets for 5 groups instead of 3
offsets = np.linspace(-3, 3, 5)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, ax = plt.subplots(figsize=(8, 6))  # Increased width for better spacing

# Define the colors for each group
colors = ["#ff7f0e", "#9467bd"]  # Orange and Purple for transportation
legend_colors = ["#ff7f0e", "#9467bd"]

# Plot the half-violins with an offset for 5 groups
for i in range(data.shape[1]):
    offset = offsets[i]

    # Plot data without memory
    kde_data = gaussian_kde(data[:, i])
    kde_x = np.linspace(0, 1, 300)
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

    # Add yellow stars at the top of each violin plot for emphasis
    ax.scatter(
        offset,
        random.uniform(0.2, 0.8),
        marker="*",
        color="yellow",
        s=260,
        zorder=3,
        edgecolor="black",
    )

# Set axis labels and limits
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_xlim(
    min(offsets) - scaling_factor - violin_width,
    max(offsets) + scaling_factor + violin_width,
)
ax.set_xticks(offsets)
ax.set_xticklabels(xticklabels)

# Adjust the legend
handles = [
    plt.Rectangle((0, 0), 1, 1, color=color, edgecolor="black")
    for color in legend_colors
]
ax.legend(handles, legend_labels, loc="upper left", ncol=1)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('violin_18.pdf', bbox_inches='tight')
