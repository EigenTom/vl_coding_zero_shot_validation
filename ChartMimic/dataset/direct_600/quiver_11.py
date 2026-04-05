
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)
# Define the vector field function for traffic flow
def traffic_vector_field(X, Y):
    # Placeholder function for the vector field
    U = -Y
    V = X
    return U, V

def modified_traffic_vector_field(X, Y):
    # Modified traffic flow
    U = -1 - X**2 + Y
    V = 1 + X - Y**2
    return U, V

# Create a grid of points representing intersections
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
X, Y = np.meshgrid(x, y)

# Compute the vector field
U, V = traffic_vector_field(X, Y)

# Compute the modified vector field
U_mod, V_mod = modified_traffic_vector_field(X, Y)

# Plot the curves representing different travel paths
x = np.linspace(0.3, 0.6, 100)  # Updated range for city block distances
xlabel = "Distance (km)"
ylabel = "Traffic Density (vehicles/km)"
patch_labels = ["Weekday Traffic Flow", "Weekend Traffic Flow"]
line_labels = ["Highway 101", "Highway 202", "City Road A", "City Road B"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(8, 6))

# Quiver plots for traffic flow
plt.quiver(X, Y, U, V, color="orangered", alpha=0.6) # Normal Flow
plt.quiver(X, Y, U_mod, V_mod, color="skyblue", alpha=0.6) # Modified Flow

# Plot different travel paths/detours
plt.plot(x, 0.09 / (x**1.2), color="#33cc33", linestyle='-')
plt.plot(x, 0.08 / (x**1.2 + 0.04), color="#ffa500", linestyle='--')
plt.plot(x, 0.075 / (x**1 + 0.04), color="#999999", linestyle='-.')
plt.plot(x, 0.12 / (x**1 + 0.05), color="#000000", linestyle=':')

# Add labels and legend
plt.xlabel(xlabel, fontsize=14, style="italic")
plt.ylabel(ylabel, fontsize=14, style="italic")

# Patches for vector fields
blue_patch = mpatches.Patch(color="#66b3ff", label=patch_labels[0], alpha=0.6)
red_patch = mpatches.Patch(color="#ff6666", label=patch_labels[1], alpha=0.6)

# Lines for travel paths
main_road_1 = mlines.Line2D([], [], color="#33cc33", linestyle='-', label=line_labels[0])
main_road_2 = mlines.Line2D([], [], color="#ffa500", linestyle='--', label=line_labels[1])
detour_1 = mlines.Line2D([], [], color="#999999", linestyle='-.', label=line_labels[2])
detour_2 = mlines.Line2D([], [], color="#000000", linestyle=':', label=line_labels[3])

# Combine all legend handles
handles = [
    blue_patch,
    red_patch,
    main_road_1,
    main_road_2,
    detour_1,
    detour_2,
]

# Add the legend to the plot with specified location
plt.legend(handles=handles, loc="upper right")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('quiver_11.pdf', bbox_inches='tight')
