# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PolyCollection


# ===================
# Part 2: Data Preparation
# ===================
# Set a random seed for reproducibility
np.random.seed(0)
# Function to create polygon under graph
def polygon_under_graph(x, y):
    return [(x[0], 0.0), *zip(x, y), (x[-1], 0.0)]

# Data for bar chart
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
solar = [1.2, 1.3, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
wind = [0.8, 1.0, 1.2, 1.5, 2.0, 2.4, 2.8, 3.2, 3.6, 4.0]

# Data for distribution graph
x = np.linspace(0.0, 10.0, 31)
technology_levels = range(1, 4)
exp = np.exp
verts = [
    polygon_under_graph(x, exp(-0.5 * (x - t) ** 2)) for t in technology_levels
]  # Gaussian distributions

# Labels and titles
xlabel_bar_chart = "Year"
ylabel_bar_chart = "Sector"
zlabel_bar_chart = "Investment (Billion USD)"
yticks_bar_chart = [0, 1]
yticklabels_bar_chart = ["Solar", "Wind"]
title_bar_chart = "Investment in Renewable Energy Sectors"

xlabel_dist_graph = "Time Since Introduction (Years)"
ylabel_dist_graph = "Technology Level"
zlabel_dist_graph = "Adoption Rate"
yticks_dist_graph = [1, 2, 3]
title_dist_graph = "Adoption Rate of Different Technologies"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Initialize figure and axes
facecolors = plt.get_cmap("viridis")(np.linspace(0, 1, len(verts)))
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(121, projection="3d")  # 3D bar chart
ax2 = fig.add_subplot(122, projection="3d")  # 3D distribution graph

# Plot data for bar chart
ax1.bar(years, solar, zs=0, zdir="y", color="#28a745", alpha=0.8)
ax1.bar(years, wind, zs=1, zdir="y", color="#0077b6", alpha=0.8)

# Set labels and ticks for bar chart
ax1.set_xlabel(xlabel_bar_chart)
ax1.set_ylabel(ylabel_bar_chart)
ax1.set_zlabel(zlabel_bar_chart)
ax1.set_yticks(yticks_bar_chart)
ax1.set_yticklabels(yticklabels_bar_chart)
ax1.set_title(title_bar_chart, pad=20)

# Add polygons to the distribution graph
poly = PolyCollection(verts, facecolors=facecolors, alpha=0.7)
ax2.add_collection3d(poly, zs=technology_levels, zdir="y")

# Set labels and limits for distribution graph
ax2.set(
    xlim=(0, 10),
    ylim=(1, 4),
    zlim=(0, 1),
    xlabel=xlabel_dist_graph,
    ylabel=ylabel_dist_graph,
    zlabel=zlabel_dist_graph,
)
ax2.set_yticks(yticks_dist_graph)
ax2.set_title(title_dist_graph, pad=20)

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout and save the figure
plt.tight_layout()
plt.savefig("3d_19.pdf", bbox_inches="tight")