
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


# ===================
# Part 2: Data Preparation
# ===================
import numpy as np; np.random.seed(0)
# Generate plausible data for user preferences in art and design
data = np.random.beta(a=[15, 25, 35, 20, 30], b=[20, 30, 25, 35, 28], size=(10, 5))
data_memory = np.random.beta(a=[18, 40, 25, 35, 45], b=[30, 35, 40, 25, 30], size=(40, 5))

xticklabels = ["Social Media", "Television", "Podcasts", "Print Media", "Streaming"]
legend_labels = ["Current Engagement", "Historical Trends"]
scaling_factor = 1
violin_width = 0.5

# Adjust the offsets for 5 groups
offsets = np.linspace(-3, 3, 5)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, ax = plt.subplots(figsize=(8, 6))  # Slightly increased size for better visualization

# Define the colors for each group
colors = ["#e377c2", "#1f77b4"]
legend_colors = ["#1f77b4", "#e377c2"]

# Plot the half-violins with an offset for 5 groups
for i in range(data.shape[1]):
    offset = offsets[i]

    # Plot data without memory
    kde_data = gaussian_kde(data[:, i])
    kde_x = np.linspace(0, 1, 300)
    kde_data_y = kde_data(kde_x)
    kde_data_y_scaled = kde_data_y / max(kde_data_y) * violin_width
    ax.fill_betweenx(kde_x, kde_data_y_scaled * scaling_factor + offset, offset, color=colors[0], edgecolor="black", alpha=0.6)

    # Plot data with memory
    kde_data_memory = gaussian_kde(data_memory[:, i])
    kde_data_memory_y = kde_data_memory(kde_x)
    kde_data_memory_y_scaled = kde_data_memory_y / max(kde_data_memory_y) * violin_width
    ax.fill_betweenx(kde_x, offset, -kde_data_memory_y_scaled * scaling_factor + offset, color=colors[1], edgecolor="black", alpha=0.6)

    # Add stylish markers at the top of each violin plot
    ax.scatter(offset, np.mean(kde_x), marker="o", color="gold", s=100, zorder=3, edgecolor="black")

# Set x and y axis labels, limits, and add x-axis tick labels for 5 groups
ax.set_xlim(min(offsets) - scaling_factor - violin_width, max(offsets) + scaling_factor + violin_width)
ax.set_xticks(offsets)
ax.set_xticklabels(xticklabels, fontsize=12, fontweight='bold')
ax.set_xlabel('Art Styles', fontsize=14, fontweight='bold')
ax.set_ylabel('Preference Distribution', fontsize=14, fontweight='bold')

# Adjust the legend
handles = [plt.Rectangle((0, 0), 1, 1, color=color, edgecolor="black") for color in legend_colors]
ax.legend(handles, legend_labels, loc="upper left", fontsize=12, title="Legend", title_fontsize='13')

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('violin_19.pdf', bbox_inches='tight')
