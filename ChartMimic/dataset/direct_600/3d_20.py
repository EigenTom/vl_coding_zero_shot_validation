# ===================
# Part 1: Importing Libraries
# ===================
import math
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import PolyCollection

# ===================
# Part 2: Data Preparation
# ===================
# Set a random seed for reproducibility
np.random.seed(0)
def polygon_under_graph(x, y):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph. This assumes x is in ascending order.
    """
    return [(x[0], 0.0), *zip(x, y), (x[-1], 0.0)]

# Define the x-axis data
x = np.linspace(0.0, 10.0, 100)  # Increased resolution
vaccination_numbers = range(1, 4)

# New function to simulate vaccine efficacy over age
def vaccine_efficacy(x, v):
    # simulate gaussian distribution for vaccine efficacy over age
    mean = 5
    sigma = 1 / v  # standard deviation inversely proportional to dose number
    return 0.35 * np.exp(-0.5 * ((x - mean) / sigma)**2)

# Generate vertices for polygons
verts = [polygon_under_graph(x, vaccine_efficacy(x, v)) for v in vaccination_numbers]

# Extracted variables
x_label = "Age"
y_label = "Vaccination Number"
z_label = "Efficacy Rate"
title = "Vaccine Efficacy Over Age by Vaccination Number"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and 3D axis
yticks = [1, 2, 3]
xlim = (0, 10)
ylim = (1, 4)
zlim = (0, 0.35)
aspect_ratio = [2, 1, 1]
view_elev = 30
view_azim = 150

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection="3d")

# Define the face colors
facecolors = plt.get_cmap("winter")(np.linspace(0, 1, len(verts)))

# Create a PolyCollection object
poly = PolyCollection(verts, facecolors=facecolors, alpha=0.7)
ax.add_collection3d(poly, zs=vaccination_numbers, zdir="y")

# Set the axis labels and limits
ax.set(xlim=xlim, ylim=ylim, zlim=zlim,
       xlabel=x_label, ylabel=y_label, zlabel=z_label)

# Add ticks and title
ax.set_yticks(yticks)
ax.set_title(title, pad=20)

# Adjust the aspect ratio and view angle
ax.set_box_aspect(aspect_ratio)
ax.view_init(elev=view_elev, azim=view_azim)

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout and save the figure
plt.tight_layout()
plt.savefig("3d_20.pdf", bbox_inches="tight")