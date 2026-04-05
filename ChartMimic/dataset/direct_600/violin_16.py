
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


# ===================
# Part 2: Data Preparation
# ===================
import numpy as np; np.random.seed(0)
# Simulated temperature data for two regions across five seasons
data_5_seasons_region_A = np.random.beta(a=[2, 2, 3, 2, 3], b=[5, 3, 2, 4, 5], size=(100, 5))
data_5_seasons_region_B = np.random.beta(a=[3, 5, 2, 2, 2], b=[2, 1, 3, 3, 4], size=(100, 5))
ylabel="Internet Traffic (GB)"
ylim=[0, 1]
violin_width = 0.4
scaling_factor = 1
kde_x = np.linspace(0, 1, 300)

# Offsets for quarters
offsets_5_seasons = np.linspace(-3, 3, 5)
labels=["Comcast", "Verizon"]
title="Quarterly Internet Traffic Distribution for ISPs"
legend_labels = ["Comcast", "Verizon"]
xticklabels=["Q1", "Q2", "Q3", "Q4", "Year-End"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure
fig, ax = plt.subplots(figsize=(10, 6))

# Define the colors for each season
colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]

# Function to plot half violins for temperature data
def plot_half_violins(ax, data_region_A, data_region_B, offsets, colors, labels, title, xticklabels):
    # Plot the half-violins with an offset for seasons
    for i in range(data_region_A.shape[1]):
        offset = offsets[i]

        # Plot data for Region A
        kde_data_A = gaussian_kde(data_region_A[:, i])
        kde_x = np.linspace(0, 1, 300)
        kde_data_A_y = kde_data_A(kde_x)
        kde_data_A_y_scaled = kde_data_A_y / max(kde_data_A_y) * violin_width
        ax.fill_betweenx(
            kde_x,
            kde_data_A_y_scaled * scaling_factor + offset,
            offset,
            color=colors[i],
            edgecolor="black",
            alpha=0.6
        )

        # Plot data for Region B
        kde_data_B = gaussian_kde(data_region_B[:, i])
        kde_data_B_y = kde_data_B(kde_x)
        kde_data_B_y_scaled = kde_data_B_y / max(kde_data_B_y) * violin_width
        ax.fill_betweenx(
            kde_x,
            offset,
            -kde_data_B_y_scaled * scaling_factor + offset,
            color=colors[i],
            edgecolor="black",
            alpha=0.3
        )

    # Set x and y axis labels, limits, and add x-axis tick labels for seasons
    ax.set_xlim(
        min(offsets) - scaling_factor - violin_width,
        max(offsets) + scaling_factor + violin_width,
    )
    ax.set_ylim(ylim)  # Set y-axis limits to 0-1 for beta distribution
    ax.set_ylabel(ylabel)
    ax.set_xticks(offsets)  # Set x-ticks to the center of each season
    ax.set_xticklabels(xticklabels)  # Label x-ticks accordingly
    ax.title.set_text(title)

# Plot the violins
plot_half_violins(
    ax,
    data_5_seasons_region_A,
    data_5_seasons_region_B,
    offsets_5_seasons,
    colors,
    labels,
    title,
    xticklabels
)

# Add a legend for the entire figure
handles = [
    plt.Line2D(
        [0], [0], marker="o", color="w", markerfacecolor="black", markersize=10, alpha=0.6
    ),
    plt.Line2D(
        [0], [0], marker="o", color="w", markerfacecolor="black", markersize=10, alpha=0.3
    ),
]

fig.legend(handles, legend_labels, loc="lower center", bbox_to_anchor=(0.5, -0.1), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Tighten the layout and show the combined plot
plt.tight_layout()

# Display the plot
plt.savefig('violin_16.pdf', bbox_inches='tight')
